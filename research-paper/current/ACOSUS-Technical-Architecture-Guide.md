# ACOSUS Technical Architecture Guide

This document provides a technical overview of the ACOSUS (AI-driven Counseling System for Underrepresented Students) platform architecture, data flows, and system design decisions.

---

## 1. System Overview

ACOSUS is a three-tier web application with a separate machine learning service layer. The architecture prioritizes:

- **Separation of Concerns**: UI, business logic, data, and ML are decoupled
- **Scalability**: Each layer can scale independently
- **Flexibility**: Survey instruments can evolve without code changes
- **Progressive Capability**: System delivers value immediately while improving over time

### 1.1 High-Level Architecture

```mermaid
flowchart TB
    subgraph Client["Client Layer"]
        UI["UI (React App)"]
    end

    subgraph Server["Application Layer"]
        Backend["Backend (Node.js)"]
        DB[(MongoDB)]
    end

    subgraph ML["Machine Learning Layer"]
        Predict["Model Server<br/>(Prediction)"]
        Train["Model Server<br/>(Training)"]
        Storage["Model Storage"]
    end

    UI <--> Backend
    Backend <--> DB
    Backend <--> Predict
    Backend --> Train
    Train --> Storage
    Predict <--> Storage

    style Client fill:#e1f5fe
    style Server fill:#fff3e0
    style ML fill:#fce4ec
```

**Figure 1.** High-level system architecture showing the three primary layers.

### 1.2 Component Summary

| Layer | Technology | Responsibility |
|-------|------------|----------------|
| **Client** | React, TypeScript, Tailwind CSS | User interfaces for students, advisors, and administrators |
| **Application** | Node.js, Express, MongoDB | Authentication, survey management, PWRS calculation, API orchestration |
| **ML - Prediction** | Python, Flask | Real-time inference (KNN or Neural Network) |
| **ML - Training** | Python, Flask, TensorFlow | Model training, GAN data generation, validation |

---

## 2. Deployment Architecture

The system is deployed on a dedicated server with containerized services behind an Nginx reverse proxy.

```mermaid
flowchart LR
    subgraph External["External"]
        GitHub["GitHub Repository"]
        DockerHub["Docker Hub"]
    end

    subgraph CI["CI/CD Pipeline"]
        Actions["GitHub Actions"]
    end

    subgraph Server["Dedicated Server (acosus.neiu.edu)"]
        Nginx["Nginx<br/>Reverse Proxy"]

        subgraph Containers["Docker Containers"]
            UIContainer["UI Container<br/>(React)"]
            BackendContainer["Backend Container<br/>(Node.js)"]
            ModelContainer["Model Server<br/>(Flask)"]
        end

        ModelStorage["Model File Storage"]
        MongoDB["Managed MongoDB"]
    end

    GitHub --> Actions
    Actions --> DockerHub
    DockerHub --> Containers

    Nginx --> UIContainer
    Nginx --> BackendContainer
    BackendContainer --> ModelContainer
    ModelContainer --> ModelStorage
    BackendContainer --> MongoDB

    style External fill:#f5f5f5
    style CI fill:#e3f2fd
    style Server fill:#e8f5e9
```

**Figure 2.** Deployment architecture with CI/CD pipeline.

### 2.1 Deployment Flow

1. **Code Push**: Developer pushes to GitHub repository
2. **Build**: GitHub Actions builds Docker images
3. **Registry**: Images pushed to Docker Hub
4. **Deploy**: Updated containers deployed to production server
5. **Routing**: Nginx routes requests to appropriate containers

### 2.2 Container Configuration

| Container | Port | Purpose |
|-----------|------|---------|
| UI (React) | 3000 | Serves static frontend assets |
| Backend (Node.js) | 5000 | REST API, business logic |
| Model Server (Flask) | 8000 | ML predictions and training |

---

## 3. Data Architecture

### 3.1 Database Collections

The MongoDB database stores all application data across interconnected collections.

