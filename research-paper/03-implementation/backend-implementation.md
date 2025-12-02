# Backend Implementation Documentation

## Document Purpose
This document provides comprehensive technical documentation of the ACOSUS backend implementation, including API endpoints, authentication mechanisms, database schemas, and data flow patterns.

---

## 1. Technology Stack

### 1.1 Runtime & Frameworks

| Component | Version | Purpose |
|-----------|---------|---------|
| **Node.js** | 20.x LTS | JavaScript runtime |
| **Express.js** | 4.19.x | Web framework |
| **TypeScript** | 5.4.x | Type-safe development |
| **MongoDB** | 7.0 | NoSQL database |
| **Mongoose** | 8.4.x | MongoDB ODM |

### 1.2 Core Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **jsonwebtoken** | 9.0.x | JWT authentication |
| **bcrypt** | 5.1.x | Password hashing |
| **zod** | 3.23.x | Runtime validation |
| **cors** | 2.8.x | Cross-origin requests |
| **helmet** | 7.1.x | Security headers |
| **morgan** | 1.10.x | HTTP logging |
| **winston** | 3.13.x | Application logging |
| **resend** | 3.2.x | Email service |
| **posthog-node** | 5.11.x | Analytics |
| **axios** | 1.7.x | HTTP client (Model Server) |

### 1.3 Database Configuration

```typescript
// Environment-based database selection
const databases = {
  production: "acosus-production-v2",
  development_seed: "acosus-seed",
  development: "acosus-dev"
};
```

---

## 2. API Endpoints

### 2.1 V2 Routes (Primary - Survey Workflow v2)

Base URL: `/api/v2`

#### 2.1.1 Student Routes (`/api/v2/student`)

**Quiz Discovery**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/quiz/target` | Get all published target quizzes |
| GET | `/quiz/factor` | Get all published factor quizzes |
| GET | `/quiz/:slug` | Get specific quiz by slug |
| GET | `/quiz/:slug/content` | Get quiz content with categories and questions |

**Answer Submission**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/answer` | Submit single answer (auto-save) |
| POST | `/answer/bulk` | Submit multiple answers atomically |
| GET | `/attempt/:attemptId/answers` | Get answers for attempt (optional grouping) |

**Attempt Completion**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/attempt/complete/single-target` | Complete single-question target quiz |
| POST | `/attempt/complete/multi-target` | Complete multi-question target quiz |
| POST | `/attempt/complete/factor` | Complete factor quiz (triggers prediction) |
| POST | `/attempt/:attemptId/submit-rating` | Submit prediction rating (1-5 scale) |
| POST | `/attempt/:attemptId/abandon` | Abandon in-progress attempt |

**Attempt Retrieval**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/attempt/:attemptId` | Get attempt details with answers |
| GET | `/attempt/quiz/:quizId` | Get attempts by quiz |
| GET | `/attempts` | Get all attempts (paginated, filtered) |

**Profile Management**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/profile/questions` | Get all profile questions grouped by category |
| POST | `/profile/answer` | Submit single profile answer |
| POST | `/profile/answers` | Submit multiple profile answers |
| GET | `/profile/answers` | Get student's profile answers |
| GET | `/profile/completion-status` | Get profile completion status |

**Workflow**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workflow/status` | Get complete survey workflow status |

#### 2.1.2 Admin Routes (`/api/v2/admin`)

**Quiz Management**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/quiz/target` | Create target quiz |
| POST | `/quiz/factor` | Create factor quiz |
| GET | `/quiz` | Get all quizzes |
| GET | `/quiz/target/list` | Get all target quizzes |
| GET | `/quiz/factor/list` | Get all factor quizzes |
| GET | `/quiz/:quizId` | Get quiz by ID |
| PUT | `/quiz/:quizId` | Update quiz |
| DELETE | `/quiz/:quizId` | Delete quiz |
| PATCH | `/quiz/:quizId/publish` | Publish quiz |
| PATCH | `/quiz/:quizId/unpublish` | Unpublish quiz |

**Category Management**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/quiz/:quizId/category` | Create quiz category |
| POST | `/profile-category` | Create profile category |
| GET | `/quiz/:quizId/categories` | Get quiz categories |
| GET | `/profile-categories` | Get profile categories |
| PATCH | `/quiz/:quizId/categories/reorder` | Reorder quiz categories |

