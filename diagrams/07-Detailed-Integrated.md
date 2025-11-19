# Detailed Architecture - Integrated Flow

**Purpose**: Comprehensive system architecture showing all components, flows, and decision points in a single diagram.

**Use Case**: Complete technical reference, thesis documentation, comprehensive Q&A.

---

## Diagram

**Note**: This is a large, comprehensive diagram. For presentation slides, consider using the side-by-side or separate detailed diagrams instead.

```mermaid
graph TB
    subgraph Frontend["🟦 FRONTEND LAYER"]
        direction LR
        SP[Student Portal<br/>- Enrollment<br/>- Surveys<br/>- Predictions<br/>- Rating UI]
        AP[Admin Portal<br/>- Survey Builder<br/>- Model Config<br/>- Dashboard]
    end

    subgraph BackendLayer["🟩 BACKEND LAYER (Node.js + Express)"]
        direction TB

        subgraph SurveyServices["Survey Services"]
            SM[Survey Management<br/>- Store templates<br/>- Retrieve surveys<br/>- Store responses<br/>- Version tracking]
            PWRS_CALC[PWRS Calculator<br/>- Priority weighting<br/>- Success rate calc<br/>- Normalization]
        end

        subgraph TrainingServices["Training Services"]
            TRB[Training Request Builder<br/>- Query training data<br/>- Format for ML<br/>- Enrollment count check]
            FBL[Feedback Loop Logic<br/>- Rating threshold<br/>- Pseudo-label creation<br/>- Target survey routing]
        end

        subgraph APIEndpoints["API Endpoints"]
            API_SURVEY["/api/surveys<br/>GET, POST"]
            API_PREDICT["/api/predict<br/>POST"]
            API_TRAIN["/api/train<br/>POST"]
            API_FEEDBACK["/api/feedback<br/>POST"]
        end
    end

    subgraph ModelServerLayer["🟨 MODEL SERVER (Python + Flask + TensorFlow)"]
        direction TB

        subgraph DataProcessing["Data Processing"]
            DN[Data Normalizer<br/>- Feature scaling (0-10)<br/>- Missing value handling<br/>- Categorical encoding]
            DV[Data Validator<br/>- Schema validation<br/>- Outlier detection<br/>- Quality checks]
        end

        subgraph PredictionServices["Prediction Services"]
            MS_SEL[Model Selector<br/>- Query enrollment count<br/>- Phase detection<br/>- Version loading]
            PE_KNN[KNN Prediction Engine<br/>- k=3 neighbors<br/>- Distance-weighted<br/>- Euclidean distance]
            PE_NN[NN Prediction Engine<br/>- Forward pass<br/>- Sigmoid output<br/>- Batch processing]
        end

        subgraph TrainingServices2["Training Services"]
            TQM[Training Queue Manager<br/>- Async job queue<br/>- FIFO scheduling<br/>- Status tracking]
            MV[Model Versioning<br/>- Performance tracking<br/>- Rollback support<br/>- Deployment logic]
        end

        subgraph ModelTrainers["Model Trainers"]
            KNN_TRAIN[KNN Trainer<br/>- Store samples<br/>- k=3, distance-weighted<br/>- 5-fold CV validation]

            GAN_TRAIN[GAN Trainer<br/>- Generator: Latent(100)→7<br/>- Discriminator: 7→Real/Fake<br/>- 100 real → 500 total<br/>- KS test validation]

            NN_TRAIN[NN Trainer<br/>- Architecture: 7→64→32→1<br/>- Train: 80% (real+synthetic)<br/>- Validate: 20% (REAL ONLY)<br/>- MSE loss, Adam optimizer]
        end
    end

    DB[(🟥 MongoDB<br/>Collections:<br/>- surveys<br/>- responses<br/>- pseudoLabels<br/>- models<br/>- trainingJobs)]

    %% ============================================
    %% PREDICTION FLOW (BOOTSTRAP PHASE: n=1-10)
    %% ============================================

    SP -->|1. Enroll + Factor Survey| API_SURVEY
    API_SURVEY -->|2. Store responses| SM
    SM -->|3. Retrieve Target Survey| SP
    SP -->|4. Complete Target Survey<br/>REQUIRED (bootstrap)| API_SURVEY
    API_SURVEY -->|5. Store Target responses| SM
    SM -->|6. Check enrollment| COUNT1{Enrollment<br/>Count ≥ 10?}
    COUNT1 -->|No| WAIT[Bootstrap Phase<br/>Wait for 10 students]
    COUNT1 -->|Yes| TRB

    %% ============================================
    %% PREDICTION FLOW (ACTIVE PHASE: n≥10)
    %% ============================================

    SP -->|1. Enroll + Factor Survey| API_SURVEY
    API_SURVEY -->|2. Store Factor responses| SM
    SM -->|3. Send to PWRS| PWRS_CALC
    PWRS_CALC -->|4. Normalize data| DN
    DN -->|5. Validate| DV
    DV -->|6. Select model| MS_SEL

    MS_SEL -->|7a. n=10-99: Use KNN| PE_KNN
    MS_SEL -->|7b. n≥100: Use NN if available| PE_NN

    PE_KNN -->|8. Raw prediction (0-1)| PWRS_CALC
    PE_NN -->|8. Raw prediction (0-1)| PWRS_CALC

    PWRS_CALC -->|9. Convert to success rate (0-100%)| API_PREDICT
    API_PREDICT -->|10. Display prediction + rating UI| SP

    SP -->|11. Student rates prediction| API_FEEDBACK
    API_FEEDBACK -->|12. Rating check| FBL

    FBL -->|13a. Rating ≥4<br/>Pseudo-label| PL_CREATE[Create Pseudo-label<br/>studentId, factors,<br/>predictedSuccess,<br/>isPseudoLabel=true, rating]
    FBL -->|13b. Rating <4<br/>Request correction| TS_REQUEST[Request Target Survey]

    PL_CREATE -->|14a. Store pseudo-label| SM
    TS_REQUEST -->|14b. Student completes Target| API_SURVEY
    API_SURVEY -->|14c. Store Target response| SM

    %% ============================================
    %% TRAINING FLOW
    %% ============================================

    AP -->|1. Create surveys| API_SURVEY
    API_SURVEY -->|2. Store templates| SM

    SM -->|3. Training trigger<br/>(manual or auto)| TRB
    TRB -->|4. Query training data| SM
    SM <-->|5. Retrieve from DB| DB

    TRB -->|6. Format training request| API_TRAIN
    API_TRAIN -->|7. Send to Model Server| TQM

    TQM -->|8. Add to job queue| PHASE_CHECK{Enrollment<br/>Count?}

    PHASE_CHECK -->|9a. 10 ≤ n < 100<br/>Phase 1| KNN_TRAIN
    PHASE_CHECK -->|9b. n ≥ 100<br/>Phase 2| GAN_TRAIN

    KNN_TRAIN -->|10a. Train KNN<br/>5-fold CV<br/>Calculate MAE, R²| KNN_MODEL[KNN Model<br/>+ Metrics]
    GAN_TRAIN -->|10b. Train GAN<br/>Generate 400 synthetic<br/>Validate: KS test| SYNTHETIC[400 Synthetic<br/>Students]

    SYNTHETIC -->|11. Input to NN| NN_TRAIN
    NN_TRAIN -->|12. Train NN<br/>100 real + 400 synthetic<br/>Validate on 20% REAL ONLY| NN_MODEL[NN Model<br/>+ Metrics]

    KNN_MODEL -->|13. Send to versioning| MV
    NN_MODEL -->|13. Send to versioning| MV

    MV -->|14. Performance check| COMPARE{New Model<br/>Better?}

    COMPARE -->|15a. Yes: new_MAE < old_MAE| DEPLOY[Deploy New Model<br/>Update Model Selector]
    COMPARE -->|15b. No| KEEP[Keep Current Model<br/>Log failure]

    DEPLOY -->|16. Store model + metadata| DB
    KEEP -->|16. Log training attempt| DB

    DB -.->|17. Model available| MS_SEL

    %% ============================================
    %% DATABASE CONNECTIONS
    %% ============================================

    SM <-->|Store/Retrieve| DB
    TRB <-->|Query Training Data| DB
    DN <-->|Feature Scaling Config| DB
    MS_SEL <-->|Load Model Versions| DB
    MV <-->|Store Models + Metadata| DB

    %% ============================================
    %% FUTURE WORK
    %% ============================================

    OpenAI[🟪 OpenAI API<br/>Future Work:<br/>- Conversational predictions<br/>- Chat-based surveys<br/>- Explanation generation<br/>- Natural language queries]
    OpenAI -.->|Integration point| SP

    %% ============================================
    %% STYLING
    %% ============================================

    classDef frontend fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    classDef backend fill:#50C878,stroke:#2E7D4E,stroke-width:2px,color:#fff
    classDef model fill:#F5A623,stroke:#C77F1B,stroke-width:2px,color:#fff
    classDef database fill:#E74C3C,stroke:#A93226,stroke-width:2px,color:#fff
    classDef decision fill:#E8E8E8,stroke:#7F8C8D,stroke-width:2px,color:#000
    classDef process fill:#AED6F1,stroke:#2874A6,stroke-width:2px,color:#000
    classDef future fill:#9B59B6,stroke:#6C3483,stroke-width:2px,color:#fff,stroke-dasharray: 5 5

    class SP,AP frontend
    class SM,PWRS_CALC,TRB,FBL,API_SURVEY,API_PREDICT,API_TRAIN,API_FEEDBACK backend
    class DN,DV,MS_SEL,PE_KNN,PE_NN,TQM,MV,KNN_TRAIN,GAN_TRAIN,NN_TRAIN model
    class DB database
    class COUNT1,PHASE_CHECK,COMPARE decision
    class WAIT,PL_CREATE,TS_REQUEST,KNN_MODEL,SYNTHETIC,NN_MODEL,DEPLOY,KEEP process
    class OpenAI future
```

