# ACOSUS Paper Space: Constraints and Guidelines

## Document Purpose

This document defines the constraints, guidelines, and instructions for writing the ACOSUS research paper targeting **CSEDU 2026** (18th International Conference on Computer Supported Education). It ensures consistency across all sections, whether written by different authors or at different times.

---

## 1. Target Venue

### Conference Details
- **Name**: CSEDU 2026 - 18th International Conference on Computer Supported Education
- **Location**: Benidorm, Spain
- **Dates**: May 18-20, 2026
- **Submission Deadline**: January 5, 2026 (Regular Paper)
- **Conference Area**: Area 1 - Artificial Intelligence in Education
- **Publisher**: SCITEPRESS

### Venue Fit
CSEDU focuses on:
- Educational tools and environments
- Technology-based learning strategies
- Institutional policies on computer-supported education
- Academic or business case studies
- Advanced prototypes, systems, tools, and techniques

Our paper fits as a **system design paper** presenting an AI-driven advising platform for transfer students, emphasizing the educational technology and advising workflow improvements rather than ML algorithmic innovations.

---

## 2. Target Audience

### Primary Audience
- **CS Education researchers** interested in AI-assisted student support systems
- **Academic advising practitioners** exploring technology solutions for transfer student populations
- **Educational technologists** building predictive analytics tools for higher education
- **Institutional researchers** concerned with transfer student retention and success

### Audience Expectations
- Understand system design rationale and methodology
- See clear connection between system features and advising challenges
- Appreciate practical deployment considerations
- **NOT** expecting deep ML/AI technical details (algorithm derivations, hyperparameter tuning, neural architecture specifics)

### Writing Implication
When describing ML components:
- **DO**: Explain *what* the system does and *why* it benefits advising
- **DO**: Mention that neural network models are used for prediction
- **DO NOT**: Explain backpropagation, loss functions, GAN discriminator/generator details
- **DO NOT**: Include mathematical formulas beyond simple weighted averages

---

## 3. Paper Structure and Page Budget

### Total Length: 10 Pages

| Section | Pages | Author | Status |
|---------|-------|--------|--------|
| 1. Introduction | 1 | - | Complete |
| 2. Literature Review | 1 | - | Complete |
| 3. System Design and Methodology | 2 | You | To Write |
| 4. System Implementation | 2 | You | To Write |
| Diagrams/Tables (Sections 3+4) | 1 | You | To Write |
| 5. Evaluation | 1 | Other | Guidelines Below |
| 6. Discussion + Future Work | 1 | Split | Guidelines Below |
| References | 1 | - | Partially Complete |

### Page Budget Breakdown for Sections 3 & 4

**Total space for Methodology + Implementation: ~5 pages** (including diagrams)

Recommended allocation:
- Section 3 (Methodology): ~2 pages of text
- Section 4 (Implementation): ~1.5 pages of text
- Diagrams and Tables: ~1 page (distributed across both sections)
- Buffer for formatting: ~0.5 page

---

## 4. Section 3: System Design and Methodology

### Section Goal
Explain the *conceptual architecture* and *design rationale* of ACOSUS. Focus on **why** these design choices address transfer student advising challenges.

### Required Content (In Order)

#### 3.1 Architectural Philosophy: Small Data by Design (~1 paragraph)
**Key points to cover:**
- Transfer cohorts are inherently small (30-50 students/year per department)
- Traditional ML requires thousands of labeled examplesinfeasible here
- ACOSUS designed for "Small Data": immediate utility, graceful evolution, burden minimization
- System delivers value from first interaction, improves as data accumulates

**Tone**: Problem-solution framing. Start with the challenge, present the philosophy as the response.

#### 3.2 The Dual-Survey Architecture (~1 paragraph)
**Key points to cover:**
- Separation of concerns: Target Surveys (labels) vs. Factor Surveys (features)
- Target Surveys capture success rate (single-question direct input OR multi-question with scoring)
- Factor Surveys capture predictive features: academic background, financial circumstances, technical preparation, temporal factors
- Factor Surveys also serve advisors by systematizing data collection (dual-purpose design)
- Survey linkage enables flexible study configurations

**Tone**: Architectural explanation. Emphasize the clean separation and dual-purpose benefit.

#### 3.3 The Progressive Learning Framework (~1-2 sentences)
**Key points to cover:**
- Three phases: Bootstrap (N<10, data collection only) ’ Instance-Based (10dN<100, KNN prediction) ’ Neural Network (Ne100, GAN-augmented training)
- System autonomously transitions between phases as data accumulates

