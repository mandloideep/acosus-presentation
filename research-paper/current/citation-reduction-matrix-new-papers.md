# Citation-Reduction Matrix — Two New DSI Papers vs. `main-v3.tex`

**Purpose.** This is a *new, standalone* analysis (it does **not** edit the paper). It maps every
literature-backed claim in the Introduction and Literature Review of
[main-v3.tex](current/overleaf/main-v3.tex) against the **two newly supplied DSI papers**, then
proposes where citations can be **reduced** while keeping each claim properly supported.

It complements — and does not replace — the two matrices that already exist:
[claim-audit-main-v3.md](current/claim-audit-main-v3.md) (claim → current-cite audit) and
[ref-table.md](past-papers/ref-table.md) (replacement-source table). The new information here is the
*per-paper support matrix for the two new papers* plus a *citation-reduction column*.

---

## ✅ APPLIED to `main-v3.tex` (this round)

The recommended changes **have now been applied** to [main-v3.tex](current/overleaf/main-v3.tex), and
`standfast2024reddit` + `nguyen2025school` were added to
[references.bib](current/overleaf/references.bib). Per-claim status is in the **"Applied to main-v3?"**
column of the Table C tables. A source-of-truth comment block was added at the top of `main-v3.tex`.
Five keys are now orphaned (no longer cited; they drop out of the reference list automatically):
`ishitani2018student`, `jabbar2019complex`, `wang2020road`, `laanan2010adjustment`, `townsend2009`.

## ⚑ Decisions & reminders (status)

These are the choices that gated the changes.

- [x] **D1 — Self-citation appetite. → DECIDED: self-citations ON.** The Recommended column commits to
  the two new papers where they fit best (12 placements: `nguyen2025school` ×10, `standfast2024reddit`
  ×2). The no-self-citation fallback for each is in **Table D**.