---

## Complete System Flows

### Flow 1: Bootstrap Phase (Students 1-10)

**Objective**: Collect initial labeled data to train first KNN model

**Steps**:
1. **Student Enrollment**: Transfer student enrolls via Student Portal
2. **Factor Survey**: Complete 7-question Factor Survey (~4 min)
3. **API Call**: POST /api/surveys with Factor responses
4. **Backend Storage**: Survey Management stores in MongoDB `responses` collection
5. **Target Survey Required**: System retrieves Target Survey (bootstrap phase)
6. **Target Survey Completion**: Student completes Target Survey (~10 min)
7. **Target Storage**: Survey Management stores Target responses with success rate
8. **Enrollment Check**: Backend checks enrollment count
9. **Waiting State**: If count < 10, wait for more students
10. **Training Trigger**: Once count = 10, trigger training automatically

**Total Time per Student**: ~15 minutes (Factor 4 min + Target 10 min + enrollment 1 min)

**Data Collected**:
- 10 Factor Survey responses (features)
- 10 Target Survey responses (labels)
- 0 Pseudo-labels (feedback loop not active yet)

---

### Flow 2: Prediction Flow (Students 11+)

**Objective**: Generate predictions for new transfer students with intelligent feedback loop

**Steps**:
1. **Student Enrollment**: Transfer student enrolls via Student Portal
2. **Factor Survey Only**: Complete 7-question Factor Survey (~4 min)
3. **API Call**: POST /api/surveys with Factor responses
4. **Survey Management**: Store Factor responses in MongoDB
5. **PWRS Calculator**: Prepare data for prediction (normalize responses)
6. **Data Normalizer**: Convert features to 0-10 scale
   - Example: GPA 3.5/4.0 → 8.75/10, Hours worked 20/40 → 5.0/10