**Tone**: Brief mention. Do not explain KNN or neural networks in detail.

#### 3.4 Priority-Weighted Response Scoring (PWRS) (~1-2 sentences)
**Key points to cover:**
- Algorithm for aggregating multi-question Target Survey responses into single numeric success rate
- Uses expert-assigned priority weights and option weightages
- Applies calibration curve for realistic predictions

**Tone**: Mention existence and purpose. Can reference that details are in supplementary materials or future work.

#### 3.5 Feedback-Driven Pseudo-Labeling (~1-2 sentences)
**Key points to cover:**
- After prediction, students rate accuracy (1-5 stars)
- High ratings (e4): prediction accepted as training label, skip Target Survey
- Low ratings (<4): student completes Target Survey for ground truth
- Reduces survey burden by 60-70% while maintaining data quality

**Tone**: Practical benefit focus. Emphasize burden reduction for students.

#### 3.6 Feature Normalization (~1-2 sentences)
**Key points to cover:**
- Survey responses normalized to common scale (0-10) for ML ingestion
- Type-aware normalization: ordinal, cardinal, continuous, temporal data handled differently

**Tone**: Technical aside. Brief mention for completeness.

#### 3.7 Model Selection and Deployment (~1 sentence)
**Key points to cover:**
- System maintains model versioning
- New models validated against current production model before deployment
- Conservative deployment: complexity must improve accuracy

**Tone**: Quality assurance mention. One sentence is sufficient.

### Section 3 Diagram Requirements

**One diagram required**: Progressive Learning Framework phases

```
Suggested Mermaid diagram (adapt as needed):

flowchart LR
    subgraph Phase1["Phase 1: Bootstrap"]
        P1["N < 10"]
        P1a["Data collection only"]
    end

    subgraph Phase2["Phase 2: Instance-Based"]
        P2["10 d N < 100"]
        P2a["KNN predictions"]
    end

    subgraph Phase3["Phase 3: Neural"]
        P3["N e 100"]
        P3a["NN predictions"]
    end

    Phase1 -->|"10th student"| Phase2
    Phase2 -->|"100th student"| Phase3
```

### Section 3 Table Requirements

**One table required**: Comparison of traditional institutional systems vs. transfer-specific factors captured by ACOSUS

| Traditional Systems | Transfer-Specific Factors (ACOSUS) |
|---------------------|-----------------------------------|
| GPA, courses (SIS) | Transfer shock severity, credits lost |
| Financial aid status | Work hours, financial anxiety |
| LMS engagement | Social integration, belonging uncertainty |
| Enrollment status | Institutional fit perception |

---

## 5. Section 4: System Implementation

### Section Goal
Describe the *technical architecture* and *implementation choices*. Focus on **how** the system is built, with enough detail for reproducibility but without overwhelming technical minutiae.

### Required Content (In Order)

#### 4.1 High-Level Architecture (~1 paragraph + diagram)
**Key points to cover:**
- Three-tier web application: Presentation, Business Logic, ML Layer
- Separation of concerns enables independent scaling
- Role-based portals: Student, Advisor, Admin

**Include ONE comprehensive Mermaid diagram** showing:
- Client layer (React)
- Application layer (Node.js + MongoDB)
- ML layer (Python/Flask for prediction and training)
- Data flows between layers

#### 4.2 Component Overview (~1 paragraph)
**Key points to cover:**
- **Presentation Layer**: React SPA with role-specific interfaces
- **Business Logic Layer**: Node.js/Express for authentication, survey management, PWRS calculation
- **Data Layer**: MongoDB for flexible document storage
- **ML Layer**: Python/Flask for KNN prediction, GAN training, neural network inference

**Tone**: Concise architectural summary. One sentence per layer.

#### 4.3 Technology Stack Summary (Table)

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend | React, TypeScript, Tailwind CSS | Role-based UI rendering |
| Backend | Node.js, Express | API orchestration, business logic |
| Database | MongoDB | Flexible document storage |
| ML Server | Python, Flask | Model training and inference |
| Authentication | JWT | Stateless session management |
| Deployment | Docker, Nginx | Containerization, reverse proxy |

#### 4.4 Unified System Diagram (~1 paragraph explanation)
**Create ONE solid diagram** that encompasses the entire system flow:
- Student journey: Survey completion ’ Prediction ’ Feedback
- Advisor journey: Search ’ Profile view ’ Survey management
- ML pipeline: Data collection ’ Training ’ Prediction
- Data flows between all components

