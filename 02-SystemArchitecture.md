# System Architecture

## Slide 7: ACOSUS System Architecture Overview (3 minutes)

### Three-Component Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ACOSUS SYSTEM                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                  FRONTEND (React + TypeScript)               │  │
│  │                                                              │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐   │  │
│  │  │   Student    │  │    Admin     │  │    Advisor     │   │  │
│  │  │   Portal     │  │    Portal    │  │   Dashboard    │   │  │
│  │  └──────────────┘  └──────────────┘  └────────────────┘   │  │
│  │                                                              │  │
│  │  • Survey UI • Profile Mgmt • Prediction Display            │  │
│  │  • Quiz Creation • Model Config • Analytics Charts          │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              ▲                                      │
│                              │ HTTPS (REST API)                     │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              BACKEND (Node.js + Express + MongoDB)          │  │
│  │                                                              │  │
│  │  • User Authentication (JWT)                                │  │
│  │  • Survey Management (Target + Factor)                      │  │
│  │  • Student Profile CRUD                                     │  │
│  │  • Answer/Attempt Tracking                                  │  │
│  │  • Success Rate Calculation (dynamicSuccessRateGen.js)      │  │
│  │  • Training Request Builder                                 │  │
│  │  • Feedback Collection & Correlation Validation             │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              ▲                                      │
│                              │ HTTP (Internal Network)              │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │          MODEL SERVER (Python + Flask + TensorFlow)         │  │
│  │                                                              │  │
│  │  • Data Normalizer (0-10 scale conversion)                  │  │
│  │  • KNN Model (scikit-learn)                                 │  │
│  │  • GAN Model (TensorFlow/Keras)                             │  │
│  │  • Neural Network (TensorFlow/Keras)                        │  │
│  │  • Model Versioning System                                  │  │
│  │  • Training Queue Manager                                   │  │
│  │  • Correlation Validator (Pearson r, KS test)               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │   MongoDB 7.0    │
                          │   Database       │
                          └──────────────────┘
```

---

### System Purpose for Advisors

**Before ACOSUS**: Scattered Data Gathering
- **Problem**: Advisors must check multiple disconnected systems
  - SIS (Student Information System) for GPA and course history
  - Financial aid portal for scholarships and loans
  - LMS (Learning Management System) for engagement metrics
  - Manual notes and email conversations
- **Impact**: 40-60% of advising time spent gathering information
- **Result**: Incomplete picture, generic advising, missed opportunities

**With ACOSUS**: Centralized Platform
- **Solution**: Single dashboard with complete transfer student profile
  - Academic: GPA, courses, enrollment status, previous institution
  - Financial: Scholarships, work hours, family support
  - Personal: Commute distance, confidence levels, career goals
  - Predictive: ML-generated success prediction + similar students
- **Impact**: 70% reduction in data gathering time
- **Result**: Personalized, data-driven advising for transfer students

---

### Advisor Workflow with ACOSUS

**Step 1: Admin Creates Customizable Surveys**
- Advisors log into Admin Portal
- Create Target Survey (success rate questions)
- Create Factor Survey (background, financial, academic questions)
- **Key Feature**: System supports dynamic addition of transfer-specific factors
  - Example transfer-specific questions:
    - "How many credits did you lose during transfer?"
    - "Do you feel connected to the university community?"
    - "How would you rate your transition experience so far?"

**Step 2: Transfer Students Complete Surveys**
- Students receive email invitation
- Complete Factor Survey first (~4 minutes)
- System makes prediction (if ≥10 students enrolled)
- If prediction rated ≥4 stars: Skip Target Survey
- If prediction rated <4 stars: Complete Target Survey

**Step 3: Advisor Reviews Complete Profile**
```
Before Meeting with Transfer Student:
  1. Open ACOSUS dashboard → 1 minute
  2. View student profile:
     - Transfer shock indicators (GPA change, credit loss)
     - Financial stress levels (work hours, family support)
     - Social integration (campus proximity, support system)
     - Academic confidence (survey responses)
     - ML Prediction: 74% success rate
     - Similar transfer students: #3, #7, #12
  3. Prepare personalized guidance → 3 minutes