- [x] **D2 — Prevalence fix (row 1). → DECIDED: option B (no reword).** Keep the community-college→four-year
  wording and cite **`monaghan2015`** (in `references.bib`; PDF supplied and **✅ verified** this session —
  it is literally *The Community College Route to the Bachelor's Degree*, fitting the wording). Shapiro is
  verified but measures all-directions transfer, so it is *not* used; its BibTeX stays in §5 only as a
  fallback if the wording ever changes.
- [~] **D3 — Row 8.** Applied as the recommended **3-cite** set (`jaggars2025` + `roksa2008credits` +
  `factoranalysis2023`), no rewording. ⚑ **Still your review:** whether to *trim* "distance between
  institutions" and "financial aid" from the sentence (the two weakest-supported items) — if you trim,
  `factoranalysis2023` can be dropped, taking row 8 to 2 cites.
- [ ] **D4 — M9 cosmetic (line 362).** Keep `socialcognitive2022` or swap to `factoranalysis2023` for
  the "Financial Stability" priority-table row? Your call.

---

## 0. The two new papers (what they are)

| Tag | Paper | Authors | Venue / Year | Method | Status in repo |
|-----|-------|---------|--------------|--------|----------------|
| **[A] `standfast2024reddit`** | *Deciding on a College Transfer: Uncovering Transition Queries and Concerns via Reddit Topic Modeling* | Standfast, Franco, Caraballo, Vargas, Wan, Wang, Bogle, Aggarwal, Rayana | DSI 2024 | Reddit scrape (664K→20K posts), LDA/CorEx/BERTopic topic modeling, VADER sentiment | PDF = `past-papers/10627343.pdf`; **not** in `references.bib` |
| **[B] `nguyen2025school`** | *School or Student? A Mixed-Method Analysis on Reddit Data for Transfer Barrier Identification* | P. M. Nguyen, Maldonado, Ty, Wan, Wang, Bogle, Aggarwal, Rayana | DSI 2025 | BERT embeddings + UMAP + HDBSCAN clustering, VADER, manual coding; ~1,000 Reddit posts + 161 computing-transfer survey responses | PDF = `past-papers/DSI25_School_or_Student_.pdf`; **not** in `references.bib` |

**Two cautions carried through the whole document:**

1. **Self-citation.** Both papers are by the ACOSUS team (same grant, NSF CNS-2219623) and both
   *cite the same primary sources the current paper already stacks* (Wang 2023 = `factoranalysis2023`,
   Ty 2024 = `computingtransfer2024`, Vargas 2022 = `socialcognitive2022`, MacDonald 2024 =
   `topicmodeling2024`, Townsend & Wilson 2006, Maliszewski & Hayes 2020 = `lukszo2020`,
   Ishitani & Flood 2018 = `ishitani2018student`). They are therefore excellent for *consolidating*
   claims, but for a hard empirical number (e.g., a prevalence statistic) the **primary** source is
   safer than the team's own synthesis. Each row below notes when this matters.
2. **Name collision.** `nguyen2025school` (Phuong Minh Nguyen — Reddit barriers) is **not** the same
   as the already-cited `nguyen2024community` (David Van **Nguyen** — articulation-agreement
   websites). Do not merge them.

---

## Table A — What `standfast2024reddit` (Reddit topic modeling) can support

Support: **✓✓ strong / direct**, **✓ partial / indirect**, **— not supported**.

| # | Claim in `main-v3.tex` | Lines | What the paper actually shows | Support |
|---|------------------------|-------|-------------------------------|---------|
| A1 | More affordable route to a bachelor's | 151 | Lit review: "affordability, scholarship, socio-economic status, geographic location … GPA as the major factors (Wang et al., 2023) in transfer decision." | ✓ |
| A2 | Coordination/credit-recognition problems | 151 | Abstract + Motivation: "credit transfer issues, adapting to new environments"; negative-sentiment topics include credit requirements, ambiguous deadlines, mandatory orientation. | ✓✓ |
| A3 | Financial pressure + weaker sense of belonging | 151 | Topics: financial situation, social life, "feeling out of place"; mental-health topic in negative subset. | ✓ |
| A4 | Measurable factors don't capture full experience | 153 | Core thesis: "survey instruments and interview questions may not encompass all crucial aspects … social media … capture such interactions." | ✓✓ |
| A5 | Social support / engagement (research, etc.) hard to capture | 153 | Topics surfaced: research opportunities, career opportunities, online community (Discord), social life — beyond structured records. | ✓ |
| A6 | Advising matters; advisor capacity is limited | 155, 177 | Motivation: "advisors may not be fully equipped to answer some of those nuanced questions … students tend to go to the internet." | ✓✓ |
| A7 | Existing systems miss transfer-specific variables | 155, 179 | Argues surveys/institutional data miss factors social media reveals. | ✓ |
| A8 | Self-efficacy / topic-modeling of open-ended + social media | 175 | This *is* the paper: topic modeling of open-ended social-media discussion of transfer. | ✓✓ |
| A9 | Transfer student capital | 177 | Discusses TSC sources (cites Townsend & Wilson 2006, Maliszewski & Hayes 2020). | ✓ |
| A10 | **Students turn to Reddit / Discord / peer forums** | 177 | Direct: entire dataset is Reddit; finds "Online Community (Discord)"; manual review shows students going to Reddit *because* advising was unsatisfactory. | ✓✓ |
| A11 | Mixed-methods approaches needed | 181 | "Social media data analysis complements these traditional approaches." | ✓✓ |
| A12 | Deng et al. RCM on social media (first-gen) | 181 | Cites and summarizes Deng et al. 2022 (RCM). | ✓ (secondary) |
| A13 | Prevalence ("more than one-third follow this route") | 151 | No national prevalence statistic. | — |
| A14 | Transfer shock = GPA decline in first two semesters | 153 | Only references transfer-shock literature; no GPA-drop finding of its own. | — |
| A15 | Predictive models biased on narrow populations | 155, 179 | Not addressed (no predictive-modeling/fairness analysis). | — |
| A16 | Cold-start / per-institution labeled-data scarcity | 183 | Not addressed. | — |

---

## Table B — What `nguyen2025school` (Reddit barrier framework) can support

| # | Claim in `main-v3.tex` | Lines | What the paper actually shows | Support |
|---|------------------------|-------|-------------------------------|---------|
| B1 | **Prevalence: ~one-third transfer** | 151 | "Nearly 38% of college students in the United States transfer at least once every six years (Shapiro et al., 2018)." *Cites primary — prefer Shapiro 2018 itself.* | ✓ (via primary) |
| B2 | Coordination / articulation / credit-recognition problems | 151 | School-centered themes: "Inconsistent Credit Transfer Policies," "Eligibility Gaps," opaque articulation (IGETC/AS-T). | ✓✓ |
| B3 | Articulation, uneven credit, limited pre-transfer visibility | 151 | Same school-centered cluster; explicit credit-loss/articulation findings. | ✓✓ |
| B4 | Financial pressure + weaker belonging | 151 | "Aid, Scholarship & Housing Instability"; student-centered "Social Belonging & Campus Fit," "Mental Health." | ✓✓ |
| B5 | Measurable factors don't capture full experience | 153 | "emphasis on measurable outcomes rather than the complex reality of student voice." | ✓✓ |
| B6 | Social support / mentorship / engagement hard to capture | 153 | Student-centered themes (belonging, career readiness, identity) absent from institutional records. | ✓ |
| B7 | SCCT framing: person inputs / transfer receptivity / self-efficacy | 175 | "Social Cognitive Theory … linked self-efficacy, outcome expectations, and institutional receptiveness" (cites Ty 2024, Vargas 2022). | ✓ (secondary) |
| B8 | Advising is central; large caseloads / under-resourced advising | 155, 177 | "under-resourced advising systems frequently force students to rely on informal help"; "Advising, Communication & Platform Failures." | ✓✓ |
| B9 | Advising dashboards/systems reproduce registrar data, omit transfer context | 155, 179 | "based on institutional statistics … may overlook … emotional or identity-centered experiences." | ✓ |
| B10 | Transfer student capital | 177 | "Townsend & Wilson (2006) and Maliszewski & Hayes (2020) … emphasized the need of transfer student capital (TSC)." | ✓ (secondary) |
| B11 | **Students turn to Reddit / peer forums when advising fails** | 177 | "many people use Reddit and other peer forums … as a last option when institutional advice fails." | ✓✓ |
| B12 | Tech tools / registrar-LMS systems miss transfer-specific variables | 179 | Whole premise; survey vs. Reddit comparison shows institutional data misses identity/mental-health themes. | ✓✓ |
| B13 | Few transfer-specific systems; calls for AI advising | 155, 179 | "guide the creation of AI-powered advising systems by recognizing non-academic factors." | ✓ |
| B14 | Mixed-methods needed | 181 | Mixed-method by design (Reddit + 161-response survey, same pipeline). | ✓✓ |
| B15 | Records split across institutions / context doesn't follow student | 183 | Credit-transfer fragmentation themes; not framed as record-portability per se. | ✓ |
| B16 | Transfer shock = GPA decline | 153 | Mentions GPA loss from credit issues; not the transfer-shock GPA-drop construct. | — |
| B17 | Predictive models biased on narrow populations | 155, 179 | Argues surveys miss populations, but no model-bias analysis. | — |
| B18 | Cold-start / labeled-data scarcity | 183 | Not addressed. | — |

---

## Table C — Master claim × citation-reduction matrix (Intro + Lit Review)

Columns: **Now** = current cite count; **New support** = which new paper(s) help (A/B and strength);
**✅ Recommended (self-cites ON)** = the citation set I recommend given your decisions (D1: self-citations
OK; D2: keep CC→4yr wording, use `monaghan2015` not Shapiro); **New paper cited** = which of the two new
papers (`standfast2024reddit` / `nguyen2025school`) the recommended set actually uses, or "—";
**Δ** = change in cite count; **Conf** = confidence.

> Recommendation only — nothing is applied to the paper. **Per your decisions:** self-citations are ON,
> so the Recommended column commits to the new papers where they are the strongest fit (12 new-self-cite
> placements total — see the tally under §1). The **🚫 no-self-citation fallback** for every one of those
> placements is in **Table D**, below the headline numbers.

### Introduction

| # | Lines | Claim (short) | Current cites | Now | New support | ✅ Recommended (self-cites ON) | New paper cited | Δ | Conf | Applied to main-v3? |
|---|-------|---------------|---------------|-----|-----|------------------|------|----|------|------|
| 1 | 151 | >1/3 follow this route | `ishitani2018student`, `roksa2008credits` | 2 | B1 (but mismatch) | **`monaghan2015`** — your call: keep CC→4yr wording, no Shapiro reword | — | −1 | Med | ✅ applied |
| 2 | 151 | More common in CS/STEM + URM/first-gen/low-income | `wali2025transfer`, `computingtransfer2024`, `jabbar2019complex` | 3 | A2/B-context | **`computingtransfer2024`, `wali2025transfer`** (drop `jabbar2019complex`) | — | −1 | Med | ✅ applied |
| 3 | 151 | More affordable route | `socialcognitive2022`, `factoranalysis2023` | 2 | A1, B4 | **`factoranalysis2023`** | — | −1 | High | ✅ applied |
| 4 | 151 | Coordination problems sending↔receiving | `topicmodeling2024`, `factoranalysis2023` | 2 | A2✓✓, B2✓✓ | **`nguyen2025school`** | `nguyen2025school` | −1 | High | ✅ applied |
| 5 | 151 | Articulation, uneven credit, limited pre-transfer visibility | `nguyen2024community`, `roksa2008credits`, `preposttransfer2014` | 3 | B3✓✓ | **`nguyen2024community`, `roksa2008credits`** | — | −1 | High | ✅ applied |
| 6 | 151 | Financial pressure + weaker belonging | `computingtransfer2024`, `wang2020road`, `socialcognitive2022` | 3 | A3, B4✓✓ | **`computingtransfer2024`, `nguyen2025school`** | `nguyen2025school` | −1 | Med | ✅ applied |
| 7 | 153 | Transfer shock (GPA + belonging, first 2 sem.) | `jaggars2025`, `laanan2010adjustment` | 2 | A14/B16 — | **`jaggars2025`** | — | −1 | High | ✅ applied |
| 8 ⚑ | 153 | Higher attrition + measurable factor list (GPA, credits, tests, distance, aid) | `wang2020road`, `factoranalysis2023`, `jaggars2025`, `thiry2023`, `townsend2009` | **5** | A1, B-context | applied as `jaggars2025` + `roksa2008credits` + `factoranalysis2023`; umbach not needed (see §2b) | — | **−2** | Med | ✅ applied — ⚑ still review D3 (trim distance/aid?) |
| 9 | 153 | Variables don't capture full experience | `topicmodeling2024`, `socialcognitive2022` | 2 | A4✓✓, B5✓✓ | **`nguyen2025school`** | `nguyen2025school` | −1 | High | ✅ applied |
| 10 | 153 | Social support/mentorship/engagement hard to capture | `topicmodeling2024`, `thiry2023` | 2 | A5, B6 | **`thiry2023`** | — | −1 | Med | ✅ applied |
| 11 | 155 | Advising is an important factor | `topicmodeling2024`, `preposttransfer2014`, `lukszo2020`, `thiry2023` | **4** | A6✓✓, B8✓✓ | **`thiry2023`, `lukszo2020`** | — | −2 | High | ✅ applied |
| 12 | 155 | Large caseloads limit individualized advising | `topicmodeling2024`, `preposttransfer2014` | 2 | A6, B8✓✓ | **`preposttransfer2014`, `nguyen2025school`** | `nguyen2025school` | 0 | Med | ✅ applied |
| 13 | 155 | Dashboards reproduce registrar/early-alert, omit transfer context | `nguyen2024community`, `preposttransfer2014` | 2 | B9 | **`nguyen2024community`, `nguyen2025school`** | `nguyen2025school` | 0 | Med | ✅ applied |
| 14 | 155 | Predictive models misclassify risk / reproduce inequity | `computingtransfer2024`, `socialcognitive2022` | 2 | — | **keep both** (no model-bias support in new papers) | — | 0 | — | — unchanged |
| 15 | 155 | Combine admin data with experiential data | `topicmodeling2024`, `socialcognitive2022` | 2 | A4✓✓, B5✓✓ | **`nguyen2025school`** | `nguyen2025school` | −1 | High | ✅ applied |

> **Provenance + verification note for row 1 (Shapiro et al. 2018).** ✅ **Now verified against the full
> report** (`past-papers/Shapiro_2018.pdf`, 29 pp., National Student Clearinghouse Signature Report 15).
> The **38.0%** figure is real and stated repeatedly (Executive Summary; Section 1, p.9: *"The total six
> year transfer rate for the fall 2011 cohort was 38.0 percent"*; Discussion, p.19: *"almost two in
> five"*). N = 2,816,648; authoritative national source.
>
> ⚠️ **But it does NOT cleanly support the sentence as written.** Shapiro defines transfer as *any*
> institutional change — *"irrespective of the timing, direction, or location of the move"* — which
> **includes reverse (4yr→2yr), lateral, and summer-swirl transfers**, and the report explicitly
> *"investigates all types of transfer, not just two- to four-year transfers."* The 38% is therefore the
> **all-directions mobility rate**, not the **community-college→four-year (vertical) route** that line 151
> describes (*"begin at community colleges and later transfer to four-year universities… follow this
> route"*). This is the **same specificity mismatch** the prior audit flagged for `ishitani2018student`.
> Vertical figures in the report are lower/split (two-year starters transfer ~37%; ~50–59% of those go
> to a four-year institution).
>
> **✅ YOUR DECISION (D2): option (B) — no reword.** Keep the CC→4yr framing and cite **`monaghan2015`**
> (*The Community College Route to the Bachelor's Degree*) — already in `references.bib` and itself cited
> *by* Shapiro. **PDF now supplied and verified:** national longitudinal transcript data + propensity
> scores; opens with "community colleges enroll ~40% of undergraduates" as the stepping-stone to a BA —
> a clean on-point source for "the community college route" without changing the sentence. (Minor nuance:
> Monaghan stresses that many CC entrants *don't* complete, so the "follow this route" framing is fine
> but "to complete their degrees" is doing some work — keep as is or soften slightly.) Option A
> (reword + `shapiro2018transfer`) remains a fallback only.

### Literature Review

| # | Lines | Claim (short) | Current cites | Now | New support | ✅ Recommended (self-cites ON) | New paper cited | Δ | Conf | Applied to main-v3? |
|---|-------|---------------|---------------|-----|-----|------------------|------|----|------|------|
| 16 | 173 | Research splits into two areas | `factoranalysis2023` | 1 | — | keep `factoranalysis2023` | — | 0 | — | — unchanged |
| 17 | 175 | Ty SCCT person inputs / receptivity | `computingtransfer2024` | 1 | B7 | keep (named paper) | — | 0 | — | — unchanged |
| 18 | 175 | Self-efficacy/goal-setting improve after transfer | `socialcognitive2022`, `topicmodeling2024` | 2 | B7 | **`socialcognitive2022`** | — | −1 | High | ✅ applied |
| 19 | 175 | Financial/reputation/distance/family factors | `factoranalysis2023` | 1 | A1 | keep (primary) | — | 0 | — | — unchanged |
| 20 | 175 | Regression: post-transfer GPA vs race/first-gen | `computingtransfer2024` | 1 | — | keep (named) | — | 0 | — | — unchanged |
| 21 | 175 | Topic modeling of open-ended + social media | `topicmodeling2024` | 1 | A8✓✓ | **`standfast2024reddit`** (swap — it *is* Reddit topic modeling, closer fit) | `standfast2024reddit` | 0 | — | ✅ applied |
| 22 | 177 | Transfer student capital | `laanan2010adjustment`, `lukszo2020` | 2 | A9, B10 | **`lukszo2020`** | — | −1 | Med | ✅ applied |
| 23 | 177 | **Students turn to Reddit/Discord/peer forums** | `topicmodeling2024`, `nguyen2024community` | 2 | A10✓✓, B11✓✓ | **`standfast2024reddit`** (direct; replaces mismatched `nguyen2024community`) | `standfast2024reddit` | −1 | High | ✅ applied |
| 24 | 177 | Relationship-based advising eases shock/belonging | `thiry2023`, `jaggars2025` | 2 | B8 | **`thiry2023`** | — | −1 | Med | ✅ applied |
| 25 | 177 | Advisors can't keep up with articulation + caseloads | `preposttransfer2014`, `nguyen2024community` | 2 | A6, B8✓✓ | **`nguyen2024community`, `nguyen2025school`** | `nguyen2025school` | 0 | Med | ✅ applied |
| 26 | 179 | Tech tools built for native populations | `nguyen2024community` | 1 | B12 | keep | — | 0 | — | — unchanged |
| 27 | 179 | Rely on registrar/LMS, miss transfer variables | `nguyen2024community`, `topicmodeling2024` | 2 | B12✓✓ | **`nguyen2024community`, `nguyen2025school`** | `nguyen2025school` | 0 | Med | ✅ applied |
| 28 | 179 | Models on narrow populations are biased | `socialcognitive2022`, `computingtransfer2024` | 2 | — | keep both | — | 0 | — | — unchanged |
| 29 | 179 | Few transfer-specific prototype systems | `topicmodeling2024`, `socialcognitive2022` | 2 | A/B (future-systems framing) | **`topicmodeling2024`** | — | −1 | Low | ✅ applied |
| 30 | 181 | Mixed-methods approaches needed | `socialcognitive2022`, `wang2020road` | 2 | A11✓✓, B14✓✓ | **`nguyen2025school`** (the paper *is* mixed-method) | `nguyen2025school` | −1 | High | ✅ applied |
| 31 | 181 | Deng et al. RCM social media | `deng2021` | 1 | A12/B | keep (named) | — | 0 | — | — unchanged |
| 32 | 181 | Thiry et al. mixed-methods STEM transfer | `thiry2023` | 1 | — | keep (named) | — | 0 | — | — unchanged |
| 33 | 183 | Records split across institutions | `nguyen2024community`, `roksa2008credits` | 2 | B15 | **`roksa2008credits`** | — | −1 | Med | ✅ applied |
| 34 | 183 | Broader context rarely follows student | `roksa2008credits`, `nguyen2024community` | 2 | B15 | **`nguyen2024community`** | — | −1 | Med | ✅ applied |
| 35 | 183 | Info undocumented / inaccessible to receiver | `preposttransfer2014`, `topicmodeling2024` | 2 | B12 | **`preposttransfer2014`** | — | −1 | Med | ✅ applied |
| 36 | 183 | Cold-start: each institution builds own dataset | `coleman2019coldstart` | 1 | — | keep | — | 0 | — | — unchanged |
| 37 | 183 | Cold-start serious in small cohorts | `coleman2019coldstart`, `socialcognitive2022`, `roksa2008credits` | 3 | — | **`coleman2019coldstart`** | — | −2 | High | ✅ applied |

### Methodology (Section 3) and Evaluation (Section 4)

These sections are far lighter, and several are **canonical method/theory citations that must stay
single** (a TAM, Bandura, Tinto citation is correct as one source — do not touch). The new papers only
help the few domain-background sentences that re-stack the same three transfer keys.

| # | Lines | Claim (short) | Current cites | Now | New support | ✅ Recommended (self-cites ON) | New paper cited | Δ | Conf | Applied to main-v3? |
|---|-------|---------------|---------------|-----|-----|------------------|------|----|------|------|
| M1 | 295 | Credit/articulation, transfer shock, belonging, financial precarity rarely captured in institutional systems | `topicmodeling2024`, `computingtransfer2024`, `socialcognitive2022` | **3** | A4✓✓, B12✓✓ | **`nguyen2025school`** | `nguyen2025school` | **−2** | High | ✅ applied |
| M2 | 295 | Advisors spend time gathering data from many sources | `preposttransfer2014`, `thiry2023` | 2 | A6, B8 | **`preposttransfer2014`** | — | −1 | Med | ✅ applied |
| M3 | 297 | Dimensions of success: self-efficacy, commitment, integration, career clarity | `factoranalysis2023`, `topicmodeling2024`, `computingtransfer2024` | **3** | B7 | **`factoranalysis2023`** | — | **−2** | Med | ✅ applied |
| M4 | 297 | "Our earlier factor-analysis grouped variables into clusters" | `factoranalysis2023` | 1 | — | keep (named self-reference) | — | 0 | — | — unchanged |
| M5 | 337 | "Our earlier factor-analysis linked indicators to constructs" | `factoranalysis2023` | 1 | — | keep (named self-reference) | — | 0 | — | — unchanged |
| M6 | 341 | Certain constructs are stronger predictors than logistical vars | `factoranalysis2023`, `computingtransfer2024` | 2 | B-context | **`factoranalysis2023`** | — | −1 | Med | ✅ applied |
| M7 | 341 | Prior research identifies some variables as more predictive | `factoranalysis2023`, `computingtransfer2024`, `socialcognitive2022` | **3** | B-context | **`computingtransfer2024`** (M6+M7 adjacent — see §2) | — | **−2** | Med | ✅ applied |
| M8 | 360 | Self-efficacy a strong predictor (priority table) | `bandura1997` | 1 | — | keep (canonical theory) | — | 0 | — | — unchanged |
| M9 | 362 | Financial stability affects retention (priority table) | `socialcognitive2022` | 1 | B4 | keep (or swap to `factoranalysis2023`) | — | 0 | — | — unchanged |
| M10 | 364 | Institutional commitment → persistence (priority table) | `tinto1993` | 1 | — | keep (canonical theory) | — | 0 | — | — unchanged |
| E1 | 670 | TAM framework for the feedback survey | `davis1989` | 1 | — | keep (canonical instrument) | — | 0 | — | — unchanged |

**New-paper placements in the recommended (self-cites ON) plan — 12 total:**
`nguyen2025school` ×10 (rows 4, 6, 9, 12, 13, 15, 25, 27, 30, M1) and `standfast2024reddit` ×2
(rows 21, 23).

---

## Table D — No-self-citation fallback (if you later avoid the two new papers)

For each of the 12 placements above, this is the best citation **without** `standfast2024reddit` /
`nguyen2025school`. Read with one caveat that changes the picture:

> **⚠️ Four of your *current* citations are already team self-citations:** `factoranalysis2023`
> (Wang et al.), `topicmodeling2024` (MacDonald et al.), `computingtransfer2024` (Ty et al.), and
> `socialcognitive2022` (Vargas et al.) are all authored by the ACOSUS group. So a *strict* "no
> self-citation" policy is a much larger change than dropping the two new papers — several fallbacks
> below just shift to **another** team paper. Genuinely external fallbacks are marked **(ext)**.

| Claim | ✅ Self-cite recommendation | 🚫 Best fallback without the 2 new papers | Note |
|-------|----------------------------|--------------------------------------------|------|
| 4 — coordination problems | `nguyen2025school` | `nguyen2024community` **(ext)** or `roksa2008credits` **(ext)** | clean external options exist |
| 6 — financial + belonging | `computingtransfer2024`, `nguyen2025school` | `computingtransfer2024` + `wang2020road` **(ext)** | external `wang2020road` covers belonging/finance |
| 9 — don't capture full experience | `nguyen2025school` | `topicmodeling2024` (team) or `wang2020road` **(ext)** | external is weaker here |
| 12 — large caseloads | `preposttransfer2014`, `nguyen2025school` | `preposttransfer2014` **(ext)**; add Townsend & Wilson 2006 / Maliszewski & Hayes 2020 (not yet in bib) | strongest fix needs a *new* external bib entry |
| 13 — dashboards reproduce registrar data | `nguyen2024community`, `nguyen2025school` | `nguyen2024community` + `dietzuhler2013` **(ext, already in bib)** | `dietzuhler2013` is the natural analytics source |
| 15 — combine admin + experiential | `nguyen2025school` | `socialcognitive2022` (team) or `topicmodeling2024` (team) | no clean external in current bib |
| 21 — topic modeling of social media | `standfast2024reddit` | `topicmodeling2024` (team) | only team papers fit; **no external** |
| 23 — Reddit/Discord/peer forums | `standfast2024reddit` | `deng2021` **(ext, partial)** | **weakest spot without the new papers** — `deng2021` is social-media but not Reddit-help-seeking; no strong external in bib |
| 25 — advisors can't keep up | `nguyen2024community`, `nguyen2025school` | `nguyen2024community` + `preposttransfer2014` **(ext)** | clean external pair |
| 27 — registrar/LMS miss variables | `nguyen2024community`, `nguyen2025school` | `nguyen2024community` + `dietzuhler2013` **(ext)** | `dietzuhler2013` (already in bib) |
| 30 — mixed-methods needed | `nguyen2025school` | `wang2020road` **(ext)** | clean external; `wang2020road` is explicitly mixed-methods |
| M1 — institutional systems miss variables | `nguyen2025school` | `topicmodeling2024` + `computingtransfer2024` (both team — the current cites) | external would need `dietzuhler2013` + `nguyen2024community` |

**Takeaways for the no-self-citation route:**
- **Clean external fallbacks exist** for rows 4, 6, 13, 25, 27, 30 (using `nguyen2024community`,
  `roksa2008credits`, `wang2020road`, `preposttransfer2014`, `dietzuhler2013` — all already in the bib).
- **Two spots have no good external source** in the current bib: row 23 (Reddit/Discord — only `deng2021`
  partially) and row 21 (topic modeling — only team papers). These are precisely where the two new
  papers are most valuable, so dropping them costs the most here.
- **Row 12** would need a brand-new external entry (Townsend & Wilson 2006 or Maliszewski & Hayes 2020)
  to be done well without self-citation.

---

## 1. Headline numbers

| Section | Current cite *instances* | Proposed minimal | Reduction |
|---------|--------------------------|------------------|-----------|
| Introduction (claims 1–15) | 38 | 23 | −15 |
| Literature Review (claims 16–37) | 36 | 25 | −11 |
| Methodology (claims M1–M10) | 18 | 10 | −8 |
| Evaluation (claim E1) | 1 | 1 | 0 |
| **Total** | **93** | **59** | **−34 (≈37%)** |

This counts citation *instances* (the in-text density that makes the section feel heavy), not distinct
bib keys. Most reductions just drop a redundant stacked source; the new papers specifically enable the
high-value ones — claims **4, 6, 9, 15, 23, 30, M1, M3** — and **fix** the two weakest spots the prior
audit flagged (the Reddit/Discord claim at line 177, claim 23; and the registrar/LMS claims, 13/27). The
Methodology gains (M1, M3, M6/M7) are pure de-duplication: the same three transfer keys
(`factoranalysis2023` / `computingtransfer2024` / `socialcognitive2022`) are re-stacked there and can
each be reduced to the single primary source. **Method/theory citations stay single** — `bandura1997`,
`tinto1993`, `davis1989` are correct as one source each and are untouched.

**Self-citation tally (with D1 = ON).** The recommended plan adds the two new papers in **12** places
(`nguyen2025school` ×10, `standfast2024reddit` ×2). Note that the paper *already* self-cites four team
works (`factoranalysis2023`, `topicmodeling2024`, `computingtransfer2024`, `socialcognitive2022`), so
total team self-citations rise rather than the reductions being purely external. That is fine given your
decision; just be aware some reviewers scan for self-citation density, and Table D shows the external
fallback for every one of the 12 if you ever want to dial it back.

---

## 2. Citation pairs that travel together (the "two adjacent lines, same two papers" case)

The example you gave — two consecutive sentences each citing roughly the same pair — shows up here in a
few real spots. In each case **one** source carries both sentences, so the pair can collapse:

| Pair of claims | Lines | Shared/overlapping cites | Single source that covers both | Action |
|----------------|-------|--------------------------|--------------------------------|--------|
| "don't capture full experience" (9) **and** "combine admin + experiential data" (15) | 153 & 155 | `topicmodeling2024` + `socialcognitive2022` on *both* | `nguyen2025school` (its entire thesis) — or `topicmodeling2024` once | Cite once across the two; drop the second stack |
| "advising important" (11) **and** "large caseloads" (12) | 155 | `topicmodeling2024` + `preposttransfer2014` on *both* | `preposttransfer2014` (capacity) + one of `thiry2023`/`nguyen2025school` | Collapse to two distinct keys total, not four instances |
| "records split" (33), "context doesn't follow" (34), "info inaccessible" (35) | 183 | `roksa2008credits` + `nguyen2024community` rotate across all three | split them: `roksa2008credits` / `nguyen2024community` / `preposttransfer2014` (one each) | 6 instances → 3 |
| "rely on registrar/LMS" (27) **and** "dashboards reproduce registrar data" (13) | 179 & 155 | `nguyen2024community` on both | `nguyen2025school` is the stronger second source for both | Use `nguyen2024community` + `nguyen2025school`, reused |
| "stronger predictors" (M6) **and** "some variables more predictive" (M7) | 341 (same paragraph, consecutive sentences) | `factoranalysis2023` + `computingtransfer2024` on *both*; M7 adds `socialcognitive2022` | `factoranalysis2023` carries the empirical priority-weighting point | Collapse 5 instances → 2 distinct keys across the two sentences |

---

## 2b. Row 8 deep-dive — best supporting papers (your request)

Row 8 (line 153) bundles **two** claims that need different sources:
**(8a)** transfer students show *higher attrition* than native students; and
**(8b)** *quantitative studies identify measurable factors* — cumulative GPA, accepted credits,
standardized test scores, distance between institutions, financial aid — associated with
retention/completion.

**Fit of the 5 current cites (grounded in the local summaries):**

| Current cite | What it is | Fit for row 8 |
|---|---|---|
| `jaggars2025` | 25,565 transfer students; GPA drop/rebound **predict departure** | ✓✓ Strong — *attrition* + GPA |
| `roksa2008credits` | Regression on **bachelor's attainment / time-to-degree**; vars incl. credits, **test score**, SES | ✓✓ Strong — credits + test scores → completion *(not currently cited in row 8)* |
| `monaghan2015` ✅ verified | National longitudinal transcript data + propensity scores; **credit loss → lower BA completion** | ✓✓ Strong — accepted credits → completion |
| `factoranalysis2023` | In-house factor analysis; financial, GPA, distance as transfer **decision** factors | ✓ Partial — GPA/financial/distance, but decision-framed |
| `wang2020road` | ANN predicting **transfer intent** (attitudes, GPA, employment) | ✗ Mismatch — outcome is *intent*, not retention; no test scores/distance |
| `thiry2023` | Qualitative **support-strategy framework** | ✗ Mismatch — not "quantitative measurable factors" |
| `townsend2009` | Qualitative **integration → persistence** (N=12) | ✗ Weak — persistence framing only |

**Best papers, ranked:**

- **(8a) attrition:** `jaggars2025` (best, large-N departure prediction — keep); `ishitani2018student`
  (*Student Transfer-Out Behavior*, already in bib — strong second).
- **(8b) measurable factors → retention/completion:**
  - **`roksa2008credits`** — strong for accepted credits + test scores → bachelor's attainment.
  - **`monaghan2015`** ✅ **now verified** (PDF supplied) — *The Community College Route to the Bachelor's
    Degree*; national transcript data + propensity scores; **credit loss → lower BA completion**. Best
    source for the "accepted credits → completion" item. ⚠️ It *refutes* financial aid as a mechanism, so
    do **not** cite it for "financial aid."
  - **`factoranalysis2023`** — in-house backing for GPA, financial, distance.
  - **`umbach2019`** — would have been ideal (*…Individual Predictors*) but **you can't access it**; not
    needed given the three above. External substitutes if you want a dedicated predictors paper: Jenkins
    & Fink 2016 (*Tracking Transfer*, CCRC), Crisp & Nuñez 2014, or Xu/Jaggars/Fletcher — **none in the
    repo; would need sourcing + verification.**

**Recommended replacement (5 → 3, all verified, no umbach2019 needed):**
**`jaggars2025` + `roksa2008credits` + `factoranalysis2023`** — with **`monaghan2015`** as the strong
add/alternative for credits→completion.

**Honest caveat:** no single available paper supports *all five* listed items as
retention/completion predictors. **"Distance between institutions"** and **"financial aid"** are the
weakest as *completion* predictors (better supported as transfer-*decision* factors via
`factoranalysis2023`). Either add `factoranalysis2023` for those two, or trim the list to
GPA/credits/test scores. The two new papers do **not** support this quantitative-retention claim.
**Applied:** `jaggars2025` + `roksa2008credits` + `factoranalysis2023` (no reword). ⚑ Your remaining
D3 call is only whether to trim "distance"/"financial aid" (which would let you drop `factoranalysis2023`
and reach 2 cites).

---

## 3. Where the new papers do **NOT** help (keep current citations)

So the verification is honest about coverage, these claims get **no** lift from the two new papers and
should retain their present sources:

- **Transfer shock as a GPA-drop construct** (7, 24) — keep `jaggars2025` / `laanan2010adjustment`.
- **Algorithmic bias / models trained on narrow cohorts** (14, 28) — keep `computingtransfer2024`,
  `socialcognitive2022`. Neither new paper does predictive modeling or fairness analysis.
- **Cold-start / per-institution labeled-data scarcity** (36, 37) — keep `coleman2019coldstart`.
- **National prevalence statistic** (1) — per D2 the recommendation is **`monaghan2015`** (keep CC→4yr
  wording). Shapiro 2018 is verified but measures all-directions transfer, so it is not used.
- **Canonical method/theory citations** (M8 `bandura1997`, M10 `tinto1993`, E1 `davis1989`) — these are
  single, correct, foundational references. The new papers are not substitutes and these should never
  be stacked or replaced.

---

## 4. Verification run (completeness check)

**Method.** Every `\cite{...}` group in the **entire** [main-v3.tex](current/overleaf/main-v3.tex) was
enumerated via `grep -n '\cite' main-v3.tex` and assigned a claim number. All 49 `\cite` groups in the
file fall in four sections; the Conclusion (Section 5) and Acknowledgments contain **no** citations.

**Coverage — Introduction.** 15 claim-cite groups across lines 151 / 153 / 155. All 15 appear in Table C
(rows 1–15). ✓
**Coverage — Literature Review.** 22 claim-cite groups across lines 173 / 175 / 177 / 179 / 181 / 183.
All 22 appear in Table C (rows 16–37). ✓
**Coverage — Methodology.** 10 claim-cite groups across lines 295 / 297 / 337 / 341 / 360 / 362 / 364.
All 10 appear in Table C (rows M1–M10). ✓
**Coverage — Evaluation.** 1 claim-cite group at line 670 (TAM). Appears as row E1. ✓
**Coverage — Conclusion / Acknowledgments.** 0 `\cite` groups (confirmed by grep). Nothing to reduce. ✓

**Every distinct bib key used anywhere in the paper is accounted for (21 keys):**
`ishitani2018student, roksa2008credits, wali2025transfer, computingtransfer2024, jabbar2019complex,
socialcognitive2022, factoranalysis2023, topicmodeling2024, nguyen2024community, preposttransfer2014,
jaggars2025, laanan2010adjustment, wang2020road, thiry2023, townsend2009, lukszo2020, deng2021,
coleman2019coldstart` (Intro/Lit Review) plus `bandura1997, tinto1993, davis1989`
(Methodology/Evaluation). Each is referenced in at least one Table C row. ✓

**Keys in `references.bib` but NOT cited anywhere in `main-v3.tex`** (so not part of this reduction):
`schulten2022collaboration, denley2014predictive, monaghan2015, umbach2019, dietzuhler2013,
turnquest2024`. Several are candidates to *add* if a claim needs a non-self primary source —
`dietzuhler2013` (learning-analytics perspective) for the registrar/LMS claims (rows 13/27),
`turnquest2024` (engagement) for the campus-engagement claim (row 10), `umbach2019`/`monaghan2015` for
the prevalence/predictor claims (rows 1, 8). ✓

**New papers' bibliographic status:** neither `standfast2024reddit` nor `nguyen2025school` is in
[references.bib](current/overleaf/references.bib). Ready-to-paste entries are in §5 below. ✓

**Source-context coverage (what has been read/verified).**
- ✅ **Full text read:** `standfast2024reddit`, `nguyen2025school`, `shapiro2018transfer`,
  **`monaghan2015`** (PDF supplied this session), `jaggars2025`, `roksa2008credits`, `townsend2009`,
  `wang2020road`.
- ✅ **Local summary available:** the 4 team papers + the rest of `ref/` (`preposttransfer2014`,
  `thiry2023`, `lukszo2020`, `jabbar2019complex`, `nguyen2024community`, `deng2021`, `dietzuhler2013`,
  `turnquest2024`, `coleman2019coldstart`, `laanan2010adjustment`, `ishitani2018student`,
  `wali2025transfer`, `schulten2022collaboration`, `denley2014predictive`).
- ❌ **No context (not read — title/role only):** **`umbach2019`** (user cannot access; row-8 reco now
  routes around it). Canonical works with no repo doc but well-established: `bandura1997`, `tinto1993`,
  `davis1989`.

**Consistency check vs. the existing audit** ([claim-audit-main-v3.md](current/claim-audit-main-v3.md)):
the four "highest-priority problems" it lists are all addressed here — prevalence (row 1), dashboard
claim (row 13), registrar/LMS claim (row 27), Reddit/Discord claim (row 23). ✓

### Open questions for you

These are the same items as the **⚑ Decisions & reminders** checklist at the top of this file, kept here
in context:

1. **D1 — Self-citation appetite.** Rows 4, 6, 9, 15, 23, 30, M1 lean on the team's own DSI papers. How
   many self-citations are you comfortable adding to Intro+Lit Review? (Affects how aggressively we
   apply `+A`/`+B`.)
2. **D2 — Prevalence fix (row 1).** Add **Shapiro et al. 2018** as a new primary source, or soften the
   "more than one-third" wording instead? Neither current cite nor the new papers prove it directly.
   See the provenance note under the Introduction table — Shapiro came from `nguyen2025school`'s
   reference list and still needs a quick verification against the original report.
3. **D3 — Row 8: you will review this yourself.** Marked ⚑ in the table; **not** to be auto-applied. The
   heaviest claim (five cites). You will personally decide whether to drop `wang2020road` / `thiry2023`
   / `townsend2009` or split the sentence. This is a reminder, not a question for me.
4. **D4 — M9 cosmetic (line 362).** Keep `socialcognitive2022` or swap to `factoranalysis2023` for the
   "Financial Stability" priority-table row? Cosmetic, your call. (Whole-paper scope is otherwise
   complete — Conclusion/Acknowledgments have no citations.)

---

## 5. BibTeX for the two new papers (for when you choose to add them)

```bibtex
@inproceedings{standfast2024reddit,
  title     = {Deciding on a College Transfer: Uncovering Transition Queries and Concerns via Reddit Topic Modeling},
  author    = {Standfast, Jason and Franco, Julian and Caraballo, Rudy and Vargas, Kay and Wan, Yun and Wang, Xiwei and Bogle, Sherrene and Aggarwal, Palvi and Rayana, Shebuti},
  booktitle = {Proceedings of the Decision Sciences Institute (DSI) Annual Conference},
  year      = {2024}
}

@inproceedings{nguyen2025school,
  title     = {School or Student? A Mixed-Method Analysis on Reddit Data for Transfer Barrier Identification},
  author    = {Nguyen, Phuong Minh and Maldonado, Donnoban and Ty, Cheyenne and Wan, Yun and Wang, Xiwei and Bogle, Sherrene and Aggarwal, Palvi and Rayana, Shebuti},
  booktitle = {Proceedings of the Decision Sciences Institute (DSI) Annual Conference},
  year      = {2025}
}
```

*Note:* `nguyen2025school` ≠ the already-present `nguyen2024community` (David Van Nguyen). Keep both keys
distinct.

**Shapiro et al. 2018 — ✅ verified against the full report (`past-papers/Shapiro_2018.pdf`). Use only
with D2 option (A) wording (all-directions mobility), not for a community-college→four-year claim:**

```bibtex
@techreport{shapiro2018transfer,
  title       = {Transfer and Mobility: A National View of Student Movement in Postsecondary Institutions, Fall 2011 Cohort},
  author      = {Shapiro, Doug and Dundar, Afet and Huie, Faye and Wakhungu, Phoebe Khasiala and Bhimdiwali, Ayesha and Nathan, Angel and Hwang, Youngsik},
  institution = {National Student Clearinghouse Research Center},
  type        = {Signature Report},
  number      = {15},
  address     = {Herndon, VA},
  month       = {July},
  year        = {2018},
  note        = {ED592100. Verified: 38.0\% six-year transfer rate, fall 2011 cohort (N=2,816,648). NOTE: this is the ALL-DIRECTIONS transfer/mobility rate, not vertical CC-to-4yr transfer. For the "community college route" framing use monaghan2015 instead.}
}
```

*Note: the report's own "Suggested Citation" page prints the last author as "Youngsik, H." — that is a
typo for surname **Hwang** (see the Authors page, "Youngsik Hwang"); the BibTeX above uses the correct
form.*

