#!/usr/bin/env python3
"""Generate a readable, compilable word-level LaTeX comparison.

The script uses only the Python standard library.
It keeps the revised document structure and inserts deleted and added text at
the closest aligned location.
"""

from __future__ import annotations

import argparse
import dataclasses
import difflib
import hashlib
import pathlib
import re
import sys
from collections.abc import Iterable, Sequence


BEGIN_DOCUMENT = r"\begin{document}"
END_DOCUMENT = r"\end{document}"
WORD_RE = re.compile(
    r"[A-Za-z0-9]+(?:[\-'][A-Za-z0-9]+)*(?:[.,;:!?])?|"
    r"``|''|---|--|~|"
    r"\\[%&#_$]|"
    r"\\[A-Za-z@]+\*?|"
    r"\s+|.",
    re.DOTALL,
)
BEGIN_RE = re.compile(r"\\begin\{([^}]+)\}")
END_RE = re.compile(r"\\end\{([^}]+)\}")
STRUCTURAL_COMMANDS = {
    r"\begin",
    r"\end",
    r"\label",
    r"\includegraphics",
    r"\usetikzlibrary",
    r"\definecolor",
    r"\tikzset",
    r"\draw",
    r"\path",
    r"\coordinate",
    r"\toprule",
    r"\midrule",
    r"\bottomrule",
    r"\addlinespace",
    r"\centering",
    r"\bigskip",
    r"\noindent",
    r"\newpage",
    r"\clearpage",
}
STRUCTURAL_GROUP_LIMITS = {
    r"\begin": 2,
    r"\end": 1,
    r"\label": 1,
    r"\includegraphics": 2,
    r"\resizebox": 2,
    r"\renewcommand": 2,
    r"\setlength": 2,
    r"\addlinespace": 1,
    r"\multicolumn": 3,
    r"\vspace": 1,
    r"\hspace": 1,
}
CITATION_COMMANDS = {
    r"\cite",
    r"\parencite",
    r"\textcite",
    r"\parencites",
}
ATOMIC_COMMANDS = CITATION_COMMANDS | {
    r"\ref",
    r"\pageref",
    r"\url",
    r"\href",
}


@dataclasses.dataclass(frozen=True)
class Unit:
    text: str
    environment: str | None = None

    @property
    def normalized(self) -> str:
        return normalize_source(self.text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old", required=True, type=pathlib.Path)
    parser.add_argument("--new", required=True, type=pathlib.Path)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    return parser.parse_args()


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_document(source: str) -> tuple[str, str, str]:
    try:
        preamble, remainder = source.split(BEGIN_DOCUMENT, 1)
        body, trailer = remainder.rsplit(END_DOCUMENT, 1)
    except ValueError as error:
        raise ValueError("Input is missing a unique LaTeX document body") from error
    return preamble, body, trailer


def strip_comment(line: str) -> str:
    for index, character in enumerate(line):
        if character != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index]
    return line


def remove_comments(source: str) -> str:
    return "".join(strip_comment(line) for line in source.splitlines(keepends=True))


def normalize_source(source: str) -> str:
    source = remove_comments(source)
    return re.sub(r"\s+", " ", source).strip()


def environment_depth_delta(line: str) -> int:
    return len(BEGIN_RE.findall(line)) - len(END_RE.findall(line))


def segment_body(body: str) -> list[Unit]:
    """Split a document body into paragraphs and complete top-level environments."""
    lines = remove_comments(body).splitlines(keepends=True)
    units: list[Unit] = []
    buffer: list[str] = []
    environment: str | None = None
    depth = 0

    def flush() -> None:
        nonlocal buffer
        text = "".join(buffer).strip()
        if text:
            units.append(Unit(text=text + "\n\n", environment=environment))
        buffer = []

    for line in lines:
        stripped = line.strip()
        if environment is None and stripped.startswith(r"\begin{"):
            flush()
            match = BEGIN_RE.search(stripped)
            environment = match.group(1) if match else "unknown"
            depth = 0

        if environment is not None:
            buffer.append(line)
            depth += environment_depth_delta(line)
            if depth == 0:
                flush()
                environment = None
            continue

        if not stripped:
            flush()
            continue

        if stripped.startswith((r"\section", r"\subsection", r"\subsubsection")):
            flush()
            units.append(Unit(text=stripped + "\n\n"))
            continue

        buffer.append(line)

    flush()
    return units