Total prep time: 4 minutes (vs 23 minutes before ACOSUS)
```

**Step 4: Personalized Advising During Meeting**
- Advisor uses ACOSUS data to provide targeted guidance
- If prediction is low (<40%): Intensive intervention
  - Recommend reduced course load
  - Connect to financial aid resources
  - Schedule weekly check-ins
  - Refer to tutoring and counseling
- If prediction is moderate (40-70%): Standard support
  - Study skills workshops
  - Regular advisor meetings
  - Time management resources
- If prediction is high (>70%): Enrichment
  - Advanced coursework recommendations
  - Peer mentorship opportunities
  - Leadership development programs

---

### Advisor Dashboard Features

**Current Implementation** (see Admin Portal at acosus.neiu.edu):
- ✅ Survey creation and management
- ✅ Student profile viewing
- ✅ ML model configuration
- ✅ Training trigger management
- ✅ Analytics dashboard (success rate distributions, survey completion rates)

**Future Enhancement** (Post-Defense):
- ⏳ Advisor-specific dashboards showing their advisee cohort
- ⏳ Early alert notifications for at-risk transfer students
- ⏳ Intervention tracking (record what guidance was provided)
- ⏳ Longitudinal outcome tracking (compare predictions vs actual outcomes)

---

### Future Vision: Short-term → Long-term

**Short-term** (Current - Spring 2026):
- **Primary Use**: Advisor tool for data centralization
- **Value**: Saves advisor time, provides complete transfer student picture
- **ML Role**: Not yet active (0/10 students)

**Mid-term** (Fall 2026 - Spring 2027):
- **Primary Use**: ML predictions inform advising decisions
- **Value**: Data-driven interventions, targeted support allocation
- **ML Role**: Active predictions (10-100 transfer students, KNN model)

**Long-term** (Fall 2027+):
- **Primary Use**: Automated student recommendations + advisor tool
- **Value**: Proactive outreach, predictive analytics, institutional insights
- **ML Role**: Mature predictions (100+ transfer students, Neural Network)

---

### Component 1: Target Survey System (Ground Truth Collection)

**Purpose**: Collect actual success rates from transfer students

**Two Survey Types**:

#### Type 1: Single-Question Target Survey
```
┌─────────────────────────────────────────────────────────┐
│  Success Rate Self-Assessment                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  On a scale of 0-100%, what is your self-assessed      │
│  likelihood of excelling in your academic and career    │
│  journey?                                               │
│                                                         │
│  0% ────────────●────────────── 100%                    │
│                75%                                      │
│                                                         │
│  [Submit]                                               │
└─────────────────────────────────────────────────────────┘

Result: Direct success rate = 75%
```

**When Used**:
- First 10 students (bootstrap phase)
- Students 11+ who rate predictions <4 stars (correction needed)

---

#### Type 2: Multi-Question Target Survey
```
┌─────────────────────────────────────────────────────────┐
│  Academic Success Assessment (Question 1 of 5)          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  How confident are you in your academic preparation?    │
│  Priority: ⭐⭐⭐⭐⭐⭐⭐⭐⭐ (9/10)                              │
│                                                         │
│  ○ Not confident at all      (weightage: 1)            │
│  ○ Somewhat confident         (weightage: 4)            │
│  ● Very confident             (weightage: 8)            │
│  ○ Extremely confident        (weightage: 10)           │
│                                                         │
│  [Previous]  [Next]                                     │
└─────────────────────────────────────────────────────────┘

After all questions:
  → Backend calculates using PWRS formula: 73%
  → Show to student: "We calculated 73%, do you agree?"
  → Student provides presumed rate: 75%
  → Correlation validation: |73-75| = 2 (excellent)
  → Store both calculated (73%) and presumed (75%) for validation