```mermaid
erDiagram
    Users ||--o{ StudentProfiles : has
    Users ||--o{ Attempts : creates

    Quizzes ||--o{ Questions : contains
    Quizzes ||--o{ Attempts : "attempted via"
    Quizzes ||--o| Quizzes : "linked to (Target)"

    Questions ||--o{ QuestionOptions : has
    Questions ||--o{ Answers : "answered by"

    Attempts ||--o{ Answers : contains

    QuestionCategories ||--o{ Questions : groups

    ModelMetaData ||--o| Quizzes : "trained for"

    Users {
        ObjectId _id
        string email
        string role
        string firstName
        string lastName
    }

    Quizzes {
        ObjectId _id
        string title
        string quizType
        string targetType
        ObjectId linkedTargetQuiz
    }

    Questions {
        ObjectId _id
        string question
        string slug
        number priorityScore
        string dataTypeForModel
        ObjectId categoryId
    }

    QuestionOptions {
        ObjectId _id
        string optionLabel
        any optionValue
        number optionWeightage
    }

    Attempts {
        ObjectId _id
        ObjectId studentId
        ObjectId quizId
        string attemptStatus
        number successRate
    }

    ModelMetaData {
        ObjectId _id
        ObjectId quizId
        string modelType
        number sampleCount
        object metrics
    }
```

**Figure 3.** Entity-relationship diagram of core database collections.

### 3.2 Key Data Entities

#### Quizzes (Surveys)
- **quizType**: `"target"` or `"factor"` - determines survey purpose
- **targetType**: `"single"` or `"multi"` - for target surveys, determines if single question or multiple questions with PWRS
- **linkedTargetQuiz**: For factor surveys, references which target survey provides the prediction label

#### Questions
- **priorityScore**: 1-10 scale indicating importance for PWRS calculation
- **dataTypeForModel**: `"ordinal"` or `"cardinal"` - determines ML normalization strategy
- **slug**: Unique identifier for answer mapping

#### QuestionOptions
- **optionWeightage**: Numeric value (0-10) representing the "score" for this answer choice
- Used in both PWRS calculation and feature normalization

#### Attempts
- **attemptStatus**: `"in-progress"` or `"completed"`
- **successRate**: Calculated via PWRS (target surveys) or predicted via ML (factor surveys)
- **modifiedBy**: Tracks if student or advisor entered/modified responses

#### ModelMetaData
- Stores trained model configuration per factor survey
- Tracks sample count, model type (KNN/NN), performance metrics
- Enables model versioning and rollback

---

## 4. Application Layer Architecture

### 4.1 Backend Service Structure

```mermaid
flowchart TB
    subgraph API["REST API Layer"]
        Auth["Authentication<br/>(/auth)"]
        Student["Student Routes<br/>(/student)"]
        Advisor["Advisor Routes<br/>(/advisor)"]
        Admin["Admin Routes<br/>(/admin)"]
        Quiz["Quiz Routes<br/>(/quiz)"]
        Model["Model Routes<br/>(/model)"]
    end

    subgraph Services["Service Layer"]
        AuthService["Auth Service<br/>(JWT)"]
        PWRSService["PWRS Engine"]
        SurveyService["Survey Manager"]
        TrainingService["Training Trigger"]
    end

    subgraph Data["Data Layer"]
        Mongoose["Mongoose ODM"]
        MongoDB[(MongoDB)]
    end

    Auth --> AuthService
    Student --> SurveyService
    Advisor --> SurveyService
    Admin --> SurveyService
    Quiz --> PWRSService
    Model --> TrainingService

    AuthService --> Mongoose
    PWRSService --> Mongoose
    SurveyService --> Mongoose
    TrainingService --> Mongoose

    Mongoose --> MongoDB

    style API fill:#e3f2fd
    style Services fill:#fff3e0
    style Data fill:#e8f5e9
```

**Figure 4.** Backend service architecture.

### 4.2 API Route Structure

| Route Prefix | Purpose | Key Endpoints |
|--------------|---------|---------------|
| `/auth` | Authentication | Login, register, refresh token |
| `/student` | Student operations | Take surveys, view predictions, submit feedback |
| `/advisor` | Advisor operations | Search students, view profiles, manage surveys |
| `/admin` | Administrative | Create surveys, configure models, view analytics |
| `/quiz` | Survey management | CRUD for quizzes, questions, options |
| `/model` | ML operations | Trigger training, check status, get predictions |

### 4.3 Authentication Flow

