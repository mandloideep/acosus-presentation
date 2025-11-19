# Detailed Architecture - Separate Diagrams

**Purpose**: Two exhaustive standalone diagrams for prediction and training workflows with complete technical specifications.

**Use Case**: Thesis appendix, comprehensive technical documentation, detailed code implementation reference.

---

## Usage Notes

These diagrams are **maximally detailed** and intended for:
- **Thesis Appendix**: Complete technical reference
- **Developer Documentation**: Implementation guide for future development
- **Code Review**: Validation of current implementation
- **Q&A Deep Dive**: Answer highly technical committee questions

For presentation slides, consider using **Diagram 08 (Side-by-Side)** instead for better visual flow.

---

## Diagram 1: Prediction Workflow (Exhaustive Detail)

```mermaid
graph TB
    START([Transfer Student<br/>Visits System]) --> LANDING[Landing Page<br/>acosus.neiu.edu]

    LANDING --> AUTH{Authenticated?}
    AUTH -->|No| LOGIN[Login/Register<br/>Student Portal]
    AUTH -->|Yes| DASHBOARD[Student Dashboard]

    LOGIN --> ENROLL_CHECK{Already<br/>Enrolled?}
    ENROLL_CHECK -->|No| ENROLL_FORM[Enrollment Form]
    ENROLL_CHECK -->|Yes| DASHBOARD

    subgraph EnrollmentProcess["Enrollment Process"]
        ENROLL_FORM --> ENROLL_DATA[Collect Data:<br/>- Name, Email, Student ID<br/>- Previous institution<br/>- Transfer credits<br/>- GPA from previous institution<br/>- Major/Program]

        ENROLL_DATA --> ENROLL_SUBMIT[POST /api/enrollment]

        ENROLL_SUBMIT --> ENROLL_STORE[Backend: Store in MongoDB<br/>Collection: students]

        ENROLL_STORE --> COUNT_CHECK[Backend: Check Enrollment Count<br/>SELECT COUNT(*) FROM students]
    end

    COUNT_CHECK --> PHASE{Bootstrap<br/>Phase?}

    PHASE -->|Yes: n<10| BOOTSTRAP_PATH[BOOTSTRAP PATH<br/>Both surveys required]
    PHASE -->|No: n≥10| PREDICTION_PATH[PREDICTION PATH<br/>Factor + Feedback loop]

    subgraph BootstrapPath["Bootstrap Path (Students 1-10)"]
        BOOTSTRAP_PATH --> BS_FACTOR[Retrieve Factor Survey<br/>Backend: GET /api/surveys/factor]

        BS_FACTOR --> BS_FACTOR_UI[Display Factor Survey<br/>7 Questions, ~4 min]

        BS_FACTOR_UI --> BS_FACTOR_RESPONSES[Student Completes Factor Survey:<br/>Q1: GPA expectation (slider 0-4.0)<br/>Q2: Course difficulty (Likert 1-10)<br/>Q3: Work hours (slider 0-40)<br/>Q4: Commute time (slider 0-120 min)<br/>Q5: Family support (Likert 1-10)<br/>Q6: Career clarity (Likert 1-10)<br/>Q7: Transfer readiness (Likert 1-10)]

        BS_FACTOR_RESPONSES --> BS_FACTOR_SUBMIT[POST /api/surveys<br/>Submit Factor Responses]

        BS_FACTOR_SUBMIT --> BS_FACTOR_STORE[Backend: Survey Management<br/>Store in MongoDB responses collection<br/>Document: studentId, surveyType=factor,<br/>responses, timestamp]

        BS_FACTOR_STORE --> BS_TARGET_REQ[Backend: Immediately Request Target Survey<br/>No prediction (model not ready)]

        BS_TARGET_REQ --> BS_TARGET_UI[Display Target Survey<br/>5-10 Questions, ~10 min]

        BS_TARGET_UI --> BS_TARGET_RESPONSES[Student Completes Target Survey:<br/>Q1: Expected first semester GPA<br/>Q2: Confidence in on-time completion<br/>Q3: Career readiness expectation<br/>Q4: Financial stability<br/>Q5-10: Additional success indicators]

        BS_TARGET_RESPONSES --> BS_TARGET_SUBMIT[POST /api/surveys<br/>Submit Target Responses]

        BS_TARGET_SUBMIT --> BS_PWRS[Backend: PWRS Calculator<br/>Apply priority weights to responses<br/>Formula: Σ(priority_i × response_i) / Σ(priority_i)]

        BS_PWRS --> BS_SUCCESS[Calculate Success Rate<br/>Example: 72%]

        BS_SUCCESS --> BS_STORE[Backend: Update responses document<br/>Add targetSuccessRate, hasTarget=true]

        BS_STORE --> BS_COUNT_UPDATE[Update enrollment count<br/>Labeled students: n+1]

        BS_COUNT_UPDATE --> BS_CHECK_10{Count = 10?}

        BS_CHECK_10 -->|Yes| BS_TRIGGER_TRAIN[Auto-Trigger KNN Training<br/>POST /api/train]
        BS_CHECK_10 -->|No| BS_WAIT[Wait for more students<br/>Display: "Thank you! Survey complete.<br/>Predictions available after 10 students enroll."]

        BS_TRIGGER_TRAIN --> BS_COMPLETE[Bootstrap Phase Complete<br/>Display: "Thank you!<br/>You're one of the first 10 transfer students.<br/>Model training will begin shortly."]
    end

    subgraph PredictionPath["Prediction Path (Students 11+)"]
        PREDICTION_PATH --> PRED_FACTOR[Retrieve Factor Survey<br/>Backend: GET /api/surveys/factor]

        PRED_FACTOR --> PRED_FACTOR_UI[Display Factor Survey<br/>Same 7 questions as bootstrap]

        PRED_FACTOR_UI --> PRED_RESPONSES[Student Completes Factor Survey<br/>Example responses:<br/>[3.5, 7, 15, 30, 9, 8, 7]]

        PRED_RESPONSES --> PRED_SUBMIT[POST /api/surveys<br/>Submit Factor Responses]

        PRED_SUBMIT --> PRED_STORE[Backend: Survey Management<br/>Store in MongoDB responses collection]

        PRED_STORE --> PRED_PREP[Backend: Prepare for Prediction<br/>Extract responses: [3.5, 7, 15, 30, 9, 8, 7]]

        PRED_PREP --> PRED_NORMALIZE_REQ[POST model-server/predict<br/>Send raw responses to Model Server]

        subgraph ModelServerPrediction["Model Server - Prediction Pipeline"]
            PRED_NORMALIZE_REQ --> MN_NORMALIZE[Data Normalizer<br/>Feature Scaling to 0-10]

            MN_NORMALIZE --> MN_STEPS[Normalization Steps:<br/>- GPA: (3.5/4.0)×10 = 8.75<br/>- Difficulty: 7.0 (already 0-10)<br/>- Hours: (15/40)×10 = 3.75<br/>- Commute: (30/120)×10 = 2.5<br/>- Family: 9.0 (already 0-10)<br/>- Career: 8.0 (already 0-10)<br/>- Readiness: 7.0 (already 0-10)]

            MN_STEPS --> MN_VECTOR[Normalized Vector:<br/>[8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]]

            MN_VECTOR --> MV_VALIDATE[Data Validator<br/>- Schema check ✓<br/>- Range check (all 0-10) ✓<br/>- Missing values check ✓<br/>- Outlier detection ✓]

            MV_VALIDATE --> MS_SELECT[Model Selector<br/>Query MongoDB: enrollment count]

            MS_SELECT --> MS_QUERY[MongoDB Query:<br/>SELECT COUNT(*) FROM responses<br/>WHERE hasTarget=true OR isPseudoLabel=true<br/>Result: 45 students]

            MS_QUERY --> MS_DECISION{Count?}

            MS_DECISION -->|10≤n<100<br/>Use KNN| MS_KNN_LOAD[Load KNN Model<br/>Query: SELECT * FROM models<br/>WHERE phase='KNN' AND isActive=true<br/>Result: knn-20260115-001]

            MS_DECISION -->|n≥100<br/>Check NN| MS_NN_CHECK{NN Model<br/>Available?}

            MS_NN_CHECK -->|Yes| MS_NN_LOAD[Load NN Model<br/>Query: SELECT * FROM models<br/>WHERE phase='NN' AND isActive=true<br/>Result: nn-20260615-001]

            MS_NN_CHECK -->|No| MS_KNN_FALLBACK[Fallback to KNN<br/>Load latest KNN model]

            MS_KNN_LOAD --> PE_KNN[KNN Prediction Engine]
            MS_NN_LOAD --> PE_NN[NN Prediction Engine]
            MS_KNN_FALLBACK --> PE_KNN

            subgraph KNNPrediction["KNN Inference (if n=10-99)"]
                PE_KNN --> KNN_LOAD_SAMPLES[Load Training Samples<br/>Query: All labeled students<br/>Count: 45 students]

                KNN_LOAD_SAMPLES --> KNN_DISTANCE[Calculate Euclidean Distance<br/>From new student to all 45 students<br/>Formula: sqrt(Σ(feature_i - sample_i)²)]

                KNN_DISTANCE --> KNN_SORT[Sort by Distance<br/>Find k=3 nearest neighbors]

                KNN_SORT --> KNN_NEIGHBORS[Nearest Neighbors Found:<br/>- Student #3: Distance=1.2, Success=78%<br/>- Student #7: Distance=1.5, Success=72%<br/>- Student #12: Distance=1.8, Success=70%]

                KNN_NEIGHBORS --> KNN_WEIGHTS[Calculate Distance Weights:<br/>w1 = 1/1.2 = 0.833<br/>w2 = 1/1.5 = 0.667<br/>w3 = 1/1.8 = 0.556<br/>Total weight: 2.056]

                KNN_WEIGHTS --> KNN_PREDICT[Weighted Average Prediction:<br/>(0.833×78 + 0.667×72 + 0.556×70) / 2.056<br/>= 73.96 ≈ 74%]

                KNN_PREDICT --> KNN_CONF[Calculate Confidence:<br/>Based on neighbor similarity<br/>Confidence = 0.82]

                KNN_CONF --> KNN_OUTPUT[KNN Output:<br/>Prediction: 0.74 (0-1 scale)<br/>Confidence: 0.82<br/>Similar students: [3, 7, 12]]
            end

            subgraph NNPrediction["NN Inference (if n≥100)"]
                PE_NN --> NN_LOAD_MODEL[Load Trained NN Model<br/>File: nn_100real_400synthetic.h5<br/>Architecture: 7→64→32→1]

                NN_LOAD_MODEL --> NN_INPUT[Input Layer<br/>7 features (normalized)]

                NN_INPUT --> NN_HIDDEN1[Hidden Layer 1<br/>64 neurons, ReLU activation<br/>Weights loaded from trained model]

                NN_HIDDEN1 --> NN_DROPOUT[Dropout Layer<br/>0.3 probability (inference: disabled)]

                NN_DROPOUT --> NN_HIDDEN2[Hidden Layer 2<br/>32 neurons, ReLU activation]

                NN_HIDDEN2 --> NN_OUTPUT_LAYER[Output Layer<br/>1 neuron, Sigmoid activation<br/>Raw output: 0.76]

                NN_OUTPUT_LAYER --> NN_CONF[Confidence Estimation<br/>Based on training history<br/>Confidence: 0.88]

                NN_CONF --> NN_OUTPUT[NN Output:<br/>Prediction: 0.76 (0-1 scale)<br/>Confidence: 0.88<br/>Model: nn-20260615-001]
            end

            KNN_OUTPUT --> PRED_RAW[Raw Prediction<br/>0-1 Scale]
            NN_OUTPUT --> PRED_RAW
        end

        PRED_RAW --> PRED_CONVERT[Backend: PWRS Calculator<br/>Convert to Success Rate<br/>0.74 → 74% or 0.76 → 76%]

        PRED_CONVERT --> PRED_DISPLAY[Display Prediction to Student<br/>---<br/>Your Predicted Success Rate: 74%<br/><br/>This prediction is based on transfer students similar to you:<br/>- Student #3 (78%) - Similar academic profile<br/>- Student #7 (72%) - Similar motivation<br/>- Student #12 (70%) - Similar resources<br/><br/>Confidence: 82% ████████▒▒<br/><br/>Model: KNN trained on 45 transfer students]

        PRED_DISPLAY --> PRED_RATE_UI[Rating Interface<br/>---<br/>How accurate do you think this prediction is for you?<br/>⭐⭐⭐⭐⭐<br/><br/>Your feedback helps improve predictions<br/>for future transfer students.]

        PRED_RATE_UI --> PRED_RATING[Student Selects Rating<br/>Scale: 1-5 stars]

        PRED_RATING --> PRED_FEEDBACK_SUBMIT[POST /api/feedback<br/>Submit rating + optional comment]

        subgraph FeedbackLoop["Feedback Loop Logic"]
            PRED_FEEDBACK_SUBMIT --> FBL_RECEIVE[Backend: Receive Feedback<br/>Extract: studentId, predictionId, rating, comment]

            FBL_RECEIVE --> FBL_THRESHOLD{Rating ≥ 4.0?}

            FBL_THRESHOLD -->|Yes: High Confidence| FBL_PSEUDO[Create Pseudo-label<br/>---<br/>Document Structure:<br/>{<br/>  studentId: "12345",<br/>  predictionId: "pred-001",<br/>  factorResponses: [8.75,7.0,3.75,2.5,9.0,8.0,7.0],<br/>  predictedSuccess: 74,<br/>  isPseudoLabel: true,<br/>  rating: 4.5,<br/>  comment: "Seems accurate",<br/>  modelUsed: "knn-20260115-001",<br/>  timestamp: "2026-01-15T10:35:00Z"<br/>}]

            FBL_PSEUDO --> FBL_STORE_PSEUDO[Store in MongoDB<br/>Collection: pseudoLabels<br/>Indexed on: studentId, isPseudoLabel]

            FBL_STORE_PSEUDO --> FBL_QUEUE_PSEUDO[Add to Training Queue<br/>Will be included in next training cycle]

            FBL_QUEUE_PSEUDO --> FBL_RESPONSE_PSEUDO[Response to Student:<br/>---<br/>✓ Thank you for your feedback!<br/><br/>Your prediction has been added to our training data<br/>to improve accuracy for future transfer students.<br/><br/>Your survey is complete.<br/>Check your email for next steps.]

            FBL_THRESHOLD -->|No: Low Confidence| FBL_TARGET_REQ[Request Target Survey<br/>---<br/>Response to Student:<br/>"Thanks for your feedback!<br/>To provide a more accurate prediction,<br/>please complete a brief Target Survey (5-10 questions, ~10 min)."]

            FBL_TARGET_REQ --> FBL_TARGET_UI[Display Target Survey<br/>Same questions as bootstrap path]

            FBL_TARGET_UI --> FBL_TARGET_COMPLETE[Student Completes Target Survey<br/>Responses: [...]

            FBL_TARGET_COMPLETE --> FBL_TARGET_SUBMIT[POST /api/surveys/target<br/>Submit Target responses]

            FBL_TARGET_SUBMIT --> FBL_PWRS[Backend: PWRS Calculator<br/>Calculate actual success rate<br/>Result: 71%]

            FBL_PWRS --> FBL_ERROR[Calculate Prediction Error<br/>Predicted: 74%, Actual: 71%<br/>Error: 3 percentage points]

            FBL_ERROR --> FBL_STORE_TARGET[Store in MongoDB responses<br/>Update document:<br/>Add targetSuccessRate: 71,<br/>hasTarget: true,<br/>predictionError: 3]

            FBL_STORE_TARGET --> FBL_QUEUE_TARGET[Add to Training Queue<br/>Correction helps improve model]

            FBL_QUEUE_TARGET --> FBL_RESPONSE_TARGET[Response to Student:<br/>---<br/>✓ Thank you for completing the Target Survey!<br/><br/>Your actual success expectation (71%) vs predicted (74%)<br/>helps us improve accuracy for future transfer students.<br/><br/>Your survey is complete.]
        end
    end

    DASHBOARD --> VIEW_HISTORY[View Previous Predictions<br/>Survey History<br/>Recommendations (future)]

    FBL_RESPONSE_PSEUDO --> END([Survey Complete])
    FBL_RESPONSE_TARGET --> END
    BS_COMPLETE --> END
    BS_WAIT --> END

    %% Future Work
    OPENAI_PRED[🟪 OpenAI API Integration<br/>Future Enhancements:<br/>- Conversational predictions<br/>  ("Why is my prediction 74%?")<br/>- Explanation generation<br/>  ("Based on your GPA and motivation...")<br/>- Chat-based surveys<br/>  (Natural language instead of forms)<br/>- Personalized recommendations]
    OPENAI_PRED -.-> PRED_DISPLAY

    %% Metrics Tracking
    METRICS_TRACK[System Metrics Tracking<br/>---<br/>Pseudo-label rate: % rating ≥4<br/>Target: 50-70%<br/><br/>Average survey time:<br/>- High confidence: ~5 min<br/>- Low confidence: ~15 min<br/>Target average: <10 min<br/><br/>Survey completion rate: >85%<br/>Missing data rate: <5%<br/><br/>Average prediction rating: >3.5/5.0]
    FBL_STORE_PSEUDO -.-> METRICS_TRACK
    FBL_STORE_TARGET -.-> METRICS_TRACK

    %% Database
    DB_PRED[(MongoDB Collections:<br/>---<br/>students:<br/>  {studentId, name, email, enrollmentDate,<br/>   previousInstitution, transferCredits}<br/><br/>responses:<br/>  {studentId, surveyType, responses,<br/>   targetSuccessRate, hasTarget, timestamp}<br/><br/>pseudoLabels:<br/>  {studentId, factorResponses, predictedSuccess,<br/>   isPseudoLabel, rating, modelUsed, timestamp}<br/><br/>surveys:<br/>  {surveyId, surveyType, version, questions}<br/><br/>predictions:<br/>  {predictionId, studentId, successRate,<br/>   confidence, modelUsed, timestamp})]

    ENROLL_STORE -.-> DB_PRED
    BS_FACTOR_STORE -.-> DB_PRED
    BS_STORE -.-> DB_PRED
    PRED_STORE -.-> DB_PRED
    FBL_STORE_PSEUDO -.-> DB_PRED
    FBL_STORE_TARGET -.-> DB_PRED
    MS_QUERY -.-> DB_PRED

    classDef frontend fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    classDef backend fill:#50C878,stroke:#2E7D4E,stroke-width:2px,color:#fff
    classDef model fill:#F5A623,stroke:#C77F1B,stroke-width:2px,color:#fff
    classDef decision fill:#E8E8E8,stroke:#7F8C8D,stroke-width:2px,color:#000
    classDef database fill:#E74C3C,stroke:#A93226,stroke-width:2px,color:#fff
    classDef process fill:#AED6F1,stroke:#2874A6,stroke-width:2px,color:#000
    classDef annotation fill:#FCF3CF,stroke:#F39C12,stroke-width:2px,color:#000
    classDef future fill:#9B59B6,stroke:#6C3483,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
    classDef knn fill:#D5F4E6,stroke:#27AE60,stroke-width:2px,color:#000
    classDef nn fill:#FADBD8,stroke:#E74C3C,stroke-width:2px,color:#000

    class START,LANDING,LOGIN,ENROLL_FORM,ENROLL_DATA,DASHBOARD,VIEW_HISTORY,BS_FACTOR_UI,BS_FACTOR_RESPONSES,BS_TARGET_UI,BS_TARGET_RESPONSES,PRED_FACTOR_UI,PRED_RESPONSES,PRED_DISPLAY,PRED_RATE_UI,PRED_RATING,FBL_TARGET_UI,FBL_TARGET_COMPLETE frontend
    class ENROLL_SUBMIT,ENROLL_STORE,COUNT_CHECK,BS_FACTOR,BS_FACTOR_SUBMIT,BS_FACTOR_STORE,BS_TARGET_REQ,BS_TARGET_SUBMIT,BS_PWRS,BS_SUCCESS,BS_STORE,BS_COUNT_UPDATE,PRED_FACTOR,PRED_SUBMIT,PRED_STORE,PRED_PREP,PRED_CONVERT,FBL_RECEIVE,FBL_PSEUDO,FBL_STORE_PSEUDO,FBL_QUEUE_PSEUDO,FBL_TARGET_REQ,FBL_TARGET_SUBMIT,FBL_PWRS,FBL_ERROR,FBL_STORE_TARGET,FBL_QUEUE_TARGET backend
    class MN_NORMALIZE,MN_STEPS,MN_VECTOR,MV_VALIDATE,MS_SELECT,MS_QUERY,MS_KNN_LOAD,MS_NN_LOAD,MS_KNN_FALLBACK,PRED_RAW model
    class KNN_LOAD_SAMPLES,KNN_DISTANCE,KNN_SORT,KNN_NEIGHBORS,KNN_WEIGHTS,KNN_PREDICT,KNN_CONF,KNN_OUTPUT knn
    class NN_LOAD_MODEL,NN_INPUT,NN_HIDDEN1,NN_DROPOUT,NN_HIDDEN2,NN_OUTPUT_LAYER,NN_CONF,NN_OUTPUT nn
    class AUTH,ENROLL_CHECK,PHASE,BS_CHECK_10,MS_DECISION,MS_NN_CHECK,FBL_THRESHOLD decision
    class DB_PRED database
    class BOOTSTRAP_PATH,PREDICTION_PATH,BS_TRIGGER_TRAIN,BS_COMPLETE,BS_WAIT,PRED_NORMALIZE_REQ,FBL_RESPONSE_PSEUDO,FBL_RESPONSE_TARGET,END process
    class OPENAI_PRED,METRICS_TRACK annotation
    class OPENAI_PRED future
```