7. **Data Validator**: Check for missing values, outliers, schema compliance
8. **Model Selector**: Query enrollment count → Select KNN or NN
9. **Prediction Engine**:
   - **If KNN (n=10-99)**: Find k=3 nearest neighbors, distance-weighted average
   - **If NN (n≥100)**: Forward pass through trained neural network
10. **PWRS Calculator**: Convert raw prediction (0-1) to success rate (0-100%)
11. **API Response**: POST /api/predict returns success rate
12. **Display to Student**: "Your predicted success rate: 74%"
13. **Rating UI**: "How accurate is this prediction? ⭐⭐⭐⭐⭐"
14. **Student Rating**: Student selects star rating (1-5)
15. **API Call**: POST /api/feedback with rating
16. **Feedback Loop Logic**:
    - **Path A (Rating ≥4)**: High confidence
      - Create pseudo-label: `{studentId, factors, predictedSuccess: 74, isPseudoLabel: true, rating: 4.5}`
      - Store in MongoDB `pseudoLabels` collection
      - Add to training data queue
      - **Student done** (~5 min total)
    - **Path B (Rating <4)**: Low confidence
      - Request Target Survey for correction
      - Student completes Target Survey (~10 min)
      - Store actual success rate in `responses` collection
      - Add to training data queue
      - **Student done** (~15 min total)

