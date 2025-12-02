# Figures and Tables Specification

This document provides detailed specifications for all figures and tables referenced in Sections 3-5 of the ACOSUS research paper. Use this as a guide when creating the actual visual assets.

---

## Summary of Placeholders

### Figures (8 total - all require creation)

| Figure | Section | Description | Status |
|--------|---------|-------------|--------|
| FIGURE 1 | 3.3.1 | High-Level System Architecture Diagram | Placeholder |
| FIGURE 2 | 3.4.1 | Frontend Component Architecture | Placeholder |
| FIGURE 3 | 3.4.3 | Model Server Component Architecture | Placeholder |
| FIGURE 4 | 3.5.1 | Dual-Survey System Architecture | Placeholder |
| FIGURE 5 | 3.5.3 | Feedback Loop Architecture | Placeholder |
| FIGURE 6 | 3.6.3 | Data Flow Architecture Diagram | Placeholder |
| FIGURE 7 | 3.7.3 | Deployment Architecture Diagram | Placeholder |
| FIGURE 8 | 4.2.5 | Prediction Feedback Interface Mockup | Placeholder |

### Tables (25 total)

| Table | Section | Description | Status |
|-------|---------|-------------|--------|
| TABLE 1 | 3.3.2 | Technology Stack Overview | Complete (inline) |
| TABLE 2 | 3.5.2 | Progressive Learning Phases | Complete (inline) |
| TABLE 3 | 3.7.1 | Container Configuration | Complete (inline) |
| TABLE 4 | 4.3.2 | Survey Attempt States | Complete (inline) |
| TABLE 5 | 4.4.3 | Expected KNN Performance by Cohort Size | Complete (inline) |
| TABLE 6 | 4.4.4 | Model Performance Comparison | Complete (inline) |
| TABLE 7 | 4.5.2 | Access Control Matrix | Complete (inline) |
| TABLE 8 | 4.8 | Implementation Status Summary | Complete (inline) |
| TABLE 9 | 5.2 | Research Questions and Evaluation Focus | Complete (inline) |
| TABLE 10 | 5.3.1 | Study Design Parameters | Complete (inline) |
| TABLE 11 | 5.4 | Participant Task Sequence | Complete (inline) |
| TABLE 12 | 5.4.2 | Target Survey Categories | Complete (inline) |
| TABLE 13 | 5.4.3 | Factor Survey Categories | Complete (inline) |
| TABLE 14 | 5.5.1 | System Usability Scale Items | Complete (inline) |
| TABLE 15 | 5.6.1 | Quantitative Data Collection | Complete (inline) |
| TABLE 16 | 5.8.1 | Alpha Testing Success Criteria | Complete (inline) |
| TABLE 17 | 5.9.1 | Participant Demographics | Placeholder (pending data) |
| TABLE 18 | 5.9.2 | Task Completion Results | Placeholder (pending data) |
| TABLE 19 | 5.9.3 | SUS Item Scores | Placeholder (pending data) |
| TABLE 20 | 5.9.4 | TAM Results | Placeholder (pending data) |
| TABLE 21 | 5.9.5 | Prediction Feedback Results | Placeholder (pending data) |
| TABLE 22 | 5.9.6 | Preliminary Theme Analysis | Placeholder (pending data) |
| TABLE 23 | 5.10.1 | Target Survey Validation Thresholds | Complete (inline) |
| TABLE 24 | 5.10.3 | Expected Feedback Loop Progression | Complete (inline) |
| TABLE 25 | 5.13 | Evaluation Timeline | Complete (inline) |

---

## Figure Specifications

### FIGURE 1: High-Level System Architecture Diagram

**Location**: Section 3.3.1 (Three-Tier Architecture)

**Caption**: "ACOSUS High-Level System Architecture: Three-Tier Design with ML Integration"

**Visualization Type**: Architecture block diagram

**What Should Be Illustrated**:
- Three-tier separation: Presentation Layer, Business Logic Layer, Data/ML Layer
- Three primary components with their technology stacks:
  1. Frontend Application (React SPA)
  2. Backend API Server (Node.js/Express)
  3. Model Server (Python/Flask)
- Communication flows between layers
- Database (MongoDB) connection
- External interfaces (users by role: Student, Advisor, Admin)

**Key Elements to Include**:
- Distinct visual grouping for each tier (use color coding or dashed boxes)
- Technology labels on each component (React 18, Node.js 20, Python 3.12, MongoDB 7.0)
- Bidirectional arrows showing API communication
- User icons for the three roles accessing the frontend
- Docker container indicators around services