---

## Diagram 1: Key Technical Specifications

### API Endpoints

#### POST /api/enrollment
**Request Body**:
```json
{
  "name": "John Doe",
  "email": "jdoe@student.neiu.edu",
  "studentId": "12345",
  "previousInstitution": "Harold Washington College",
  "transferCredits": 45,
  "previousGPA": 3.2,
  "major": "Computer Science"
}
```

**Response**:
```json
{
  "success": true,
  "studentId": "12345",
  "nextStep": "factor_survey",
  "surveyUrl": "/surveys/factor"
}
```

---

#### POST /api/surveys
**Request Body** (Factor Survey):
```json
{
  "studentId": "12345",
  "surveyType": "factor",
  "responses": [3.5, 7, 15, 30, 9, 8, 7],
  "timestamp": "2026-01-15T10:30:00Z"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Factor survey stored",
  "nextAction": "predict"  // or "target_survey" if bootstrap
}
```

---

#### POST /api/predict
**Request Body**:
```json
{
  "studentId": "12345"
}
```

**Response**:
```json
{
  "success": true,
  "prediction": {
    "successRate": 74,
    "confidence": 0.82,
    "modelUsed": "KNN",
    "modelVersion": "knn-20260115-001",
    "similarStudents": [
      {"id": 3, "successRate": 78, "similarity": 0.95},
      {"id": 7, "successRate": 72, "similarity": 0.89},
      {"id": 12, "successRate": 70, "similarity": 0.85}
    ]
  },
  "predictionId": "pred-001"
}
```

