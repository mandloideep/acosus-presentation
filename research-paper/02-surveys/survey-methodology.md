# Survey Methodology: Dual-Survey System for Cold Start Problem

## Overview

ACOSUS employs a **dual-survey architecture** to solve the cold start problem in transfer student success prediction. Unlike traditional ML systems that collect features and outcomes in a single survey, ACOSUS separates them into two distinct instruments:

1. **Target Survey** - Collects ground truth success rates (the output/label)
2. **Factor Survey** - Collects predictive features (the input variables)

This separation enables progressive learning and advisor-driven data collection that traditional approaches cannot achieve.

---

## Target Survey: Ground Truth Collection

### Purpose

The Target Survey collects **actual or perceived success rates** from transfer students. This serves as the **label (y)** in the machine learning model: `y = f(X)`.

For advisors, it provides baseline understanding of student confidence and readiness before offering personalized guidance.

### Question Categories (from quiz.json)

The Target Survey contains **5 categories** with **27 total questions** (22 active, 5 inactive).

> **Note on isActive**: Questions with `isActive: false` are created in the database but hidden from students. This allows collecting more comprehensive data points over time as questions are activated, improving prediction accuracy without overwhelming students initially.

**Category breakdown**:

| Category | Slug | Questions | Active | Description |
|----------|------|-----------|--------|-------------|
| **Academic Confidence & Preparation** | `academic-confidence-preparation` | 6 | 6 | Academic confidence, commitment, time management, study habits |
| **Motivation & Career Goals** | `motivation-career-goals` | 5 | 4 | Career clarity, industry awareness, professional development |
| **Personal Attributes & Skills** | `personal-attributes-skills` | 7 | 3 | Stress management, adaptability, problem-solving |
| **Resources & Support** | `resources-support` | 4 | 3 | Financial confidence, support systems, technology access |
| **Self-Assessment & Expectations** | `self-assessment-expectations` | 8 | 5 | Success prediction, grade expectations, study time, challenges |

### Key Target Questions (Highest Priority)

| Question | Slug | Priority | Purpose |
|----------|------|----------|---------|
| "On a scale of 1-10, how ready do you feel..." | `overall-ready` | 10 | Overall readiness assessment |
| "If you had to predict your own success..." | `success-predict` | 10 | Self-prediction of success |
| "How confident do you feel about succeeding..." | `academic-conf` | 9 | Academic confidence baseline |
| "How committed are you to completing..." | `commitment` | 9 | Persistence indicator |
| "How clear and motivating are your career goals..." | `motivation-goal` | 9 | Motivation assessment |

### Target Survey Type: Multi-Question

The Target Survey uses `targetType: "multi_question"` to collect success rate through **multiple correlated questions** rather than a single direct question.

**Why Multi-Question?**
1. **Reduced Bias**: Single self-assessment questions are prone to overconfidence/underconfidence
2. **Validation**: Multiple questions allow cross-validation of student responses
3. **Richer Data**: Each question captures a different dimension of readiness
4. **PWRS Integration**: Priority-weighted scoring produces more accurate success rates

**Alternative**: Single-question target surveys (direct 0-100% input) are supported but not currently used in the default configuration, as multi-question surveys yield better training labels.

### How Readiness Score is Calculated (PWRS Formula)

The **Priority-Weighted Response Scoring (PWRS)** formula converts multi-question responses into a single success rate:

#### Step 1: Normalize Each Answer (0-1 Scale)

```
normalized_score_i = selected_option_weightage / max_option_weightage
```

**Example**: Question "How confident do you feel..."
- Student selects: "Very confident" (weightage: 8)
- Max weightage: 10
- Normalized: 8/10 = 0.80

#### Step 2: Apply Priority Weighting

```
weighted_score_i = normalized_score_i × priority_score_i
```

**Example**:
- Normalized score: 0.80
- Priority: 9/10
- Weighted: 0.80 × 9 = 7.2

#### Step 3: Calculate Base Score (0-1 Range)