**Layout Suggestion**:
```
┌─────────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  React Frontend (TypeScript)                            │   │
│  │  • Student Interface  • Advisor Interface  • Admin UI   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │ REST API
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Node.js Backend (Express)                              │   │
│  │  • Auth  • Survey Workflow  • Success Calc  • ML Orch   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │ Internal API
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA / ML LAYER                            │
│  ┌──────────────────────┐    ┌─────────────────────────────┐   │
│  │  MongoDB             │    │  Model Server (Flask)       │   │
│  │  • Users  • Surveys  │    │  • Training  • Inference    │   │
│  │  • Answers • Models  │    │  • GAN  • KNN  • NN         │   │
│  └──────────────────────┘    └─────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Data Sources**: Section 3.3.1 text, Table 1 (Technology Stack)

---

### FIGURE 2: Frontend Component Architecture

**Location**: Section 3.4.1 (Frontend Architecture)

**Caption**: "Frontend Application Component Architecture with State Management Layers"

**Visualization Type**: Component hierarchy diagram / layered architecture diagram

**What Should Be Illustrated**:
- Directory structure as component hierarchy (components, features, hooks, services, contexts, utils)
- Context providers and their scope (UserContext, WorkflowContext, StudentContext)
- Service layer abstraction for API communication
- React Query integration for server state
- Auto-save mechanism flow

**Key Elements to Include**:
- UI layer: Primitive components (Button, Input, Card) and Composite components (Header, Sidebar)
- Feature modules: auth, survey, dashboard, admin
- State management: Context providers shown as encompassing layers
- Service layer with React Query hooks
- Data flow arrows showing unidirectional state flow

**Layout Suggestion**:
```
┌────────────────────────────────────────────────────────────┐
│                    Context Providers                        │
│  ┌──────────────┐ ┌────────────────┐ ┌─────────────────┐  │
│  │ UserContext  │ │ WorkflowContext│ │ StudentContext  │  │
│  └──────────────┘ └────────────────┘ └─────────────────┘  │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │                  Feature Modules                      │ │
│  │  ┌────────┐ ┌────────┐ ┌───────────┐ ┌───────────┐  │ │
│  │  │  Auth  │ │ Survey │ │ Dashboard │ │   Admin   │  │ │
│  │  └────────┘ └────────┘ └───────────┘ └───────────┘  │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              Shared UI Components                     │ │
│  │  Primitives: Button, Input, Card, Modal              │ │
│  │  Composites: Header, Sidebar, SurveyRenderer         │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              Service Layer (React Query)              │ │
│  │  useAuth() useSurvey() usePrediction() useAdmin()    │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
                              │
                              ▼ HTTP/REST
                        Backend API
```

**Data Sources**: Section 3.4.1, Section 4.2.1 (Application Structure)

---

### FIGURE 3: Model Server Component Architecture

**Location**: Section 3.4.3 (Model Server Architecture)

**Caption**: "Model Server Component Architecture with Asynchronous Training Queue"

**Visualization Type**: Component/process flow diagram

**What Should Be Illustrated**:
- Flask application structure with REST endpoints
- Training Queue Manager with background thread execution
- Model Storage (HDF5 files, pickle scalers) in shared Docker volume
- Prediction Pipeline flow
- Callback mechanism to backend

**Key Elements to Include**:
- REST API endpoints: /train, /predict, /status
- Queue manager with job queue visualization
- Background worker threads
- Model artifacts storage (shared volume)
- Scaler and model loading/caching
- Progress callback arrows to backend
- Timing metrics output

**Layout Suggestion**:
```
                    ┌────────────────────────────┐
                    │      Flask REST API        │
                    │  /train  /predict  /status │
                    └─────────────┬──────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
┌──────────────────────┐ ┌────────────────┐ ┌─────────────────┐
│  Training Queue      │ │ Prediction     │ │ Status          │
│  Manager             │ │ Pipeline       │ │ Monitor         │
│  ┌────────────────┐  │ │                │ │                 │
│  │ Job Queue      │  │ │ • Load Model   │ │ • Job Progress  │
│  │ ────────────── │  │ │ • Apply Scaler │ │ • Metrics       │
│  │ │Job 1│Job 2│  │  │ │ • Inference    │ │                 │
│  └────────────────┘  │ │ • Return       │ │                 │
│         │            │ └────────────────┘ └─────────────────┘
│         ▼            │          │
│  Background Workers  │          │
│  (Thread Pool)       │          ▼
└──────────────────────┘ ┌────────────────────────────────────┐
         │               │       Shared Docker Volume          │
         │               │  ┌─────────┐  ┌─────────────────┐  │
         │               │  │ .h5     │  │ .pkl (scalers)  │  │
         │               │  │ Models  │  │                 │  │
         │               │  └─────────┘  └─────────────────┘  │
         │               └────────────────────────────────────┘
         │
         ▼ Progress Callbacks
    Backend API