**Paragraph should explain the diagram**, highlighting:
- How student data flows through the system
- How advisors access unified student profiles
- How the ML pipeline integrates with the survey system

### Section 4 Diagram Requirements

**One comprehensive system diagram** (full-page or half-page)

Suggested structure:
```
flowchart TB
    subgraph Users["User Portals"]
        Student["Student Portal"]
        Advisor["Advisor Portal"]
        Admin["Admin Portal"]
    end

    subgraph Core["Application Core"]
        API["REST API"]
        Auth["Authentication"]
        PWRS["PWRS Engine"]
        Survey["Survey Manager"]
    end

    subgraph Data["Data Layer"]
        DB[(MongoDB)]
    end

    subgraph ML["ML Pipeline"]
        Predict["Prediction Service"]
        Train["Training Service"]
        Models["Model Storage"]
    end

    Users --> Core
    Core --> Data
    Core <--> ML
```

---

## 6. Section 5: Evaluation (Guidelines for Other Author)

### Section Goal
Report findings from the pilot usability study with transfer students.

### Required Content

#### 5.1 Study Design (~0.25 pages)
- Research questions (RQ1-RQ5 from methodology draft)
- Participants: 10 transfer students in computing majors
- Protocol: Onboarding ’ Target Survey ’ Factor Survey ’ Prediction Review ’ Evaluation Survey

#### 5.2 Evaluation Instruments (~0.25 pages)
- Technology Acceptance Model (TAM) constructs: Perceived Usefulness, Perceived Ease of Use
- Prediction quality assessment items
- Open-ended feedback questions

#### 5.3 Results (~0.5 pages)
- Quantitative: Mean/SD for TAM constructs, completion rates
- Qualitative: Thematic analysis of open-ended responses
- Key findings related to each research question

### Evaluation Tables
- Table: TAM construct scores (PU items, PEOU items)
- Table: Prediction alignment ratings

### Tone Alignment
- Use same academic tone as Sections 3-4
- Present findings objectively without overclaiming
- Connect findings back to system design rationale

`[CHECK WITH PROFESSOR: Confirm evaluation study completion timeline and available data]`

---

## 7. Section 6: Discussion + Future Work

### Page Budget: ~1 page total
- Discussion: ~0.5 pages
- Future Work: ~0.5 pages

### 6.1 Discussion Content
- Summary of contributions (4 architectural innovations)
- Limitations:
  - Heuristic dependency in Bootstrap phase
  - Domain specificity (computing majors)
  - Proxy outcome measure (self-assessment vs. graduation)
  - Sample size (N=10 for pilot)

### 6.2 Future Work Content
- Longitudinal outcome validation (correlate predictions with actual graduation)
- Cross-institutional deployment
- Advisor dashboard enhancements (cohort analytics, early alerts)
- GAN architecture optimization (if NN phase reached)

`[CHECK WITH PROFESSOR: Specific future directions to emphasize]`

---

## 8. Writing Style and Tone

### Voice
- **Third person**: "The system implements..." not "We implement..."
- **Active voice preferred**: "The system predicts success rates" not "Success rates are predicted by the system"
- **Present tense for system descriptions**: "ACOSUS employs a dual-survey architecture"
- **Past tense for study descriptions**: "Participants completed the evaluation survey"

### Academic Tone
- Match the tone established in Introduction and Literature Review
- Professional but accessibleavoid jargon where possible
- Define acronyms on first use (e.g., "Priority-Weighted Response Scoring (PWRS)")

### Sentence Structure
- Prefer concise sentences (15-25 words)
- One idea per sentence
- Use topic sentences to start paragraphs
- Use transitions between paragraphs

### Avoiding Common Pitfalls
- **NO** superlatives without evidence ("groundbreaking", "revolutionary")
- **NO** first-person plural for single-author sections
- **NO** informal language ("pretty good", "a lot of")
- **NO** unexplained acronyms
- **NO** deep ML technical details (loss functions, gradients, etc.)

---

## 9. Diagram Requirements

### Format
- **Mermaid diagrams ONLY**
- Use flowchart, sequenceDiagram, or erDiagram as appropriate
- Keep diagrams readable at single-column width

### Style Guidelines
- Use consistent node shapes: rectangles for processes, diamonds for decisions, cylinders for databases
- Use subgraphs to group related components
- Include brief labels (2-4 words per node)
- Add figure captions below each diagram