**Expected Distribution**:
- 50-70% of students: Path A (pseudo-label, 5 min)
- 30-50% of students: Path B (Target Survey, 15 min)
- **Average time**: ~8-10 minutes per student (vs 15 min without feedback loop)

---

### Flow 3: Training Flow - Phase 1 (KNN, n=10-99)

**Objective**: Train KNN model for immediate predictions with small transfer student cohort

**Steps**:
1. **Admin Trigger**: Admin triggers training manually OR auto-trigger after 10 new students
2. **API Call**: POST /api/train
3. **Training Request Builder**:
   - Query MongoDB for training data:
     ```sql
     SELECT factorResponses, targetResponses FROM responses WHERE hasTarget = true
     UNION
     SELECT factorResponses, predictedSuccess FROM pseudoLabels WHERE rating >= 4.0
     ```
   - Check enrollment count: `SELECT COUNT(*) = 25 students`
   - Format training data:
     ```json
     {
       "studentCount": 25,
       "features": [[8,7,6,9,7,8,7], [6,8,7,5,9,7,8], ...],
       "labels": [74, 82, 65, ...],
       "phase": "KNN"
     }
     ```
4. **API Call to Model Server**: POST model-server/train
5. **Training Queue Manager**: Add job to async queue, status: "in_progress"
6. **KNN Trainer**:
   - Store all 25 labeled samples (lazy learning - no actual training)
   - Set hyperparameters: k=3, distance metric=Euclidean, weighting=distance-weighted
   - **Validation**: 5-fold cross-validation
     - Split data into 5 folds
     - Train on 4 folds (20 students), validate on 1 fold (5 students)
     - Repeat 5 times, average metrics
   - Calculate metrics: MAE, R², RMSE
   - Expected performance: MAE ~12-14, R² ~0.50
7. **Model Versioning**:
   - Store model metadata:
     ```json
     {
       "modelId": "knn-20260115-001",
       "phase": "KNN",
       "studentCount": 25,
       "MAE": 13.2,
       "R2": 0.52,
       "RMSE": 16.8,
       "trainingDate": "2026-01-15T14:00:00Z",
       "filePath": "/models/knn_samples_25.pkl"
     }
     ```
8. **Performance Comparison**: Compare to previous KNN model (if exists)
9. **Deployment**: If new model better OR first model → Deploy
10. **Model Selector Update**: Model Selector loads new KNN model
11. **Notification**: Training Queue Manager sends completion status to Backend

**Training Time**: ~2-5 minutes (most time spent on validation)

---

### Flow 4: Training Flow - Phase 2 (GAN, n=100+)

**Objective**: Generate synthetic transfer students to enable Neural Network training