```

**Data Sources**: Section 3.4.3, Section 4.4.6 (Model Versioning and Serving)

---

### FIGURE 4: Dual-Survey System Architecture

**Location**: Section 3.5.1 (Dual-Survey Architecture)

**Caption**: "Dual-Survey Architecture: Separation of Ground Truth and Feature Collection"

**Visualization Type**: Process/system diagram with two parallel paths

**What Should Be Illustrated**:
- Two distinct survey types with their purposes:
  - Target Survey: Ground truth collection (success rate)
  - Factor Survey: Feature collection (ML inputs)
- How separation enables progressive learning
- Reduction in survey burden after model training
- Pseudo-labeling pathway

**Key Elements to Include**:
- Target Survey box with: 27 questions, ~15 min, readiness categories, PWRS calculation
- Factor Survey box with: 11 questions, ~5 min, demographic features, normalized vectors
- Before/After model training workflows
- Clear labels showing "Ground Truth" vs "ML Features"
- Time savings indicator (18 min → 5 min)

**Layout Suggestion**:
```
┌─────────────────────────────────────────────────────────────────┐
│                    DUAL-SURVEY ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────┐    ┌─────────────────────────────┐ │
│  │     TARGET SURVEY       │    │       FACTOR SURVEY         │ │
│  │   (Ground Truth)        │    │     (ML Features)           │ │
│  ├─────────────────────────┤    ├─────────────────────────────┤ │
│  │ • 27 Questions          │    │ • 11 Questions              │ │
│  │ • ~15 minutes           │    │ • ~5 minutes                │ │
│  │ • Self-reported         │    │ • Objective data            │ │
│  │   readiness factors     │    │ • Demographics, GPA, etc.   │ │
│  │                         │    │                             │ │
│  │         ▼               │    │          ▼                  │ │
│  │ ┌─────────────────┐     │    │ ┌───────────────────┐       │ │
│  │ │ PWRS Formula    │     │    │ │ Feature Vector    │       │ │
│  │ │ → Success Rate  │     │    │ │ (Normalized)      │       │ │
│  │ │   (0-100%)      │     │    │ │ → ML Input        │       │ │
│  │ └─────────────────┘     │    │ └───────────────────┘       │ │
│  └─────────────────────────┘    └─────────────────────────────┘ │
│              │                              │                    │
│              │         TRAINING DATA        │                    │
│              └──────────────┬───────────────┘                    │
│                             ▼                                    │
│                    ┌─────────────────┐                          │
│                    │   ML MODEL      │                          │
│                    │ Learns: Features│                          │
│                    │    → Success    │                          │
│                    └─────────────────┘                          │
│                                                                  │
│  ═══════════════════════════════════════════════════════════    │
│  AFTER MODEL TRAINING: Factor Survey Only → Predicted Success   │
│  Survey burden reduced: 18 min → 5 min                          │
└─────────────────────────────────────────────────────────────────┘
```

**Data Sources**: Section 3.5.1, Section 5.4.2-5.4.3 (survey details)

---

### FIGURE 5: Feedback Loop Architecture

**Location**: Section 3.5.3 (Pseudo-Labeling Feedback Loop)

**Caption**: "Pseudo-Labeling Feedback Loop: Reducing Survey Burden Through High-Confidence Predictions"

**Visualization Type**: Flowchart with decision points

**What Should Be Illustrated**:
- Complete feedback loop workflow
- Decision point at rating threshold (≥4 stars vs <4 stars)
- Pseudo-label acceptance path (high confidence)
- Correction path via Target Survey (low confidence)
- Data flowing back to training pipeline

**Key Elements to Include**:
- Step 1: Student completes Factor Survey (~3 min)
- Step 2: System generates prediction
- Step 3: Student rates accuracy (1-5 stars)
- Decision diamond: Rating ≥ 4?
- YES path: Prediction accepted as pseudo-label, Target Survey skipped
- NO path: Student redirected to Target Survey for correction
- Both paths feed into training data
- Time savings annotation

**Layout Suggestion**:
```
┌───────────────────────────────────────────────────────────────┐
│                    FEEDBACK LOOP WORKFLOW                      │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│    ┌────────────────────────┐                                 │
│    │ 1. Complete Factor     │                                 │
│    │    Survey (~3 min)     │                                 │
│    └───────────┬────────────┘                                 │
│                ▼                                               │
│    ┌────────────────────────┐                                 │
│    │ 2. View ML Prediction  │                                 │
│    │    (Success Rate %)    │                                 │
│    └───────────┬────────────┘                                 │
│                ▼                                               │
│    ┌────────────────────────┐                                 │
│    │ 3. Rate Accuracy       │                                 │
│    │    ⭐⭐⭐⭐⭐ (1-5)      │                                 │
│    └───────────┬────────────┘                                 │
│                ▼                                               │
│         ◆ Rating ≥ 4? ◆                                       │
│        ╱              ╲                                        │
│      YES               NO                                      │
│       │                 │                                      │
│       ▼                 ▼                                      │
│  ┌──────────────┐  ┌──────────────────┐                       │
│  │ HIGH         │  │ LOW CONFIDENCE   │                       │
│  │ CONFIDENCE   │  │                  │                       │
│  │              │  │ Complete Target  │                       │
│  │ Accept as    │  │ Survey for       │                       │
│  │ Pseudo-Label │  │ Correction       │                       │
│  │              │  │ (~15 min)        │                       │
│  │ Skip Target  │  │                  │                       │
│  │ Survey       │  │ Use corrected    │                       │
│  │              │  │ rate as label    │                       │
│  └──────┬───────┘  └────────┬─────────┘                       │
│         │                   │                                  │
│         └─────────┬─────────┘                                  │
│                   ▼                                            │
│         ┌─────────────────┐                                   │
│         │ TRAINING DATA   │                                   │
│         │ (for model      │                                   │
│         │  improvement)   │                                   │
│         └─────────────────┘                                   │
│                                                                │
│  ════════════════════════════════════════════════════════     │
│  Result: Avg survey time reduced from 18 min to ~5 min        │
└───────────────────────────────────────────────────────────────┘
```

**Data Sources**: Section 3.5.3, Section 4.4.5 (implementation code)

---

### FIGURE 6: Data Flow Architecture Diagram

**Location**: Section 3.6.3 (Model Training Flow)

**Caption**: "End-to-End Data Flow: From Survey Submission to ML Training and Prediction"

**Visualization Type**: Comprehensive data flow diagram with swim lanes

**What Should Be Illustrated**:
- Three major flows:
  1. Survey Submission Flow (3.6.1)
  2. Prediction Generation Flow (3.6.2)
  3. Model Training Flow (3.6.3)
- Data transformations at each stage
- Component interactions

**Key Elements to Include**:
- Survey Submission: Client validation → Debounced persistence → Dual write → Normalization → Workflow update
- Prediction: Completion notification → Model metadata → Feature vector → Model Server request → Store prediction → Display
- Training: Admin initiation → Data aggregation → Job queue → Synthetic generation (if GAN) → Training → Validation (real only) → Save → Callback → Activation
- Swim lanes for: Client, Backend, Model Server, Database

**Layout Suggestion**:
```
CLIENT          BACKEND           MODEL SERVER       DATABASE
  │                │                   │                │
  │ SURVEY SUBMISSION FLOW            │                │
  ├───Validation───▶│                  │                │
  │                ├──────────────────────────────────▶│
  │                │                   │         Store Answers
  │                │                   │                │
  │ PREDICTION GENERATION FLOW        │                │
  │                │◀──────────────────────────────────┤
  │                │         Get Active Model          │
  │                ├──Build Feature──▶│                │
  │                │      Vector       │                │
  │                │◀───Prediction────┤                │
  │◀──Display──────┤                   │                │
  │   Prediction   │                   │                │
  │                │                   │                │
  │ MODEL TRAINING FLOW               │                │
  │ (Admin)        │                   │                │
  │────Initiate───▶│                   │                │
  │                ├──Aggregate Data──────────────────▶│
  │                │◀─────────────────────────────────┤
  │                ├──Queue Job───────▶│               │
  │                │                   ├──Train──────▶ │
  │                │◀──Progress────────┤               │
  │                │◀──Complete────────┤               │
  │                ├──Activate Model─────────────────▶│
  │◀──Notify───────┤                   │               │