---

#### POST /api/feedback
**Request Body**:
```json
{
  "studentId": "12345",
  "predictionId": "pred-001",
  "rating": 4.5,
  "comment": "Seems accurate for my situation"
}
```

**Response** (if rating ≥4):
```json
{
  "success": true,
  "action": "pseudo_label_created",
  "message": "Thank you! Your prediction has been added to training data.",
  "surveyComplete": true
}
```

**Response** (if rating <4):
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

### Data Normalization Logic

**Feature Scaling to 0-10 Range**:

```python
def normalize_feature(value, feature_type):
    if feature_type == "GPA":
        # GPA: 0-4.0 → 0-10
        return (value / 4.0) * 10

    elif feature_type == "HOURS":
        # Work hours: 0-40 → 0-10
        return (value / 40.0) * 10

    elif feature_type == "COMMUTE":
        # Commute time: 0-120 minutes → 0-10
        return (value / 120.0) * 10

    elif feature_type == "LIKERT":
        # Likert scale: 1-10 → 0-10 (already in range)
        return value

    elif feature_type == "BINARY":
        # Yes/No → 10/0
        return 10 if value == "Yes" else 0

    else:
        # Default: assume already 0-10
        return value
```

**Example**:
```python
student_responses = [3.5, 7, 15, 30, 9, 8, 7]
feature_types = ["GPA", "LIKERT", "HOURS", "COMMUTE", "LIKERT", "LIKERT", "LIKERT"]

normalized = [
    normalize_feature(3.5, "GPA"),      # → 8.75
    normalize_feature(7, "LIKERT"),     # → 7.0
    normalize_feature(15, "HOURS"),     # → 3.75
    normalize_feature(30, "COMMUTE"),   # → 2.5
    normalize_feature(9, "LIKERT"),     # → 9.0
    normalize_feature(8, "LIKERT"),     # → 8.0
    normalize_feature(7, "LIKERT")      # → 7.0
]
# Result: [8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]
```

---

### KNN Prediction Algorithm

**Python Implementation**:

```python
import numpy as np
from scipy.spatial.distance import euclidean

def knn_predict(new_student, training_data, k=3):
    """
    K-Nearest Neighbors prediction with distance weighting

    Args:
        new_student: Normalized feature vector [8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]
        training_data: List of (features, success_rate) tuples
        k: Number of neighbors (default: 3)

    Returns:
        prediction: Predicted success rate (0-100)
        confidence: Prediction confidence (0-1)
        neighbors: List of similar students
    """

    # Calculate distances to all training samples
    distances = []
    for idx, (features, success_rate) in enumerate(training_data):
        dist = euclidean(new_student, features)
        distances.append((idx, dist, success_rate))

    # Sort by distance and get k nearest
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]

    # Distance-weighted prediction
    weights = [1 / (d + 1e-6) for (idx, d, sr) in neighbors]  # Add small epsilon to avoid division by zero
    weighted_sum = sum(w * sr for w, (idx, d, sr) in zip(weights, neighbors))
    total_weight = sum(weights)

    prediction = weighted_sum / total_weight

    # Confidence based on neighbor similarity
    avg_distance = np.mean([d for (idx, d, sr) in neighbors])
    confidence = 1 / (1 + avg_distance)  # Closer neighbors = higher confidence

    neighbor_info = [
        {"id": idx, "distance": d, "successRate": sr}
        for (idx, d, sr) in neighbors
    ]

    return prediction, confidence, neighbor_info

# Example usage:
new_student = [8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]
training_data = [
    ([8.5, 7.2, 3.9, 2.8, 8.8, 7.9, 7.1], 78),  # Student 3
    ([8.3, 6.8, 4.1, 3.2, 9.2, 8.1, 6.9], 72),  # Student 7
    ([8.0, 7.5, 3.5, 2.2, 8.5, 7.7, 7.3], 70),  # Student 12
    # ... 42 more students
]

prediction, confidence, neighbors = knn_predict(new_student, training_data, k=3)
print(f"Prediction: {prediction:.0f}%")  # 74%
print(f"Confidence: {confidence:.2f}")   # 0.82
print(f"Similar students: {[n['id'] for n in neighbors]}")  # [3, 7, 12]
```

---

### Neural Network Prediction Algorithm

**Python Implementation** (TensorFlow/Keras):

```python
import tensorflow as tf
import numpy as np

def nn_predict(new_student, model_path="nn_100real_400synthetic.h5"):
    """
    Neural Network prediction

    Args:
        new_student: Normalized feature vector [8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]
        model_path: Path to trained NN model

    Returns:
        prediction: Predicted success rate (0-1 scale, convert to 0-100)
        confidence: Prediction confidence (estimated from training history)
    """

    # Load trained model
    model = tf.keras.models.load_model(model_path)

    # Reshape input for model (batch size 1, 7 features)
    input_data = np.array([new_student]).reshape(1, 7)

    # Forward pass
    raw_prediction = model.predict(input_data, verbose=0)[0][0]

    # Confidence estimation (simplified)
    # In practice, could use ensemble predictions, dropout sampling, etc.
    confidence = 0.88  # Loaded from model metadata

    return raw_prediction, confidence

# Example usage:
new_student = [8.75, 7.0, 3.75, 2.5, 9.0, 8.0, 7.0]
prediction, confidence = nn_predict(new_student)
print(f"Prediction: {prediction * 100:.0f}%")  # 76%
print(f"Confidence: {confidence:.2f}")          # 0.88
```

---

### PWRS Formula (Priority-Weighted Response Scoring)

**Formula**:
```
Success Rate = Σ(priority_i × response_i) / Σ(priority_i)
```

**Python Implementation**:

```python
def calculate_pwrs(responses, priorities):
    """
    Calculate Priority-Weighted Response Scoring

    Args:
        responses: List of survey responses (normalized to 0-10 or 0-100 scale)
        priorities: List of priority weights for each question (1-10)

    Returns:
        success_rate: Calculated success rate (0-100%)
    """

    if len(responses) != len(priorities):
        raise ValueError("Responses and priorities must have same length")

    weighted_sum = sum(priority * response for priority, response in zip(priorities, responses))
    total_priority = sum(priorities)

    success_rate = weighted_sum / total_priority

    return success_rate

# Example: Target Survey with 5 questions
target_responses = [
    (3.2 / 4.0) * 10,  # Q1: GPA expectation → 8.0
    6.0,               # Q2: Confidence (Likert 1-10) → 6.0
    8.0,               # Q3: Career readiness (Likert 1-10) → 8.0
    7.0,               # Q4: Financial stability (Likert 1-10) → 7.0
    6.5                # Q5: Overall success (direct 0-10) → 6.5
]

priorities = [10, 8, 7, 9, 10]  # Question importance weights

success_rate = calculate_pwrs(target_responses, priorities)
print(f"Calculated Success Rate: {success_rate:.1f}%")  # 70.9%
```

**Explanation**:
```
Weighted sum = (10×8.0) + (8×6.0) + (7×8.0) + (9×7.0) + (10×6.5)
             = 80 + 48 + 56 + 63 + 65
             = 312

Total priority = 10 + 8 + 7 + 9 + 10 = 44

Success rate = 312 / 44 = 7.09 → 70.9%
```

---

## Diagram 1: Usage Notes

### For Thesis Documentation

**Chapter 4: Prediction Workflow**
- Include full diagram as Figure 4.1
- Reference specific nodes when explaining:
  - Bootstrap phase (Section 4.1)
  - Prediction phase (Section 4.2)
  - Feedback loop (Section 4.3)

**Chapter 5: Machine Learning Components**
- Extract Model Server subgraph as Figure 5.1
- Detail KNN and NN inference algorithms
- Include Python code snippets

**Appendix A: API Documentation**
- Reference API endpoint specifications from this diagram
- Include request/response examples

---

### For Code Implementation

**Backend Development**:
- Use API endpoint specs as implementation guide
- Validate request/response formats match diagram
- Implement feedback loop logic exactly as shown

**Model Server Development**:
- Implement normalization logic from Python code
- Follow KNN prediction algorithm precisely
- Use NN architecture specifications for model building

**Database Schema**:
- Use MongoDB collection structures from diagram annotations
- Ensure document fields match diagram specifications

---

### For Q&A Preparation

**Question**: "Walk me through what happens when a transfer student completes a survey."

**Answer** (referencing diagram nodes):
1. "Student completes enrollment form → ENROLL_FORM node"
2. "System checks enrollment count → COUNT_CHECK node"
3. "If n<10, bootstrap path: Both Factor and Target surveys required → BOOTSTRAP_PATH"
4. "If n≥10, prediction path: Factor survey → Model Server → Prediction display → PREDICTION_PATH"
5. "Student rates prediction → Feedback Loop Logic → Either pseudo-label or Target survey"

**Question**: "How does KNN prediction work technically?"

**Answer** (show KNN subgraph):
- "Load all training samples → KNN_LOAD_SAMPLES"
- "Calculate Euclidean distances → KNN_DISTANCE"
- "Find k=3 nearest neighbors → KNN_NEIGHBORS"
- "Apply distance weighting → KNN_WEIGHTS"
- "Return weighted average → KNN_PREDICT"
- "Here's the Python implementation..." (show code snippet)

---

## Diagram 2: Training Workflow (Exhaustive Detail)

**Note**: Due to length constraints, I'll create Diagram 2 in the same file below with equal level of detail.

---