**Question Management**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/quiz/:quizId/question` | Create quiz question |
| POST | `/profile-question` | Create profile question |
| GET | `/quiz/:quizId/questions` | Get all quiz questions |
| GET | `/profile-questions` | Get all profile questions |
| PUT | `/question/:questionId` | Update question |
| DELETE | `/question/:questionId` | Delete question |

**Dashboard**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard/summary` | Get dashboard summary |
| GET | `/dashboard/profile-completion` | Profile completion metrics |
| GET | `/dashboard/target-survey-completion` | Target survey metrics |
| GET | `/dashboard/factor-survey-completion` | Factor survey metrics |

#### 2.1.3 Advisor Routes (`/api/v2/advisor`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Search students (query: q, type, page, limit) |
| GET | `/student/:studentId/profile` | Get student profile |
| GET | `/student/:studentId/attempts` | List student's quiz attempts |
| PUT | `/student/:studentId/quiz/:quizId/attempt/:attemptId/predict` | Trigger prediction |
| POST | `/student/:studentId/quiz/:quizId/attempt/start` | Start new attempt for student |

### 2.2 V1 Routes (Legacy - Still Active)

Base URL: `/api/v1`

**Public Routes**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register student |
| POST | `/verify-account` | Verify email |
| POST | `/login` | User login |
| POST | `/reset-password` | Create reset password token |
| GET | `/consent` | Get consent form |
| POST | `/ml/job-status/:modelId` | ML service job status callback |

**Account Routes (Protected)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/account/change-password` | Change password |
| POST | `/account/update-details` | Update account details |
| GET | `/account/getUserDetails` | Get user details |
| POST | `/account/logout` | User logout |

---

## 3. Authentication & Authorization

### 3.1 JWT-Based Authentication

```typescript
// Token acquisition flow
export const authenticate = async (req, res, next) => {
  const token =
    req.cookies.accessToken ||
    req.headers.authorization?.split(" ")[1] ||
    req.headers["x-access-token"];

  const decoded = jwt.verify(token, process.env.ACCESS_TOKEN_SECRET);
  const user = await User.findById(decoded._id);

  // Auto-refresh if expiring within 12 hours
  if (exp - now < 43200) {
    const newToken = generateAccessToken(user);
    res.cookie("accessToken", newToken, COOKIES_OPTIONS);
  }

  req.user = user;
  next();
};
```

### 3.2 Role-Based Authorization

```typescript
// Role constants
export const ROLE_ADMIN = "admin";
export const ROLE_ADVISOR = "advisor";
export const ROLE_STUDENT = "student";
export const ROLE_MODERATOR = "moderator";

// Authorization middleware
export const authorize = (...roles: string[]) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return next(new ApiError(403, "Access denied"));
    }
    next();
  };
};
```

### 3.3 Token Refresh Flow

```typescript
// Automatic refresh when access token expires
if (error.name === "TokenExpiredError" && refreshToken) {
  const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
  const user = await User.findById(decoded._id);

  if (user.refreshToken === refreshToken) {
    const newAccessToken = generateAccessToken(user);
    res.cookie("accessToken", newAccessToken, COOKIES_OPTIONS);
    req.user = user;
  }
}
```

---

## 4. Database Schemas

### 4.1 User Schema

```typescript
interface IUser {
  _id: ObjectId;
  fullName: string;
  email: string;              // Unique, indexed
  password: string;           // bcrypt hashed
  role: "admin" | "advisor" | "student" | "moderator";
  refreshToken?: string;
  isEmailVerified: boolean;
  isBlocked: boolean;
  consent: {
    isAgreed: boolean;
    agreedAt: Date;
  };
  verificationCode?: string;
  resetPasswordToken?: string;
  createdAt: Date;
  updatedAt: Date;
}
```

### 4.2 Student Profile Schema

```typescript
interface IStudentProfile {
  _id: ObjectId;
  email: string;              // Unique, indexed
  studentId: ObjectId;        // ref: User