```

**Data Sources**: Section 3.6.1, 3.6.2, 3.6.3

---

### FIGURE 7: Deployment Architecture Diagram

**Location**: Section 3.7.3 (CI/CD Pipeline)

**Caption**: "Production Deployment Architecture with Container Orchestration"

**Visualization Type**: Infrastructure/deployment diagram

**What Should Be Illustrated**:
- Docker container topology from Table 3
- Nginx reverse proxy and load balancing
- Three Docker networks (Frontend, Backend, ML)
- CI/CD pipeline flow
- GitHub Actions integration

**Key Elements to Include**:
- Container instances: 2x Frontend, 3x Backend (4 workers each), 3x Model Server
- Resource allocations from Table 3
- Nginx load balancer with least-connections algorithm
- Network segmentation visualization
- GitHub → Docker Hub → Production Server flow
- Database connection (MongoDB Atlas)

**Layout Suggestion**:
```
┌─────────────────────────────────────────────────────────────────┐
│                     CI/CD PIPELINE                               │
│  GitHub ──▶ GitHub Actions ──▶ Docker Hub ──▶ Production SSH    │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PRODUCTION SERVER                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    NGINX (Reverse Proxy)                  │   │
│  │              Least-Connections Load Balancing             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                    │                    │                        │
│  ════════════════════════════════════════════════════════════   │
│  FRONTEND NETWORK                                                │
│  ┌─────────────┐    ┌─────────────┐                             │
│  │ Frontend 1  │    │ Frontend 2  │   (2 CPU, 1GB each)        │
│  │ React/Nginx │    │ React/Nginx │                             │
│  └─────────────┘    └─────────────┘                             │
│  ════════════════════════════════════════════════════════════   │
│  BACKEND NETWORK                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐                      │
│  │Backend 1  │ │Backend 2  │ │Backend 3  │ (4 CPU, 10GB each)  │
│  │(4 workers)│ │(4 workers)│ │(4 workers)│                      │
│  └───────────┘ └───────────┘ └───────────┘                      │
│         │             │             │                            │
│         └─────────────┼─────────────┘                            │
│                       │                                          │
│  ════════════════════════════════════════════════════════════   │
│  ML NETWORK                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐    ┌─────────────────┐  │
│  │Model 1   │ │Model 2   │ │Model 3   │    │ Shared Volume   │  │
│  │(Python)  │ │(Python)  │ │(Python)  │───▶│ (Model Storage) │  │
│  └──────────┘ └──────────┘ └──────────┘    └─────────────────┘  │
│  (4 CPU, 4GB each)                                               │
└─────────────────────────────────────────────────────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  MongoDB Atlas  │
              │  (Managed DB)   │
              └─────────────────┘

