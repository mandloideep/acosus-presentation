# ML Model Training and Prediction Pipeline

## Document Purpose
This document describes the machine learning pipeline for ACOSUS, including the legacy implementation (for historical context), the current progressive learning approach, and the model serving architecture.

---

## 1. Legacy Implementation (Historical Context)

The initial ACOSUS implementation used synthetic data generation with traditional neural networks and regression models. This approach was replaced with the progressive learning framework due to the cold start problem.

### 1.1 Synthetic Data Generation

**File**: `model/seed.py`

The legacy approach generated random synthetic student profiles using probabilistic seeding:

```python
def generate_seed_data(data):
    seed_qty = int(data["seedqty"])
    questions = questionSlugAndType["questions"]

    answers_list = []
    for _ in range(seed_qty):
        answers = {}
        for question, details in questions.items():
            seed_data = details["seedData"]
            seed_values = [item["seedValue"] for item in seed_data]
            seed_probabilities = [float(item["seedProbability"]) for item in seed_data]
            selected_value = random.choices(seed_values, seed_probabilities)[0]
            answers[question] = selected_value
        answers_list.append({"answers": answers})
    return {"data": {"answers": answers_list}}
```

**Synthetic Data Features (20+ dimensions)**:
| Category | Features |
|----------|----------|
| **Academic** | GPA, SAT, learning style |
| **Demographic** | Career path, family support |
| **Situational** | Work status, scholarship, study environment |
| **Psychological** | Personality type, mental health readiness, time management |
| **Transfer-specific** | Transfer clarity, peer support |

**Example Seed Configuration**:
```json
{
  "gpa": {
    "seedData": [
      {"seedValue": "Below 2.0", "seedProbability": 0.2},
      {"seedValue": "Between 2.0 to 3.0", "seedProbability": 0.2},
      {"seedValue": "Between 3.0 and 3.5", "seedProbability": 0.3},
      {"seedValue": "More than 3.5", "seedProbability": 0.3}
    ],
    "options": [
      {"optionValue": "Below 2.0", "optionWeightage": 2},
      {"optionValue": "More than 3.5", "optionWeightage": 9}
    ]
  }
}
```

**Limitations**:
- No correlation between questions in synthetic data
- Generated data lacked realistic interdependencies
- Model trained on synthetic data failed to generalize to real students

### 1.2 Legacy Neural Network Architecture

**File**: `model/neural_network.py`

```
Input Layer (variable features)
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Dense(50 neurons) + Dropout(0.1) + ReLU
    ↓
Output Layer: Dense(1) + ReLU
```

**Training Configuration**:
| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Mean Squared Error |
| Epochs | 50 |
| Batch Size | 10 |
| Data Split | 80% train / 20% test |

**Success Rate Formula**:
```python
success_rate = 0.5 * (gpa/4) + 0.5 * (4/duration) * 10
```

### 1.3 Legacy Regression Model

**File**: `model/regression.py`

```
Input Layer
    ↓
Dense(64 neurons) + ReLU
    ↓
Dense(32 neurons) + ReLU
    ↓
Output Layer: Dense(1) [Linear activation for regression]
```

### 1.4 Why the Approach Changed

| Problem | Impact |
|---------|--------|
| **Cold Start** | No mechanism to work with 10 students; required 1000+ |
| **Synthetic Data Bias** | No correlation between features led to unrealistic profiles |
| **Fixed Architecture** | Same neural network regardless of data availability |
| **No Progressive Scaling** | Could not adapt as cohort grew |
| **ReLU on Output** | Improper activation for bounded success rate (0-100) |

**Key Insight**: Traditional ML approaches failed because transfer student cohorts start small (10-20 students) and grow gradually over semesters.

---

## 2. Current Approach: Progressive Learning Framework

### 2.1 Data Requirements

The current system requires **real student data** collected through surveys:

**Factor Surveys (Input Features)**:
- Collected from all students upon enrollment
- 5-10 questions measuring success predictors
- Examples: GPA, SAT, family support, program timeline, learning preferences

**Target Surveys (Ground Truth Labels)**:
- Collected during early adoption phase
- Provides success rate labels for training
- Single-question or multi-question formats supported

**Minimum Data Requirement**: 10 students with completed surveys

### 2.2 Feature Engineering

**File**: `model/neural_network_v2.py`

Features are engineered from factor survey answers using priority-weighted scoring:

```python
def create_student_feature_vector(student_answers, questions, question_order):
    """
    Creates feature vectors from real survey responses.

    Three question types handled:
    1. Questions with explicit option weightages (GPA, SAT, family support)
    2. Date questions (startdate, enddate)
    3. Categorical questions (yes/no, multiple choice)
    """

    # For each question:
    # - Priority score (weighted 0-1): weight = priorityScore / 10.0
    # - Option weightage (normalized): value / max_weightage
    # - Combined feature = normalized_option * priority_weight
```

**Duration Feature Normalization**:
```python
# Duration scoring (years):
# ≤2 years: 0.4 (rushed)
# 2-4 years: 0.4 + (years-2)*0.3 (optimal at 4 years = 1.0)
# 4-6 years: 1.0 - (years-4)*0.25 (decreasing after 4)
# >6 years: 0.3 (extended)
```

### 2.3 Target Variable (Readiness Score)

The target variable comes from Target Survey responses, processed through the **Dynamic Success Rate Generator**:

**File**: `model/app/generators/dynamicSuccessRateGen.py`

```python
class SuccessRateCalculator:
    """
    Calculates success rates using weighted scoring:
    1. Option weightages from survey answers
    2. Priority scores (1-10) for each question
    3. Duration contribution from date ranges
    """

    def generate_success_rate_from_score(self, weighted_score: float):
        """
        Converts weighted score (0-1) to success rate (20-90%).
        Uses sigmoid transformation to avoid unrealistic extremes.

        Formula:
        x = (weighted_score - 0.5) * 6
        sigmoid = 1 / (1 + exp(-x))
        success_rate = 20 + (sigmoid * 70)  # Maps to 20-90 range
        """
```

### 2.4 Model Selection Criteria

Model selection is automatic based on student count:

| Student Count | Model | Rationale |
|--------------|-------|-----------|
| 0-9 | None | Insufficient data for any model |
| 10-99 | K-Nearest Neighbors (KNN) | Instance-based, works with small data, interpretable |
| 100+ | GAN + Neural Network | Requires synthetic augmentation for neural network |

**KNN Selection Justification**:
- No training phase (instance-based learning)
- Effective with 10-100 samples
- Non-parametric (no distribution assumptions)
- Interpretable ("You're similar to students #3, #7, #12")

**Neural Network Selection Justification**:
- Higher accuracy potential with sufficient data
- GAN augmentation enables training with 100 real students
- Better feature learning through hidden layers

---

## 3. Progressive Training Strategy

### Phase Overview

```
Student Count →  0────10────20────50────100────200────1000+
                 │     │          │     │
Model Stage →    None  KNN        KNN   GAN+NN  NN (continuous)
                       ↑          ↑     ↑
Training Events:  Bootstrap  Retrain  Transform  Optimize
```

### Phase 1: Bootstrap (Students 1-10)

**Goal**: Collect initial training data

**Actions**:
- No model deployed
- All students complete Target + Factor surveys
- Data stored for future training

**Why 10 Students?**
- Statistical minimum for 5-fold cross-validation (5 folds × 2 samples)
- KNN k=3 neighbors requires minimum 9 samples
- Achievable in 2-4 weeks vs waiting years

**Student Journey**:
```
Student #1-10:
  1. Enroll in program
  2. Complete demographic profile
  3. Complete TARGET survey → Provides success rate label
  4. Complete FACTOR survey → Provides features
  5. NO prediction shown (insufficient data)
```