### Figure Numbering
- Continue numbering from Introduction/Literature Review figures
- Format: "Figure X. [Caption describing what the figure shows]"

### Recommended Diagrams (Total: 2-3)
1. **Section 3**: Progressive Learning Framework phases (small, ~1/4 page)
2. **Section 4**: Comprehensive system architecture (larger, ~1/2 page)
3. **Optional**: Feedback-driven pseudo-labeling flow (if space permits)

---

## 10. Table Requirements

### Format
- Use standard academic table format
- Bold headers
- Left-align text columns, center-align numeric columns
- Include table captions above each table

### Table Numbering
- Continue numbering from Introduction/Literature Review tables
- Format: "Table X. [Caption describing what the table shows]"

### Recommended Tables (Total: 2-3)
1. **Section 3**: Traditional systems vs. transfer-specific factors
2. **Section 4**: Technology stack summary
3. **Section 5**: TAM construct scores (Evaluation section)

---

## 11. References

### Existing References
The Introduction and Literature Review establish references [1]-[20]. Continue numbering from [21] onward.

### Citation Style
- IEEE format (numeric citations in square brackets)
- Multiple citations: [1], [2], [5] or [1]-[3]
- Citation placement: before punctuation

### Key References to Include
- Prior ACOSUS-related publications (Vargas et al., Wang et al., MacDonald et al.)
- Transfer student success literature
- Educational data mining / learning analytics references
- Technology acceptance model (TAM) for evaluation

`[CHECK WITH PROFESSOR: Additional references needed for methodology or implementation]`

---

## 12. Formatting Notes (SCITEPRESS)

### General
- SCITEPRESS provides LaTeX and Word templates
- Single-column format for submission (converted to two-column for proceedings)
- Page limit: 10 pages (strict)

### Font and Spacing
- Follow SCITEPRESS template specifications
- Typically: 10pt font, single-spaced

### Figures and Tables
- Embed within text flow (not at end)
- Ensure readability when printed in grayscale

`[CHECK WITH PROFESSOR: Confirm template version and any specific formatting requirements]`

---

## 13. `[CHECK WITH PROFESSOR]` Items

The following items from the methodology draft require verification:

1. **Section 3.1.1** - Time estimates for advisor data gathering (~23 min/student, 38 hours/week)
2. **Section 3.2.3** - Advisor time savings (23 min ’ 7 min, 70% reduction)
3. **Section 3.3.1** - Bootstrap threshold of 10 students: correct and configurable?
4. **Section 3.3.3** - GAN augmentation ratio (100 real ’ 400-500 synthetic)
5. **Section 3.5.2** - Estimated percentage of high-rating feedback (50-70%)
6. **Section 5.1.2** - Institution name and compensation details for pilot study
7. **Section 5.4** - Timeline and specific outcome measures for longitudinal validation
8. **Section 6.3** - Specific GAN research directions for future work
9. **Reference [9]** - Verify AMCIS 2023 citation details

---

## 14. Additional Reference Material

The following detailed content from the methodology and technical architecture documents can be referenced if additional depth is needed. **Use sparingly**only pull content if page budget allows.

**Instructions**: When writing the paper, if you need more detail for a particular section, consult this reference material. Copy relevant portions and condense to fit page constraints. Always prioritize the condensed version specified in Section 4 and 5 of this document.

### From Methodology Draft (ACOSUS-System-Design-Methodology.md)

#### Advisor Data Fragmentation Problem (Section 3.1.1)
> Academic advisors lack unified access to information needed to support transfer students. Advisors spend 40-60% of their time gathering student information from disparate sources: SIS, financial aid portals, LMS, email/notes. This fragmentation requires navigating 5+ separate systems, consuming ~20-25 minutes per student before substantive advising begins.

*Use if*: Need to strengthen the "problem" framing in Section 3.1.

#### PWRS Worked Example
> Five-question Target Survey example showing step-by-step calculation:
> - Normalize: 0.80, 0.80, 0.40, 0.80, 0.60
> - Weight: 7.2, 6.4, 3.2, 7.2, 4.8 ’ Sum = 28.8
> - Base Score: 28.8 / 42 = 0.686
> - Logistic calibration: 75.3%

*Use if*: Reviewer requests more detail on PWRS calculation.

#### KNN Dynamic Neighbor Selection Formula
> k = min(max(3, N), 10)

*Use if*: Need to show mathematical grounding without deep ML explanation.

#### Calibration Curve Options Table
> Linear, Bounded Linear, Logistic (recommended), Sigmoid with formulas and characteristics.