```mermaid
sequenceDiagram
    participant Client
    participant Backend
    participant DB as MongoDB

    Client->>Backend: POST /auth/login {email, password}
    Backend->>DB: Find user, verify password
    DB-->>Backend: User record
    Backend->>Backend: Generate JWT (access + refresh)
    Backend-->>Client: {accessToken, refreshToken, user}

    Note over Client: Store tokens

    Client->>Backend: GET /api/protected<br/>Authorization: Bearer {accessToken}
    Backend->>Backend: Verify JWT signature
    Backend->>Backend: Check role permissions
    Backend-->>Client: Protected resource
```

**Figure 5.** JWT authentication flow.

### 4.4 Role-Based Access Control

| Role | Capabilities |
|------|-------------|
| **Student** | Take assigned surveys, view own predictions, provide feedback |
| **Advisor** | Search students, view any student profile, manage surveys, act-as student |
| **Admin** | All advisor capabilities + create surveys, configure models, trigger training |

---

## 5. Frontend Architecture

### 5.1 Portal Structure

The frontend is organized into three distinct portals, each serving a specific user role.

```mermaid
flowchart TB
    subgraph App["React Application"]
        Router["React Router"]

        subgraph Student["Student Portal"]
            SDash["Dashboard"]
            STake["Take Survey"]
            SView["View Predictions"]
            SFeedback["Provide Feedback"]
        end

        subgraph Advisor["Advisor Portal"]
            ADash["Dashboard<br/>(Student Search)"]
            AProfile["Student Profile"]
            ASurvey["Survey Management"]
            AActAs["Act-As Mode"]
        end

        subgraph Admin["Admin Portal"]
            AdminDash["Dashboard"]
            QuizBuilder["Survey Builder"]
            ModelConfig["Model Configuration"]
            Analytics["Analytics"]
        end
    end

    Router --> Student
    Router --> Advisor
    Router --> Admin

    style Student fill:#e3f2fd
    style Advisor fill:#fff3e0
    style Admin fill:#fce4ec
```

**Figure 6.** Frontend portal structure.

### 5.2 Student Portal Features

| Feature | Description |
|---------|-------------|
| **Survey List** | View assigned surveys with completion status |
| **Survey Taking** | Question-by-question interface with progress tracking |
| **Auto-Save** | Responses saved automatically to prevent data loss |
| **Prediction View** | Display predicted success rate with feedback prompt |
| **Feedback Rating** | 1-5 star rating of prediction accuracy |

### 5.3 Advisor Portal Features

| Feature | Description |
|---------|-------------|
| **Student Search** | Search by name, email, or student ID with filters |
| **Unified Profile** | Tabbed view of student data organized by category |
| **Survey Management** | View attempts, completion status, individual responses |
| **Act-As Capability** | Complete surveys on behalf of students during sessions |
| **Copy & Edit** | Duplicate attempts with modifications for data refinement |

### 5.4 Admin Portal Features

| Feature | Description |
|---------|-------------|
| **Survey Builder** | Create target and factor surveys with questions/options |
| **Question Configuration** | Set priority scores, option weightages, data types |
| **Survey Linkage** | Connect factor surveys to target surveys |
| **Model Training** | Trigger training, view status, compare model versions |
| **Analytics Dashboard** | Completion rates, prediction distributions, feedback scores |

---

## 6. Machine Learning Architecture

### 6.1 Model Server Overview

The ML layer is split into two logical components:

1. **Prediction Server**: Handles real-time inference requests
2. **Training Server**: Handles asynchronous model training jobs

```mermaid
flowchart TB
    subgraph Prediction["Model Server (Prediction)"]
        PredictAPI["Predict API"]
        DataTransform["Data Transformation"]
        Scaling["Feature Scaling"]
        ModelSelect["Model Selection"]
        Inference["Perform Prediction"]
        Output["Readiness Score Output"]
    end

    subgraph Training["Model Server (Training)"]
        Queue["Training Queue"]
        Gather["Gather Data"]
        Transform["Data Transformation"]

        subgraph KNNPath["KNN Path (N < 100)"]
            KNNTrain["Store Samples"]
            KNNValidate["Cross-Validation"]
            KNNMeta["Save Metadata"]
        end

        subgraph NNPath["NN Path (N ≥ 100)"]
            GANTrain["GAN Training"]
            SynthGen["Generate Synthetic"]
            NNTrain["Train Neural Net"]
            NNValidate["Validate (Real Only)"]
        end

        Version["Model Versioning"]
        Deploy["Deploy if Better"]
    end

    Storage[(Model Storage)]

    PredictAPI --> DataTransform --> Scaling --> ModelSelect --> Inference --> Output
    ModelSelect <--> Storage

    Queue --> Gather --> Transform
    Transform --> KNNPath
    Transform --> NNPath
    KNNPath --> Version
    NNPath --> Version
    Version --> Deploy --> Storage

    style Prediction fill:#e8f5e9
    style Training fill:#fff3e0
```

