# ACOSUS Research Paper - Mermaid Diagrams for TikZ Conversion

This file contains the Mermaid diagram source code from the research paper for later conversion to TikZ diagrams in LaTeX.

---

## Figure 3: Dual-Survey Architecture with Survey Linkage

**Location in paper:** Section 3.1 (The Dual-Survey Architecture)

**Caption:** Dual-Survey Architecture with survey linkage. Target Surveys collect the label (Y), Factor Surveys collect features (X). Dashed lines show linkage relationships enabling flexible study configurations.

```mermaid
flowchart TB
    subgraph TargetSurveys["TARGET SURVEYS (Label: Y)"]
        direction TB
        TS1["Single-Question<br/>Direct 0-100 Scale"]
        TS2["Multi-Question<br/>PWRS Aggregated"]
    end

    subgraph FactorSurveys["FACTOR SURVEYS (Features: X)"]
        direction TB
        FS1["Academic Background<br/>GPA, SAT, Credits"]
        FS2["Financial Support<br/>Scholarship, Family Income"]
        FS3["Logistics & Commitment<br/>Distance, Work Hours"]
        FS4["Interest & Experience<br/>Career Goals, Prior Experience"]
        FS5["[Future Surveys]<br/>Adaptable to New Predictors"]
    end

    subgraph Processing["DATA PROCESSING"]
        direction LR
        Norm["Feature<br/>Normalization<br/>(0-10 scale)"]
        PWRS["PWRS<br/>Calculation<br/>(if multi-Q)"]
    end

    subgraph Output["ML MODEL"]
        direction TB
        Model["Y = f(X)<br/>Predict Readiness"]
        Score["Readiness Score<br/>(0-1 continuous)"]
    end

    %% Linkage connections
    TS1 -.->|"linkage"| FS1
    TS1 -.->|"linkage"| FS2
    TS1 -.->|"linkage"| FS3
    TS2 -.->|"linkage"| FS1
    TS2 -.->|"linkage"| FS3
    TS2 -.->|"linkage"| FS4

    %% Data flow
    FS1 --> Norm
    FS2 --> Norm
    FS3 --> Norm
    FS4 --> Norm
    TS2 --> PWRS

    Norm --> Model
    PWRS --> Model
    TS1 --> Model
    Model --> Score

    style TargetSurveys fill:#fff3e0
    style FactorSurveys fill:#e3f2fd
    style Processing fill:#f3e5f5
    style Output fill:#e8f5e9
```

