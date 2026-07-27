# ACOSUS Presentation and Research Agent Guide

## Responsibility

This repository owns research papers, diagrams, presentation material, and supporting claims about ACOSUS.
It consumes verified facts from the runtime repositories but does not define runtime behavior.

## Source-of-truth rules

Verify architecture, endpoints, algorithms, metrics, feature status, and deployment claims against the pushed runtime branches before changing research material.
Separate implemented behavior, experimental local work, planned work, and study interpretation.
Do not describe local-only model work as deployed.
Do not infer numerical results from implementation alone.

Every quantitative claim must identify its dataset, evaluation method, time period, and reproducible source.
Do not expose participant identities, student records, credentials, private URLs, or environment values.

## Content areas

- Research paper source under `research-paper/`.
- Architecture and research diagrams under `diagrams/`.
- Presentation and resume evidence in repository Markdown files.
- Generated PDFs and temporary LaTeX artifacts may exist locally.

Do not manually edit generated PDF output.
Do not treat temporary scan scripts, compiled files, or editor artifacts as source.

## Verification

Compile changed LaTeX documents using the repository's established toolchain.
Inspect the rendered PDF for overflow, missing figures, incorrect references, font substitutions, and layout regressions.
Verify figures against the current system architecture.
Verify citations and bibliography resolution.
Reconcile feature descriptions with the master cross-repository gap register before publication.

## Repository rules

Resolve the checked-out branch and upstream before making changes.
Do not assume `main` is the active research branch.
Do not stage existing paper edits, generated PDFs, temporary DSI files, scan scripts, or unrelated resume changes.
The local `scratchpad/` directory is intentionally ignored.
When substantially editing Markdown, put every complete sentence on its own physical line.