  // Demographics
  degreeType: "undergraduate" | "graduate" | "non-traditional-degree-program";
  major: string;
  studentStatus: "full-time" | "part-time" | "on-leave" | "graduated";
  ageGroup: string;
  gender: string;
  ethnicity: string;
  isFirstGeneration: "yes" | "no" | "prefer-not-to-say";

  // Academic
  earnedCredits: number;
  currentCredits: number;
  currentSemester: string;
  previousInstitutionType: string;

  // Dates
  startDate: Date;
  endDate: Date;
  isGraduated: boolean;
}
```

### 4.3 Quiz Schema

```typescript
interface IQuiz {
  _id: ObjectId;
  title: string;
  slug: string;               // Unique
  description: string;

  // Quiz type system
  quizType: "target" | "factor";
  targetType?: "single_question" | "multi_question";  // Only for target

  // Linking
  linkedFactorQuizIds?: ObjectId[];   // For target quiz
  linkedTargetQuizId?: ObjectId;      // For factor quiz

  // Model configuration
  modelConfig: {
    knn: {
      n_neighbors: number | "auto";
      weights: "uniform" | "distance";
      metric: "euclidean" | "manhattan" | "minkowski";
    };
    gan: {
      epochs: number;
      batch_size: number;
      synthetic_multiplier: number;
    };
    neural: {
      architecture: { layers: number[]; dropout_rates: number[] };
      training: { epochs: number; learning_rate: number };
    };
  };

  // Training triggers
  trainingTriggers: {
    initialKnnThreshold: number;      // Default: 10
    knnRetrainInterval: number;       // Default: 10
    ganTrainThreshold: number;        // Default: 20
    feedbackRatingThreshold: number;  // Default: 3.5
    enableAutomaticTraining: boolean;
  };

  isPublished: boolean;
  isActive: boolean;
}
```

### 4.4 Attempt Schema (Core Survey Workflow)

```typescript
interface IAttempt {
  _id: ObjectId;
  studentId: ObjectId;
  quizId: ObjectId;
  quizType: "target" | "factor";

  // Questions and answers
  questions: Array<{
    questionId: ObjectId;
    answer: string | number | boolean | string[];
    answerWeightage?: number;
    answerId: ObjectId;
    updatedBy: ObjectId;
    updatedByRole: "student" | "advisor" | "admin";
    updatedAt: Date;
  }>;

  // Status
  attemptStatus: "started" | "in-progress" | "completed" | "abandoned";
  attemptNumber: number;
  startedAt: Date;
  completedAt?: Date;

  // === TARGET SURVEY FIELDS ===
  calculatedSuccessRate?: number;     // From PWRS formula (0-100)
  presumedSuccessRate?: number;       // Student self-assessment
  finalSuccessRate?: number;          // Used for training
  successRateSource?: "self_reported" | "calculated" | "pseudo_label" | "feedback_corrected";

  // === FACTOR SURVEY FIELDS ===
  modelId?: ObjectId;                 // ref: ModelMetaData
  modelVersionUsed?: string;
  predictionRequestId?: ObjectId;     // ref: PredictionRequest
  predictionShown?: number;           // 0-100
  feedbackRating?: number;            // 1-5
  feedbackTimestamp?: Date;

  // OpenAI response
  openAIResponse?: {
    text: string;
    generatedAt: Date;
    tokensUsed: number;
    model: string;
  };