*Use if*: Space available and want to show PWRS flexibility.

#### Factor Survey Categories Detail
> - Academic Background: Pre-transfer GPA, credits earned, credits transferred, prior institution type
> - Financial Circumstances: Employment intensity, financial aid status, perceived financial security
> - Logistical Factors: Commute time, caregiving responsibilities, housing stability
> - Technical Preparation: Programming experience, familiarity with specific languages/tools
> - Temporal Factors: Expected time to degree, enrollment intensity

*Use if*: Want to enumerate specific factors collected.

#### Phase Transition Details
> - Phase 1 (Bootstrap, N<10): Students complete both Target and Factor surveys. No predictions generated. Seeds dataset with high-quality labeled observations.
> - Phase 2 (Instance-Based, 10dN<100): KNN regression with dynamic k=N. Students complete Factor Survey only, receive prediction, provide feedback rating.
> - Phase 3 (Neural, Ne100): GAN generates synthetic data for training augmentation. Neural network trained on real+synthetic, validated on real only.

*Use if*: Need more detail on what happens in each phase.

### From Technical Architecture Guide (ACOSUS-Technical-Architecture-Guide.md)

#### Database Entity Descriptions
> Detailed field descriptions for Users, Quizzes, Questions, QuestionOptions, Attempts, ModelMetaData collections.

*Use if*: Reviewer requests data model details (unlikely for CSEDU audience).

#### API Route Structure
> Route prefixes: /auth, /student, /advisor, /admin, /quiz, /model with purposes and key endpoints.

*Use if*: Implementation section needs more depth.

#### Role-Based Access Control Table
> - Student: Take assigned surveys, view own predictions, provide feedback
> - Advisor: Search students, view any student profile, manage surveys, act-as student
> - Admin: All advisor capabilities + create surveys, configure models, trigger training

*Use if*: Want to emphasize multi-stakeholder design.

#### Advisor Portal Features
> - Student Search: Search by name, email, or student ID with filters
> - Unified Profile: Tabbed view of student data organized by category
> - Survey Management: View attempts, completion status, individual responses
> - Act-As Capability: Complete surveys on behalf of students during sessions
> - Copy & Edit: Duplicate attempts with modifications for data refinement

*Use if*: Emphasizing advisor-centric design contribution.

#### Security Architecture
> - Transport: HTTPS/TLS encryption
> - Authentication: JWT with access/refresh tokens
> - Authorization: Role-based middleware
> - Passwords: bcrypt hashing

*Use if*: Reviewer asks about security considerations.

### Mermaid Diagram Library

The Technical Architecture Guide contains 24 Mermaid diagrams. Key diagrams to potentially adapt:

1. **Figure 1**: High-level architecture (3 layers)
2. **Figure 3**: Database ER diagram
3. **Figure 6**: Frontend portal structure
4. **Figure 7**: Model server architecture
5. **Figure 10**: Model selection logic
6. **Figure 11**: Progressive learning phases
7. **Figure 13**: Phase 2 student flow with feedback
8. **Figure 16**: PWRS calculation pipeline
9. **Figure 17**: Feedback-driven pseudo-labeling
10. **Figure 18**: Advisor search and profile flow

*Recommendation*: Combine elements from Figures 1, 6, 7, and 11 into one comprehensive diagram for Section 4.

---

## 15. Quick Reference Checklist

Before submission, verify:

### Content
- [ ] Section 3 covers all 7 required subsections
- [ ] Section 4 covers all 4 required subsections
- [ ] All `[CHECK WITH PROFESSOR]` items resolved or removed
- [ ] ML details kept minimal (no algorithm internals)
- [ ] Advisor benefit clearly articulated (data centralization)

### Formatting
- [ ] Total length d 10 pages
- [ ] All diagrams are Mermaid format
- [ ] Figure/Table numbering is sequential
- [ ] References numbered [21]+ continuing from Lit Review
- [ ] SCITEPRESS template used

### Style
- [ ] Consistent tone with Introduction/Literature Review
- [ ] Third person voice throughout
- [ ] No superlatives without evidence
- [ ] All acronyms defined on first use

### Diagrams and Tables
- [ ] 2-3 diagrams total (Sections 3+4)
- [ ] 2-3 tables total (Sections 3+4)
- [ ] All have captions
- [ ] Readable at print size

---

*Document Version: 1.0*
*Last Updated: December 2024*
*For: CSEDU 2026 Submission*