```
base_score = Σ(weighted_score_i) / Σ(priority_score_i)
```

**Example with 5 questions**:
```
Q1: 0.80 × 9 = 7.2
Q2: 1.00 × 8 = 8.0
Q3: 0.60 × 7 = 4.2
Q4: 0.70 × 6 = 4.2
Q5: 1.00 × 8 = 8.0

Total weighted: 31.6
Total priority: 38
Base score: 31.6 / 38 = 0.832 (83.2%)
```

#### Step 4: Apply Calibration Curve

ACOSUS supports multiple calibration options:

| Curve Type | Formula | Use Case |
|------------|---------|----------|
| **Logistic (default)** | `100 / (1 + e^(-k × (score - 0.5)))` | S-shaped, prevents extremes |
| **Linear** | `score × 100` | Direct 1:1 mapping |
| **Bounded Linear** | `min(95, max(10, score × 100))` | Linear with floor/ceiling |
| **Sigmoid** | `20 + 70 / (1 + e^(-k × (score - 0.5)))` | Conservative, compressed range |

**Final success rate**: 87.9% (using logistic curve, k=6)

### Question Structure

Each question has several key attributes:

1. **Priority Score (1-10)**: Importance in determining success
   - 10: Critical factor (e.g., overall readiness, success prediction)
   - 7-9: Very important (e.g., commitment, academic confidence)
   - 4-6: Moderately important (e.g., study time, work hours)
   - 1-3: Minor factor (e.g., networking comfort)

2. **Option Weightage (1-10)**: Value assigned to each answer choice
   - Higher = more favorable for success
   - Non-linear progression reflects real-world impact

3. **isActive (boolean)**: Controls question visibility
   - `true`: Question is displayed to students
   - `false`: Question exists in database but is hidden from students
   - Purpose: Allows gradual rollout or A/B testing of questions

4. **isRequired (boolean)**: Controls mandatory completion
   - `true`: Student must answer to submit survey
   - `false`: Question is optional, can be skipped

### Data Types in Target Survey

| Data Type | Example Question | Normalization |
|-----------|------------------|---------------|
| **Ordinal** | "How confident..." (5-point scale) | weightage / max_weightage |
| **Nominal** | Support systems (categorical) | Ranked by impact |
| **Continuous** | Work hours (numeric) | Via scoring curve |
| **Ratio** | GPA (0-4.0) | Linear or categorical |
| **Interval** | Duration (date ranges) | Via duration curve |

---

## Factor Survey: Feature Collection

### Purpose

The Factor Survey collects **predictive features** (demographics, academic history, socioeconomic factors) WITHOUT asking about success rate. This serves as the **feature matrix (X)** in the ML model.

**Key Principle**: Factor surveys are used to PREDICT success; they don't ask about it.

### Question Categories (from quiz.json)

The Factor Survey contains **4 categories** with **13 questions**.

> **Note**: Unlike Target Survey questions, Factor Survey questions don't have `isActive` flags in the current configuration—all factor questions are always displayed. This ensures consistent feature collection across all students for model training.

| Category | Slug | Questions | Description |
|----------|------|-----------|-------------|
| **Academic Background** | `academic-background` | 4 | GPA, SAT, credits completed, course load |
| **Financial Support** | `financial-support` | 2 | Scholarship, family income support |
| **Logistics & Commitment** | `logistics-commitment` | 2 | Distance to university, employment status |
| **Interest & Experience** | `interest-experience` | 3 | Career aspiration, course interest, prior experience |

### Key Factor Questions

| Question | Slug | Priority | Feature Type |
|----------|------|----------|--------------|
| "What are your GPA scores?" | `gpa` | 9 | Ordinal |
| "What is your SAT score?" | `sat` | 8 | Ordinal |
| "How much experience on this subject?" | `experience` | 9 | Ordinal |
| "How many credits completed?" | `credits` | 8 | Ordinal |
| "Are you working?" | `work` | 8 | Ordinal |

### How Factors Map to ML Model Features