  // === WORKFLOW TRACKING ===
  triggeredByFactorAttemptId?: ObjectId;
  linkedTargetAttemptId?: ObjectId;
  workflowStage: "early_adoption" | "production";
  predictionAcceptedAsLabel?: boolean;
}
```

### 4.5 Answer Schema

```typescript
interface IAnswer {
  _id: ObjectId;
  questionId: ObjectId;
  quizId: ObjectId;
  studentId: ObjectId;
  attemptId?: ObjectId;       // Links quiz answers to attempts

  answer: string | number | boolean | string[];
  answerWeightage?: number;
  questionSlug: string;

  answerScope: "quiz" | "profile";
  isDeleted: boolean;

  modifiedBy?: {
    userId: ObjectId;
    role: "student" | "advisor" | "admin";
    modifiedAt: Date;
  };
}

// Indexes
// Compound unique to prevent duplicate answers
{ attemptId: 1, questionId: 1, studentId: 1 }  // unique, partial
```

### 4.6 Prediction Request Schema

```typescript
interface IPredictionReq {
  _id: ObjectId;
  studentId: ObjectId;
  quizId: ObjectId;           // Factor quiz
  attemptId: ObjectId;

  // Input
  factorAnswers: Record<string, any>;

  // Model info
  modelUsedId: ObjectId;
  modelVersion: string;
  modelType: "knn" | "gan" | "neural";

  // Results
  prediction: {
    predictedSuccessRate: number;  // 0-100
    confidence?: number;           // 0-1
    confidenceInterval?: { lower: number; upper: number };
    featureImportance?: Array<{ feature: string; importance: number }>;
  };

  // OpenAI response
  openAIResponseObj?: {
    text: string;
    generatedAt: Date;
    tokensUsed: number;
    model: string;
  };

  // Performance
  performance: {
    timeTook: number;
    modelLoadTime?: number;
    inferenceTime?: number;
    openAITime?: number;
  };

  // Feedback
  hasFeedback: boolean;
  feedbackId?: ObjectId;

  // Actual outcome (filled later)
  actualOutcome?: {
    actualSuccessRate: number;
    source: "self_reported" | "calculated" | "feedback_corrected" | "pseudo_label";
    collectedAt: Date;
  };
}
```

### 4.7 Model Metadata Schema

```typescript
interface IModelMetaData {
  _id: ObjectId;
  modelName: string;
  modelUniqueId: string;      // Unique
  modelVersion: string;       // e.g., "v3_neural_20250929_102000"
  modelType: "knn" | "gan" | "neural";
  quizId: ObjectId;
  filePath: string;

  // Training metrics
  trainingMetrics: {
    mae: number;
    mse: number;
    rmse: number;
    r2: number;
    crossValidationScores?: {
      mae: number[];
      mean_mae: number;
    };
  };

  // Training data summary
  trainingDataSummary: {
    totalStudents: number;
    totalRealStudents: number;
    syntheticStudentsGenerated?: number;
    labelSources: {
      self_reported: number;
      calculated: number;
      pseudo_label: number;
      feedback_corrected: number;
    };
    totalFeatures: number;
    featureNames: string[];
  };

  // Configuration snapshot
  configSnapshot: {
    knn?: { n_neighbors; weights; metric };
    gan?: { epochs; batch_size; synthetic_multiplier };
    neural?: { architecture; training };
  };

  // Training context
  trainingContext: {
    trainTime: number;        // Milliseconds
    trainedAt: Date;
    trainedBy: ObjectId;
    triggerType: "initial_knn" | "knn_retrain" | "gan_train" | "neural_train" | "manual";
  };

  // Status
  status: {
    stage: "pending" | "queued" | "training" | "validation" | "completed" | "failed";
    state: "started" | "completed" | "failed" | "in-progress";
  };