**Figure 7.** Model server architecture showing prediction and training flows.

### 6.2 Prediction Flow

```mermaid
sequenceDiagram
    participant Backend
    participant ModelServer
    participant Storage

    Backend->>ModelServer: POST /predict<br/>{quizId, features}

    ModelServer->>Storage: Load model metadata
    Storage-->>ModelServer: {modelType, config}

    ModelServer->>ModelServer: Transform features<br/>(normalize to 0-10)

    alt KNN Model
        ModelServer->>Storage: Load training samples
        Storage-->>ModelServer: Labeled samples
        ModelServer->>ModelServer: Find k nearest neighbors
        ModelServer->>ModelServer: Weighted average
    else Neural Network
        ModelServer->>Storage: Load NN weights
        Storage-->>ModelServer: Trained model
        ModelServer->>ModelServer: Forward pass
    end

    ModelServer-->>Backend: {prediction: 74.2, confidence: 0.82}
```

**Figure 8.** Prediction request flow.

### 6.3 Data Transformation Pipeline

All survey responses must be normalized to a common scale (0-10) before ML ingestion.

```mermaid
flowchart LR
    subgraph Input["Raw Responses"]
        Ordinal["Ordinal<br/>(Confidence: 'High')"]
        Cardinal["Cardinal<br/>(Institution: 'CC')"]
        Continuous["Continuous<br/>(GPA: 3.4)"]
        Temporal["Temporal<br/>(Grad: 2026)"]
    end

    subgraph Transform["Transformation"]
        OrdinalT["Use option<br/>weightage directly"]
        CardinalT["Sum selected /<br/>Sum total × 10"]
        ContinuousT["Min-max<br/>normalization"]
        TemporalT["Duration scoring<br/>curve"]
    end

    subgraph Output["Normalized (0-10)"]
        O1["8.0"]
        O2["5.0"]
        O3["8.5"]
        O4["9.0"]
    end

    Ordinal --> OrdinalT --> O1
    Cardinal --> CardinalT --> O2
    Continuous --> ContinuousT --> O3
    Temporal --> TemporalT --> O4

    style Input fill:#ffebee
    style Transform fill:#fff3e0
    style Output fill:#e8f5e9
```

**Figure 9.** Feature normalization pipeline by data type.

### 6.4 Model Selection Logic

The system automatically selects the appropriate model based on available training data.

```mermaid
flowchart TD
    Start["Prediction Request"]
    Check["Check sample count<br/>for this survey"]

    LT10{"N < 10?"}
    LT100{"N < 100?"}

    NoModel["No Prediction<br/>(Bootstrap Phase)"]
    KNN["Use KNN Model"]
    NN["Use Neural Network"]
    NNCheck{"NN Available<br/>& Better?"}

    Start --> Check --> LT10
    LT10 -->|Yes| NoModel
    LT10 -->|No| LT100
    LT100 -->|Yes| KNN
    LT100 -->|No| NNCheck
    NNCheck -->|Yes| NN
    NNCheck -->|No| KNN

    style NoModel fill:#ffcdd2
    style KNN fill:#c8e6c9
    style NN fill:#bbdefb
```

**Figure 10.** Automatic model selection based on data availability.

---

## 7. Progressive Learning Framework

### 7.1 Phase Transitions

The system progresses through three phases as data accumulates.