**Steps**:
1. **Auto-Trigger**: When enrollment count reaches 100, auto-trigger GAN training
2. **Training Request Builder**: Query 100 real transfer students
3. **Training Queue Manager**: Add GAN training job to queue
4. **GAN Trainer**:
   - **Architecture**:
     - Generator: Input latent vector (100-dim) → Dense(128, ReLU) → Dense(64, ReLU) → Output(7 features)
     - Discriminator: Input features (7-dim) → Dense(64, ReLU) → Dense(32, ReLU) → Output(1, Sigmoid)
   - **Training Loop** (10,000 epochs or until convergence):
     - Step 1: Train Discriminator on real students (label=1) and fake students (label=0)
     - Step 2: Train Generator to fool Discriminator
     - Step 3: Repeat until Discriminator accuracy ~50% (Generator creates realistic students)
   - **Generation**: Use trained Generator to create 400 synthetic students
   - **Validation**:
     - **KS Test**: For each feature (7 features), run Kolmogorov-Smirnov test
       - Null hypothesis: Real and synthetic distributions are same
       - Acceptance criterion: p-value >0.05 for all features
     - **Correlation Similarity**: Compare correlation matrices
       - Real students: Calculate 7×7 correlation matrix
       - Synthetic students: Calculate 7×7 correlation matrix
       - Acceptance criterion: Difference <0.2 for all pairs
     - **Visual Inspection**: Plot distributions (histograms) for manual review
5. **Validation Results**:
   - If validation passes: Store 400 synthetic students, proceed to NN training
   - If validation fails: Retry GAN training with different hyperparameters (max 3 retries)
6. **Store Synthetic Data**: Save to MongoDB `syntheticData` collection

**Training Time**: ~30-60 minutes (depends on convergence)

---

### Flow 5: Training Flow - Phase 3 (Neural Network, n=100+)

**Objective**: Train Neural Network on augmented dataset for improved prediction accuracy

**Steps**:
1. **Input Data**: 100 real transfer students + 400 synthetic students = 500 total
2. **Data Split**:
   - **Training Set** (80% = 400 students): 80 real + 320 synthetic
   - **Validation Set** (20% = 100 students): 20 real + 0 synthetic ← **CRITICAL**
3. **NN Trainer**:
   - **Architecture**:
     - Input layer: 7 features (normalized Factor Survey responses)
     - Hidden layer 1: 64 neurons, ReLU activation, He initialization
     - Dropout layer: 0.3 (prevent overfitting to synthetic data)
     - Hidden layer 2: 32 neurons, ReLU activation, He initialization
     - Output layer: 1 neuron, Sigmoid activation (0-1 prediction)
   - **Training Configuration**:
     - Loss function: Mean Squared Error (MSE)
     - Optimizer: Adam (learning rate: 0.001, beta1: 0.9, beta2: 0.999)
     - Batch size: 32
     - Epochs: 100 (with early stopping)
     - Early stopping: Patience=10, monitor=validation_loss
   - **Training Loop**:
     - Epoch 1-100:
       - Forward pass on training set (80 real + 320 synthetic)
       - Calculate loss (MSE between predicted and actual success rates)
       - Backpropagation + weight updates (Adam optimizer)
       - Validation pass on **REAL students only** (20 students)
       - If validation loss doesn't improve for 10 epochs → Stop early
   - **Validation Metrics** (on 20 REAL students):
     - MAE (Mean Absolute Error): Target <10
     - R² (Coefficient of Determination): Target >0.60
     - RMSE (Root Mean Squared Error): Target <13
4. **Model Versioning**:
   - Store trained NN model + metadata:
     ```json
     {
       "modelId": "nn-20260615-001",
       "phase": "NN",
       "studentCount": 100,
       "syntheticCount": 400,
       "MAE": 8.7,
       "R2": 0.73,
       "RMSE": 11.2,
       "trainingDate": "2026-06-15T10:00:00Z",
       "architecture": "7-64-32-1",
       "filePath": "/models/nn_100real_400synthetic.h5"
     }
     ```
5. **Performance Comparison**: Compare NN metrics to current KNN metrics
   - Load current KNN: MAE=12.5, R²=0.55
   - New NN: MAE=8.7, R²=0.73
   - Decision: NN is better (lower MAE, higher R²) → Deploy NN
6. **Deployment**: Model Selector switches from KNN to NN
7. **A/B Testing** (optional): Run both models in parallel, track user satisfaction

**Training Time**: ~10-20 minutes (depends on early stopping)

---

## Component Specifications

### Backend API Endpoints

#### POST /api/surveys
**Purpose**: Store survey responses (Factor, Target, or both)