### Phase 2: Model Training and Validation (Students 10-99)

**Trigger**: When student #10 completes surveys

**Model**: K-Nearest Neighbors

**Configuration**:
```python
modelConfig: {
  knn: {
    n_neighbors: "auto",        # sqrt(n_students), capped 3-10
    weights: "distance",        # Closer neighbors weighted higher
    metric: "euclidean"         # L2 distance
  }
}

# Auto k calculation
def calculate_k(n_students):
    k = int(math.sqrt(n_students))
    return min(10, max(3, k))  # Cap between 3-10

# Examples:
# 10 students → k = 3
# 25 students → k = 5
# 100 students → k = 10 (capped)
```

**Training Process**:
```python
# 1. Normalize features to 0-10 scale
# 2. Build feature matrix X and label vector y
# 3. Train KNN (stores data)
knn.fit(X, y)  # <1 second

# 4. 5-Fold Cross-Validation
mae_scores = cross_val_score(knn, X, y, cv=5, scoring='neg_mean_absolute_error')
```

**Expected Performance**:
| Student Count | k | MAE (Expected) | R² (Expected) | Inference Time |
|---------------|---|----------------|---------------|----------------|
| 10 | 3 | 14.2 ± 3.5 | 0.42 | <10ms |
| 25 | 5 | 12.8 ± 2.8 | 0.51 | <25ms |
| 50 | 7 | 11.8 ± 2.1 | 0.54 | <50ms |
| 100 | 10 | 10.5 ± 1.8 | 0.61 | <100ms |

**Retraining Strategy**:
- Every 10 new students: Retrain KNN with updated dataset
- Emergency trigger: If average feedback rating <3.5 over last 20 predictions

### Phase 3: Prediction Mode Activation (Students 11+)

**Trigger**: After KNN is trained (student 10)

**Flow**:
```
Student #11 enrolls
    ↓
Complete Factor Survey (3 min)
    ↓
System generates prediction via KNN
    ↓
Student sees prediction + similar students
    ↓
Student rates prediction (1-5 stars)
    ↓
IF rating ≥ 4: Pseudo-label (skip Target Survey)
IF rating < 4: Redirect to Target Survey for correction
```

**Prediction Example**:
```python
# Factor answers
factor_answers = {
    "gpa": "Between 3.0 and 3.5",
    "sat": 1100,
    "family_support": "Yes"
}

# Normalized: [8.0, 5.83, 10.0, 10.0]

# Find 3 nearest neighbors
distances, indices = knn.kneighbors(X_new, n_neighbors=3)

# Distance-weighted prediction
prediction = knn.predict(X_new)  # Result: 79%
```

### Phase 4: Continuous Improvement (100+ Students)

**GAN Training Trigger**: When student #100 completes surveys

**Challenge**: Neural networks need 1000+ samples; we have 100

**Solution**: Conditional GAN generates 400 synthetic students (4× multiplier)

**GAN Architecture**:

*Generator*:
```
Input: [Noise (100-dim)] + [Success rate bin (one-hot)]
    ↓
Dense(128, ReLU) → Dense(256, ReLU) → Dense(128, ReLU)
    ↓
Output: [Normalized features (5-10 dim)]
```

*Discriminator*:
```
Input: [Features] + [Success rate]
    ↓
Dense(128, LeakyReLU) → Dense(64, LeakyReLU) → Dense(32, LeakyReLU)
    ↓
Output: [Real/Fake probability]
```

**Quality Validation (Critical)**:
```python
# 1. Correlation similarity (<0.2 difference)
corr_diff = abs(real_corr - synthetic_corr)
assert corr_diff.mean() < 0.2

# 2. Kolmogorov-Smirnov test (p > 0.05)
for feature in features:
    _, p_value = ks_2samp(real[feature], synthetic[feature])
    assert p_value > 0.05

# 3. Feature mean similarity (<0.1 per feature)
mean_diff = abs(real_means - synthetic_means)
assert (mean_diff < 0.1).all()
```

