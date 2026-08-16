# AI Revision Reference Archive

This folder archives every bibliography entry that appears in `main-v4-ai-edit-references.bib` but not in `main-v4-submitted-references.bib`.
The comparison yields eight added entries.
The files were retrieved on August 7, 2026, from official product pages, journal hosts, or arXiv.

## Inventory

| BibTeX key | Reference type | Local source | Searchable Markdown | Current paper use |
| --- | --- | --- | --- | --- |
| `assistResource2026` | Official web page | Web source only | [ASSIST source notes](assistResource2026.md) | Cited in the system comparison |
| `collegeSourceTES2026` | Official web page | Web source only | [TES source notes](collegeSourceTES2026.md) | Cited in the system comparison |
| `transferologySupport2026` | Official support page | Web source only | [Transferology source notes](transferologySupport2026.md) | Cited in the system comparison |
| `navigate3602026` | Official web page | Web source only | [Navigate360 source notes](navigate3602026.md) | Present in the AI bibliography but not cited in the current TeX source |
| `mathieson1995transfer` | Journal article | [PDF](mathieson1995transfer.pdf) | [PDF text extraction](mathieson1995transfer.pdf.md) | Present in the AI bibliography but not cited in the current TeX source |
| `nguyen2024optimal` | Journal article and open preprint | [PDF](nguyen2024optimal.pdf) | [PDF text extraction](nguyen2024optimal.pdf.md) | Cited in the research-prototype comparison |
| `mattei2014advising` | Open preprint | [PDF](mattei2014advising.pdf) | [PDF text extraction](mattei2014advising.pdf.md) | Cited in the research-prototype comparison |
| `mi2025smartcourse` | Open preprint | [PDF](mi2025smartcourse.pdf) | [PDF text extraction](mi2025smartcourse.pdf.md) | Cited in the research-prototype comparison |

## Retrieval notes

The ASSIST and Transferology pages were downloaded directly and transcribed into focused Markdown records.
The CollegeSource TES and EAB Navigate360 pages returned HTTP 403 to direct command-line requests.
Their Markdown records preserve the relevant content obtained from the official pages through indexed browser access and link back to the live sources.

The AIS eLibrary download endpoint also returned HTTP 403 for the 1995 Mathieson and Lederer article.
The same open-access article was downloaded from the Journal of Information Systems Education's official archive at `jise.org`.

The three newer research papers were downloaded from arXiv.
The Nguyen paper is the latest arXiv version linked to the published journal DOI in the bibliography.

## Conversion notes

Each PDF is retained unchanged alongside an automatically generated Markdown text extraction.
The Markdown files support searching and preliminary claim review, but the original PDF remains authoritative for exact wording, figures, tables, equations, and page references.

The 1995 article is an image-derived archival PDF with imperfect embedded OCR.
Its Markdown extraction contains visible OCR errors, so quotations and detailed claims must be checked against the PDF page image.

The conversion can be reproduced with [convert_pdf_sources.py](convert_pdf_sources.py).

## PDF integrity

| File | Pages | SHA-256 |
| --- | ---: | --- |
| `mathieson1995transfer.pdf` | 7 | `40843c36036562ce21527a8f029c70731fccae689278aeb25219b9008c8816bc` |
| `nguyen2024optimal.pdf` | 23 | `743cff51a6d621813e7775779c6e44a5c6e76de40f0dbd94d5d64d1c5aea6780` |
| `mattei2014advising.pdf` | 8 | `96df987b255c77a0fee7cbcb3dcaffe556980c2819d5a0ab5cc34315072ba60c` |
| `mi2025smartcourse.pdf` | 6 | `0d60a6e626a914774f65519f57ae2d7ddcaa98ff2525e5318bc3d4a45461d543` |

## Official source links

- [ASSIST Resource Center](https://resource.assist.org/)
- [CollegeSource TES](https://collegesource.com/transfer-tools/tes/)
- [Transferology support article](https://transferology-support.collegesource.com/article/51-how-to-use-will-my-courses-transfer)
- [EAB Navigate360](https://eab.com/solutions/navigate360/)
- [Mathieson and Lederer article page](https://jise.org/Volume7/n3/JISEv7n3p96.html)
- [Nguyen, Doroudi, and Epstein arXiv record](https://arxiv.org/abs/2307.04500)
- [Mattei et al. arXiv record](https://arxiv.org/abs/1312.4113)
- [SmartCourse arXiv record](https://arxiv.org/abs/2507.22946)

## Scope of this archive

This archive establishes local availability and provenance.
It does not by itself conclude that every sentence in the ACOSUS paper is supported.
A separate claim-by-claim evidence audit should cite exact pages or official-page sections from these local sources.