```mermaid
graph TB
    START_TRAIN([Admin Portal<br/>Admin Login]) --> AUTH_ADMIN{Authenticated?}

    AUTH_ADMIN -->|No| LOGIN_ADMIN[Admin Login<br/>Username + Password]
    AUTH_ADMIN -->|Yes| ADMIN_DASH[Admin Dashboard]

    LOGIN_ADMIN --> ADMIN_DASH

    ADMIN_DASH --> ADMIN_MENU{Select Action}

    ADMIN_MENU -->|Create Surveys| SURVEY_CREATE
    ADMIN_MENU -->|Trigger Training| TRAIN_TRIGGER
    ADMIN_MENU -->|View Models| MODEL_VIEW
    ADMIN_MENU -->|View Metrics| METRICS_VIEW

    subgraph SurveyCreation["Survey Creation Workflow"]
        SURVEY_CREATE[Survey Builder Interface] --> SURVEY_TYPE{Survey Type?}

        SURVEY_TYPE -->|Target Survey| TARGET_CREATE[Create Target Survey<br/>Measures Success]
        SURVEY_TYPE -->|Factor Survey| FACTOR_CREATE[Create Factor Survey<br/>Predicts Success]

        subgraph TargetSurveyDesign["Target Survey Design"]
            TARGET_CREATE --> TARGET_MODE{Survey Mode?}

            TARGET_MODE -->|Single Question| TARGET_SINGLE[Single Question Mode:<br/>"What is your expected success rate?"<br/>Type: Slider (0-100%)<br/>Completion time: ~30 seconds]

            TARGET_MODE -->|Multi Question| TARGET_MULTI[Multi-Question Mode:<br/>5-10 questions with priority weights<br/>Completion time: ~10 minutes]

            TARGET_MULTI --> TARGET_QUESTIONS[Design Questions:<br/>---<br/>Q1: Expected GPA (Slider 0-4.0, Priority: 10)<br/>Q2: Confidence in completion (Likert 1-10, Priority: 8)<br/>Q3: Career readiness (Likert 1-10, Priority: 7)<br/>Q4: Financial stability (Likert 1-10, Priority: 9)<br/>Q5-10: Additional indicators...]

            TARGET_SINGLE --> TARGET_SAVE[Save Target Survey Template]
            TARGET_QUESTIONS --> TARGET_SAVE
        end

        subgraph FactorSurveyDesign["Factor Survey Design"]
            FACTOR_CREATE --> FACTOR_CATEGORIES[Design by Categories:<br/>---<br/>1. Academic Confidence<br/>2. Motivation & Career Goals<br/>3. Personal Attributes<br/>4. Resources & Support<br/>5. Self-Assessment]

            FACTOR_CATEGORIES --> FACTOR_QUESTIONS[Design Questions:<br/>---<br/>Category 1 - Academic:<br/>  Q1: GPA expectation (Slider 0-4.0)<br/>  Q2: Course difficulty perception (Likert 1-10)<br/><br/>Category 2 - Motivation:<br/>  Q3: Career goal clarity (Likert 1-10)<br/><br/>Category 3 - Personal:<br/>  Q4: Work hours (Slider 0-40)<br/>  Q5: Commute time (Slider 0-120 min)<br/><br/>Category 4 - Resources:<br/>  Q6: Family support (Likert 1-10)<br/><br/>Category 5 - Self-Assessment:<br/>  Q7: Transfer readiness (Likert 1-10)]

            FACTOR_QUESTIONS --> FACTOR_TRANSFER[Optional Transfer-Specific Questions:<br/>---<br/>- Credits lost during transfer<br/>- Previous institution type<br/>- GPA change from community college<br/>- Social integration challenges]

            FACTOR_TRANSFER --> FACTOR_SAVE[Save Factor Survey Template]
        end

        TARGET_SAVE --> SURVEY_API[POST /api/surveys/create<br/>Submit survey template to backend]
        FACTOR_SAVE --> SURVEY_API

        SURVEY_API --> SURVEY_STORE[Backend: Survey Management<br/>Store in MongoDB surveys collection]

        SURVEY_STORE --> SURVEY_CONFIRM[Confirmation:<br/>"Survey created successfully!<br/>Students can now complete it."]
    end

    subgraph TrainingTrigger["Training Trigger Workflow"]
        TRAIN_TRIGGER[Training Configuration] --> TRAIN_CHECK_DATA[Check Available Data<br/>Query: COUNT labeled students]

        TRAIN_CHECK_DATA --> TRAIN_COUNT_RESULT[Result: 105 students<br/>- 60 with Target Survey<br/>- 45 with pseudo-labels]

        TRAIN_COUNT_RESULT --> TRAIN_SUFFICIENT{Count ≥ 10?}

        TRAIN_SUFFICIENT -->|No| TRAIN_ERROR[Error:<br/>"Insufficient data for training.<br/>Need at least 10 labeled students.<br/>Current count: 7"]

        TRAIN_SUFFICIENT -->|Yes| TRAIN_CONFIG[Training Configuration:<br/>---<br/>Auto-trigger: After N new students (default: 10)<br/>Manual trigger: Click "Train Now"<br/>Phase: Auto-detect based on count<br/>Validation: 5-fold CV (KNN) or 80/20 split (NN)]

        TRAIN_CONFIG --> TRAIN_SUBMIT[POST /api/train<br/>Trigger training request]
    end

    subgraph TrainingDataCollection["Training Data Collection"]
        TRAIN_SUBMIT --> TRB_START[Backend: Training Request Builder<br/>Aggregate labeled data]

        TRB_START --> TRB_QUERY1[Query 1: Factor Responses<br/>---<br/>SELECT factorResponses FROM responses<br/>WHERE studentId IN (labeled_students)<br/>Result: 105 feature vectors]

        TRB_QUERY1 --> TRB_QUERY2[Query 2: Target Responses<br/>---<br/>SELECT targetSuccessRate FROM responses<br/>WHERE hasTarget = true<br/>Result: 60 actual success rates]

        TRB_QUERY2 --> TRB_QUERY3[Query 3: Pseudo-labels<br/>---<br/>SELECT predictedSuccess FROM pseudoLabels<br/>WHERE rating >= 4.0<br/>Result: 45 pseudo-labeled success rates]

        TRB_QUERY3 --> TRB_COMBINE[Combine All Sources:<br/>---<br/>Total: 105 students<br/>- Features: 105 x 7 matrix<br/>- Labels: 105 success rates (60 real + 45 pseudo)]

        TRB_COMBINE --> TRB_FORMAT[Format Training Request:<br/>---<br/>{<br/>  "requestId": "train-20260615-001",<br/>  "studentCount": 105,<br/>  "realCount": 60,<br/>  "pseudoCount": 45,<br/>  "features": [[...], [...], ...],<br/>  "labels": [74, 82, 65, ...],<br/>  "timestamp": "2026-06-15T10:00:00Z"<br/>}]

        TRB_FORMAT --> TRB_SEND[POST model-server/train<br/>Send to Model Server]
    end

    subgraph ModelServerTraining["Model Server - Training Pipeline"]
        TRB_SEND --> QUEUE_RECV[Training Queue Manager<br/>Receive training request]

        QUEUE_RECV --> QUEUE_CHECK{Training Job<br/>In Progress?}

        QUEUE_CHECK -->|Yes| QUEUE_WAIT[Add to Queue<br/>Status: Waiting<br/>Position: 2]

        QUEUE_CHECK -->|No| QUEUE_START[Start Training Job<br/>Status: In Progress]

        QUEUE_WAIT --> QUEUE_START

        QUEUE_START --> QUEUE_TRACK[Create Job Record:<br/>---<br/>{<br/>  "jobId": "train-20260615-001",<br/>  "status": "in_progress",<br/>  "studentCount": 105,<br/>  "phase": "TBD",<br/>  "startTime": "2026-06-15T10:00:05Z",<br/>  "estimatedDuration": "60 minutes"<br/>}]

        QUEUE_TRACK --> PHASE_DETECT[Phase Detection<br/>Based on student count]

        PHASE_DETECT --> PHASE_DECISION{Student<br/>Count?}

        PHASE_DECISION -->|10 ≤ n < 100<br/>Phase 1| KNN_PHASE[KNN Training Phase]
        PHASE_DECISION -->|n ≥ 100<br/>Phase 2 & 3| GAN_PHASE[GAN + NN Training Phase]

        %% KNN TRAINING PATH
        subgraph KNNTraining["Phase 1: KNN Training"]
            KNN_PHASE --> KNN_PREP[Prepare Training Data<br/>105 students (but example shows typical n=25-99)]

            KNN_PREP --> KNN_STORE[Store All Labeled Samples<br/>Lazy learning: No actual training<br/>Just store samples for inference]

            KNN_STORE --> KNN_CONFIG[Set Hyperparameters:<br/>---<br/>k = 3 (number of neighbors)<br/>distance_metric = "euclidean"<br/>weighting = "distance_weighted"<br/>normalization = "already_done"]

            KNN_CONFIG --> KNN_CV[5-Fold Cross-Validation<br/>---<br/>Fold 1: Train on 80%, Test on 20%<br/>Fold 2: Different 80/20 split<br/>...<br/>Fold 5: Final 80/20 split]

            KNN_CV --> KNN_FOLD1[Fold 1 Execution:<br/>---<br/>Training: Students 1-84<br/>Validation: Students 85-105<br/><br/>For each validation student:<br/>  1. Find k=3 nearest in training set<br/>  2. Distance-weighted prediction<br/>  3. Calculate |predicted - actual|<br/><br/>Fold 1 MAE: 11.2]

            KNN_FOLD1 --> KNN_FOLD2[Fold 2-5 Execution:<br/>---<br/>Fold 2 MAE: 13.5<br/>Fold 3 MAE: 12.8<br/>Fold 4 MAE: 10.9<br/>Fold 5 MAE: 12.1]

            KNN_FOLD2 --> KNN_METRICS[Calculate Final Metrics:<br/>---<br/>Average MAE = (11.2+13.5+12.8+10.9+12.1)/5 = 12.1<br/>R² = Calculate from all folds = 0.58<br/>RMSE = sqrt(mean squared errors) = 15.3]

            KNN_METRICS --> KNN_VERSION[Create Model Version:<br/>---<br/>{<br/>  "modelId": "knn-20260615-001",<br/>  "phase": "KNN",<br/>  "studentCount": 105,<br/>  "hyperparameters": {<br/>    "k": 3,<br/>    "metric": "euclidean",<br/>    "weighting": "distance"<br/>  },<br/>  "validation": {<br/>    "method": "5-fold CV",<br/>    "MAE": 12.1,<br/>    "R2": 0.58,<br/>    "RMSE": 15.3<br/>  },<br/>  "trainingDate": "2026-06-15T10:05:00Z",<br/>  "filePath": "/models/knn_samples_105.pkl"<br/>}]
        end

        %% GAN + NN TRAINING PATH
        subgraph GANNNTraining["Phase 2 & 3: GAN + NN Training"]
            GAN_PHASE --> GAN_PREP[Prepare 100 Real Students<br/>Prioritize real labels over pseudo-labels]

            GAN_PREP --> GAN_ARCH[GAN Architecture Setup:<br/>---<br/>Generator:<br/>  Input: Latent(100) ~ N(0,1)<br/>  Layer 1: Dense(128, ReLU, He init)<br/>  Layer 2: Dense(64, ReLU, He init)<br/>  Output: Dense(7, Linear)<br/><br/>Discriminator:<br/>  Input: Features(7)<br/>  Layer 1: Dense(64, ReLU, He init)<br/>  Layer 2: Dense(32, ReLU, He init)<br/>  Output: Dense(1, Sigmoid)]

            GAN_ARCH --> GAN_TRAIN_LOOP[GAN Training Loop (10,000 epochs):<br/>---<br/>For epoch in 1 to 10000:<br/>  1. Sample 32 real students<br/>  2. Generate 32 fake students (Generator)<br/>  3. Train Discriminator:<br/>     - Real students: label=1<br/>     - Fake students: label=0<br/>     - Loss: Binary cross-entropy<br/>  4. Train Generator:<br/>     - Generate 32 fake students<br/>     - Fool Discriminator (want output=1)<br/>     - Loss: Binary cross-entropy (flipped)<br/>  5. Check convergence:<br/>     - If Discriminator accuracy ≈ 50%: STOP<br/>     - Else: Continue]

            GAN_TRAIN_LOOP --> GAN_CONVERGE[Convergence Reached at Epoch 8,547:<br/>---<br/>Discriminator accuracy: 51.2%<br/>Generator loss: 0.68<br/>Discriminator loss: 0.69]

            GAN_CONVERGE --> GAN_GENERATE[Generate Synthetic Students:<br/>---<br/>For i in 1 to 400:<br/>  1. Sample latent: z ~ N(0,1), shape=(100,)<br/>  2. Forward pass through Generator<br/>  3. Output: 7 features (normalized 0-10)<br/><br/>Example synthetic student:<br/>  [7.8, 6.5, 4.2, 5.0, 8.3, 7.0, 6.8]<br/><br/>Total: 400 synthetic students generated]

            GAN_GENERATE --> GAN_VAL[GAN Validation:<br/>---<br/>1. Kolmogorov-Smirnov Test (each feature)<br/>2. Correlation Matrix Comparison<br/>3. Visual Inspection (histograms)]

            GAN_VAL --> GAN_KS[KS Test Results:<br/>---<br/>Feature 1 (GPA): p-value = 0.32 > 0.05 ✓<br/>Feature 2 (Difficulty): p-value = 0.41 > 0.05 ✓<br/>Feature 3 (Hours): p-value = 0.28 > 0.05 ✓<br/>Feature 4 (Commute): p-value = 0.35 > 0.05 ✓<br/>Feature 5 (Family): p-value = 0.29 > 0.05 ✓<br/>Feature 6 (Career): p-value = 0.38 > 0.05 ✓<br/>Feature 7 (Readiness): p-value = 0.31 > 0.05 ✓<br/><br/>All features PASS (p > 0.05)]

            GAN_KS --> GAN_CORR[Correlation Check:<br/>---<br/>Real correlation matrix (7x7):<br/>  r(F1,F6) = 0.45<br/>  r(F2,F5) = 0.38<br/>  ...<br/><br/>Synthetic correlation matrix (7x7):<br/>  r(F1,F6) = 0.43 (diff = 0.02 < 0.2) ✓<br/>  r(F2,F5) = 0.36 (diff = 0.02 < 0.2) ✓<br/>  ...<br/><br/>All correlations PASS (diff < 0.2)]

            GAN_CORR --> GAN_DECISION{Validation<br/>Passed?}

            GAN_DECISION -->|Yes| GAN_STORE[Store 400 Synthetic Students<br/>MongoDB collection: syntheticData<br/>Document: batchId, features, labels, validation]

            GAN_DECISION -->|No| GAN_RETRY[Retry GAN Training<br/>Attempt 2/3<br/>Adjust hyperparameters:<br/>- Learning rate: 0.0002 → 0.0001<br/>- Epochs: 10000 → 15000]

            GAN_RETRY --> GAN_TRAIN_LOOP

            GAN_STORE --> NN_PREP[NN Preparation:<br/>---<br/>Combine datasets:<br/>- 100 real students<br/>- 400 synthetic students<br/>Total: 500 students]

            NN_PREP --> NN_SPLIT[CRITICAL Data Split:<br/>---<br/>Training Set (80% = 400):<br/>  - 80 real students<br/>  - 320 synthetic students<br/><br/>Validation Set (20% = 100):<br/>  - 20 REAL students ONLY<br/>  - 0 synthetic students<br/><br/>PRINCIPLE: Train on synthetic, validate on real]

            NN_SPLIT --> NN_ARCH[NN Architecture:<br/>---<br/>Input(7) - Normalized features<br/>  ↓<br/>Dense(64, ReLU, He init)<br/>  ↓<br/>Dropout(0.3) - Prevent overfitting<br/>  ↓<br/>Dense(32, ReLU, He init)<br/>  ↓<br/>Dense(1, Sigmoid) - Output prediction 0-1]

            NN_ARCH --> NN_COMPILE[Compile Model:<br/>---<br/>Loss: Mean Squared Error (MSE)<br/>Optimizer: Adam(lr=0.001, beta1=0.9, beta2=0.999)<br/>Metrics: MAE, R²<br/>Batch size: 32<br/>Epochs: 100 (max)<br/>Early stopping: patience=10, monitor=val_loss]

            NN_COMPILE --> NN_TRAIN[NN Training Loop:<br/>---<br/>Epoch 1:<br/>  - Shuffle training set (400 students)<br/>  - Batch 1-13 (400/32 batches):<br/>    * Forward pass<br/>    * Calculate MSE loss<br/>    * Backpropagation<br/>    * Adam weight update<br/>  - Validation (20 REAL students):<br/>    * Forward pass only<br/>    * Calculate val_loss: 180<br/>    * Calculate MAE: 12.5<br/><br/>Epoch 2:<br/>  - Training loss: 150<br/>  - Validation loss: 165 (improved!)<br/><br/>...<br/><br/>Epoch 25:<br/>  - Training loss: 85<br/>  - Validation loss: 95 (best so far)<br/><br/>Epoch 26-35:<br/>  - Validation loss: 96, 98, 97, 99, 100...<br/>  - No improvement for 10 epochs<br/>  - EARLY STOPPING TRIGGERED]

            NN_TRAIN --> NN_BEST[Load Best Model from Epoch 25:<br/>---<br/>Validation loss: 95<br/>MAE: 8.7<br/>R²: 0.73<br/>RMSE: 11.2]

            NN_BEST --> NN_VERSION[Create Model Version:<br/>---<br/>{<br/>  "modelId": "nn-20260615-001",<br/>  "phase": "NN",<br/>  "studentCount": 100,<br/>  "syntheticCount": 400,<br/>  "architecture": "7-64-32-1",<br/>  "training": {<br/>    "realStudents": 80,<br/>    "syntheticStudents": 320,<br/>    "totalEpochs": 35,<br/>    "bestEpoch": 25<br/>  },<br/>  "validation": {<br/>    "realStudents": 20,<br/>    "syntheticStudents": 0,<br/>    "MAE": 8.7,<br/>    "R2": 0.73,<br/>    "RMSE": 11.2,<br/>    "validatedOn": "real_only"<br/>  },<br/>  "trainingDate": "2026-06-15T10:50:00Z",<br/>  "filePath": "/models/nn_100real_400synthetic.h5"<br/>}]
        end

        KNN_VERSION --> VERSIONING[Model Versioning Service]
        NN_VERSION --> VERSIONING

        VERSIONING --> VERSION_STORE[Store in MongoDB models collection:<br/>---<br/>Fields:<br/>- modelId, phase, studentCount<br/>- hyperparameters/architecture<br/>- validation metrics (MAE, R², RMSE)<br/>- trainingDate, filePath<br/>- isActive (boolean)]

        VERSION_STORE --> VERSION_COMPARE[Performance Comparison:<br/>---<br/>Load current active model:<br/>  Current: knn-20260115-001<br/>  MAE: 13.2, R²: 0.52<br/><br/>New model: nn-20260615-001<br/>  MAE: 8.7, R²: 0.73<br/><br/>Improvement:<br/>  - MAE: 34% reduction<br/>  - R²: 40% increase]

        VERSION_COMPARE --> VERSION_DECISION{New Model<br/>Better?}

        VERSION_DECISION -->|Yes: new_MAE < old_MAE| DEPLOY_MODEL[Deploy New Model:<br/>---<br/>1. Set old model isActive=false<br/>2. Set new model isActive=true<br/>3. Update Model Selector cache<br/>4. Send notification to Backend]

        VERSION_DECISION -->|No: new_MAE ≥ old_MAE| KEEP_MODEL[Keep Current Model:<br/>---<br/>1. Log training attempt<br/>2. Store new model (isActive=false)<br/>3. Send failure notification<br/>4. Recommend: Collect more data or tune hyperparameters]

        DEPLOY_MODEL --> COMPLETE_SUCCESS[Training Complete - SUCCESS:<br/>---<br/>New model deployed: nn-20260615-001<br/>Performance improvement:<br/>  - MAE: 13.2 → 8.7 (34% better)<br/>  - R²: 0.52 → 0.73 (40% better)<br/><br/>Model now available for predictions.<br/>Expected impact: More accurate predictions,<br/>higher student satisfaction.]

        KEEP_MODEL --> COMPLETE_FAIL[Training Complete - NO DEPLOYMENT:<br/>---<br/>New model did not improve performance.<br/>Current model remains active: knn-20260115-001<br/><br/>Recommendation:<br/>- Collect more labeled data<br/>- Adjust hyperparameters<br/>- Review feature engineering]
    end

    %% Update job record
    COMPLETE_SUCCESS --> JOB_UPDATE_SUCCESS[Update Training Job:<br/>---<br/>Status: completed<br/>Result: deployed<br/>ModelId: nn-20260615-001<br/>Duration: 50 minutes<br/>EndTime: 2026-06-15T10:50:00Z]

    COMPLETE_FAIL --> JOB_UPDATE_FAIL[Update Training Job:<br/>---<br/>Status: completed<br/>Result: not_deployed<br/>Reason: performance_insufficient<br/>Duration: 50 minutes]

    %% Notification to admin
    JOB_UPDATE_SUCCESS --> ADMIN_NOTIF_SUCCESS[Admin Notification:<br/>---<br/>✓ Training completed successfully!<br/><br/>New model: nn-20260615-001<br/>Improvement: MAE 13.2 → 8.7<br/>Status: DEPLOYED<br/><br/>Next predictions will use this model.]

    JOB_UPDATE_FAIL --> ADMIN_NOTIF_FAIL[Admin Notification:<br/>---<br/>⚠ Training completed - Model NOT deployed<br/><br/>New model performance:<br/>  MAE: 13.5 (vs current 13.2)<br/>  R²: 0.50 (vs current 0.52)<br/><br/>Current model remains active.<br/>Recommendation: Collect more data.]

    %% Database
    DB_TRAIN[(MongoDB Collections:<br/>---<br/>surveys:<br/>  {surveyId, surveyType, version, questions, priorities}<br/><br/>responses:<br/>  {studentId, surveyType, responses, targetSuccessRate, hasTarget}<br/><br/>pseudoLabels:<br/>  {studentId, factorResponses, predictedSuccess, isPseudoLabel, rating}<br/><br/>models:<br/>  {modelId, phase, studentCount, validation, isActive, filePath}<br/><br/>syntheticData:<br/>  {batchId, count, features, labels, validationResults}<br/><br/>trainingJobs:<br/>  {jobId, status, phase, startTime, endTime, result, modelId})]

    SURVEY_STORE -.-> DB_TRAIN
    TRB_QUERY1 -.-> DB_TRAIN
    TRB_QUERY2 -.-> DB_TRAIN
    TRB_QUERY3 -.-> DB_TRAIN
    VERSION_STORE -.-> DB_TRAIN
    GAN_STORE -.-> DB_TRAIN
    JOB_UPDATE_SUCCESS -.-> DB_TRAIN
    JOB_UPDATE_FAIL -.-> DB_TRAIN

    classDef admin fill:#9B59B6,stroke:#6C3483,stroke-width:2px,color:#fff
    classDef backend fill:#50C878,stroke:#2E7D4E,stroke-width:2px,color:#fff
    classDef model fill:#F5A623,stroke:#C77F1B,stroke-width:2px,color:#fff
    classDef decision fill:#E8E8E8,stroke:#7F8C8D,stroke-width:2px,color:#000
    classDef database fill:#E74C3C,stroke:#A93226,stroke-width:2px,color:#fff
    classDef knn fill:#D5F4E6,stroke:#27AE60,stroke-width:2px,color:#000
    classDef gan fill:#FADBD8,stroke:#E74C3C,stroke-width:2px,color:#000
    classDef nn fill:#D6EAF8,stroke:#3498DB,stroke-width:2px,color:#000
    classDef success fill:#ABEBC6,stroke:#229954,stroke-width:3px,color:#000
    classDef fail fill:#F5B7B1,stroke:#C0392B,stroke-width:3px,color:#000

    class START_TRAIN,LOGIN_ADMIN,ADMIN_DASH,SURVEY_CREATE,TARGET_CREATE,FACTOR_CREATE,TRAIN_TRIGGER,MODEL_VIEW,METRICS_VIEW admin
    class SURVEY_STORE,TRB_START,TRB_QUERY1,TRB_QUERY2,TRB_QUERY3,TRB_COMBINE,TRB_FORMAT,TRB_SEND backend
    class QUEUE_RECV,QUEUE_START,QUEUE_TRACK,PHASE_DETECT,VERSIONING,VERSION_STORE,VERSION_COMPARE model
    class KNN_PREP,KNN_STORE,KNN_CONFIG,KNN_CV,KNN_FOLD1,KNN_FOLD2,KNN_METRICS,KNN_VERSION knn
    class GAN_PREP,GAN_ARCH,GAN_TRAIN_LOOP,GAN_CONVERGE,GAN_GENERATE,GAN_VAL,GAN_KS,GAN_CORR,GAN_STORE gan
    class NN_PREP,NN_SPLIT,NN_ARCH,NN_COMPILE,NN_TRAIN,NN_BEST,NN_VERSION nn
    class AUTH_ADMIN,ADMIN_MENU,SURVEY_TYPE,TARGET_MODE,TRAIN_SUFFICIENT,QUEUE_CHECK,PHASE_DECISION,GAN_DECISION,VERSION_DECISION decision
    class DB_TRAIN database
    class COMPLETE_SUCCESS,JOB_UPDATE_SUCCESS,ADMIN_NOTIF_SUCCESS,DEPLOY_MODEL success
    class COMPLETE_FAIL,JOB_UPDATE_FAIL,ADMIN_NOTIF_FAIL,KEEP_MODEL,TRAIN_ERROR fail
```