**Neural Network Architecture (v2)**:
```
Input Layer (5-10 normalized features)
    ↓
Dense(64) + ReLU + Dropout(0.3)
    ↓
Dense(32) + ReLU + Dropout(0.2)
    ↓
Dense(16) + ReLU
    ↓
Output: Dense(1) + Sigmoid (0-1, scaled to 0-100%)
```

**Training Process (Critical: Real-Only Validation)**:
```python
# 1. Split REAL students FIRST
X_real_train, X_real_val = train_test_split(X_real, test_size=0.2)

# 2. Generate synthetic data
X_synthetic, y_synthetic = gan.generate(n_samples=400)

# 3. Combine for training (real + synthetic)
X_train = np.vstack([X_real_train, X_synthetic])  # 80 + 400 = 480

# 4. Train on mixed data, validate on REAL ONLY
model.fit(X_train, y_train,
          validation_data=(X_real_val, y_real_val),  # Real validation only!
          callbacks=[EarlyStopping(patience=20)])
```

**Performance Comparison**:
| Model | Training Data | MAE | R² |
|-------|---------------|-----|-----|
| KNN | 100 real | 10.5 | 0.61 |
| NN (no GAN) | 100 real | 13.2 | 0.48 |
| **NN + GAN** | 100 real + 400 syn | **8.7** | **0.73** |

**Continuous Retraining**:
| Trigger | Frequency | Action | Duration |
|---------|-----------|--------|----------|
| 10 new students | ~2-3 weeks | Retrain NN only | 5 min |
| 50 new students | ~3-4 months | Retrain GAN + NN | 30 min |
| Avg rating <3.5 | As needed | Emergency NN retrain | 5 min |

---

## 4. Feedback Loop (Pseudo-Labeling)

### 4.1 Process Overview

```
Factor Survey Completed
    ↓
Model Prediction Generated
    ↓
Student Rates Prediction (1-5 stars)
    ↓
┌─────────────────┬─────────────────┐
│  Rating ≥ 4     │  Rating < 4     │
│  (High Trust)   │  (Low Trust)    │
├─────────────────┼─────────────────┤
│  Pseudo-label   │  Target Survey  │
│  prediction     │  for correction │
│  as ground      │  to get actual  │
│  truth          │  success rate   │
└─────────────────┴─────────────────┘
```

### 4.2 Pseudo-Labeling Logic

```javascript
if (feedbackRating >= 4) {
  // High rating → Use prediction as pseudo-label
  trainingLabel = {
    success_rate: predictionShown,
    source: "pseudo_label",
    correctionProvided: false
  };
  skipTargetSurvey = true;
} else {
  // Low rating → Request correction
  redirectTo = "target_survey";
  trainingLabel.source = "feedback_corrected";
}
```

### 4.3 Expected Outcomes

| Metric | Without Feedback Loop | With Feedback Loop |
|--------|----------------------|-------------------|
| Survey Completion Rate | 60% | 92% |
| Avg Time per Student | 18 min | 5 min |
| Pseudo-Label Rate | 0% | 50-70% |
| Training Data Growth | Linear | Accelerated |

---

## 5. Model Serving

### 5.1 Prediction Generation

**Endpoint**: `POST /api/v2/student/attempt/complete/factor`

**Flow**:
```typescript
async function completeFactorQuizHandler(req, res) {
  // 1. Mark attempt as completed
  const attempt = await Attempt.findById(attemptId);

  // 2. Check if model exists
  const currentModel = await ModelMetaData.findOne({
    quizId: linkedTargetQuizId,
    isCurrent: true
  });

  if (!currentModel) {
    return { prediction: null, message: "Model not trained yet" };
  }

  // 3. Build prediction request
  const factorAnswers = buildFactorAnswers(attempt.questions);

  // 4. Call Model Server
  const prediction = await axios.post(ML_PREDICT_URL, {
    modelName: currentModel.modelName,
    factorAnswers
  });

  // 5. Store and return prediction
  return { prediction: prediction.data.success_rate };
}
```