Total Resources: 30 CPU cores, 46 GB RAM, 8 containers
```

**Data Sources**: Section 3.7.1 (Table 3), Section 3.7.2, Section 3.7.3

---

### FIGURE 8: Prediction Feedback Interface Mockup

**Location**: Section 4.2.5 (Prediction Feedback Interface)

**Caption**: "Prediction Feedback Interface: Student View After Factor Survey Completion"

**Visualization Type**: UI mockup / wireframe

**What Should Be Illustrated**:
- Complete prediction feedback screen as students see it
- Visual representation of predicted success rate
- 5-star rating input
- Optional feedback text field
- Conditional navigation based on rating

**Key Elements to Include**:
- Header with "Your Readiness Score" or similar
- Large visual gauge/meter showing percentage (e.g., 72%)
- Score interpretation band (At-Risk: 0-40%, Moderate: 40-70%, High Readiness: 70%+)
- Contextual message based on score
- "How accurate does this feel?" prompt
- 5 clickable star icons
- "Optional: Tell us more" text area
- "Continue" button
- Note: "Your feedback helps improve our predictions"

**Layout Suggestion**:
```
┌─────────────────────────────────────────────────────────────────┐
│  ← Back                           ACOSUS                    ≡   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    Your Readiness Score                          │
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │                 │                          │
│                    │   ▓▓▓▓▓▓▓░░░    │                          │
│                    │      72%        │     HIGH READINESS       │
│                    │                 │                          │
│                    └─────────────────┘                          │
│                                                                  │
│   Based on your responses, you show strong readiness for        │
│   academic success in your computing program.                   │
│                                                                  │
│   ─────────────────────────────────────────────────────────     │
│                                                                  │
│   How accurate does this assessment feel?                       │
│                                                                  │
│              ☆  ☆  ☆  ☆  ☆                                      │
│         Not at all        Exactly right                         │
│                                                                  │
│   ─────────────────────────────────────────────────────────     │
│                                                                  │
│   Optional: Tell us more about your reaction                    │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                                                         │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│   ℹ️ Your feedback helps us improve predictions for future      │
│      students.                                                   │
│                                                                  │
│                    ┌────────────────────┐                       │
│                    │     Continue       │                       │
│                    └────────────────────┘                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Data Sources**: Section 4.2.5, Section 3.5.3 (feedback logic)