```mermaid
flowchart LR
    Start(("Deploy")) --> Bootstrap

    subgraph Bootstrap["Phase 1: Bootstrap"]
        B1["N < 10 students"]
        B2["No predictions"]
        B3["Collect Target + Factor"]
    end

    subgraph KNN["Phase 2: Instance-Based"]
        K1["10 ≤ N < 100"]
        K2["KNN predictions"]
        K3["Factor only + Feedback"]
    end

    subgraph Neural["Phase 3: Neural Network"]
        N1["N ≥ 100"]
        N2["GAN augmentation"]
        N3["NN predictions"]
    end

    Bootstrap -->|"10th student"| KNN
    KNN -->|"100th student"| Neural
    Neural -.->|"NN underperforms"| KNN

    style Bootstrap fill:#fff3e0
    style KNN fill:#e3f2fd
    style Neural fill:#e8f5e9
```

**Figure 11.** Progressive learning phase state diagram.

### 7.2 Phase 1: Bootstrap (N < 10)

```mermaid
flowchart LR
    Enroll["Student<br/>Enrolls"]
    Target["Take Target<br/>Survey"]
    PWRS["PWRS<br/>Calculation"]
    Factor["Take Factor<br/>Survey"]
    Store["Store<br/>Labeled Data"]
    Thanks["Thank You"]

    Enroll --> Target --> PWRS --> Factor --> Store --> Thanks

    style Target fill:#ffcc80
    style Factor fill:#80deea
```

**Figure 12.** Phase 1 student flow—both surveys required.

### 7.3 Phase 2: Instance-Based Learning (10 ≤ N < 100)

```mermaid
flowchart TB
    Enroll["Student<br/>Enrolls"]
    Factor["Take Factor<br/>Survey (~5 min)"]
    Predict["KNN<br/>Prediction"]
    Show["Show Prediction<br/>'Your success rate: 74%'"]
    Rate["Student Rates<br/>Prediction (1-5)"]

    High{"Rating ≥ 4?"}

    Accept["Accept as<br/>Pseudo-Label"]
    Target["Take Target<br/>Survey (~10 min)"]
    PWRSCalc["Calculate<br/>Ground Truth"]

    Store["Add to<br/>Training Data"]
    Thanks["Thank You"]

    Enroll --> Factor --> Predict --> Show --> Rate --> High
    High -->|Yes| Accept --> Store --> Thanks
    High -->|No| Target --> PWRSCalc --> Store --> Thanks

    style Factor fill:#80deea
    style Target fill:#ffcc80
    style Accept fill:#c8e6c9
```

**Figure 13.** Phase 2 student flow with feedback-driven pseudo-labeling.

### 7.4 Phase 3: Neural Network (N ≥ 100)

```mermaid
flowchart TB
    subgraph Training["Training Pipeline"]
        Gather["Gather 100<br/>Real Students"]
        Split["Split: 80 Train<br/>20 Validate"]
        GAN["Train GAN on<br/>80 Real"]
        Generate["Generate 400<br/>Synthetic"]
        Combine["Combine: 80 Real<br/>+ 400 Synthetic"]
        TrainNN["Train Neural<br/>Network"]
        Validate["Validate on<br/>20 Real ONLY"]
        Compare{"Better than<br/>KNN?"}
        Deploy["Deploy NN"]
        Keep["Keep KNN"]
    end

    Gather --> Split --> GAN --> Generate --> Combine --> TrainNN --> Validate --> Compare
    Compare -->|Yes| Deploy
    Compare -->|No| Keep

    style GAN fill:#ce93d8
    style Generate fill:#ce93d8
    style Validate fill:#fff59d
```

**Figure 14.** Phase 3 GAN-augmented neural network training pipeline.

---

## 8. Survey System Architecture

### 8.1 Survey Types

```mermaid
flowchart TB
    subgraph Surveys["Survey System"]
        subgraph Target["Target Surveys (Labels)"]
            Single["Single Question<br/>Direct 0-100 input"]
            Multi["Multi Question<br/>PWRS calculation"]
        end

        subgraph Factor["Factor Surveys (Features)"]
            Academic["Academic Background"]
            Financial["Financial Circumstances"]
            Technical["Technical Preparation"]
            Temporal["Temporal Factors"]
        end

        Link["Survey Linkage"]
    end

    Target -.->|"provides label for"| Link
    Factor -.->|"provides features for"| Link

    style Target fill:#ffcc80
    style Factor fill:#80deea
```

**Figure 15.** Survey type hierarchy.

### 8.2 Question Configuration

Each question has configuration that affects both PWRS calculation and ML feature extraction.