  isCurrent: boolean;
  isArchived: boolean;
}
```

---

## 5. Data Flow: Survey Submission

### 5.1 Answer Submission Flow

```typescript
// POST /api/v2/student/answer
async function submitAnswerHandler(req, res) {
  const { quizId, attemptId, answers } = req.body;
  const studentId = req.user._id;

  // 1. Get or create attempt
  let attempt = attemptId
    ? await Attempt.findById(attemptId)
    : await createAttempt(studentId, quizId);

  // 2. Dual-write pattern: Answer + Attempt.questions
  for (const ans of answers) {
    // Write to Answer collection
    await Answer.findOneAndUpdate(
      { attemptId, questionId: ans.questionId, studentId },
      { answer: ans.answer, answerWeightage: ans.weightage },
      { upsert: true }
    );

    // Sync to Attempt.questions array
    syncAnswerToAttempt(attempt, ans);
  }

  // 3. Update tracking
  await QuizAttemptTracking.updateAttemptProgress(studentId, quizId, attemptId);

  return { success: true, attemptId: attempt._id };
}
```

### 5.2 Target Survey Completion Flow

```typescript
// POST /api/v2/student/attempt/complete/single-target
async function completeSingleQuestionTargetHandler(req, res) {
  const { attemptId, successRate } = req.body;

  // 1. Validate attempt exists and is in-progress
  const attempt = await Attempt.findById(attemptId);
  if (attempt.attemptStatus === "completed") throw new ApiError(400, "Already completed");

  // 2. Store success rate directly (single-question = direct input)
  attempt.finalSuccessRate = successRate;
  attempt.successRateSource = "self_reported";
  attempt.attemptStatus = "completed";
  attempt.completedAt = new Date();

  await attempt.save();

  // 3. Update tracking
  await QuizAttemptTracking.updateAttemptCompletion(attempt);

  return { success: true, finalSuccessRate: successRate };
}
```

### 5.3 Factor Survey & Prediction Flow

```typescript
// POST /api/v2/student/attempt/complete/factor
async function completeFactorQuizHandler(req, res) {
  const { attemptId } = req.body;

  // 1. Mark attempt as completed
  const attempt = await Attempt.findById(attemptId).populate("quizId");
  attempt.attemptStatus = "completed";
  attempt.completedAt = new Date();

  // 2. Check if model exists for prediction
  const currentModel = await ModelMetaData.findOne({
    quizId: attempt.quizId.linkedTargetQuizId,
    isCurrent: true
  });

  if (!currentModel) {
    // Early adoption: no model yet
    return { prediction: null, message: "Model not trained yet" };
  }

  // 3. Build prediction request
  const factorAnswers = buildFactorAnswers(attempt.questions);

  // 4. Call Model Server
  const prediction = await axios.post(ML_PREDICT_URL, {
    modelName: currentModel.modelName,
    factorAnswers
  });

  // 5. Store prediction
  const predReq = await PredictionReq.create({
    studentId: attempt.studentId,
    quizId: attempt.quizId,
    attemptId,
    factorAnswers,
    modelUsedId: currentModel._id,
    modelVersion: currentModel.modelVersion,
    modelType: currentModel.modelType,
    prediction: {
      predictedSuccessRate: prediction.data.success_rate,
      confidence: prediction.data.confidence
    },
    performance: { timeTook: prediction.data.timeTook }
  });

  // 6. Update attempt with prediction
  attempt.predictionRequestId = predReq._id;
  attempt.predictionShown = prediction.data.success_rate;
  attempt.modelId = currentModel._id;
  attempt.modelVersionUsed = currentModel.modelVersion;
  await attempt.save();

  return { prediction: prediction.data.success_rate };
}
```

### 5.4 Rating Submission & Pseudo-Labeling

```typescript
// POST /api/v2/student/attempt/:attemptId/submit-rating
async function submitRatingHandler(req, res) {
  const { attemptId } = req.params;
  const { rating } = req.body;  // 1-5 scale

  const attempt = await Attempt.findById(attemptId);

  // 1. Store rating
  attempt.feedbackRating = rating;
  attempt.feedbackTimestamp = new Date();
  attempt.ratingSubmittedAt = new Date();

  // 2. Pseudo-labeling decision
  if (rating >= 4) {
    // High rating: use prediction as pseudo-label
    attempt.predictionAcceptedAsLabel = true;
    attempt.finalSuccessRate = attempt.predictionShown;
    attempt.successRateSource = "pseudo_label";
  } else {
    // Low rating: require target survey for correction
    attempt.predictionAcceptedAsLabel = false;
    // Frontend will redirect to target survey
  }

  await attempt.save();

  return {
    acceptedAsLabel: attempt.predictionAcceptedAsLabel,
    requiresTargetSurvey: rating <= 3
  };
}
```

---

## 6. Data Validation

### 6.1 Zod Validation Schemas

```typescript
// Success rate validation (0-100)
const successRateSchema = z.number()
  .min(0, "Success rate must be at least 0")
  .max(100, "Success rate must be at most 100");