**Color scheme:**
- Target Surveys: Orange background (#fff3e0)
- Factor Surveys: Blue background (#e3f2fd)
- Processing: Purple background (#f3e5f5)
- Output: Green background (#e8f5e9)

---

## Figure 4: The Three-Stage Progressive Pipeline

**Location in paper:** Section 3.2 (Architectural Philosophy: Small Data by Design)

**Caption:** The Three-Stage Progressive Pipeline. Each stage represents a pluggable component that can be substituted with alternative algorithms. The framework progresses from data acquisition through augmentation to refined prediction, with feedback loops enabling continuous improvement.

```mermaid
flowchart TB
    subgraph Framework["ACOSUS THREE-STAGE PROGRESSIVE PIPELINE"]
        direction TB

        subgraph Stage1["STAGE 1: FOUNDATION"]
            S1Title["Data Collection & Initial Prediction"]
            S1Desc["• Collect high-quality labeled observations<br/>• Establish ground truth corpus<br/>• Lightweight similarity-based predictions"]
            S1Plug["⚙️ Pluggable: Any similarity-based method"]
        end

        subgraph Stage2["STAGE 2: AUGMENTATION"]
            S2Title["Synthetic Data Generation"]
            S2Desc["• Learn distributional characteristics<br/>• Synthesize training observations<br/>• Preserve statistical properties"]
            S2Plug["⚙️ Pluggable: Any generative technique"]
        end

        subgraph Stage3["STAGE 3: REFINEMENT"]
            S3Title["Advanced Non-Linear Modeling"]
            S3Desc["• Train on augmented corpus<br/>• Capture complex relationships<br/>• Continuous improvement via feedback"]
            S3Plug["⚙️ Pluggable: Any deep learning architecture"]
        end
    end

    subgraph Input["DATA INPUT"]
        Surveys["Survey Responses<br/>(Features X, Labels Y)"]
    end

    subgraph Output["PREDICTION OUTPUT"]
        Score["Readiness Score<br/>(0-1 continuous)"]
    end

    subgraph Feedback["FEEDBACK LOOP"]
        FB["Student Feedback<br/>→ Model Improvement"]
    end

    Input --> Stage1
    Stage1 -->|"Minimal corpus established"| Stage2
    Stage2 -->|"Sufficient volume achieved"| Stage3
    Stage3 --> Output
    Output --> Feedback
    Feedback -.->|"New authentic observations"| Stage1
    Feedback -.->|"Validation on real data"| Stage3

    style Stage1 fill:#d4edda,stroke:#28a745
    style Stage2 fill:#fff3cd,stroke:#ffc107
    style Stage3 fill:#cce5ff,stroke:#007bff
    style Framework fill:#f8f9fa,stroke:#6c757d
```

**Color scheme:**
- Stage 1 (Foundation): Green (#d4edda, border #28a745)
- Stage 2 (Augmentation): Yellow (#fff3cd, border #ffc107)
- Stage 3 (Refinement): Blue (#cce5ff, border #007bff)
- Framework container: Light gray (#f8f9fa, border #6c757d)

---

## Figure 5: Survey Data Processing Pipeline

**Location in paper:** Section 4.1 (Survey Data Processing)

**Caption:** Survey data processing pipeline. Raw responses undergo priority weighting and type-aware normalization to produce standardized feature vectors for model ingestion.

```mermaid
flowchart LR
    subgraph Collection["SURVEY COLLECTION"]
        Q1["Question 1<br/>(Ordinal)"]
        Q2["Question 2<br/>(Cardinal)"]
        Q3["Question 3<br/>(Continuous)"]
    end

    subgraph Processing["DATA PROCESSING"]
        direction TB
        PW["Priority<br/>Weighting"]
        TN["Type-Aware<br/>Normalization"]
    end

    subgraph Output["MODEL INPUT"]
        FV["Normalized<br/>Feature Vector<br/>(0-10 scale)"]
    end

    Q1 --> PW
    Q2 --> PW
    Q3 --> PW
    PW --> TN
    TN --> FV

    style Collection fill:#e3f2fd
    style Processing fill:#fff3e0
    style Output fill:#e8f5e9
```

**Color scheme:**
- Collection: Blue background (#e3f2fd)
- Processing: Orange background (#fff3e0)
- Output: Green background (#e8f5e9)

---

## Figure 6: ACOSUS System Architecture

**Location in paper:** Section 4.2 (System Architecture)

**Caption:** ACOSUS system architecture. Four layers separate presentation, business logic, data persistence, and machine learning concerns, enabling independent scaling and clear separation of responsibilities.

```mermaid
flowchart TB
    subgraph Presentation["PRESENTATION LAYER"]
        direction LR
        Student["Student Portal<br/>Survey | Prediction | Feedback"]
        Advisor["Advisor Portal<br/>Search | Profile | Dashboard"]
        Admin["Admin Portal<br/>Configure | Train | Analytics"]
    end

    subgraph Business["BUSINESS LOGIC LAYER"]
        direction LR
        Auth["Authentication"]
        Survey["Survey<br/>Management"]
        Workflow["Phase<br/>Orchestration"]
        Trigger["Training<br/>Triggers"]
    end

    subgraph Data["DATA LAYER"]
        DB["Document Storage"]
        Collections["Users | Surveys | Responses | Models | Feedback"]
    end

    subgraph ML["MODEL LAYER"]
        direction LR
        Norm["Data<br/>Normalizer"]
        Predict["Prediction<br/>Service"]
        Train["Training<br/>Pipeline"]
        Version["Model<br/>Versioning"]
    end

    Presentation -->|"REST API"| Business
    Business --> Data
    Business -->|"Async"| ML

    style Presentation fill:#e3f2fd
    style Business fill:#fff3e0
    style Data fill:#e8f5e9
    style ML fill:#fce4ec
```

**Color scheme:**
- Presentation Layer: Blue (#e3f2fd)
- Business Logic Layer: Orange (#fff3e0)
- Data Layer: Green (#e8f5e9)
- Model Layer: Pink (#fce4ec)

---

## Notes for TikZ Conversion

### General Recommendations:
1. Use `tikz` with the `positioning` library for node placement
2. Use `fit` library for grouping nodes into subgraphs
3. Consider `shapes.geometric` for varied node shapes
4. Use `arrows.meta` for arrow styling

### Color Definitions (LaTeX):
```latex
\definecolor{targetsurvey}{HTML}{fff3e0}
\definecolor{factorsurvey}{HTML}{e3f2fd}
\definecolor{processing}{HTML}{f3e5f5}
\definecolor{output}{HTML}{e8f5e9}
\definecolor{stage1}{HTML}{d4edda}
\definecolor{stage2}{HTML}{fff3cd}
\definecolor{stage3}{HTML}{cce5ff}
\definecolor{modellayer}{HTML}{fce4ec}
```

### Suggested TikZ Style:
```latex
\tikzstyle{surveybox} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm, text centered, draw=black]
\tikzstyle{arrow} = [thick,->,>=stealth]
\tikzstyle{dashedarrow} = [thick,->,>=stealth,dashed]
```