| Field | Purpose | Values |
|-------|---------|--------|
| **priorityScore** | PWRS weighting | 1-10 (higher = more important) |
| **dataTypeForModel** | ML normalization strategy | `"ordinal"` or `"cardinal"` |
| **isRequired** | Completion enforcement | `true` or `false` |
| **categoryId** | UI organization | Reference to category |

### 8.3 Option Configuration

| Field | Purpose | Example |
|-------|---------|---------|
| **optionLabel** | Display text | "Very Confident" |
| **optionValue** | Storage value | "very_confident" |
| **optionWeightage** | Numeric score | 9 (out of 10) |

### 8.4 PWRS Calculation Flow

```mermaid
flowchart LR
    subgraph Input["Survey Responses"]
        R1["Q1: Option A (8/10)"]
        R2["Q2: Option C (4/10)"]
        R3["Q3: Option B (7/10)"]
    end

    subgraph Step1["Step 1: Normalize"]
        N1["0.80"]
        N2["0.40"]
        N3["0.70"]
    end

    subgraph Step2["Step 2: Weight by Priority"]
        W1["0.80 × 9 = 7.2"]
        W2["0.40 × 7 = 2.8"]
        W3["0.70 × 8 = 5.6"]
    end

    subgraph Step3["Step 3: Base Score"]
        Sum["Sum: 15.6"]
        Div["÷ (9+7+8) = 24"]
        Base["Base: 0.65"]
    end

    subgraph Step4["Step 4: Calibrate"]
        Logistic["Logistic(0.65)"]
        Final["Success Rate: 71%"]
    end

    R1 --> N1 --> W1 --> Sum
    R2 --> N2 --> W2 --> Sum
    R3 --> N3 --> W3 --> Sum
    Sum --> Div --> Base --> Logistic --> Final

    style Final fill:#c8e6c9
```

**Figure 16.** PWRS calculation pipeline.

---

## 9. Feedback Loop Architecture

### 9.1 Feedback Collection Flow

```mermaid
flowchart TD
    Predict["System predicts: 74%"]
    Show["Display to student"]
    Ask["'How accurate is this?'"]
    Rate["Student rates: ⭐⭐⭐⭐"]

    Check{"Rating ≥ 4?"}

    subgraph Accept["High Rating Path"]
        Pseudo["Use 74% as label"]
        Flag1["Flag: pseudo-labeled"]
        Skip["Skip Target Survey"]
    end

    subgraph Reject["Low Rating Path"]
        Request["Request Target Survey"]
        Complete["Student completes"]
        Calculate["PWRS → 62%"]
        Replace["Use 62% as label"]
        Flag2["Flag: ground-truth"]
    end

    Store["Add to training data"]

    Predict --> Show --> Ask --> Rate --> Check
    Check -->|"≥ 4"| Accept --> Store
    Check -->|"< 4"| Reject --> Store

    style Accept fill:#c8e6c9
    style Reject fill:#ffcc80
```

**Figure 17.** Feedback-driven pseudo-labeling decision flow.

### 9.2 Training Data Labels

| Source | Label Type | Usage |
|--------|-----------|-------|
| **Phase 1** | Ground Truth | Student completed Target Survey, PWRS calculated |
| **High Rating (≥4)** | Pseudo-Label | Model prediction accepted by student |
| **Low Rating (<4)** | Ground Truth | Model prediction rejected, Target Survey completed |

### 9.3 Retraining Triggers

| Trigger Type | Condition | Action |
|--------------|-----------|--------|
| **Manual** | Admin clicks "Train Model" | Immediate training job |
| **Milestone** | Every 10 new students | Automatic training job |
| **Scheduled** | Weekly (configurable) | Batch training job |

---

## 10. Advisor Portal Technical Flow

### 10.1 Student Search and Profile View

```mermaid
sequenceDiagram
    participant Advisor
    participant Frontend
    participant Backend
    participant DB

    Advisor->>Frontend: Search "john doe"
    Frontend->>Backend: GET /advisor/students?q=john+doe
    Backend->>DB: Query users + profiles
    DB-->>Backend: Matching students
    Backend-->>Frontend: [{id, name, email, ...}]
    Frontend-->>Advisor: Display search results

    Advisor->>Frontend: Click student row
    Frontend->>Backend: GET /advisor/student/{id}/profile
    Backend->>DB: Get profile, categories, questions, answers
    DB-->>Backend: Complete profile data
    Backend-->>Frontend: Structured profile with tabs
    Frontend-->>Advisor: Display tabbed profile view
```