def token_key(token: str) -> str:
    if token.isspace():
        return "\n\n" if "\n\n" in token else " "
    return token


def tokenize(source: str) -> list[str]:
    return WORD_RE.findall(source)


def command_name(token: str) -> str | None:
    if re.fullmatch(r"\\[A-Za-z@]+\*?", token):
        return token.rstrip("*")
    return None


def leading_command_name(token: str) -> str | None:
    match = re.match(r"(\\[A-Za-z@]+)\*?", token)
    return match.group(1) if match else None


def is_word(token: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9]+(?:[\-'][A-Za-z0-9]+)*(?:[.,;:!?])?", token))


def is_markable_symbol(token: str) -> bool:
    return token in {"``", "''", "---", "--"}


def consume_balanced_group(tokens: Sequence[str], index: int) -> tuple[list[str], int]:
    opening = tokens[index]
    closing = "}" if opening == "{" else "]"
    depth = 0
    pieces: list[str] = []
    while index < len(tokens):
        token = tokens[index]
        pieces.append(token)
        if token == opening:
            depth += 1
        elif token == closing:
            depth -= 1
        index += 1
        if depth == 0:
            break
    return pieces, index


def group_atomic_commands(tokens: Sequence[str]) -> list[str]:
    """Keep structural, citation, and reference command arguments intact."""
    grouped: list[str] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        name = command_name(token)
        if name not in ATOMIC_COMMANDS and name not in STRUCTURAL_GROUP_LIMITS:
            grouped.append(token)
            index += 1
            continue

        pieces = [token]
        index += 1
        group_count = 0
        group_limit = STRUCTURAL_GROUP_LIMITS.get(name)
        begin_environment: str | None = None
        while index < len(tokens):
            current = tokens[index]
            if current.isspace():
                pieces.append(current)
                index += 1
                continue
            if current not in {"[", "{"}:
                break
            group, index = consume_balanced_group(tokens, index)
            pieces.extend(group)
            group_count += 1
            if name == r"\begin" and group_count == 1:
                begin_environment = "".join(group[1:-1]).strip()
                if begin_environment == "tabularx":
                    # Keep the environment name, target width, and column
                    # specification together. Diff markup in a column
                    # specification is invalid LaTeX.
                    group_limit = 3
            if group_limit is not None and group_count >= group_limit:
                break
        grouped.append("".join(pieces))
    return grouped


def wrap_token(token: str, operation: str) -> str:
    macro = r"\DIFdel" if operation == "delete" else r"\DIFadd"
    if is_word(token) or is_markable_symbol(token):
        return f"{macro}{{{token}}}"
    name = leading_command_name(token)
    if name in STRUCTURAL_COMMANDS or name in STRUCTURAL_GROUP_LIMITS:
        return "" if operation == "delete" else token
    if name in ATOMIC_COMMANDS:
        citation_macro = r"\DIFdelcite" if operation == "delete" else r"\DIFaddcite"
        return f"{citation_macro}{{{token}}}"
    if token.startswith("\\") and "{" in token:
        return f"{macro}{{{token}}}"
    if token.isspace():
        return token
    return "" if operation == "delete" else token


def render_changed(tokens: Iterable[str], operation: str) -> str:
    return "".join(wrap_token(token, operation) for token in tokens)


def verify_opcodes(old: Sequence[str], new: Sequence[str], opcodes: Sequence[tuple[str, int, int, int, int]]) -> None:
    reconstructed_old: list[str] = []
    reconstructed_new: list[str] = []
    for tag, old_start, old_end, new_start, new_end in opcodes:
        if tag in {"equal", "delete", "replace"}:
            reconstructed_old.extend(old[old_start:old_end])
        if tag in {"equal", "insert", "replace"}:
            reconstructed_new.extend(new[new_start:new_end])
    if reconstructed_old != list(old) or reconstructed_new != list(new):
        raise AssertionError("Diff opcode reconstruction failed")


def diff_source(old_source: str, new_source: str) -> str:
    old_tokens = group_atomic_commands(tokenize(old_source))
    new_tokens = group_atomic_commands(tokenize(new_source))
    matcher = difflib.SequenceMatcher(
        None,
        [token_key(token) for token in old_tokens],
        [token_key(token) for token in new_tokens],
        autojunk=False,
    )
    opcodes = matcher.get_opcodes()
    verify_opcodes(old_tokens, new_tokens, opcodes)

    rendered: list[str] = []
    math_mode = False
    bracket_depth = 0

    def update_context(text: str) -> None:
        nonlocal math_mode, bracket_depth
        for position, character in enumerate(text):
            escaped = position > 0 and text[position - 1] == "\\"
            if character == "$" and not escaped:
                math_mode = not math_mode
            elif character == "[" and not escaped and not math_mode:
                bracket_depth += 1
            elif character == "]" and not escaped and not math_mode:
                bracket_depth = max(0, bracket_depth - 1)

    for tag, old_start, old_end, new_start, new_end in opcodes:
        old_chunk = old_tokens[old_start:old_end]
        new_chunk = new_tokens[new_start:new_end]
        if tag == "equal":
            text = "".join(new_chunk)
            rendered.append(text)
            update_context(text)
            continue
        changed_text = "".join(new_chunk if new_chunk else old_chunk)
        protected_context = math_mode or bracket_depth > 0 or "[" in changed_text
        if protected_context:
            if tag in {"insert", "replace"}:
                text = "".join(new_chunk)
                rendered.append(text)
                update_context(text)
            continue
        if tag in {"delete", "replace"}:
            rendered.append(render_changed(old_chunk, "delete"))
        if tag == "replace":
            rendered.append(" ")
        if tag in {"insert", "replace"}:
            text = render_changed(new_chunk, "insert")
            rendered.append(text)
            update_context("".join(new_chunk))
    return "".join(rendered)


def unit_similarity(old: Unit, new: Unit) -> float:
    if old.environment != new.environment:
        return 0.0
    return difflib.SequenceMatcher(None, old.normalized, new.normalized, autojunk=False).ratio()


def pair_replacement_units(old_units: Sequence[Unit], new_units: Sequence[Unit]) -> list[tuple[Unit | None, Unit | None]]:
    """Pair changed units in order, preferring the closest structurally compatible match."""
    pairs: list[tuple[Unit | None, Unit | None]] = []
    old_index = 0
    new_index = 0
    while old_index < len(old_units) and new_index < len(new_units):
        direct = unit_similarity(old_units[old_index], new_units[new_index])
        skip_old = (
            unit_similarity(old_units[old_index + 1], new_units[new_index])
            if old_index + 1 < len(old_units)
            else 0.0
        )
        skip_new = (
            unit_similarity(old_units[old_index], new_units[new_index + 1])
            if new_index + 1 < len(new_units)
            else 0.0
        )
        if direct >= 0.18 or (direct >= skip_old and direct >= skip_new):
            pairs.append((old_units[old_index], new_units[new_index]))
            old_index += 1
            new_index += 1
        elif skip_old > skip_new:
            pairs.append((old_units[old_index], None))
            old_index += 1
        else:
            pairs.append((None, new_units[new_index]))
            new_index += 1
    pairs.extend((unit, None) for unit in old_units[old_index:])
    pairs.extend((None, unit) for unit in new_units[new_index:])
    return pairs


def render_unit_pair(old: Unit | None, new: Unit | None) -> str:
    if old is None and new is not None:
        return diff_source("", new.text)
    if new is None and old is not None:
        return diff_source(old.text, "")
    if old is None or new is None:
        return ""
    if old.environment == "figure" and r"\begin{tikzpicture}" in old.text and r"\begin{tikzpicture}" in new.text:
        old_visible = extract_figure_text(old.text)
        new_visible = extract_figure_text(new.text)
        if normalize_source(old_visible) == normalize_source(new_visible):
            return new.text
        changes = diff_source(old_visible, new_visible)
        return (
            new.text
            + "\\begin{quote}\\footnotesize\n"
            + "\\textit{Diagram text changes:} "
            + changes
            + "\n\\end{quote}\n\n"
        )
    return diff_source(old.text, new.text)


def extract_figure_text(source: str) -> str:
    """Extract captions and visible TikZ node text for a safe comparison note."""
    visible: list[str] = []

    def clean(text: str) -> str:
        text = text.replace(r"\\", " ")
        text = re.sub(r"\\(?:footnotesize|tiny|scriptsize|small|bfseries)\b", "", text)
        text = text.replace(r"\textbar{}", "|")
        return re.sub(r"\s+", " ", text).strip()

    for line in remove_comments(source).splitlines():
        stripped = line.strip()
        if stripped.startswith(r"\caption{"):
            caption = clean(stripped[len(r"\caption{") :].rsplit("}", 1)[0])
            if caption:
                visible.append(caption)
            continue
        if not stripped.startswith(r"\node"):
            continue
        match = re.search(r".*\)\s*\{(.*)\}\s*;\s*$", stripped)
        if match:
            node_text = clean(match.group(1))
            if node_text:
                visible.append(node_text)
    return "; ".join(visible)


def diff_body(old_body: str, new_body: str) -> str:
    old_units = segment_body(old_body)
    new_units = segment_body(new_body)
    matcher = difflib.SequenceMatcher(
        None,
        [unit.normalized for unit in old_units],
        [unit.normalized for unit in new_units],
        autojunk=False,
    )
    rendered: list[str] = []
    for tag, old_start, old_end, new_start, new_end in matcher.get_opcodes():
        if tag == "equal":
            rendered.extend(unit.text for unit in new_units[new_start:new_end])
            continue
        pairs = pair_replacement_units(old_units[old_start:old_end], new_units[new_start:new_end])
        rendered.extend(render_unit_pair(old, new) for old, new in pairs)
    return "".join(rendered)


def inject_diff_preamble(preamble: str) -> str:
    additions = r"""

% Word-level comparison support generated by generate-word-diff.py.
\usepackage[normalem]{ulem}
\hypersetup{pdftitle={ACOSUS Submitted v4 to Final v5 Comparison}}
\definecolor{diffdelbg}{RGB}{255,214,214}
\definecolor{diffdeltext}{RGB}{145,20,20}
\definecolor{diffaddbg}{RGB}{215,245,220}
\definecolor{diffaddtext}{RGB}{20,110,45}
\setlength{\emergencystretch}{4em}
\newcommand{\DIFdel}[1]{%
  \begingroup\setlength{\fboxsep}{0.5pt}%
  \colorbox{diffdelbg}{\textcolor{diffdeltext}{\sout{#1}}}%
  \endgroup}
\newcommand{\DIFadd}[1]{%
  \begingroup\setlength{\fboxsep}{0.5pt}%
  \colorbox{diffaddbg}{\textcolor{diffaddtext}{#1}}%
  \endgroup}
\newcommand{\DIFdelcite}[1]{%
  \DIFdel{-}\textcolor{diffdeltext}{#1}}
\newcommand{\DIFaddcite}[1]{%
  \DIFadd{+}\textcolor{diffaddtext}{#1}}
\newcommand{\DIFaddedreference}[1]{%
  \par\noindent\begingroup\color{diffaddtext}%
  \textbf{Added citation: }\fullcite{#1}\par\endgroup}
\newcommand{\DIFremovedreference}[1]{%
  \par\noindent\begingroup\color{diffdeltext}%
  \textbf{Removed citation: }\fullcite{#1}\par\endgroup}
\newcommand{\DIFlegend}{%
  \begin{center}\small
  \textbf{Submitted v4 to final v5 comparison}\\[4pt]
  \DIFdel{Removed text}\quad\DIFadd{Added text}\quad Unchanged text
  \end{center}\medskip}
"""
    return preamble.rstrip() + additions + "\n"


def add_legend(body: str) -> str:
    center_end = body.find(r"\end{center}")
    if center_end == -1:
        return "\n\\DIFlegend\n" + body
    insertion = center_end + len(r"\end{center}")
    return body[:insertion] + "\n\\DIFlegend" + body[insertion:]


def citation_keys(source: str) -> set[str]:
    keys: set[str] = set()
    tokens = group_atomic_commands(tokenize(remove_comments(source)))
    for token in tokens:
        if leading_command_name(token) not in CITATION_COMMANDS:
            continue
        for argument in re.findall(r"\{([^{}]+)\}", token):
            keys.update(key.strip() for key in argument.split(",") if key.strip())
    return keys


def add_bibliography_summary(body: str, old_source: str, new_source: str) -> str:
    marker = r"\printbibliography"
    position = body.find(marker)
    if position == -1:
        return body

    old_keys = citation_keys(old_source)
    new_keys = citation_keys(new_source)
    added = sorted(new_keys - old_keys, key=str.casefold)
    removed = sorted(old_keys - new_keys, key=str.casefold)

    lines = [
        r"\clearpage",
        r"\section{Bibliography Changes}",
        "This summary compares works cited in the submitted version with works cited in the final draft.",
    ]
    if added:
        lines.extend([r"\subsection{Added Citations}", *[f"\\DIFaddedreference{{{key}}}" for key in added]])
    else:
        lines.extend([r"\subsection{Added Citations}", "No citations were added."])
    if removed:
        lines.extend(
            [r"\subsection{Removed Citations}", *[f"\\DIFremovedreference{{{key}}}" for key in removed]]
        )
    else:
        lines.extend([r"\subsection{Removed Citations}", "No citations were removed."])
    lines.append(r"\clearpage")
    summary = "\n\n".join(lines) + "\n\n"
    return body[:position] + summary + body[position:]


def generate(old_path: pathlib.Path, new_path: pathlib.Path, output_path: pathlib.Path) -> None:
    old_source = old_path.read_text(encoding="utf-8")
    new_source = new_path.read_text(encoding="utf-8")
    _, old_body, _ = split_document(old_source)
    new_preamble, new_body, new_trailer = split_document(new_source)

    diffed_body = diff_body(old_body, new_body)
    diffed_body = add_bibliography_summary(diffed_body, old_body, new_body)
    diffed_body = add_legend(diffed_body)
    script_path = pathlib.Path(__file__).resolve()
    try:
        script_path = script_path.relative_to(pathlib.Path.cwd().resolve())
    except ValueError:
        pass
    command = f"python3 {script_path} --old {old_path} --new {new_path} --output {output_path}"
    header = (
        "% GENERATED FILE. Regenerate it instead of editing diff markup by hand.\n"
        f"% Old source: {old_path} ({sha256(old_path)})\n"
        f"% New source: {new_path} ({sha256(new_path)})\n"
        f"% Command: {command}\n"
    )
    output = (
        header
        + inject_diff_preamble(new_preamble)
        + BEGIN_DOCUMENT
        + diffed_body
        + END_DOCUMENT
        + new_trailer
    )
    output_path.write_text(output, encoding="utf-8")


def main() -> int:
    arguments = parse_args()
    try:
        generate(arguments.old, arguments.new, arguments.output)
    except (OSError, ValueError, AssertionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
