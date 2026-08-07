#!/usr/bin/env python3
"""Count the active abstract after removing common LaTeX markup."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


BEGIN_MARKER = "% REV-ABSTRACT-001 BEGIN"
END_MARKER = "% REV-ABSTRACT-001 END"


def active_abstract(source: str) -> str:
    begin = source.index(BEGIN_MARKER)
    end = source.index(END_MARKER, begin)
    lines = source[begin:end].splitlines()[1:]
    return "\n".join(line.split("%", 1)[0] for line in lines)


def latex_aware_words(text: str) -> list[str]:
    text = re.sub(r"\\(?:textbf|textit|emph)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"[{}$~]", " ", text)
    return re.findall(r"[A-Za-z0-9]+(?:[.'’-][A-Za-z0-9]+)*", text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("tex", type=Path)
    parser.add_argument("--maximum", type=int, default=100)
    args = parser.parse_args()

    words = latex_aware_words(active_abstract(args.tex.read_text(encoding="utf-8")))
    print(f"latex_aware_abstract_words={len(words)}")
    if len(words) > args.maximum:
        raise SystemExit(f"abstract exceeds {args.maximum} words")


if __name__ == "__main__":
    main()