```

**When Used**:
- First 10 students (if admin chooses multi-question approach)
- Students 11+ who rate predictions <4 stars AND quiz is multi-question type

**PWRS Formula** (detailed in next section):
```
Step 1: Normalize each answer (0-1)
Step 2: Apply priority weighting
Step 3: Calculate base score
Step 4: Apply calibration curve (logistic/linear/sigmoid/bounded)
→ Final Success Rate (0-100%)
```

---

### Component 2: Factor Survey System (Feature Collection)

**Purpose**: Collect predictive features WITHOUT asking success rate

**Key Principle**: Factor surveys predict success; they don't ask about it directly.

**Example Factor Survey Questions**:

```
┌─────────────────────────────────────────────────────────┐
│  Academic Background Survey (Question 1 of 7)           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  What is your high school GPA?                          │
│  Priority: ⭐⭐⭐⭐⭐⭐⭐⭐⭐ (9/10)                              │
│                                                         │
│  ○ Below 2.0                  (weightage: 2)            │
│  ○ Between 2.0 and 3.0        (weightage: 4)            │
│  ● Between 3.0 and 3.5        (weightage: 8)            │
│  ○ More than 3.5              (weightage: 10)           │
│                                                         │
│  [Previous]  [Next]                                     │
└─────────────────────────────────────────────────────────┘
```

**Question Categories**:

1. **Academic Performance** (Ordinal)
   - High school GPA
   - SAT/ACT scores
   - Transfer credits
   - Previous coursework

2. **Demographics** (Categorical)
   - Age group
   - Gender
   - Ethnicity
   - First-generation status

3. **Socioeconomic** (Categorical & Ordinal)
   - Family financial support
   - Work hours per week
   - Scholarship status

4. **Temporal** (Date → Duration)
   - Program start date
   - Expected graduation date
   - Calculated duration (ideal: 3.5-4.5 years)

**Data Normalization** (all converted to 0-10 scale):
```typescript
// Example normalized output for Model Server
{
  "gpa": 8.0,           // "Between 3.0 and 3.5" → 8/10
  "sat": 7.08,          // 1250/1600 → normalized
  "family_support": 10.0, // "Yes" → 10/10
  "duration": 10.0      // 3.75 years → ideal range
}
```

---

### Component 3: Model Server (Progressive ML Pipeline)

**Purpose**: Train models, make predictions, track performance

**Sub-Components**:

#### 3.1 Data Normalizer
**Function**: Convert heterogeneous data to 0-10 scale

```python
# Input: Raw survey answers (mixed types)
raw_answers = {
    "gpa": "More than 3.5",          # String (categorical)
    "sat": 1250,                     # Integer (numeric)
    "family_support": "Yes",         # String (categorical)
    "start_date": "08/2021",         # Date string
    "end_date": "05/2025"            # Date string
}

# Output: Normalized features (all 0-10)
normalized_features = {
    "gpa": 10.0,        # Max weightage option
    "sat": 7.08,        # (1250-400)/(1600-400) * 10
    "family_support": 10.0,  # "Yes" → max weightage
    "duration": 10.0    # 3.75 years → ideal range
}
```

**Normalization Strategies**:

| Question Type | Input Example | Normalization Method | Output |
|---------------|---------------|----------------------|--------|
| **Single Option** (Ordinal) | "More than 3.5" | Use option weightage directly | 10.0 |
| **Multiple Options** (Checkbox) | ["Internship", "Research"] | Sum selected / Sum all × 10 | 6.32 |
| **Numeric** (Continuous) | 1250 (SAT score) | (value - min) / (max - min) × 10 | 7.08 |
| **Date Range** (Duration) | "08/2021" to "05/2025" | Duration scoring curve | 10.0 |

---

#### 3.2 Model Selector
**Function**: Choose KNN or NN based on student count

```python
def select_active_model(student_count):
    """
    Automatic model selection based on enrollment
    """
    if student_count < 10:
        return None  # Collect data only, no predictions
    elif student_count < 100:
        return "knn"  # K-Nearest Neighbors
    else:
        return "neural"  # Neural Network (GAN-augmented)