---

## Diagram 2: Complete Technical Specifications

### GAN Training Algorithm

**Python Implementation** (TensorFlow/Keras):

```python
import tensorflow as tf
import numpy as np
from scipy.stats import ks_2samp

def train_gan(real_data, epochs=10000, latent_dim=100):
    """
    Train GAN to generate synthetic transfer students

    Args:
        real_data: np.array of shape (100, 7) - 100 real students, 7 features
        epochs: Training epochs (default: 10000)
        latent_dim: Latent vector dimension (default: 100)

    Returns:
        generator: Trained generator model
        synthetic_data: Generated synthetic students (400, 7)
        validation_results: KS test and correlation check results
    """

    n_features = real_data.shape[1]  # 7 features

    # Generator architecture
    generator = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_dim=latent_dim, kernel_initializer='he_normal'),
        tf.keras.layers.Dense(64, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dense(n_features, activation='linear')  # Output: 7 features
    ])

    # Discriminator architecture
    discriminator = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_dim=n_features, kernel_initializer='he_normal'),
        tf.keras.layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Output: Real (1) or Fake (0)
    ])

    # Compile discriminator
    discriminator.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # GAN (combined model)
    discriminator.trainable = False
    gan = tf.keras.Sequential([generator, discriminator])
    gan.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
        loss='binary_crossentropy'
    )

    # Training loop
    batch_size = 32
    for epoch in range(epochs):
        # Train Discriminator
        # Real samples
        idx = np.random.randint(0, real_data.shape[0], batch_size)
        real_samples = real_data[idx]
        real_labels = np.ones((batch_size, 1))

        # Fake samples
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        fake_samples = generator.predict(noise, verbose=0)
        fake_labels = np.zeros((batch_size, 1))

        # Train on real and fake
        d_loss_real = discriminator.train_on_batch(real_samples, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_samples, fake_labels)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # Train Generator
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        g_loss = gan.train_on_batch(noise, np.ones((batch_size, 1)))

        # Check convergence
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}: D_loss={d_loss[0]:.3f}, D_acc={d_loss[1]:.3f}, G_loss={g_loss:.3f}")

            # Convergence criterion: Discriminator accuracy ≈ 50%
            if 0.45 <= d_loss[1] <= 0.55:
                print(f"Convergence reached at epoch {epoch}")
                break

    # Generate 400 synthetic students
    noise = np.random.normal(0, 1, (400, latent_dim))
    synthetic_data = generator.predict(noise, verbose=0)

    # Validate synthetic data
    validation_results = validate_gan(real_data, synthetic_data)

    return generator, synthetic_data, validation_results


def validate_gan(real_data, synthetic_data):
    """
    Validate GAN-generated data using KS test and correlation check

    Args:
        real_data: (100, 7) real students
        synthetic_data: (400, 7) synthetic students

    Returns:
        validation_results: Dict with KS test and correlation check results
    """

    results = {"ks_test": {}, "correlation_check": {}}

    # KS Test for each feature
    for i in range(7):
        real_feature = real_data[:, i]
        synthetic_feature = synthetic_data[:, i]

        statistic, p_value = ks_2samp(real_feature, synthetic_feature)

        results["ks_test"][f"feature_{i+1}"] = {
            "p_value": p_value,
            "passed": p_value > 0.05
        }

    # Correlation matrix comparison
    real_corr = np.corrcoef(real_data.T)
    synthetic_corr = np.corrcoef(synthetic_data.T)
    corr_diff = np.abs(real_corr - synthetic_corr)

    results["correlation_check"] = {
        "max_difference": np.max(corr_diff),
        "passed": np.max(corr_diff) < 0.2
    }

    # Overall validation
    ks_passed = all([results["ks_test"][f"feature_{i+1}"]["passed"] for i in range(7)])
    corr_passed = results["correlation_check"]["passed"]

    results["overall_passed"] = ks_passed and corr_passed

    return results

# Example usage:
real_students = np.random.rand(100, 7) * 10  # Placeholder: 100 real students with 7 features (0-10 scale)
generator, synthetic_students, validation = train_gan(real_students, epochs=10000)

if validation["overall_passed"]:
    print("✓ GAN validation PASSED")
    print(f"Generated {synthetic_students.shape[0]} synthetic students")
else:
    print("✗ GAN validation FAILED - Retry training")
```