**Figure 18.** Advisor student search and profile retrieval flow.

### 10.2 Act-As Capability

```mermaid
sequenceDiagram
    participant Advisor
    participant Frontend
    participant Backend
    participant DB

    Advisor->>Frontend: Click "Complete Survey for Student"
    Frontend->>Frontend: Enter Act-As mode
    Frontend->>Backend: GET /advisor/student/{id}/surveys/{quizId}
    Backend-->>Frontend: Survey questions + existing answers

    Advisor->>Frontend: Fill in responses
    Frontend->>Backend: POST /advisor/student/{id}/surveys/{quizId}/answers
    Note over Backend: Mark responses with<br/>modifiedBy: "advisor"
    Backend->>DB: Save answers with advisor attribution
    Backend-->>Frontend: Success

    Frontend-->>Advisor: "Survey completed on behalf of student"
```

**Figure 19.** Advisor Act-As survey completion flow.

### 10.3 Copy and Edit Workflow

```mermaid
flowchart LR
    Original["Original Attempt<br/>#1 (Completed)"]
    View["Advisor Views<br/>Responses"]
    Edit["Click 'Copy & Edit'"]
    Modify["Modify Specific<br/>Answers"]
    Save["Save as New<br/>Attempt #2"]

    Original --> View --> Edit --> Modify --> Save

    Note1["Original preserved<br/>for audit trail"]
    Note2["New attempt linked<br/>to original"]

    Original -.-> Note1
    Save -.-> Note2

    style Original fill:#e0e0e0
    style Save fill:#c8e6c9
```

**Figure 20.** Copy and edit workflow for iterative data refinement.

---

## 11. Model Training Pipeline

### 11.1 KNN Training (N < 100)

```mermaid
flowchart TB
    Trigger["Training Triggered"]
    Gather["Gather all labeled samples<br/>for this survey"]
    Store["Store samples in DB<br/>(no model file needed)"]
    Config["Set hyperparameters:<br/>k = min(max(3, √N), 10)<br/>distance = euclidean<br/>weights = distance"]
    Validate["5-fold cross-validation"]
    Check{"Validation<br/>passed?"}
    Meta["Save metadata:<br/>modelId, sampleCount, k, metrics"]
    Retry["Retry with<br/>different params"]

    Trigger --> Gather --> Store --> Config --> Validate --> Check
    Check -->|Yes| Meta
    Check -->|No| Retry --> Config

    style Meta fill:#c8e6c9
```

**Figure 21.** KNN training pipeline—samples stored, not model file.

### 11.2 Neural Network Training (N ≥ 100)

```mermaid
flowchart TB
    Trigger["Training Triggered<br/>(N ≥ 100)"]

    subgraph DataPrep["Data Preparation"]
        Gather["Gather 100 real samples"]
        Split["Split 80/20"]
        Train80["80 for training"]
        Val20["20 for validation"]
    end

    subgraph GANPhase["GAN Phase"]
        TrainGAN["Train GAN on 80 real"]
        Generate["Generate 400 synthetic"]
        ValidateGAN["Validate synthetic quality<br/>(distribution similarity)"]
        GANCheck{"Quality<br/>OK?"}
        StoreSynth["Store synthetic samples"]
        RetryGAN["Retry GAN training"]
    end

    subgraph NNPhase["Neural Network Phase"]
        Combine["Combine: 80 real + 400 synth"]
        TrainNN["Train Neural Network"]
        ValidateNN["Validate on 20 REAL only"]
        Compare{"Better than<br/>current model?"}
        Deploy["Deploy new model"]
        Keep["Keep current model<br/>Log attempt"]
    end

    Trigger --> DataPrep
    Split --> Train80 --> TrainGAN
    Split --> Val20
    TrainGAN --> Generate --> ValidateGAN --> GANCheck
    GANCheck -->|Yes| StoreSynth --> Combine
    GANCheck -->|No| RetryGAN --> TrainGAN
    Combine --> TrainNN --> ValidateNN --> Compare
    Compare -->|Yes| Deploy
    Compare -->|No| Keep

    style Val20 fill:#fff59d
    style ValidateNN fill:#fff59d
    style Deploy fill:#c8e6c9
```