**Request Body**:
```json
{
  "studentId": "12345",
  "surveyType": "factor",
  "responses": [8, 7, 6, 9, 7, 8, 7],
  "timestamp": "2026-01-15T10:30:00Z"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Survey response stored",
  "nextAction": "predict" // or "target_survey" if bootstrap phase
}
```

**Error Handling**:
- 400: Invalid survey data (schema validation failed)
- 409: Duplicate submission (student already completed this survey)
- 500: Database error

---

#### POST /api/predict
**Purpose**: Generate success rate prediction for a student

**Request Body**:
```json
{
  "studentId": "12345",
  "features": [8, 7, 6, 9, 7, 8, 7]
}
```

**Response**:
```json
{
  "success": true,
  "prediction": {
    "successRate": 74,
    "confidence": 0.82,
    "similarStudents": [3, 7, 12],
    "modelUsed": "KNN",
    "modelVersion": "knn-20260115-001"
  }
}
```

**Error Handling**:
- 400: Invalid feature data
- 503: Model not ready (bootstrap phase, count <10)
- 500: Prediction error

---

#### POST /api/feedback
**Purpose**: Process student rating and apply feedback loop logic

**Request Body**:
```json
{
  "studentId": "12345",
  "predictionId": "pred-20260115-123",
  "rating": 4.5,
  "comment": "Seems accurate for my situation" // optional
}
```

**Response (Rating ≥4)**:
```json
{
  "success": true,
  "action": "pseudo_label_created",
  "message": "Thank you! Your prediction has been added to training data.",
  "surveyComplete": true
}
```

**Response (Rating <4)**:
```json
{
  "success": true,
  "action": "target_survey_requested",
  "message": "Please complete the Target Survey for a more accurate prediction.",
  "targetSurveyUrl": "/surveys/target",
  "surveyComplete": false
}
```

---

#### POST /api/train
**Purpose**: Trigger model training (manual or auto-triggered)

**Request Body**:
```json
{
  "trigger": "auto", // or "manual"
  "requestedBy": "admin@neiu.edu" // if manual
}
```

**Response**:
```json
{
  "success": true,
  "jobId": "train-20260115-001",
  "status": "queued",
  "estimatedTime": "5 minutes",
  "phase": "KNN" // or "GAN", "NN"
}
```

**Error Handling**:
- 400: Insufficient data (count <10)
- 409: Training already in progress
- 500: Training queue error

---

### Model Server API Endpoints

#### POST /train
**Purpose**: Train KNN, GAN, or NN model

**Request Body**:
```json
{
  "studentCount": 25,
  "features": [[8,7,6,9,7,8,7], [6,8,7,5,9,7,8], ...],
  "labels": [74, 82, 65, ...],
  "phase": "KNN", // or "GAN", "NN"
  "requestId": "train-20260115-001"
}
```

**Response**:
```json
{
  "success": true,
  "jobId": "train-20260115-001",
  "status": "completed",
  "metrics": {
    "MAE": 13.2,
    "R2": 0.52,
    "RMSE": 16.8
  },
  "modelId": "knn-20260115-001"
}
```

---

#### POST /predict
**Purpose**: Generate prediction using trained model

**Request Body**:
```json
{
  "features": [8, 7, 6, 9, 7, 8, 7],
  "modelId": "knn-20260115-001" // optional, uses latest if not specified
}
```

**Response**:
```json
{
  "prediction": 0.74, // raw prediction (0-1 scale)
  "confidence": 0.82,
  "modelUsed": "KNN",
  "modelVersion": "knn-20260115-001",
  "nearestNeighbors": [3, 7, 12] // if KNN
}
```

---

## Database Schema

### MongoDB Collections

#### surveys
```json
{
  "_id": "survey-001",
  "surveyType": "factor", // or "target"
  "version": "1.0",
  "questions": [
    {
      "id": "q1",
      "text": "What is your expected GPA?",
      "type": "slider",
      "min": 0,
      "max": 4.0,
      "priority": 10
    },
    ...
  ],
  "createdBy": "admin@neiu.edu",
  "createdAt": "2025-11-01T00:00:00Z"
}
```