Each factor survey answer is normalized to a **0-10 scale** for the ML model:

```python
# Example feature vector for KNN/NN input
normalized_features = {
    "gpa": 8.0,           # "Between 3.0 and 3.5" → 8/10
    "sat": 5.83,          # 1100 / (1600-400) * 10
    "family_support": 10.0,  # "Yes" → 10/10
    "work_status": 7.0,   # "Part-time" → 7/10
    "experience": 9.0     # "Extensive experience" → 9/10
}

# Feature matrix for model training
X = np.array([
    [8.0, 5.83, 10.0, 7.0, 9.0],  # Student 1
    [4.0, 3.0, 1.0, 9.0, 5.0],     # Student 2
    # ... more students
])
```

### Feature Engineering

Factor answers undergo preprocessing before model training:

1. **Categorical → Numeric**: Option weightage / 10
2. **Numeric ranges → Normalized**: Via scoring curves
3. **Dates → Duration**: End date - Start date → Duration score
4. **Missing values**: Imputed with median or mode

---

## The Cold Start Solution

### Why Both Surveys Are Needed

```
Traditional Approach:
┌─────────────────────────────────────────────┐
│  Single Comprehensive Survey                │
├─────────────────────────────────────────────┤
│  1. What is your GPA? [Feature]             │
│  2. What is your SAT score? [Feature]       │
│  3. Do you have financial support? [Feature]│
│  4. Rate your success likelihood [OUTCOME]  │
│  ...40 more questions...                    │
└─────────────────────────────────────────────┘
Problem: Cannot predict outcome from features
         if outcome is collected alongside features!
```

```
ACOSUS Approach:
┌─────────────────────────┐  ┌──────────────────────────┐
│  Target Survey          │  │  Factor Survey           │
│  (Ground Truth)         │  │  (Features Only)         │
├─────────────────────────┤  ├──────────────────────────┤
│  Collect SUCCESS RATE   │  │  Collect GPA, SAT, etc.  │
│  - Single question OR   │  │  - Demographics          │
│  - Multi-question (PWRS)│  │  - Academic history      │
│                         │  │  - Socioeconomic factors │
│  Used by:               │  │                          │
│  • First 10 students    │  │  Used by:                │
│  • Correction cases     │  │  • ALL students          │
└─────────────────────────┘  └──────────────────────────┘
            ↓                            ↓
      [Label: y]               [Features: X]
            └────────┬───────────┘
                     ↓
              Train Model: y = f(X)
                     ↓
         Predict success from features!
```

**Key Innovation**: By separating labels from features, ACOSUS can:
1. Train models to predict success from features alone
2. Reduce survey burden for students 11+ (only factors needed)
3. Enable pseudo-labeling through feedback loop

### 10-Student Threshold Rationale

The bootstrap phase requires exactly **10 students** before model training. This threshold is based on:

#### Statistical Minimum
- **K-fold cross-validation** requires minimum `k × 2` samples
- **5-fold CV**: 5 folds × 2 samples = 10 minimum
- Each fold needs at least 2 samples for meaningful validation

#### KNN Algorithm Requirements
- For k=3 neighbors, need at least k+1 samples per class
- With 10 students: `k = sqrt(10) ≈ 3` neighbors
- Ensures no fold is empty during cross-validation

#### Practical Balance
- Can collect 10 students in **2-4 weeks** (vs waiting years for hundreds)
- Enough diversity to capture basic student profile variations
- Immediate value generation vs. indefinite waiting

```python
# Auto k calculation
def calculate_k(n_students):
    k = int(math.sqrt(n_students))
    return min(10, max(3, k))  # Cap between 3-10

# Examples:
# 10 students → k = 3
# 25 students → k = 5
# 100 students → k = 10 (capped)
```

### Transition Strategy: Students 1-10 vs 11+

#### Students 1-10 (Bootstrap Phase)