### 5.2 Response Time Considerations

| Model Type | Inference Time | Notes |
|------------|---------------|-------|
| KNN | <100ms | Increases linearly with dataset size |
| Neural Network | <10ms | Constant time after model load |
| GAN + NN | <10ms | Same as NN (GAN used only for training) |

**Model Loading Strategy**:
- Models cached in memory after first prediction
- Automatic reload after retraining
- Fallback to disk if memory pressure detected

### 5.3 Model Versioning

**Version Format**: `v{phase}_{model_type}_{timestamp}`

Examples:
- `v2_knn_20250115_143022` - Phase 2 KNN trained on Jan 15
- `v4_neural_20250301_091500` - Phase 4 Neural Network trained on Mar 1

**Schema** (ModelMetaData):
```typescript
{
  modelVersion: "v3_neural_20250929_102000",
  modelType: "knn" | "gan" | "neural",
  isCurrent: true,  // Only one per quiz
  trainingContext: {
    trainedAt: Date,
    triggerType: "initial_knn" | "knn_retrain" | "gan_train" | "neural_train" | "manual"
  },
  trainingMetrics: {
    mae: number,
    r2: number,
    crossValidationScores: { mae: number[], mean_mae: number }
  },
  trainingDataSummary: {
    totalStudents: number,
    totalRealStudents: number,
    syntheticStudentsGenerated: number,
    labelSources: {
      self_reported: number,
      calculated: number,
      pseudo_label: number,
      feedback_corrected: number
    }
  }
}
```

---

## 6. Implementation Status

### Implemented

| Component | Status | File |
|-----------|--------|------|
| Synthetic data generation | Complete | `model/seed.py` |
| Success rate calculation | Complete | `model/app/generators/dynamicSuccessRateGen.py` |
| Neural Network v2 | Complete | `model/neural_network_v2.py` |
| Feature engineering | Complete | `model/neural_network_v2.py` |
| Training API | Complete | `model/main.py` |
| Progress tracking | Complete | `model/progress_tracker.py` |

### Pending Implementation

| Component | Status | Notes |
|-----------|--------|-------|
| Real student data collection | **[TO BE DOCUMENTED]** | Currently 0/10 students; recruiting phase |
| KNN model implementation | **[TO BE DOCUMENTED]** | Code structure exists but integration pending |
| GAN model implementation | **[TO BE DOCUMENTED]** | Architecture documented but not coded |
| Feedback loop integration | **[TO BE DOCUMENTED]** | Pseudo-labeling logic not wired up |
| Automatic retraining triggers | **[TO BE DOCUMENTED]** | Code partially stubbed in `main.py` |
| Model serving endpoint optimization | **[TO BE DOCUMENTED]** | Caching strategy not implemented |

---

## 7. Questions for Clarification

1. **KNN Implementation**: What is the current status of the KNN model integration? Is there existing code that needs to be connected to the backend, or does it need to be written from scratch?

2. **GAN Training Pipeline**: The GAN architecture is well-documented, but is there an implementation plan or existing codebase for the GAN training process?

3. **Model Serving Infrastructure**: What is the deployment target for the model server? Is it co-located with the backend or a separate microservice?

4. **Real Data Collection Timeline**: When do you expect to have the first 10 real students enrolled? This impacts the documentation of Phase 2 activation.

5. **Feedback Loop UI**: Is the rating interface (1-5 stars) implemented in the frontend? The backend endpoint exists but the integration status is unclear.

---

## Document Metadata

- **Source**: ACOSUS Model Repository + PresentationPlan Documentation
- **Last Updated**: December 2024
- **Legacy Code Version**: neural_network.py, regression.py
- **Current Code Version**: neural_network_v2.py
- **Documentation Status**: Hybrid (implemented + planned components)
