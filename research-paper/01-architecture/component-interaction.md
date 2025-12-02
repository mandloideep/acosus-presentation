# ACOSUS Component Interaction Architecture

## Document Purpose
This document maps the interactions between frontend, backend, and model components of the ACOSUS system, detailing API endpoints, data flows, and technology stacks for academic research paper preparation.

---

## 1. Component Diagram Description

### 1.1 System Components Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              ACOSUS SYSTEM                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                     FRONTEND (React + TypeScript)                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │ │
│  │  │   Public    │  │   Student   │  │   Advisor   │  │    Admin    │       │ │
│  │  │   Website   │  │   Portal    │  │  Dashboard  │  │    Panel    │       │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘       │ │
│  │        │                │                │                │                │ │
│  │        └────────────────┴────────────────┴────────────────┘                │ │
│  │                                    │                                       │ │
│  │                      ┌─────────────────────────┐                          │ │
│  │                      │  Service Layer (V2 API) │                          │ │
│  │                      │  • React Query Hooks    │                          │ │
│  │                      │  • Axios HTTP Client    │                          │ │
│  │                      │  • State Management     │                          │ │
│  │                      └─────────────────────────┘                          │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
│                                        │                                        │
│                                        │ REST API (JSON)                        │
│                                        │ /api/v1/* and /api/v2/*                │
│                                        ▼                                        │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                    BACKEND (Node.js + Express + MongoDB)                   │ │
│  │  ┌──────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                          ROUTING LAYER                                │ │ │
│  │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │ │ │
│  │  │  │  Public  │  │ Student  │  │ Advisor  │  │  Admin   │            │ │ │
│  │  │  │  Routes  │  │  Routes  │  │  Routes  │  │  Routes  │            │ │ │
│  │  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │ │ │
│  │  └──────────────────────────────────────────────────────────────────────┘ │ │
│  │                                     │                                      │ │
│  │  ┌──────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                       CONTROLLER LAYER                                │ │ │
│  │  │  • Quiz Controller      • Attempt Controller    • Predict Controller │ │ │
│  │  │  • User Controller      • Answer Controller     • Train Controller   │ │ │
│  │  │  • Profile Controller   • Dashboard Controller  • Prompt Controller  │ │ │
│  │  └──────────────────────────────────────────────────────────────────────┘ │ │
│  │                                     │                                      │ │
│  │  ┌──────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                         SERVICE LAYER                                 │ │ │
│  │  │  • Quiz Service         • Attempt Service       • ModelMetaData Svc  │ │ │
│  │  │  • User Service         • Answer Service        • SurveyWorkflow Svc │ │ │
│  │  │  • Question Service     • Profile Service       • Prompt Service     │ │ │
│  │  └──────────────────────────────────────────────────────────────────────┘ │ │
│  │                                     │                                      │ │
│  │  ┌──────────────────────────────────────────────────────────────────────┐ │ │
│  │  │                          MODEL LAYER                                  │ │ │
│  │  │  Quiz, Question, Category, Answer, Attempt, User, Student,           │ │ │
│  │  │  ModelMetaData, Prompt, QuizAttemptTracking, TrainingTriggerLog      │ │ │
│  │  └──────────────────────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
│                                        │                                        │
│                    ┌───────────────────┴───────────────────┐                   │
│                    │ HTTP (Internal)                        │                   │
│                    ▼                                        ▼                   │
│  ┌─────────────────────────────┐          ┌────────────────────────────────┐  │
│  │     MongoDB Atlas           │          │  MODEL SERVER (Python + Flask) │  │
│  │  ┌───────────────────────┐  │          │  ┌────────────────────────────┐│  │
│  │  │  Collections:         │  │          │  │  Endpoints:                ││  │
│  │  │  • users              │  │          │  │  /trainNeural              ││  │
│  │  │  • quizzes            │  │          │  │  /seed, /seed2             ││  │
│  │  │  • questions          │  │          │  │  /predict_neural           ││  │
│  │  │  • answers            │  │          │  │  /predict_regression       ││  │
│  │  │  • attempts           │  │          │  │  /genai                    ││  │
│  │  │  • students           │  │          │  │  /job_status/<id>          ││  │
│  │  │  • modelmetadatas     │  │          │  │  /queue_status             ││  │
│  │  │  • prompts            │  │          │  └────────────────────────────┘│  │
│  │  └───────────────────────┘  │          │  ┌────────────────────────────┐│  │
│  └─────────────────────────────┘          │  │  ML Components:            ││  │
│                                           │  │  • Neural Network (v1/v2)  ││  │
│                                           │  │  • Regression Model        ││  │
│                                           │  │  • Queue Manager           ││  │
│                                           │  │  • Success Rate Calculator ││  │
│                                           │  │  • Progress Tracker        ││  │
│                                           │  └────────────────────────────┘│  │
│                                           │  ┌────────────────────────────┐│  │
│                                           │  │  Shared Volume:            ││  │
│                                           │  │  model_storage/            ││  │
│                                           │  │  • .h5 model files         ││  │
│                                           │  │  • .pkl scaler files       ││  │
│                                           │  └────────────────────────────┘│  │
│                                           └────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 What Should Be Illustrated

A **component diagram** for ACOSUS should illustrate:

1. **Three-Tier Architecture**
   - Presentation Layer (Frontend)
   - Business Logic Layer (Backend)
   - ML/Data Layer (Model Server + Database)

2. **Frontend Components**
   - Public website pages (home, insights, team, contact)
   - Student portal (dashboard, quizzes, profile)
   - Advisor dashboard (student management, surveys)
   - Admin panel (quiz management, user management, model testing)
   - Shared components (auth, navigation, forms)

3. **Backend Components**
   - Route handlers (V1 legacy, V2 modern)
   - Controllers (request processing)
   - Services (business logic)
   - Models (data access)
   - Middleware (auth, validation, logging)

4. **Model Server Components**
   - Flask REST API endpoints
   - Neural network training modules
   - Prediction inference pipeline
   - Training job queue
   - Model file storage

5. **External Services**
   - MongoDB Atlas (database)
   - PostHog (analytics)
   - Resend (email)
   - OpenAI API (AI-generated feedback)

---

## 2. API Endpoint Categories

### 2.1 Authentication & Account Management

| Endpoint | Method | Purpose | Auth Required |
|----------|--------|---------|---------------|
| `/api/v1/public/login` | POST | User login with email/password | No |
| `/api/v1/public/logout` | POST | User logout (clear tokens) | Yes |
| `/api/v1/public/register` | POST | New user registration | No |
| `/api/v1/public/forgot-password` | POST | Initiate password reset | No |
| `/api/v1/public/verify-otp` | POST | Verify OTP for password reset | No |
| `/api/v1/account/update` | PUT | Update account information | Yes |
| `/api/v1/public/consent` | GET/POST | Get/accept consent form | No |

### 2.2 Survey/Quiz Management (Admin)

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v2/admin/quiz` | GET | List all quizzes | Admin |
| `/api/v2/admin/quiz` | POST | Create new quiz | Admin |
| `/api/v2/admin/quiz/:slug` | GET | Get quiz by slug | Admin |
| `/api/v2/admin/quiz/:slug` | PUT | Update quiz | Admin |
| `/api/v2/admin/quiz/:slug/publish` | POST | Publish quiz | Admin |
| `/api/v2/admin/quiz/:slug/category` | GET/POST | Manage categories | Admin |
| `/api/v2/admin/quiz/:slug/question` | GET/POST | Manage questions | Admin |
| `/api/v2/admin/quiz/:slug/question/:questionSlug` | PUT/DELETE | Update/delete question | Admin |

### 2.3 Survey Submission (Student)

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v2/student/quiz/target` | GET | Get available target quizzes | Student |
| `/api/v2/student/quiz/factor` | GET | Get available factor quizzes | Student |
| `/api/v2/student/quiz/:slug` | GET | Get quiz details | Student |
| `/api/v2/student/quiz/:slug/content` | GET | Get full quiz with questions | Student |
| `/api/v2/student/attempt` | POST | Start new quiz attempt | Student |
| `/api/v2/student/attempt/:attemptId` | GET | Get attempt details | Student |
| `/api/v2/student/attempt/:attemptId/complete` | POST | Complete attempt | Student |
| `/api/v2/student/answer` | POST | Submit single answer | Student |
| `/api/v2/student/answer/bulk` | POST | Submit multiple answers | Student |
| `/api/v2/student/workflow/status` | GET | Get workflow state | Student |

### 2.4 Prediction & Model Management

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v1/admin/predictions` | POST | Request prediction for student | Admin |
| `/api/v1/admin/train` | POST | Train new ML model | Admin |
| `/api/v1/admin/train/q/:slug/seed` | POST | Train with synthetic data | Admin |
| `/api/v1/admin/models/quiz/:slug` | GET | Get models for quiz | Admin |
| `/api/v1/admin/models/quiz/:quizId/model/:modelId` | POST | Set active model | Admin |
| `/api/v1/ml/job-status/:modelId` | POST | Callback for training status | Internal |

### 2.5 User Management (Admin)

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v1/admin/users` | GET | List all users | Admin |
| `/api/v1/admin/users/:userId` | GET | Get user by ID | Admin |
| `/api/v1/admin/users/:userId` | PUT | Update user | Admin |
| `/api/v1/admin/users/:userId` | DELETE | Soft delete user | Admin |
| `/api/v1/admin/users/role/:role` | GET | Get users by role | Admin |

### 2.6 Student Profile Management

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v2/student/profile` | GET | Get student profile | Student |
| `/api/v2/student/profile` | PUT | Update student profile | Student |
| `/api/v2/student/profile/completion` | GET | Check profile completion status | Student |
| `/api/v2/advisor/student/:studentId/profile` | GET | View student profile | Advisor |

### 2.7 Advisor Operations

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v2/advisor/students` | GET | List assigned students | Advisor |
| `/api/v2/advisor/student/:studentId` | GET | Get student details | Advisor |
| `/api/v2/advisor/student/:studentId/surveys` | GET | Get student's surveys | Advisor |
| `/api/v2/advisor/student/:studentId/attempt` | POST | Create attempt for student | Advisor |
| `/api/v2/advisor/student/:studentId/answer` | POST | Submit answer for student | Advisor |

### 2.8 Dashboard & Analytics

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v1/admin/dashboard/summary` | GET | Overall system summary | Admin |
| `/api/v1/admin/dashboard/users/counts` | GET | User counts by role | Admin |
| `/api/v1/admin/dashboard/quizzes/completion` | GET | Quiz completion metrics | Admin |
| `/api/v1/admin/dashboard/students/engagement` | GET | Student engagement stats | Admin |
| `/api/v1/admin/dashboard/models/metrics` | GET | Model performance metrics | Admin |

### 2.9 AI Prompt Management

| Endpoint | Method | Purpose | Role |
|----------|--------|---------|------|
| `/api/v1/admin/prompt` | POST | Create new prompt | Admin |
| `/api/v1/admin/prompt/:quizSlug` | GET | Get prompts for quiz | Admin |
| `/api/v1/admin/prompt/id/:promptId` | GET | Get prompt by ID | Admin |
| `/api/v1/admin/prompt/id/:promptId/update` | PUT | Update prompt | Admin |
| `/api/v1/admin/prompt/id/:promptId/current` | POST | Set as current prompt | Admin |

### 2.10 Model Server Endpoints (Internal)

| Endpoint | Method | Purpose | Called By |
|----------|--------|---------|-----------|
| `/trainNeural` | POST | Train neural network | Backend |
| `/seed` | POST | Generate synthetic data (sync) | Backend |
| `/seed2` | POST | Generate synthetic data (async queue) | Backend |
| `/predict_neural` | POST | Get prediction from NN | Backend |
| `/predict_regression` | POST | Get prediction from regression | Backend |
| `/genai` | POST | Generate AI feedback | Backend |
| `/job_status/<model_id>` | GET | Check training job status | Backend |
| `/queue_status` | GET | Get queue metrics | Backend |
| `/cancel_job/<model_id>` | POST | Cancel training job | Backend |

---

## 3. Data Flow for Key User Journeys

### 3.1 New Student Onboarding

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         NEW STUDENT ONBOARDING FLOW                              │
└─────────────────────────────────────────────────────────────────────────────────┘

User Action                    Frontend                         Backend                          Database
─────────────────────────────────────────────────────────────────────────────────────────────────────────

1. Visit Registration
   │
   └──► [/register page]
        │
        └──► Fill form: email, password, name
             │
             └──────────────────────────────► POST /api/v1/public/register
                                              │
                                              ├──► Validate with Zod schema
                                              │
                                              ├──► Check email uniqueness ──────────► users.findOne({email})
                                              │
                                              ├──► Hash password (bcrypt)
                                              │
                                              └──► Create user record ─────────────► users.insertOne({
                                                   │                                    email, password,
                                                   │                                    role: "student"
                                                   │                                  })
                                                   │
2. Email Verification           ◄─────────────────┘
   │
   └──► [/otp page]
        │
        └──► Enter OTP code
             │
             └──────────────────────────────► POST /api/v1/public/verify-otp
                                              │
                                              └──► Mark email verified ────────────► users.updateOne({
                                                                                       isEmailVerified: true
                                                                                     })

3. Login
   │
   └──► [/login page]
        │
        └──► Enter credentials
             │
             └──────────────────────────────► POST /api/v1/public/login
                                              │
                                              ├──► Verify password ────────────────► users.findOne({email})
                                              │
                                              ├──► Generate JWT tokens
                                              │
                                              ├──► Set cookies:
                                              │    • accessToken (short-lived)
                                              │    • refreshToken (long-lived)
                                              │
                                              └──► Return user data ─────────────► Update login history

4. Consent Agreement            ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Consent modal]
        │
        └──► Read & accept consent
             │
             └──────────────────────────────► POST /api/v1/public/consent
                                              │
                                              └──► Record consent ─────────────────► users.updateOne({
                                                                                       consent: {
                                                                                         accepted: true,
                                                                                         timestamp: Date
                                                                                       }
                                                                                     })

5. Complete Profile             ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [/app/student/profile]
        │
        └──► Fill profile sections:
             • Account (name, email)
             • Academic (GPA, major, credits)
             • Personal (demographics)
             │
             └──────────────────────────────► PUT /api/v2/student/profile
                                              │
                                              ├──► Validate profile data
                                              │
                                              └──► Create/update student ─────────► students.upsert({
                                                                                     userId, gpa, major,
                                                                                     demographics, etc.
                                                                                   })

6. View Dashboard               ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [/app/student/dashboard]
        │
        └──► WorkflowContext fetches ───────► GET /api/v2/student/workflow/status
                                              │
                                              ├──► Get system stage (earlyAdoption/production)
                                              │
                                              ├──► Get available quizzes ─────────► quizzes.find({
                                              │                                      published: true,
                                              │                                      type: "target"/"factor"
                                              │                                    })
                                              │
                                              └──► Return workflow status:
                                                   • isEarlyAdoption: boolean
                                                   • targetQuizzes: [...]
                                                   • factorQuizzes: [...]
                                                   • profileComplete: boolean
```

### 3.2 Target Survey Completion

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        TARGET SURVEY COMPLETION FLOW                             │
│              (Collects ground truth success rate - first 10 students)            │
└─────────────────────────────────────────────────────────────────────────────────┘

User Action                    Frontend                         Backend                          Database
─────────────────────────────────────────────────────────────────────────────────────────────────────────

1. Select Target Survey
   │
   └──► [Dashboard] Click "Start Survey"
        │
        └──► Navigate to quiz ──────────────► GET /api/v2/student/quiz/:slug/content
                                              │
                                              └──► Return quiz structure ─────────► quizzes.findOne({slug})
                                                   │                               questions.find({quizId})
                                                   │                               categories.find({quizId})
                                                   │
                                                   Returns:
                                                   {
                                                     quiz: {...},
                                                     categories: [...],
                                                     questions: [...with options]
                                                   }

2. Start Attempt                ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Quiz page loads]
        │
        └──► Create attempt ────────────────► POST /api/v2/student/attempt
                                              │                               Body: {quizId, attemptType: "target"}
                                              │
                                              ├──► Validate quiz availability
                                              │
                                              └──► Create attempt record ─────────► attempts.insertOne({
                                                                                     studentId, quizId,
                                                                                     status: "started",
                                                                                     attemptType: "target",
                                                                                     startedAt: Date
                                                                                   })

3. Answer Questions             ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [For each question]
        │
        ├──► Select/enter answer
        │    │
        │    └──► Auto-save (debounced) ────► POST /api/v2/student/answer
        │                                     │                         Body: {attemptId, questionId, value}
        │                                     │
        │                                     └──► Save answer ───────────────────► answers.upsert({
        │                                                                            attemptId, questionId,
        │                                                                            value, weightage,
        │                                                                            savedAt: Date
        │                                                                          })
        │
        └──► [Also saved to localStorage as backup]

4. Provide Success Rate         ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Target Survey - single question type]
        │
        └──► Enter self-assessed success rate (0-100%)
             │
             └──► Auto-save ────────────────► POST /api/v2/student/answer
                                              │
                                              └──► Save as success rate answer

   OR

   └──► [Target Survey - multi-question PWRS type]
        │
        └──► Answer 5-10 questions with priority weights
             │
             └──► Backend calculates success rate using PWRS formula

5. Submit Survey                ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► Click "Submit"
        │
        └──► Complete attempt ──────────────► POST /api/v2/student/attempt/:attemptId/complete
                                              │
                                              ├──► Validate all required questions answered
                                              │
                                              ├──► For multi-question: Calculate PWRS success rate
                                              │    │
                                              │    └──► normalizedScore = Σ(answer.weight * question.priority)
                                              │                          / Σ(maxWeight * question.priority)
                                              │         successRate = sigmoid(normalizedScore)
                                              │
                                              ├──► Update attempt ────────────────► attempts.updateOne({
                                              │                                      status: "completed",
                                              │                                      completedAt: Date,
                                              │                                      targetSurveyData: {
                                              │                                        successRate: number,
                                              │                                        rateType: "self_reported" |
                                              │                                                  "calculated"
                                              │                                      }
                                              │                                    })
                                              │
                                              └──► Update tracking ───────────────► quizAttemptTracking.updateOne({
                                                                                     completedCount: +1
                                                                                   })

6. Confirmation                 ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Thank you page]
        │
        └──► Display completion message
             │
             └──► Redirect to dashboard after 3s
```

### 3.3 Factor Survey Completion

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         FACTOR SURVEY COMPLETION FLOW                            │
│                    (Collects features for prediction model)                      │
└─────────────────────────────────────────────────────────────────────────────────┘

User Action                    Frontend                         Backend                          Database
─────────────────────────────────────────────────────────────────────────────────────────────────────────

1. Select Factor Survey
   │
   └──► [Dashboard] Click factor survey card
        │
        └──► Fetch quiz content ────────────► GET /api/v2/student/quiz/:slug/content
                                              │
                                              └──► Return quiz with categories ───► quizzes.aggregate([
                                                                                     {$match: {slug}},
                                                                                     {$lookup: questions},
                                                                                     {$lookup: categories}
                                                                                   ])

2. Start Factor Attempt         ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► Quiz component mounts
        │
        └──► Create factor attempt ─────────► POST /api/v2/student/attempt
                                              │                    Body: {quizId, attemptType: "factor"}
                                              │
                                              └──► Create attempt ────────────────► attempts.insertOne({
                                                                                     studentId, quizId,
                                                                                     attemptType: "factor",
                                                                                     status: "started"
                                                                                   })

3. Answer by Category           ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Category-based navigation]
        │
        ├──► Academic Background category
        │    ├──► GPA question (numeric)
        │    ├──► Transfer credits (numeric)
        │    └──► Previous institution (dropdown)
        │
        ├──► Demographics category
        │    ├──► Age group (radio)
        │    ├──► First-generation status (boolean)
        │    └──► Ethnicity (dropdown)
        │
        ├──► Socioeconomic category
        │    ├──► Work hours per week (numeric)
        │    ├──► Financial support (likert)
        │    └──► Housing situation (dropdown)
        │
        └──► For each answer ───────────────► POST /api/v2/student/answer
                                              │
                                              ├──► Validate against question.restrictions
                                              │    (min/max values, regex patterns)
                                              │
                                              └──► Store with question metadata ──► answers.upsert({
                                                                                     attemptId,
                                                                                     questionId,
                                                                                     value: mixed,
                                                                                     questionType,
                                                                                     questionDataType
                                                                                   })

4. Submit Factor Survey         ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► Click "Complete Survey"
        │
        └──► Finalize attempt ──────────────► POST /api/v2/student/attempt/:attemptId/complete
                                              │
                                              ├──► Validate completeness
                                              │
                                              ├──► Mark attempt complete ─────────► attempts.updateOne({
                                              │                                      status: "completed",
                                              │                                      factorSurveyData: {
                                              │                                        predictionShown: false,
                                              │                                        feedbackRating: null
                                              │                                      }
                                              │                                    })
                                              │
                                              └──► Update workflow tracking ──────► Check if student
                                                                                    qualifies for prediction

5. Data Ready for Model         ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [System marks data as available]
        │
        └──► Student data now in training pool for next model iteration
```

### 3.4 Receiving Prediction

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          RECEIVING PREDICTION FLOW                               │
│             (Student receives predicted success rate from ML model)              │
└─────────────────────────────────────────────────────────────────────────────────┘

User Action                    Frontend                         Backend                          Model Server
─────────────────────────────────────────────────────────────────────────────────────────────────────────────

1. Request Prediction (Admin initiates OR automatic after factor survey)
   │
   └──► [Admin panel OR automatic trigger]
        │
        └──► Request prediction ────────────► POST /api/v1/admin/predictions
                                              │              Body: {studentId, quizSlug}
                                              │
                                              ├──► Fetch current model for quiz ──► modelMetaDatas.findOne({
                                              │                                      quizId, isCurrent: true,
                                              │                                      status: "completed"
                                              │                                    })
                                              │
                                              ├──► Fetch student answers ─────────► answers.aggregate([
                                              │                                      {$match: {studentId, quizId}},
                                              │                                      {$group by question}
                                              │                                    ])
                                              │
                                              ├──► Fetch student profile ─────────► students.findOne({userId})
                                              │
                                              ├──► Assemble prompt (if AI feedback):
                                              │    │
                                              │    ├──► Fetch current prompt ─────► prompts.findOne({
                                              │    │                                 quizId, isCurrent: true
                                              │    │                               })
                                              │    │
                                              │    └──► Replace template variables:
                                              │         {studentName}, {gpa}, {major},
                                              │         {surveyAnswers}, {predictedRate}
                                              │
                                              └──► Call ML service ───────────────────────────────────────────►

2. Model Inference                                                                  ◄─────────────────────────
   │                                                                                │
   │                                                                                ├──► Load model file
   │                                                                                │    models/{name}/{name}.h5
   │                                                                                │
   │                                                                                ├──► Load scaler
   │                                                                                │    models/{name}/{name}.pkl
   │                                                                                │
   │                                                                                ├──► Preprocess answers:
   │                                                                                │    │
   │                                                                                │    ├──► Convert to numeric
   │                                                                                │    │    (LabelEncoder for categorical)
   │                                                                                │    │
   │                                                                                │    ├──► Fill missing with 0
   │                                                                                │    │
   │                                                                                │    └──► Apply MinMaxScaler
   │                                                                                │
   │                                                                                ├──► Run neural network inference
   │                                                                                │    prediction = model.predict(X)
   │                                                                                │
   │                                                                                └──► Return result:
   │                                                                                     {
   │                                                                                       successRate: 78.5,
   │                                                                                       timeTook: 0.234
   │                                                                                     }

3. Generate AI Feedback         ◄───────────────────────────────────────────────────────────────────────────
   │
   │                             ◄──────────────────────────────────────────────────────────────────────────
   │                             │                                POST /genai
   │                             │                                {prompt: assembled_prompt}
   │                             │                                │
   │                             │                                └──► OpenAI API call
   │                             │                                     model: "gpt-4"
   │                             │                                     temperature: 0.7
   │                             │                                     │
   │                             │                                     Returns: personalized feedback text
   │                             │
   │                             └──► Store prediction request ───────► predictReqs.insertOne({
   │                                                                     studentId, quizId, modelId,
   │                                                                     predictedRate: 78.5,
   │                                                                     prompt: assembled_prompt,
   │                                                                     aiResponse: feedback_text
   │                                                                   })

4. Display to Student           ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Prediction result page]
        │
        ├──► Show predicted success rate: 78.5%
        │
        ├──► Show AI-generated feedback:
        │    "Based on your academic background and responses,
        │     you have a strong foundation for success. Consider
        │     focusing on time management and utilizing tutoring
        │     resources to maximize your potential..."
        │
        └──► Update attempt with prediction ─► PUT /api/v2/student/attempt/:attemptId
                                               │
                                               └──► Mark prediction shown ────────► attempts.updateOne({
                                                                                     factorSurveyData: {
                                                                                       predictionShown: true,
                                                                                       predictedRate: 78.5,
                                                                                       predictionDate: Date
                                                                                     }
                                                                                   })

5. Student Views Result         ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Dashboard shows prediction]
        │
        └──► Prediction card displays rate + feedback
```

### 3.5 Providing Feedback (Pseudo-Labeling Loop)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          FEEDBACK SUBMISSION FLOW                                │
│              (Student rates prediction accuracy - enables pseudo-labeling)       │
└─────────────────────────────────────────────────────────────────────────────────┘

User Action                    Frontend                         Backend                          Database
─────────────────────────────────────────────────────────────────────────────────────────────────────────

1. View Prediction Result
   │
   └──► [Prediction page shows]
        │
        ├──► "Your predicted success rate: 78%"
        │
        └──► "How accurate does this prediction feel?"
             │
             └──► ★ ★ ★ ★ ★ (5-star rating widget)

2. Submit High Rating (≥4 stars) - PSEUDO-LABEL PATH
   │
   └──► Click 5 stars (very accurate)
        │
        └──► Submit feedback ───────────────► POST /api/v2/student/attempt/:attemptId/feedback
                                              │                    Body: {rating: 5}
                                              │
                                              ├──► Rating ≥ 4: Use prediction as label
                                              │
                                              ├──► Update attempt ────────────────► attempts.updateOne({
                                              │                                      factorSurveyData: {
                                              │                                        feedbackRating: 5,
                                              │                                        feedbackDate: Date
                                              │                                      },
                                              │                                      targetSurveyData: {
                                              │                                        successRate: 78,
                                              │                                        rateType: "pseudo_labeled"
                                              │                                      }
                                              │                                    })
                                              │
                                              └──► Log correlation ───────────────► feedbackCorrelations.insertOne({
                                                                                     predictedRate: 78,
                                                                                     feedbackRating: 5,
                                                                                     usedAsPseudoLabel: true
                                                                                   })

   ◄─────────────────────────────────────────────────────────────────────────────────────────────────────────
   │
   └──► [Show thank you message]
        │
        └──► "Thank you! Your feedback helps improve predictions."
             │
             └──► Redirect to dashboard (NO target survey required)

─────────────────────────────────────────────────────────────────────────────────────────────────────────────

3. Submit Low Rating (<4 stars) - CORRECTION PATH
   │
   └──► Click 2 stars (inaccurate)
        │
        └──► Submit feedback ───────────────► POST /api/v2/student/attempt/:attemptId/feedback
                                              │                    Body: {rating: 2}
                                              │
                                              ├──► Rating < 4: Request correction
                                              │
                                              ├──► Update attempt ────────────────► attempts.updateOne({
                                              │                                      factorSurveyData: {
                                              │                                        feedbackRating: 2,
                                              │                                        feedbackDate: Date,
                                              │                                        needsCorrection: true
                                              │                                      }
                                              │                                    })
                                              │
                                              └──► Return correction prompt ──────► {
                                                                                     requiresCorrection: true,
                                                                                     message: "Please help us improve"
                                                                                   }

   ◄─────────────────────────────────────────────────────────────────────────────────────────────────────────
   │
   └──► [Correction modal appears]
        │
        ├──► "What do you think your actual success rate is?"
        │
        └──► Slider: 0% ─────────────────────── 100%
             │
             └──► Submit correction: 45%
                  │
                  └──► Save correction ─────────► POST /api/v2/student/attempt/:attemptId/correction
                                                  │                    Body: {correctedRate: 45}
                                                  │
                                                  ├──► Update attempt ────────────► attempts.updateOne({
                                                  │                                  targetSurveyData: {
                                                  │                                    successRate: 45,
                                                  │                                    rateType: "student_corrected"
                                                  │                                  }
                                                  │                                })
                                                  │
                                                  └──► Log for model learning ───► feedbackCorrelations.insertOne({
                                                                                    predictedRate: 78,
                                                                                    actualRate: 45,
                                                                                    difference: 33,
                                                                                    feedbackRating: 2
                                                                                  })

4. Model Improvement Cycle      ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Automatic retraining trigger]
        │
        ├──► Check if training threshold reached (e.g., every 10 new labels)
        │
        └──► If threshold met ──────────────► POST /api/v1/admin/train
                                              │
                                              ├──► Aggregate all training data:
                                              │    • Students with target survey (real labels)
                                              │    • Students with pseudo-labels (high-rated predictions)
                                              │    • Students with corrections (corrected labels)
                                              │
                                              └──► Trigger model training ───────► Queue training job
                                                                                   (See Section 3.6)

5. Virtuous Cycle
   │
   └──► Better model → Higher ratings → More pseudo-labels → Less survey burden
```

### 3.6 Model Training Flow (Admin-Triggered)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MODEL TRAINING FLOW                                    │
│              (Admin triggers training with real + synthetic data)                │
└─────────────────────────────────────────────────────────────────────────────────┘

Admin Action                   Frontend                         Backend                          Model Server
─────────────────────────────────────────────────────────────────────────────────────────────────────────────

1. Navigate to Model Management
   │
   └──► [Admin > Quiz > Models tab]
        │
        └──► View existing models ──────────► GET /api/v1/admin/models/quiz/:slug
                                              │
                                              └──► Return model list ─────────────► modelMetaDatas.find({quizId})
                                                   │
                                                   Returns:
                                                   [{
                                                     name: "nn_20241201_success-factors_abc123",
                                                     algorithmType: "nn_v2",
                                                     metrics: {mae: 9.2, r2: 0.68},
                                                     isCurrent: true,
                                                     studentCount: 85,
                                                     syntheticCount: 340
                                                   }, ...]

2. Trigger Training             ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► Click "Train New Model"
        │
        └──► Configure training:
             │
             ├──► Seed quantity: 400 (synthetic students)
             ├──► Algorithm: Neural Network v2
             │
             └──► Submit ───────────────────► POST /api/v1/admin/train/q/:slug/seed
                                              │                    Body: {seedQty: 400, algorithmType: "nn_v2"}
                                              │
                                              ├──► Create model metadata ─────────► modelMetaDatas.insertOne({
                                              │                                      quizId,
                                              │                                      name: generated_name,
                                              │                                      status: "queued",
                                              │                                      algorithmType: "nn_v2"
                                              │                                    })
                                              │
                                              ├──► Aggregate training data:
                                              │    │
                                              │    ├──► Real students with labels ─► attempts.aggregate([
                                              │    │                                  {$match: {quizId, status: "completed"}},
                                              │    │                                  {$lookup: answers},
                                              │    │                                  {$project: {answers, successRate}}
                                              │    │                                ])
                                              │    │
                                              │    └──► Question seed data ────────► questions.find({quizId})
                                              │                                      .project({seedData, priority})
                                              │
                                              └──► Queue training job ─────────────────────────────────────────►
                                                   POST /seed2
                                                   {
                                                     data: {
                                                       answers: [...realStudents],
                                                       modelName: "nn_20241201_...",
                                                       algorithmType: "nn_v2",
                                                       questionSlugAndType: [...]
                                                     },
                                                     seedQty: 400
                                                   }

3. Synthetic Data Generation                                                        ◄─────────────────────────
   │                                                                                │
   │                                                                                ├──► Add job to queue
   │                                                                                │    QueueManager.add_job(job_id, data)
   │                                                                                │
   │                                                                                ├──► For each synthetic student:
   │                                                                                │    │
   │                                                                                │    ├──► For each question:
   │                                                                                │    │    └──► Random selection weighted by
   │                                                                                │    │         seedData.seedProbability
   │                                                                                │    │
   │                                                                                │    └──► Calculate success rate using
   │                                                                                │         SuccessRateCalculator:
   │                                                                                │         • Weighted score from options
   │                                                                                │         • Sigmoid transformation
   │                                                                                │         • Realistic noise injection
   │                                                                                │
   │                                                                                └──► Progress callback (25%)
                                                                                         POST http://backend:3000/api/v1/ml/job-status/{modelId}
                                                                                         {status: "training", progress: 0.25, message: "Seeding complete"}

4. Neural Network Training                                                          ◄─────────────────────────
   │                                                                                │
   │                                                                                ├──► Combine real + synthetic data
   │                                                                                │    total_students = 85 + 400 = 485
   │                                                                                │
   │                                                                                ├──► Preprocess features:
   │                                                                                │    │
   │                                                                                │    ├──► Convert categorical → numeric
   │                                                                                │    │
   │                                                                                │    ├──► MinMaxScaler normalization
   │                                                                                │    │
   │                                                                                │    └──► Save scaler as .pkl file
   │                                                                                │
   │                                                                                ├──► Train/test split (80/20)
   │                                                                                │
   │                                                                                ├──► Build neural network:
   │                                                                                │    Dense(50) → Dropout(0.1) → ... → Dense(1)
   │                                                                                │
   │                                                                                ├──► Train with callbacks:
   │                                                                                │    • EarlyStopping (patience=10)
   │                                                                                │    • ReduceLROnPlateau
   │                                                                                │
   │                                                                                ├──► Evaluate on test set
   │                                                                                │    MAE: 8.7, MSE: 145.3, R²: 0.71
   │                                                                                │
   │                                                                                ├──► Save model as .h5 file
   │                                                                                │    models/nn_20241201_.../nn_20241201_....h5
   │                                                                                │
   │                                                                                └──► Final callback (100%)
                                                                                         POST http://backend:3000/api/v1/ml/job-status/{modelId}
                                                                                         {
                                                                                           status: "completed",
                                                                                           metrics: {mae: 8.7, mse: 145.3, r2: 0.71},
                                                                                           filePath: "models/nn_20241201_.../..."
                                                                                         }

5. Update Model Metadata        ◄─────────────────────────────────────────────────────────────────────────
   │
   │                             ◄──────────────────────────────────────────────────────────────────────────
   │                             │
   │                             └──► Receive callback ──────────────► modelMetaDatas.updateOne({
   │                                                                    _id: modelId,
   │                                                                    status: "completed",
   │                                                                    metrics: {mae, mse, r2},
   │                                                                    filePath,
   │                                                                    trainingSummary: {
   │                                                                      realStudents: 85,
   │                                                                      syntheticStudents: 400,
   │                                                                      trainingTime: 45.2
   │                                                                    }
   │                                                                  })

6. Set as Active Model          ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► [Models list refreshes]
        │
        └──► New model appears with metrics
             │
             └──► Click "Set as Active"
                  │
                  └──► Activate model ──────────► POST /api/v1/admin/models/quiz/:quizId/model/:modelId
                                                  │
                                                  ├──► Unset previous current ────► modelMetaDatas.updateMany({
                                                  │                                  quizId, isCurrent: true
                                                  │                                }, {isCurrent: false})
                                                  │
                                                  └──► Set new current ───────────► modelMetaDatas.updateOne({
                                                                                     _id: modelId,
                                                                                     isCurrent: true
                                                                                   })

7. Model Ready for Predictions  ◄─────────────────────────────────────────────────────────────────────────
   │
   └──► New predictions will use updated model
```

---

## 4. Technology Stack Summary

### 4.1 Frontend Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Framework** | React | 18.3.1 | UI component library |
| **Language** | TypeScript | 5.x | Type-safe JavaScript |
| **Build Tool** | Vite | 5.3.1 | Fast development/build |
| **Routing** | React Router | 6.23.1 | Client-side routing |
| **State Management** | TanStack React Query | 5.45.1 | Server state caching |
| **HTTP Client** | Axios | 1.7.2 | REST API communication |
| **Form Handling** | React Hook Form | 7.52.0 | Form state management |
| **Validation** | Zod | 3.23.8 | Schema validation |
| **UI Components** | Radix UI | various | Accessible primitives |
| **Styling** | Tailwind CSS | 3.4.4 | Utility-first CSS |
| **Charts** | Recharts | 2.12.7 | Data visualization |
| **Icons** | Tabler Icons | 3.6.0 | Icon library |
| **Rich Text** | Lexical | 0.34.0 | Rich text editor |
| **Notifications** | Sonner | 1.5.0 | Toast notifications |
| **Analytics** | PostHog | 1.292.0 | User analytics |

### 4.2 Backend Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Runtime** | Node.js | 20 LTS | JavaScript runtime |
| **Framework** | Express.js | 4.19.x | HTTP server framework |
| **Language** | TypeScript | 5.4.x | Type-safe JavaScript |
| **Database** | MongoDB | 7.0 | Document database |
| **ODM** | Mongoose | 8.4.x | MongoDB object modeling |
| **Authentication** | JWT | jsonwebtoken | Token-based auth |
| **Password Hashing** | bcrypt | 5.x | Secure password storage |
| **Validation** | Zod | 3.23.x | Request validation |
| **HTTP Security** | Helmet | 7.x | Security headers |
| **CORS** | cors | 2.8.x | Cross-origin requests |
| **Logging** | Morgan + Winston | various | Request/app logging |
| **Email** | Resend | 3.x | Transactional email |
| **Analytics** | PostHog | 3.x | Server-side analytics |
| **PDF Generation** | PDFKit | 0.x | Report generation |
| **Process Management** | cluster | native | Multi-worker scaling |

### 4.3 Model Server Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Language** | Python | 3.12 | ML programming |
| **Web Framework** | Flask | 3.x | REST API server |
| **ML Framework** | TensorFlow/Keras | 2.x | Neural network training |
| **ML Utilities** | scikit-learn | 1.x | Preprocessing, KNN |
| **Data Processing** | pandas | 2.x | Data manipulation |
| **Numerical Computing** | NumPy | 1.x | Array operations |
| **AI Integration** | OpenAI SDK | 1.x | GPT feedback generation |
| **Model Storage** | HDF5 (.h5) | - | Neural network weights |
| **Serialization** | Pickle (.pkl) | - | Scaler persistence |
| **Queue Management** | Threading | native | Background job processing |

### 4.4 Infrastructure & DevOps

| Category | Technology | Purpose |
|----------|------------|---------|
| **Containerization** | Docker | Application packaging |
| **Orchestration** | Docker Compose | Multi-container management |
| **Reverse Proxy** | Nginx | Load balancing, SSL termination |
| **CI/CD** | GitHub Actions | Automated build/deploy |
| **SSL/TLS** | Let's Encrypt | HTTPS certificates |
| **Database Hosting** | MongoDB Atlas | Managed cloud database |
| **Server OS** | RHEL 9 | Production server |
| **Container Registry** | Docker Hub | Image storage |

### 4.5 External Services

| Service | Purpose | Integration Point |
|---------|---------|-------------------|
| **MongoDB Atlas** | Cloud database | Backend persistence |
| **PostHog Cloud** | Analytics & tracking | Frontend + Backend |
| **Resend** | Transactional email | Backend (password reset, notifications) |
| **OpenAI API** | AI-generated feedback | Model server (prompt completion) |

---

## 5. Communication Protocols

### 5.1 Frontend ↔ Backend Communication

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    FRONTEND ↔ BACKEND PROTOCOL                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  Protocol: HTTPS (TLS 1.2/1.3)                                               │
│  Format: JSON (application/json)                                             │
│  Authentication: JWT Bearer Token + HTTP-Only Cookies                        │
│                                                                               │
│  Request Headers:                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  Authorization: Bearer <accessToken>                                    │ │
│  │  Content-Type: application/json                                         │ │
│  │  X-Requested-With: XMLHttpRequest                                       │ │
│  │  Cookie: accessToken=<jwt>; refreshToken=<jwt>                          │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
│  Response Format (V2 API):                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  {                                                                      │ │
│  │    "data": <response_payload>,                                          │ │
│  │    "message": "Success message",                                        │ │
│  │    "meta": {                                                            │ │
│  │      "pagination": { "page": 1, "limit": 20, "total": 100 }            │ │
│  │    }                                                                    │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
│  Error Format:                                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  {                                                                      │ │
│  │    "error": "Error message",                                            │ │
│  │    "statusCode": 400,                                                   │ │
│  │    "details": { ... }                                                   │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Backend ↔ Model Server Communication

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    BACKEND ↔ MODEL SERVER PROTOCOL                            │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  Protocol: HTTP (internal network)                                           │
│  Format: JSON                                                                │
│  Authentication: None (internal network isolation)                           │
│                                                                               │
│  Training Request:                                                           │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  POST /seed2                                                            │ │
│  │  {                                                                      │ │
│  │    "data": {                                                            │ │
│  │      "answers": [                                                       │ │
│  │        {                                                                │ │
│  │          "answers": {"gpa": 3.5, "sat": 1200, ...},                    │ │
│  │          "success_rate": 75                                             │ │
│  │        }, ...                                                           │ │
│  │      ],                                                                 │ │
│  │      "modelName": "nn_20241201_quiz-slug_abc123",                       │ │
│  │      "algorithmType": "nn_v2",                                          │ │
│  │      "questionSlugAndType": [                                           │ │
│  │        {"slug": "gpa", "type": "cardinal", "priority": 9}, ...         │ │
│  │      ]                                                                  │ │
│  │    },                                                                   │ │
│  │    "seedQty": 400                                                       │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
│  Prediction Request:                                                         │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  POST /predict_neural                                                   │ │
│  │  {                                                                      │ │
│  │    "modelDetails": {                                                    │ │
│  │      "_id": "model_id",                                                 │ │
│  │      "name": "nn_20241201_quiz-slug_abc123",                            │ │
│  │      "filePath": "models/nn_20241201_.../model.h5",                     │ │
│  │      "algorithmType": "nn_v2"                                           │ │
│  │    },                                                                   │ │
│  │    "allAnswers": [                                                      │ │
│  │      {"gpa": {"value": "3.5", "weight": 0.9}},                         │ │
│  │      {"sat": {"value": "1200", "weight": 0.8}}, ...                    │ │
│  │    ],                                                                   │ │
│  │    "studentId": "student_id"                                            │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
│  Prediction Response:                                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  {                                                                      │ │
│  │    "successRate": 78.5,                                                 │ │
│  │    "timeTook": 0.234                                                    │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
│  Training Status Callback (Model → Backend):                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │  POST http://backend:3000/api/v1/ml/job-status/{modelId}                │ │
│  │  {                                                                      │ │
│  │    "status": "completed" | "training" | "failed",                       │ │
│  │    "progress": 1.0,                                                     │ │
│  │    "message": "Training complete",                                      │ │
│  │    "metrics": {"mae": 8.7, "mse": 145.3, "r2": 0.71},                  │ │
│  │    "filePath": "models/nn_20241201_.../model.h5"                        │ │
│  │  }                                                                      │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Key File Locations Reference

### 6.1 Frontend Key Files

| Component | Location |
|-----------|----------|
| Entry Point | `frontend/src/main.tsx` |
| Router | `frontend/src/mainRouter.tsx` |
| Axios Config | `frontend/src/lib/axios.ts`, `axiosV2.ts` |
| User Context | `frontend/src/context/UserContext.tsx` |
| Workflow Context | `frontend/src/contexts/WorkflowContext.tsx` |
| Student Dashboard | `frontend/src/pages/student/dashboard/` |
| Quiz Taking | `frontend/src/pages/student/quizzes/quiz/` |
| Admin Quiz Management | `frontend/src/pages/admin/quizzes/` |
| V2 API Services | `frontend/src/service/v2/` |

### 6.2 Backend Key Files

| Component | Location |
|-----------|----------|
| Server Entry | `backend/src/index.ts` |
| App Config | `backend/src/app.ts` |
| V2 Routes | `backend/src/routes/api/v2/` |
| Controllers | `backend/src/controllers/` |
| Services | `backend/src/services/` |
| Models | `backend/src/models/` |
| Auth Middleware | `backend/src/middlewares/auth.middleware.ts` |
| Predict Controller | `backend/src/controllers/predict.controller.ts` |
| Train Controller | `backend/src/controllers/trainController.ts` |
| Constants | `backend/src/utils/constants.ts` |

### 6.3 Model Server Key Files

| Component | Location |
|-----------|----------|
| Flask App | `model/main.py` |
| Neural Network v1 | `model/neural_network.py` |
| Neural Network v2 | `model/neural_network_v2.py` |
| Regression Model | `model/regression.py` |
| Queue Manager | `model/queue_manager.py` |
| Progress Tracker | `model/progress_tracker.py` |
| Success Rate Calculator | `model/app/generators/dynamicSuccessRateGen.py` |
| AI Prompts | `model/prompts.py` |
| Model Storage | `model/models/` (shared volume) |

---

## Document Metadata

- **Author**: Generated from codebase analysis
- **Last Updated**: December 2024
- **Related Documents**:
  - [System Overview](./system-overview.md)
  - [Deployment Architecture](./deployment-architecture.md)