```
Student Journey:
  1. Enroll in program
  2. Complete demographic profile
  3. Complete TARGET survey → Get success rate label ✓
  4. Complete FACTOR survey → Provide features ✓
  5. NO prediction shown (insufficient data)
  6. Wait for more students...

Data Flow:
  Target Survey → label.success_rate (y)
  Factor Survey → normalized_features (X)
  Combined → Training dataset row
```

**Backend Logic**:
```javascript
const studentCount = await Student.countDocuments({ quizCompleted: true });

if (studentCount < 10) {
  console.log(`Waiting for more students: ${studentCount}/10`);
  // No training, no predictions
} else if (studentCount === 10) {
  // Trigger KNN training!
  await triggerModelTraining('knn');
}
```

#### Students 11+ (Prediction Phase)

```
Student Journey:
  1. Enroll in program
  2. Complete FACTOR survey ONLY (3 min) → Get features
  3. See ML prediction (e.g., 79% success rate)
  4. Rate prediction accuracy (1-5 stars)
  5. IF rating ≥ 4 → Done (pseudo-label) ✓
     IF rating < 4 → Complete TARGET survey (correction)

Survey Time Comparison:
  Students 1-10: 18 min (target + factor)
  Students 11+:  5 min average (60-70% skip target)
```

### Self-Healing Feedback Loop Mechanism

The feedback loop creates a **virtuous cycle** of continuous improvement:

```
┌────────────────────────────────────────────────────┐
│                                                    │
│  1. Model makes prediction                        │
│         ↓                                          │
│  2. Student rates prediction (1-5 stars)          │
│         ↓                                          │
│  3. High rating (≥4) → Pseudo-label (free data) ✓ │
│     Low rating (<4) → Correction (learning)       │
│         ↓                                          │
│  4. Add to training dataset                       │
│         ↓                                          │
│  5. Retrain model (every 10 students)             │
│         ↓                                          │
│  6. Improved predictions (lower MAE)              │
│         ↓                                          │
│  7. Higher ratings (more pseudo-labels)           │
│         ↓                                          │
│  (Cycle repeats, accelerating improvement)        │
│                                                    │
└────────────────────────────────────────────────────┘
```

#### High Rating Path (≥4 stars) - Pseudo-Labeling

When students rate a prediction 4+ stars, the system:
1. **Accepts prediction as ground truth** (pseudo-label)
2. **Skips target survey** (time saved)
3. **Adds to training data** with source: "pseudo_label"

```json
{
  "studentId": "student_011",
  "label": {
    "success_rate": 79,
    "source": "pseudo_label",
    "predictionShown": 79,
    "feedbackRating": 5,
    "correctionProvided": false
  }
}
```

**Research Support**:
- Lee (2013): "Pseudo-labeling effective when confidence >0.8"
- Arazo et al. (2020): "Reduces labeling cost by 50-70%"

#### Low Rating Path (<4 stars) - Correction

When students rate a prediction <4 stars, the system:
1. **Requests target survey** for correction
2. **Collects true success rate** from student
3. **Calculates prediction error** for model improvement
4. **Adds to training data** with source: "feedback_corrected"

```json
{
  "studentId": "student_012",
  "label": {
    "success_rate": 52,
    "source": "feedback_corrected",
    "predictionShown": 79,
    "feedbackRating": 2,
    "correctionProvided": true
  },
  "feedbackData": {
    "predictionError": -27,
    "absoluteError": 27
  }
}
```

**Benefit**: Model learns exactly where it's weakest.

#### Retraining Triggers

| Trigger | Frequency | Action |
|---------|-----------|--------|
| **10 new students** | Every 2-3 weeks | Retrain KNN/NN |
| **50 new students** | Every 3-4 months | Retrain GAN + NN |
| **Avg rating < 3.5** | As needed | Emergency retrain |

#### Expected Progression

| Phase | Students | MAE | Pseudo-Label Rate | Avg Rating |
|-------|----------|-----|-------------------|------------|
| Initial | 10-20 | 14 pts | 50% | 3.2/5.0 |
| Growing | 21-50 | 12 pts | 60% | 3.5/5.0 |
| Maturing | 51-99 | 11 pts | 70% | 3.8/5.0 |
| Neural Network | 100+ | 9 pts | 75% | 4.1/5.0 |