---

### Neural Network Training Algorithm

**Python Implementation** (TensorFlow/Keras):

```python
import tensorflow as tf
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

def train_neural_network(real_data, real_labels, synthetic_data, synthetic_labels):
    """
    Train Neural Network on combined real + synthetic data
    CRITICAL: Validate ONLY on real students

    Args:
        real_data: (100, 7) real student features
        real_labels: (100,) real success rates
        synthetic_data: (400, 7) synthetic student features
        synthetic_labels: (400,) synthetic success rates

    Returns:
        model: Trained NN model
        metrics: Validation metrics (MAE, R², RMSE) on REAL students only
    """

    # Split REAL data: 80% train, 20% validation
    n_real = real_data.shape[0]
    n_train_real = int(0.8 * n_real)  # 80 real students for training
    n_val_real = n_real - n_train_real  # 20 real students for validation

    indices = np.arange(n_real)
    np.random.shuffle(indices)

    train_real_idx = indices[:n_train_real]
    val_real_idx = indices[n_train_real:]

    X_train_real = real_data[train_real_idx]
    y_train_real = real_labels[train_real_idx]

    X_val = real_data[val_real_idx]  # CRITICAL: Validation = REAL ONLY
    y_val = real_labels[val_real_idx]

    # Split SYNTHETIC data: 80% for training, 0% for validation
    n_synthetic = synthetic_data.shape[0]
    n_train_synthetic = int(0.8 * n_synthetic)  # 320 synthetic for training

    X_train_synthetic = synthetic_data[:n_train_synthetic]
    y_train_synthetic = synthetic_labels[:n_train_synthetic]

    # Combine training data: 80 real + 320 synthetic = 400 total
    X_train = np.vstack([X_train_real, X_train_synthetic])
    y_train = np.hstack([y_train_real, y_train_synthetic])

    # Shuffle combined training data
    train_indices = np.arange(X_train.shape[0])
    np.random.shuffle(train_indices)
    X_train = X_train[train_indices]
    y_train = y_train[train_indices]

    print(f"Training set: {X_train.shape[0]} students (80 real + 320 synthetic)")
    print(f"Validation set: {X_val.shape[0]} students (20 REAL ONLY)")

    # Build NN architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(7,)),
        tf.keras.layers.Dense(64, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Output: 0-1 (convert to 0-100% later)
    ])

    # Compile model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999),
        loss='mse',
        metrics=['mae']
    )

    # Early stopping callback
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True,
        verbose=1
    )

    # Train model
    history = model.fit(
        X_train, y_train / 100.0,  # Normalize labels to 0-1 scale for sigmoid
        validation_data=(X_val, y_val / 100.0),
        epochs=100,
        batch_size=32,
        callbacks=[early_stopping],
        verbose=1
    )

    # Evaluate on REAL validation set
    y_pred = model.predict(X_val, verbose=0) * 100.0  # Convert back to 0-100%
    y_true = y_val

    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))

    metrics = {
        "MAE": mae,
        "R2": r2,
        "RMSE": rmse,
        "validated_on": "real_students_only",
        "n_validation": X_val.shape[0],
        "best_epoch": len(history.history['loss']) - 10  # Subtract patience
    }

    print(f"\nValidation Metrics (on {X_val.shape[0]} REAL students):")
    print(f"  MAE: {mae:.2f}")
    print(f"  R²: {r2:.2f}")
    print(f"  RMSE: {rmse:.2f}")

    return model, metrics

# Example usage:
real_data = np.random.rand(100, 7) * 10  # 100 real students, 7 features (0-10 scale)
real_labels = np.random.rand(100) * 100  # Success rates 0-100%
synthetic_data = np.random.rand(400, 7) * 10  # 400 synthetic students from GAN
synthetic_labels = np.random.rand(400) * 100  # Synthetic success rates

model, metrics = train_neural_network(real_data, real_labels, synthetic_data, synthetic_labels)

if metrics["MAE"] < 10 and metrics["R2"] > 0.60:
    print("\n✓ NN model meets performance targets - DEPLOY")
    model.save("nn_100real_400synthetic.h5")
else:
    print("\n✗ NN model does not meet targets - Do NOT deploy")
```