---

## Table Specifications

### Tables Already Complete (Inline in Sections)

The following tables are already fully specified with data in the section drafts:

| Table | Location | Notes |
|-------|----------|-------|
| TABLE 1 | Section 3.3.2 | Technology Stack - 11 rows with Layer, Technology, Version, Justification |
| TABLE 2 | Section 3.5.2 | Progressive Learning Phases - 3 phases with student count, model, trigger |
| TABLE 3 | Section 3.7.1 | Container Configuration - 3 services with instances, CPU, memory |
| TABLE 4 | Section 4.3.2 | Survey Attempt States - 7 states with transitions |
| TABLE 5 | Section 4.4.3 | KNN Performance - 4 cohort sizes with k, MAE, R², time |
| TABLE 6 | Section 4.4.4 | Model Performance Comparison - 3 models with MAE, R² |
| TABLE 7 | Section 4.5.2 | Access Control Matrix - 6 resources × 4 roles |
| TABLE 8 | Section 4.8 | Implementation Status - 10 components with status |
| TABLE 9 | Section 5.2 | Research Questions - 5 RQs with focus areas |
| TABLE 10 | Section 5.3.1 | Study Design Parameters - 7 parameters |
| TABLE 11 | Section 5.4 | Participant Tasks - 6 tasks with duration, criteria |
| TABLE 12 | Section 5.4.2 | Target Survey Categories - 5 categories with question counts |
| TABLE 13 | Section 5.4.3 | Factor Survey Categories - 4 categories with examples |
| TABLE 14 | Section 5.5.1 | SUS Items - 10 items with scale |
| TABLE 15 | Section 5.6.1 | Quantitative Data Collection - 9 measures with sources |
| TABLE 16 | Section 5.8.1 | Success Criteria - 7 metrics with targets |
| TABLE 23 | Section 5.10.1 | Validation Thresholds - 4 quality levels |
| TABLE 24 | Section 5.10.3 | Feedback Loop Progression - 4 phases with metrics |
| TABLE 25 | Section 5.13 | Evaluation Timeline - 10 phases with dates/status |

### Tables Requiring Data (Pending User Study)

These tables have structure defined but await data collection:

| Table | Location | Structure | Data Source |
|-------|----------|-----------|-------------|
| TABLE 17 | Section 5.9.1 | Demographics: Gender, Age, First-Gen, Transfer Type | Participant surveys |
| TABLE 18 | Section 5.9.2 | Task Completion: Rate, Mean Time, SD per task | System logs |
| TABLE 19 | Section 5.9.3 | SUS Scores: Mean, SD per 10 items + Overall | Qualtrics responses |
| TABLE 20 | Section 5.9.4 | TAM Results: Mean, SD, Cronbach's α per construct | Qualtrics responses |
| TABLE 21 | Section 5.9.5 | Prediction Feedback: Mean rating, % high/low confidence | In-app feedback |
| TABLE 22 | Section 5.9.6 | Theme Analysis: Theme, Frequency, Representative Quote | Qualitative coding |

**Note**: These tables should be populated after data collection in Spring 2026. The current placeholders with "--" values are intentional and should remain until real data is available.

---

## Production Guidelines

### Figure Creation Tools
- **Architecture Diagrams**: draw.io, Lucidchart, or PlantUML
- **UI Mockups**: Figma, Sketch, or Balsamiq
- **Flowcharts**: draw.io, Lucidchart, or Mermaid

### Style Recommendations
1. Use consistent color scheme across all figures
2. Maintain readable font sizes (minimum 10pt in final output)
3. Use high-contrast colors for accessibility
4. Export at 300 DPI minimum for print
5. Provide vector formats (SVG/PDF) where possible

### Labeling Conventions
- All figures should have captions below
- All tables should have captions above
- Use consistent numbering (FIGURE 1, TABLE 1)
- Include source references where applicable

### Academic Formatting
- Figures/tables should fit within standard page margins
- Consider single-column vs. two-column layouts
- Ensure all text is legible when printed in grayscale