```

**Model Progression**:
```
Students 1-9:   No model → Data collection phase
Student 10:     Train KNN → First predictions
Students 11-99: Use KNN → Feedback loop active
Student 100:    Train GAN + NN → Best accuracy
Students 101+:  Use NN → Continuous improvement
```

---

#### 3.3 Training Queue Manager
**Function**: Manage asynchronous model training

**Training Triggers**:
```typescript
// Backend configuration (admin-adjustable)
trainingTriggers: {
  initialKnnThreshold: 10,      // Train first KNN at 10 students
  knnRetrainInterval: 10,       // Retrain KNN every 10 new students
  ganTrainThreshold: 100,       // Train GAN at 100 students
  neuralRetrainInterval: 10,    // Retrain NN every 10 new students
  ganRetrainInterval: 50,       // Retrain GAN every 50 new students
  feedbackRatingThreshold: 3.5, // Emergency retrain if avg rating < 3.5
  enableAutomaticTraining: true // Auto-trigger or manual only
}
```

**Training Workflow**:
```
Student #10 enrolls and completes surveys
  ↓
Backend checks: student_count == 10?
  ↓ Yes
Backend sends training request to Model Server
  ↓
POST /api/v1/train
  {
    "modelName": "model_quiz_ABC123",
    "trainingStage": "knn",
    "students": [...10 student records...],
    "modelConfig": {...KNN hyperparameters...}
  }
  ↓
Model Server: Async job queued
  ↓
Model Server: Train KNN (5-fold cross-validation)
  ↓
Model Server: Save model version (v1_knn_20251118_093045)
  ↓
Model Server: Return training metrics
  {
    "mae": 14.2,
    "r2": 0.42,
    "cv_folds": 5,
    "modelReady": true
  }
  ↓
Backend: Update modelMetaData collection
  ↓
Backend: Set model as active
  ↓
Student #11: Receives prediction! ✅
```

---

#### 3.4 Prediction Engine
**Function**: Serve real-time predictions

```python
# Prediction Request (from Backend)
POST /api/v1/predict
{
  "modelName": "model_quiz_ABC123",
  "factorAnswers": {
    "gpa": "Between 3.0 and 3.5",
    "sat": 1100,
    "family_support": "Yes",
    "start_date": "08/2025",
    "end_date": "05/2029"
  }
}