---

## Diagram 2: Usage Notes

### For Thesis Documentation

**Chapter 6: Training Workflow**
- Include Diagram 2 as Figure 6.1
- Reference GAN training algorithm in Section 6.2
- Reference NN training algorithm in Section 6.3
- Detail model versioning in Section 6.4

**Appendix B: Training Algorithms**
- Include complete Python implementations
- Add pseudocode for clarity
- Provide complexity analysis

---

### For Defense Presentation

**Recommended Approach**:
1. Don't show full diagram on slide (too complex)
2. Extract key subgraphs:
   - Slide 1: Survey Creation (TargetSurveyDesign + FactorSurveyDesign)
   - Slide 2: Data Collection (TrainingDataCollection subgraph)
   - Slide 3: KNN Training (KNNTraining subgraph)
   - Slide 4: GAN + NN Training (GANNNTraining subgraph)
3. Keep full diagram as backup reference for Q&A

**Speaking Points**:
- "Admins create two types of surveys: Target measures success, Factor predicts success"
- "Data collection combines three sources: Real Target surveys, Pseudo-labels from feedback, Factor surveys"
- "At 10-99 students, we train KNN using 5-fold cross-validation"
- "At 100+ students, we train GAN to generate 400 synthetic students, then train NN on 500 total but validate on 20 REAL students only"

---

**Complexity**: Very High (reference document only)
**Audience**: Thesis appendix, comprehensive technical documentation
**Estimated Presentation Time**: N/A (not suitable for direct presentation)
**Recommendation**: Use as technical reference, extract subgraphs for slides