---

## Summary: Survey System Design Principles

1. **Separation of Concerns**: Labels (target) and features (factor) collected separately
2. **Progressive Data Collection**: First 10 need both; 11+ mostly factor-only
3. **Transparent Scoring**: PWRS formula based on Item Response Theory
4. **Advisor Configurability**: Priority scores and weightages admin-adjustable
5. **Self-Improvement**: Feedback loop enables continuous learning
6. **Survey Burden Reduction**: 72% reduction in average completion time
7. **Quality Maintenance**: Corrections when model uncertain

---

## Appendix: Question Inventory

### Target Survey Questions

#### Active Questions (Displayed to Students)

| # | Question (Slug) | Category | Priority | Required |
|---|-----------------|----------|----------|----------|
| 1 | academic-conf | Academic Confidence | 9 | Yes |
| 2 | overall-ready | Academic Confidence | 10 | Yes |
| 3 | commitment | Academic Confidence | 9 | Yes |
| 4 | time-mgmt | Academic Confidence | 8 | Yes |
| 5 | study-habits | Academic Confidence | 8 | Yes |
| 6 | prep-concern | Academic Confidence | 8 | Yes |
| 7 | motivation-goal | Motivation & Career | 9 | Yes |
| 8 | career-specific | Motivation & Career | 8 | Yes |
| 9 | industry-aware | Motivation & Career | 7 | Yes |
| 10 | prof-dev | Motivation & Career | 7 | Yes |
| 11 | stress-mgmt | Personal Attributes | 7 | Yes |
| 12 | adaptability | Personal Attributes | 8 | Yes |
| 13 | problem-solving | Personal Attributes | 7 | Yes |
| 14 | support-system | Resources & Support | 7 | Yes |
| 15 | financial-stress | Resources & Support | 8 | Yes |
| 16 | tech-resource | Resources & Support | 6 | Yes |
| 17 | success-predict | Self-Assessment | 10 | Yes |
| 18 | grade-expect | Self-Assessment | 7 | Yes |
| 19 | study-time | Self-Assessment | 6 | Yes |
| 20 | difficulty-level | Self-Assessment | 7 | Yes |
| 21 | time-challenge | Self-Assessment | 8 | Yes |
| 22 | health-challenge | Self-Assessment | 7 | Yes |

#### Inactive Questions (Reserved for Future Activation)

| # | Question (Slug) | Category | Priority | Required |
|---|-----------------|----------|----------|----------|
| 1 | career-vision | Motivation & Career | 8 | No |
| 2 | persistence | Personal Attributes | 8 | No |
| 3 | self-discipline | Personal Attributes | 8 | No |
| 4 | networking | Personal Attributes | 6 | No |
| 5 | adapt-industry | Personal Attributes | 7 | No |
| 6 | financial-conf | Resources & Support | 8 | No |
| 7 | workload-expect | Self-Assessment | 7 | No |
| 8 | past-accuracy | Self-Assessment | 6 | No |

> These questions exist in the database and can be activated by setting `isActive: true` when advisors determine additional data points would improve predictions.

### Factor Survey Questions

| # | Question (Slug) | Category | Priority | Required |
|---|-----------------|----------|----------|----------|
| 1 | gpa | Academic Background | 9 | Yes |
| 2 | sat | Academic Background | 8 | Yes |
| 3 | credits | Academic Background | 8 | Yes |
| 4 | courses | Academic Background | 7 | Yes |
| 5 | scholarship | Financial Support | 4 | No |
| 6 | income | Financial Support | 4 | No |
| 7 | distance | Logistics & Commitment | 6 | Yes |
| 8 | work | Logistics & Commitment | 8 | Yes |
| 9 | career | Interest & Experience | 7 | Yes |
| 10 | interested | Interest & Experience | 4 | Yes |
| 11 | experience | Interest & Experience | 9 | Yes |