**Figure 22.** Complete neural network training pipeline with GAN augmentation.

### 11.3 Model Versioning

| Field | Description |
|-------|-------------|
| **modelId** | Unique identifier for this training run |
| **quizId** | Which factor survey this model serves |
| **modelType** | `"knn"` or `"neural"` |
| **sampleCount** | Number of real samples used |
| **syntheticCount** | Number of synthetic samples (NN only) |
| **metrics** | Validation performance (MAE, R², etc.) |
| **isActive** | Currently deployed for predictions |
| **createdAt** | Training timestamp |

---

## 12. Integration Points

### 12.1 Backend ↔ Model Server Communication

```mermaid
sequenceDiagram
    participant Backend
    participant ModelServer

    Note over Backend,ModelServer: Prediction Request
    Backend->>ModelServer: POST /predict<br/>{quizId, features: {...}}
    ModelServer-->>Backend: {prediction: 74.2, neighbors: [...]}

    Note over Backend,ModelServer: Training Request
    Backend->>ModelServer: POST /train<br/>{quizId}
    ModelServer-->>Backend: {jobId: "abc123", status: "queued"}

    Note over Backend,ModelServer: Training Status Check
    Backend->>ModelServer: GET /train/status/abc123
    ModelServer-->>Backend: {status: "completed", metrics: {...}}
```

**Figure 23.** Backend to Model Server API communication patterns.

### 12.2 Future Integration: OpenAI API

The architecture supports future integration with language models for personalized guidance generation.

```mermaid
flowchart LR
    Prediction["Prediction: 74%"]
    Factors["Key Factors:<br/>- Low financial support<br/>- High academic confidence"]

    Prompt["Generate Prompt"]
    OpenAI["OpenAI API"]
    Response["Personalized<br/>Guidance Text"]

    Display["Display to<br/>Student/Advisor"]

    Prediction --> Prompt
    Factors --> Prompt
    Prompt --> OpenAI --> Response --> Display

    style OpenAI fill:#e0e0e0,stroke-dasharray: 5 5
    style Response fill:#e0e0e0,stroke-dasharray: 5 5
```

**Figure 24.** Planned OpenAI integration for natural language guidance (future work).

---

## 13. Security Architecture

### 13.1 Authentication & Authorization

| Layer | Mechanism |
|-------|-----------|
| **Transport** | HTTPS/TLS encryption |
| **Authentication** | JWT with access/refresh tokens |
| **Authorization** | Role-based middleware (Student, Advisor, Admin) |
| **Session** | Stateless (token-based) |

### 13.2 Data Protection

| Data Type | Protection |
|-----------|------------|
| **Passwords** | bcrypt hashing |
| **Tokens** | Short-lived access (15 min), longer refresh (7 days) |
| **Student Data** | Role-based access control |
| **Model Data** | Server-side storage only |

---

## 14. Scalability Considerations

### 14.1 Current Architecture

| Component | Scaling Strategy |
|-----------|-----------------|
| **Frontend** | Static assets via CDN (future) |
| **Backend** | Horizontal scaling via container replicas |
| **Database** | MongoDB managed service with auto-scaling |
| **Model Server** | Separate prediction/training to prevent blocking |

### 14.2 Training Queue

Long-running training jobs are managed through a queue system:

1. **Request**: Backend submits training job
2. **Queue**: Job added to training queue
3. **Process**: Training server processes sequentially
4. **Status**: Backend polls for completion
5. **Deploy**: New model deployed if validation passes

This prevents training jobs from blocking prediction requests.

---

## 15. Summary

The ACOSUS architecture is designed around three core principles:

1. **Progressive Capability**: The system delivers value from day one and automatically improves as data accumulates, transitioning from heuristics → KNN → Neural Networks without manual intervention.

2. **Dual Purpose**: Every component serves both the ML prediction goal and the advisor data centralization goal. Factor Surveys are simultaneously feature vectors and structured data collection instruments.

3. **Separation of Concerns**: Clear boundaries between UI, business logic, data storage, and ML enable independent scaling, testing, and evolution of each layer.

The technical architecture supports the research innovations described in the methodology paper while providing a production-ready platform for transfer student advising.