// Complete single-question target
export const completeSingleTargetSchema = z.object({
  quizId: objectIdSchema.optional(),
  quizSlug: z.string().min(1).optional(),
  attemptId: objectIdSchema,
  successRate: successRateSchema,
}).refine((data) => data.quizId || data.quizSlug, {
  message: "Either quizId or quizSlug must be provided"
});

// Rating submission (1-5)
export const submitRatingSchema = z.object({
  params: z.object({ attemptId: objectIdSchema }),
  body: z.object({
    rating: z.number().int().min(1).max(5)
  })
});

// Attempt query with pagination
export const attemptQuerySchema = z.object({
  page: z.string().optional().transform(v => parseInt(v) || 1),
  limit: z.string().optional().transform(v => Math.min(parseInt(v) || 20, 100)),
  quizType: z.enum(["target", "factor"]).optional(),
  status: z.enum(["started", "in-progress", "completed", "abandoned"]).optional()
});
```

### 6.2 MongoDB ObjectId Validation

```typescript
const objectIdSchema = z.union([
  z.string().regex(/^[0-9a-fA-F]{24}$/, "Invalid ObjectId format"),
  z.instanceof(Types.ObjectId)
]);
```

### 6.3 Error Handling

```typescript
// Custom API error class
export class ApiError extends Error {
  statusCode: number;

  constructor(statusCode: number, message: string) {
    super(message);
    this.statusCode = statusCode;
  }
}