# Prediction Response (from Model Server)
{
  "status": "success",
  "prediction": {
    "success_rate": 74,       # Predicted success rate
    "confidence": 0.82,       # Model confidence (0-1)
    "model_type": "knn",      # Which model was used
    "model_version": "v1_knn_20251118_093045"
  },
  "nearestNeighbors": [       # KNN specific: interpretability
    {
      "studentId": "student_003",
      "distance": 0.12,       # Euclidean distance in feature space
      "success_rate": 82,     # Neighbor's success rate
      "similarity_factors": [
        "Similar GPA range",
        "Same family support status"
      ]
    },
    {
      "studentId": "student_007",
      "distance": 0.18,
      "success_rate": 71
    },
    {
      "studentId": "student_012",
      "distance": 0.21,
      "success_rate": 69
    }
  ],
  "predictedAt": "2025-11-18T10:00:15Z"
}
```

**Inference Performance**:
- KNN: <100ms (distance calculations)
- Neural Network: <5ms (forward pass)

---

### Data Flow: The Complete Journey

#### Scenario 1: First 10 Students (Bootstrap)

```
┌───────────────────────────────────────────────────────────────┐
│ Student #1 Enrolls                                            │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼
        ┌───────────────────┐
        │ Frontend:         │
        │ Create Profile    │
        │ (demographics)    │
        └───────┬───────────┘
                │
                ▼
        ┌───────────────────┐
        │ Frontend:         │
        │ Complete Target   │
        │ Survey            │
        │ (success rate)    │
        └───────┬───────────┘
                │
                ▼
        ┌───────────────────────────────────┐
        │ Backend:                          │
        │ - Store answer in DB              │
        │ - If multi-question:              │
        │   Calculate PWRS formula          │
        │   Request presumed rate           │
        │ - Store label.success_rate        │
        └───────┬───────────────────────────┘
                │
                ▼
        ┌───────────────────┐
        │ Frontend:         │
        │ Complete Factor   │
        │ Survey            │
        │ (features)        │
        └───────┬───────────┘
                │
                ▼
        ┌───────────────────────────────────┐
        │ Backend:                          │
        │ - Store answers in DB             │
        │ - Check: student_count == 10?     │
        │   No → Wait for more students     │
        └───────┬───────────────────────────┘
                │
                │ (After student #10)
                │
                ▼
        ┌───────────────────────────────────┐
        │ Backend:                          │
        │ - Build training request          │
        │ - POST /api/v1/train              │
        │ - Include all 10 students         │
        └───────┬───────────────────────────┘
                │
                ▼
        ┌───────────────────────────────────┐
        │ Model Server:                     │
        │ - Normalize all features (0-10)   │
        │ - Train KNN (k=3, distance-weighted) │
        │ - 5-fold cross-validation         │
        │ - Save model version              │
        │ - Return metrics (MAE, R²)        │
        └───────┬───────────────────────────┘
                │
                ▼
        ┌───────────────────────────────────┐
        │ Backend:                          │
        │ - Store modelMetaData             │
        │ - Set model as active             │
        │ - Notify admin: "Model trained!"  │
        └───────────────────────────────────┘
```

---

#### Scenario 2: Student #11+ (Feedback Loop)

```
┌───────────────────────────────────────────────────────────────┐
│ Student #11 Enrolls                                           │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼
        ┌───────────────────┐
        │ Frontend:         │
        │ Create Profile    │
        └───────┬───────────┘
                │
                ▼
        ┌───────────────────┐
        │ Frontend:         │
        │ Complete Factor   │
        │ Survey ONLY       │
        │ (NO target yet)   │
        └───────┬───────────┘
                │
                ▼
        ┌────────────────────────────────────┐
        │ Backend:                           │
        │ - Store factor answers             │
        │ - Check: model trained?            │
        │   Yes → Request prediction         │
        │ - POST /api/v1/predict             │
        └───────┬────────────────────────────┘
                │
                ▼
        ┌────────────────────────────────────┐
        │ Model Server:                      │
        │ - Normalize factor answers         │
        │ - Load active KNN model            │
        │ - Find 3 nearest neighbors         │
        │ - Calculate distance-weighted avg  │
        │ - Return prediction: 74%           │
        └───────┬────────────────────────────┘
                │
                ▼
        ┌────────────────────────────────────┐
        │ Frontend:                          │
        │ - Display prediction: 74%          │
        │ - Show similar students            │
        │ - Request feedback rating (1-5 ⭐)  │
        └───────┬────────────────────────────┘
                │
                ▼
        ┌─────────────────────────────────────────────┐
        │ Student Rates Prediction                    │
        ├─────────────────────────────────────────────┤
        │                                             │
        │  IF Rating ≥ 4 stars (Accurate):            │
        │    - Use prediction as label (pseudo-label) │
        │    - label.success_rate = 74                │
        │    - label.source = "pseudo_label"          │
        │    - Skip target survey ✅                   │
        │                                             │
        │  IF Rating < 4 stars (Inaccurate):          │
        │    - Request target survey                  │
        │    - Student provides actual: 52%           │
        │    - label.success_rate = 52                │
        │    - label.source = "feedback_corrected"    │
        │    - Model learns from error ✅              │
        │                                             │
        └─────────────────┬───────────────────────────┘
                          │
                          ▼
                ┌─────────────────────────┐
                │ Backend:                │
                │ - Store training label  │
                │ - Track feedback data   │
                │ - Check retrain trigger │
                │   (every 10 students)   │
                └─────────────────────────┘
```

---

### Technology Stack Details

#### Frontend (React + TypeScript)
```typescript
// Tech Stack
- Framework: React 18.x + Vite
- Language: TypeScript 5.x
- UI Components: Radix UI + shadcn/ui
- Styling: Tailwind CSS
- State Management: React Context API + Custom Hooks
- Charts: Recharts, D3.js
- Forms: React Hook Form + Zod validation
- Routing: React Router v6

// Key Features
- Responsive design (mobile-first)
- Accessible (WCAG 2.1 AA compliant)
- Dark mode support
- Real-time updates (polling-based, future: WebSockets)
- Progressive Web App (PWA) capabilities
```

**Frontend Architecture**:
```
src/
├── components/
│   ├── admin/          # Quiz builder, model config UI
│   ├── student/        # Survey UI, prediction display
│   ├── advisor/        # Analytics dashboards
│   └── common/         # Shared UI components
├── pages/
│   ├── AdminDashboard.tsx
│   ├── StudentDashboard.tsx
│   └── SurveyPage.tsx
├── hooks/
│   ├── useAuth.ts
│   ├── usePrediction.ts
│   └── useModelMetrics.ts
├── service/
│   ├── api.ts          # API client
│   └── modelService.ts # Model Server communication
└── contexts/
    ├── AuthContext.tsx
    └── QuizContext.tsx
```

---

#### Backend (Node.js + Express)
```typescript
// Tech Stack
- Runtime: Node.js v20.x
- Framework: Express.js 4.x
- Language: TypeScript 5.x
- Database: MongoDB 7.0
- ODM: Mongoose 8.x
- Authentication: JWT + bcrypt
- API: RESTful (future: GraphQL)
- Validation: Zod schemas
- Email: Resend API
- Logging: Winston
- Cron Jobs: node-cron (automated training triggers)

// Architecture Pattern
- MVC (Model-View-Controller)
- Service layer for business logic
- Repository pattern for data access
- Middleware-based request pipeline
```

**Backend Architecture**:
```
src/
├── models/
│   ├── quiz.model.ts           # Quiz definitions (target/factor)
│   ├── question.model.ts       # Individual questions
│   ├── questionOptions.model.ts # Answer options with weightages
│   ├── answer.model.ts         # Student responses
│   ├── attempt.model.ts        # Quiz attempts
│   ├── quizAttemptTracking.model.ts # Metadata
│   ├── student.model.ts        # Student profiles
│   ├── modelMetaData.model.ts  # Trained model versions
│   └── feedbackCorrelation.model.ts # Validation metrics
├── controllers/
│   ├── v2/admin/
│   │   └── admin.quiz.controller.ts  # Create/manage quizzes
│   └── v2/student/
│       ├── student.quiz.controller.ts
│       ├── student.answer.controller.ts
│       └── student.attempt.controller.ts
├── services/
│   ├── dynamicSuccessRateGen.js  # PWRS formula implementation
│   ├── modelService.ts           # Model Server API client
│   └── trainingService.ts        # Build training requests
└── routes/
    ├── admin.routes.ts
    ├── student.routes.ts
    └── model.routes.ts
```

**Database Collections**:
```javascript
// MongoDB Collections
{
  users,                  // Authentication, roles
  studentProfiles,        // Demographics + academic data
  quizzes,                // Survey definitions (target/factor)
  questions,              // Individual question configs
  questionOptions,        // Answer choices with weightages
  answers,                // Student responses
  attempts,               // Quiz completion records
  quizAttemptTracking,    // Aggregated attempt metadata
  modelMetaData,          // Trained model versions
  feedbackCorrelation     // Validation metrics (Pearson r, etc.)
}
```

---

#### Model Server (Python + Flask)
```python
# Tech Stack
- Framework: Flask 3.x + Flask-CORS
- Language: Python 3.10+
- ML Libraries:
  - scikit-learn 1.3+ (KNN, preprocessing)
  - TensorFlow 2.x (Neural Network, GAN)
  - NumPy, Pandas (data manipulation)
  - SciPy (statistical validation)
- Job Queue: Python threading (future: Celery)
- Model Storage: Pickle (KNN), HDF5 (TensorFlow)

# Components
- Training queue manager (async job processing)
- Progress tracker (real-time status updates)
- Model versioning system (save/load models)
- Data normalizer (heterogeneous → 0-10 scale)
- PWRS calculator (success rate formula)
- Correlation validator (Pearson r, KS test)
```

**Model Server Architecture**:
```python
app/
├── models/
│   ├── knn_model.py       # K-Nearest Neighbors implementation
│   ├── gan_model.py       # Conditional GAN for augmentation
│   └── neural_model.py    # Feedforward Neural Network
├── utils/
│   ├── data_normalizer.py # Feature normalization (0-10)
│   ├── pwrs_calculator.py # Success rate calculation
│   └── validators.py      # Correlation, KS test, quality checks
├── services/
│   ├── training_service.py   # Training orchestration
│   ├── prediction_service.py # Prediction serving
│   └── versioning_service.py # Model versioning
├── routes/
│   ├── train.py           # POST /api/v1/train
│   ├── predict.py         # POST /api/v1/predict
│   └── correlation.py     # POST /api/v1/calculate_correlation
└── app.py                 # Flask app initialization
```

---

#### Infrastructure (Docker + Nginx)
```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  mongodb:
    image: mongo:7.0
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  backend:
    build: ./backend
    ports:
      - "3000:3000"
    depends_on:
      - mongodb
    environment:
      - DATABASE_URL=mongodb://mongodb:27017/acosus
      - JWT_SECRET=${JWT_SECRET}

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    depends_on:
      - backend

  model-server:
    build: ./model
    ports:
      - "5000:5000"
    volumes:
      - model_storage:/app/models

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./infra/nginx.conf:/etc/nginx/nginx.conf
      - ./infra/ssl:/etc/nginx/ssl
    depends_on:
      - backend
      - frontend
      - model-server

volumes:
  mongo_data:
  model_storage:
```

**Nginx Reverse Proxy**:
```nginx
# SSL Termination + Routing
server {
    listen 443 ssl;
    server_name acosus.neiu.edu;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # Frontend (React SPA)
    location / {
        proxy_pass http://frontend:5173;
    }

    # Backend API
    location /api/ {
        proxy_pass http://backend:3000;
    }

    # Model Server (internal only)
    location /model/ {
        proxy_pass http://model-server:5000;
        # Restrict access to backend only
        allow 172.16.0.0/12;  # Docker network
        deny all;
    }
}
```

---

### Deployment Status (as of Nov 18, 2025)

| Component | Status | Version | Uptime | Notes |
|-----------|--------|---------|--------|-------|
| **Frontend** | 🟢 Live | 0.0.1 | 99.8% | Full UI deployed |
| **Backend** | 🟢 Live | 0.0.1 | 99.9% | API + DB operational |
| **Model Server** | 🟡 Partial | 0.0.1 | 95.0% | Legacy version (seeding-based) |
| **Database** | 🟢 Live | 7.0 | 99.9% | MongoDB cluster |
| **Infrastructure** | 🟢 Live | - | 99.5% | Docker + Nginx |

**Current Limitation**:
- Model Server using **legacy implementation** (synthetic seeding for testing)
- **Migration in progress** to Target+Factor architecture
- Bootstrap phase: **0/10 students enrolled** (waiting for real data)

---

### Speaking Points Summary

**Key Talking Points**:

1. **Three-Layer Architecture**: "ACOSUS separates concerns cleanly - Frontend handles UX, Backend manages business logic and data, Model Server focuses purely on ML."

2. **Target vs Factor Surveys**: "We innovate by separating ground truth collection (target) from feature collection (factor) - this enables progressive learning."

3. **Progressive Model Server**: "The Model Server automatically selects the right algorithm based on data availability - KNN for small data, Neural Networks for large data."

4. **Production-Grade Stack**: "We use industry-standard technologies - React, Node.js, Python, MongoDB - ensuring maintainability and scalability."

5. **Real-Time Training**: "When the 10th student completes surveys, the system automatically triggers KNN training within seconds - no manual intervention."
