# ACOSUS V2 Architecture Diagrams

This directory contains 9 Mermaid diagrams organized by detail level and presentation style.

## Directory Structure

### High-Level Diagrams (Simple Overview)
- **[01-HighLevel-Integrated.md](./01-HighLevel-Integrated.md)** - Single combined flow
- **[02-HighLevel-SideBySide.md](./02-HighLevel-SideBySide.md)** - Prediction | Training parallel
- **[03-HighLevel-Separate.md](./03-HighLevel-Separate.md)** - Two independent diagrams

### Medium-Level Diagrams (Key Components)
- **[04-MediumLevel-Integrated.md](./04-MediumLevel-Integrated.md)** - Backend services visible
- **[05-MediumLevel-SideBySide.md](./05-MediumLevel-SideBySide.md)** - Prediction | Training with services
- **[06-MediumLevel-Separate.md](./06-MediumLevel-Separate.md)** - Two detailed diagrams

### Detailed Diagrams (Complete Step-by-Step)
- **[07-Detailed-Integrated.md](./07-Detailed-Integrated.md)** - All flows combined
- **[08-Detailed-SideBySide.md](./08-Detailed-SideBySide.md)** - Prediction | Training comprehensive
- **[09-Detailed-Separate.md](./09-Detailed-Separate.md)** - Two exhaustive diagrams

## Usage Recommendations

### For Thesis Defense Presentation
- **Slide 1 (Overview)**: Use `01-HighLevel-Integrated.md` for system introduction
- **Slide 2 (Architecture Deep Dive)**: Use `08-Detailed-SideBySide.md` for technical explanation
- **Backup/Reference**: Keep `09-Detailed-Separate.md` for Q&A session

### For Technical Documentation
- Use detailed diagrams (07, 08, 09) for comprehensive documentation
- Use medium-level diagrams (04, 05, 06) for developer onboarding

### For Stakeholder Presentations
- Use high-level diagrams (01, 02, 03) for non-technical audiences

## Features Across All Diagrams

✅ **Dual-Survey System**: Factor, Target, and Unified flows
✅ **Model Server Components**: Data Normalizer, PWRS Calculator, Model Selector, Training Queue, Versioning
✅ **Progressive Learning**: KNN → GAN → Neural Network phases
✅ **Feedback Loop**: Pseudo-labeling with rating threshold (≥4 stars)
✅ **OpenAI API**: Annotated as future work
✅ **MongoDB**: Generic database (no collection details)

## Color Legend

- 🟦 **Frontend Components** (Student Portal, Admin Portal)
- 🟩 **Backend Components** (Survey Management, PWRS Calculator, Training Request Builder)
- 🟨 **Model Server Components** (Data Normalizer, Model Selector, Prediction Engine, etc.)
- 🟥 **Database** (MongoDB)
- ⚪ **Decision Points** (Conditionals, branching logic)
- 🟪 **Future Work** (OpenAI API integration)

## Viewing the Diagrams

### In VSCode
1. Install "Markdown Preview Mermaid Support" extension
2. Open any diagram markdown file
3. Click "Open Preview to the Side" (Ctrl+K V)

### In GitHub
- GitHub automatically renders Mermaid diagrams in markdown files

### Online Mermaid Editor
1. Copy the Mermaid code block
2. Paste into https://mermaid.live/
3. Export as PNG/SVG for presentations

---

**Created**: November 19, 2025
**Version**: 1.0
**Author**: Deep Mandloi (ACOSUS Thesis)