// Async handler wrapper
export const asyncHandler = (fn: Function) => {
  return (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
};

// Global error handler
app.use((err, req, res, next) => {
  const statusCode = err.statusCode || 500;
  res.status(statusCode).json({
    success: false,
    message: err.message,
    ...(process.env.NODE_ENV === "development" && { stack: err.stack })
  });
});
```

---

## 7. Survey Workflow Service

### 7.1 Workflow Status Endpoint

```typescript
// GET /api/v2/student/workflow/status
export async function getWorkflowStatus(studentId: string): Promise<SurveyWorkflowStatusResponse> {
  // 1. Determine current system stage
  const systemStage = await determineCurrentSystemStage();

  // 2. Fetch all published quizzes
  const [targetQuizzes, factorQuizzes] = await Promise.all([
    getPublishedTargetQuizzes(),
    getPublishedFactorQuizzes()
  ]);

  // 3. Fetch all student attempts
  const studentAttempts = await Attempt.find({ studentId });

  // 4. Calculate status for each quiz
  const targetStatus = targetQuizzes.map(q =>
    calculateTargetQuizStatus(q, studentAttempts, systemStage)
  );

  const factorStatus = factorQuizzes.map(q =>
    calculateFactorQuizStatus(q, studentAttempts, systemStage)
  );

  // 5. Calculate pending actions
  const pendingActions = await calculatePendingActions(studentAttempts, allQuizzes);

  return {
    systemStage,
    availableQuizzes: { target: targetStatus, factor: factorStatus },
    pendingActions,
    systemProgress: await getSystemProgress()
  };
}
```

### 7.2 System Stage Determination

```typescript
export async function determineCurrentSystemStage(): Promise<"early_adoption" | "production"> {
  const threshold = await getSetting(SETTINGS_KEYS.SURVEY.EARLY_ADOPTION_THRESHOLD) || 50;

  // Count students with BOTH surveys completed
  const result = await Attempt.aggregate([
    { $match: { attemptStatus: "completed", quizType: { $in: ["target", "factor"] } } },
    { $group: { _id: "$studentId", surveyTypes: { $addToSet: "$quizType" } } },
    { $match: { surveyTypes: { $all: ["target", "factor"] } } },
    { $count: "totalStudents" }
  ]);

  const total = result[0]?.totalStudents || 0;
  return total >= threshold ? "production" : "early_adoption";
}
```

---

## 8. Key Constants

```typescript
// User Roles
export const ROLE_ADMIN = "admin";
export const ROLE_ADVISOR = "advisor";
export const ROLE_STUDENT = "student";
export const ROLE_MODERATOR = "moderator";

// Attempt Status
export const ATTEMP_STATUS_ENUM = {
  STARTED: "started",
  IN_PROGRESS: "in-progress",
  COMPLETED: "completed",
  ABANDONED: "abandoned"
};

// Cookie Options
export const COOKIES_OPTIONS = {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: process.env.NODE_ENV === "production" ? "none" : "lax",
  path: "/"
};

// ML Service URLs
export const ML_SERVICE = {
  TRAIN_URL: "/trainNeural",
  PREDICT_URL: "/predict",
  PREDICT_URL_NEURAL: "/predict_neural",
  PROMPT_URL: "/genai"
};
```

---

## 9. Database Indexes

### 9.1 Attempt Collection Indexes

```javascript
// Efficient querying patterns
{ studentId: 1, quizId: 1, attemptNumber: -1 }
{ quizId: 1, attemptStatus: 1 }
{ quizType: 1, completedAt: -1 }
{ predictionRequestId: 1 }
{ workflowStage: 1, attemptStatus: 1 }
{ studentId: 1, quizType: 1, attemptStatus: 1, completedAt: -1 }
```

### 9.2 Answer Collection Indexes

```javascript
// Prevent duplicate answers within attempt
{ attemptId: 1, questionId: 1, studentId: 1 }  // unique, partial filter
{ attemptId: 1, questionId: 1 }
{ studentId: 1, quizId: 1, attemptId: 1 }
```

### 9.3 Model Metadata Indexes

```javascript
{ quizId: 1, isCurrent: 1 }           // Get current active model
{ quizId: 1, createdAt: -1 }          // Version history
{ modelVersion: 1 }                    // unique
{ modelType: 1 }
```

---

## 10. Project Structure

```
src/
├── index.ts                    # Server entry point
├── app.ts                      # Express app configuration
├── config/                     # Configuration files
├── controllers/
│   ├── v1/                     # Legacy controllers
│   └── v2/
│       ├── admin/              # Admin endpoints
│       ├── student/            # Student endpoints
│       └── advisor/            # Advisor endpoints
├── models/                     # MongoDB schemas (15 models)
├── routes/
│   └── api/
│       ├── v1/                 # Legacy routes
│       └── v2/                 # Survey workflow v2
├── services/                   # Business logic layer
│   ├── answer/
│   ├── attempt/
│   ├── quiz/
│   ├── surveyWorkflow/
│   └── modelMetaData/
├── middlewares/                # Auth, PostHog
├── validation/                 # Zod schemas
├── utils/                      # Helpers, constants
├── lib/                        # Shared utilities
└── db/                         # Database connection
```

---

## Document Metadata

- **Source**: ACOSUS Backend Repository
- **Last Updated**: December 2024
- **Backend Version**: 0.0.1
- **API Version**: v2 (primary), v1 (legacy support)