#### responses
```json
{
  "_id": "resp-001",
  "studentId": "12345",
  "surveyId": "survey-001",
  "surveyType": "factor",
  "responses": [8, 7, 6, 9, 7, 8, 7],
  "timestamp": "2026-01-15T10:30:00Z",
  "hasTarget": true, // or false
  "targetSuccessRate": 74 // if hasTarget = true
}
```

#### pseudoLabels
```json
{
  "_id": "pseudo-001",
  "studentId": "12345",
  "predictionId": "pred-001",
  "factorResponses": [8, 7, 6, 9, 7, 8, 7],
  "predictedSuccess": 74,
  "rating": 4.5,
  "isPseudoLabel": true,
  "timestamp": "2026-01-15T10:35:00Z",
  "modelUsed": "knn-20260115-001"
}
```

#### models
```json
{
  "_id": "model-001",
  "modelId": "knn-20260115-001",
  "phase": "KNN", // or "GAN", "NN"
  "studentCount": 25,
  "syntheticCount": 0, // 400 for NN
  "MAE": 13.2,
  "R2": 0.52,
  "RMSE": 16.8,
  "trainingDate": "2026-01-15T14:00:00Z",
  "filePath": "/models/knn_samples_25.pkl",
  "isActive": true,
  "deployedAt": "2026-01-15T14:10:00Z"
}
```

#### trainingJobs
```json
{
  "_id": "job-001",
  "jobId": "train-20260115-001",
  "phase": "KNN",
  "status": "completed", // or "in_progress", "failed"
  "studentCount": 25,
  "startTime": "2026-01-15T14:00:00Z",
  "endTime": "2026-01-15T14:05:00Z",
  "resultModelId": "knn-20260115-001",
  "error": null
}
```

---

## Key Metrics Tracking

### System Performance Metrics
- **Pseudo-label Rate**: % of students with rating ≥4 (target: 50-70%)
- **Average Survey Time**: Factor + Target + Rating (target: <10 min)
- **Survey Completion Rate**: % of students who complete all required surveys (target: >85%)
- **Missing Data Rate**: % of survey questions left blank (target: <5%)

### Model Performance Metrics
- **MAE (Mean Absolute Error)**: Average prediction error in percentage points
  - KNN target: <15
  - NN target: <10
- **R² (Coefficient of Determination)**: Variance explained by model
  - KNN target: >0.40
  - NN target: >0.60
- **RMSE (Root Mean Squared Error)**: Penalizes large errors more than MAE
  - KNN target: <18
  - NN target: <13

### User Satisfaction Metrics
- **Average Prediction Rating**: 1-5 stars (target: >3.5)
- **Rating Distribution**: Track % of 1★, 2★, 3★, 4★, 5★
- **User Comments**: Qualitative feedback on prediction accuracy

---

## Speaking Points

**For Presentation**:

> "This comprehensive diagram shows the entire ACOSUS system architecture. The frontend provides student and admin portals. The backend layer contains survey services, training services, and API endpoints. The model server handles all machine learning operations."

> "Notice three distinct flows: Bootstrap phase for the first 10 transfer students requires both Factor and Target surveys. Prediction phase for students 11+ uses the intelligent feedback loop - high ratings create pseudo-labels, low ratings request Target Survey corrections."

> "The training flow implements progressive learning: At 10-99 students, we train KNN using 5-fold cross-validation. At 100+ students, we activate GAN-based data augmentation to generate 400 synthetic students, then train a Neural Network validated ONLY on real transfer students."

> "MongoDB serves as the central data hub with five collections: surveys for templates, responses for actual data, pseudoLabels for high-confidence predictions, models for versioning, and trainingJobs for queue management."

> "The system tracks comprehensive metrics: Pseudo-label rate to measure feedback loop effectiveness, model performance metrics (MAE, R², RMSE) for validation, and user satisfaction metrics (ratings, completion rates) for continuous improvement."

---

**Complexity**: High (2-3 slides or reference document)
**Audience**: Comprehensive technical documentation, thesis appendix, detailed Q&A
**Estimated Presentation Time**: 15-20 minutes (if presenting all details)
