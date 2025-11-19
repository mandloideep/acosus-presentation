# Validation Plan & Expected Results

## Slide 11: Multi-Phase Validation Strategy (3 minutes)

### Validation Philosophy

**Three Dimensions of Validation**:

1. **Model Performance** (Statistical Accuracy)
   - MAE, R², Cross-validation scores
   - Objective metrics, reproducible

2. **User Experience** (Student/Admin Satisfaction)
   - System Usability Scale (SUS)
   - Task completion rates
   - Feedback ratings

3. **Real-World Impact** (Actual Outcomes)
   - Predicted vs. actual student success
   - Intervention effectiveness
   - Longitudinal study (6-12 months)

---

## Current Status Note

**Important**: ACOSUS is currently recruiting the first 10 NEIU transfer students. The system is deployed and ready, but ML models are not yet trained due to pending data collection (0/10 students enrolled as of Nov 18, 2025).

**Success Rate Definition**: The definition of "success rate" requires further study and validation. It may include:
- GPA maintenance (e.g., >3.0 throughout program)
- On-time graduation likelihood
- Career readiness indicators
- Composite metric combining academic and career outcomes

This definition will be refined based on advisor feedback and empirical validation during the first cohort.

---

## Phase 1: Bootstrap Validation (Current - Students 1-10)

**Status**: 🟡 In Progress (0/10 NEIU transfer students enrolled as of Nov 18, 2025)
**Estimated Timeline**: Spring 2026 (targeting NEIU transfer student enrollment)

### Objectives

✅ Validate data collection pipeline
✅ Test system usability (admin + student interfaces)
✅ Ensure data quality and completeness

---

### 1.1 System Usability Testing

**Participants**:
- 2 administrators (NEIU advisors/faculty)
- 10 NEIU transfer students (first bootstrap cohort)

**Method**: Think-aloud protocol + System Usability Scale (SUS)

**Tasks for Admins**:
```
Task 1: Create a target survey (single-question type)
  Expected time: <5 minutes
  Success criterion: Survey created without errors

Task 2: Create a factor survey (7 questions with priorities)
  Expected time: <10 minutes
  Success criterion: All questions configured correctly

Task 3: Configure model settings (KNN parameters)
  Expected time: <3 minutes
  Success criterion: Settings saved successfully

Task 4: Assign surveys to student cohort
  Expected time: <2 minutes
  Success criterion: All students receive email notifications
```

**Tasks for Students**:
```
Task 1: Complete demographic profile
  Expected time: <5 minutes
  Success criterion: Profile 100% complete

Task 2: Complete target survey
  Expected time: <3 minutes (single) or <10 minutes (multi)
  Success criterion: Success rate recorded

Task 3: Complete factor survey
  Expected time: <5 minutes
  Success criterion: All questions answered
```

**Metrics**:
| Metric | Target | Measurement |
|--------|--------|-------------|
| Task completion rate | >90% | % of tasks completed without errors |
| Avg completion time | <15 min | Time from login to survey submission |
| SUS score | >70 | Standard 10-question SUS survey |
| Critical errors | 0 | Errors preventing task completion |

**SUS Questions** (1-5 scale):
1. I think I would like to use this system frequently
2. I found the system unnecessarily complex
3. I thought the system was easy to use
4. I think I would need support to use this system
5. I found the various functions well integrated
6. There was too much inconsistency in this system
7. I would imagine most people would learn this system quickly
8. I found the system very cumbersome to use
9. I felt very confident using the system
10. I needed to learn a lot before I could get going

**Pass Criteria**:
- ✅ SUS score >70 (acceptable usability)
- ✅ Task completion rate >90%
- ✅ No critical errors

---

### 1.2 Data Quality Validation

**Automated Checks** (Backend validation):

```typescript
// Run after each survey submission
async function validateDataQuality(studentId) {
  const checks = [];
  
  // Check 1: Missing data rate
  const profile = await Student.findById(studentId);
  const totalFields = 15;  // Expected profile fields
  const filledFields = countNonNullFields(profile);
  const missingDataRate = (totalFields - filledFields) / totalFields;
  
  checks.push({
    check: "Missing data rate",
    target: "<5%",
    actual: `${missingDataRate * 100}%`,
    pass: missingDataRate < 0.05
  });
  
  // Check 2: Invalid responses
  const answers = await Answer.find({ studentId });
  const invalidAnswers = answers.filter(a => !isValidAnswer(a));
  
  checks.push({
    check: "Invalid responses",
    target: "0",
    actual: invalidAnswers.length,
    pass: invalidAnswers.length === 0
  });
  
  // Check 3: Duplicate submissions
  const attempts = await Attempt.find({ studentId, quizId });
  const duplicates = attempts.length > 1;
  
  checks.push({
    check: "Duplicate submissions",
    target: "0",
    actual: attempts.length - 1,
    pass: !duplicates
  });
  
  return checks;
}
```

**Manual Review** (Researcher oversight):
- Review all 10 submissions for anomalies
- Interview 3 students: "Did you understand all questions?"
- Check for response patterns (e.g., all answers = first option)

**Pass Criteria**:
- ✅ Missing data rate <5% per field
- ✅ Invalid responses = 0 (enforced by Zod validation)
- ✅ Duplicate submissions = 0 (prevented by DB constraints)
- ✅ No suspicious response patterns

---

## Phase 2: KNN Model Validation (Students 10-20)

**Status**: 🔴 Pending (awaits 10 NEIU transfer student enrollment)
**Estimated Timeline**: Summer-Fall 2026

### Objectives

✅ Validate KNN prediction accuracy
✅ Test feedback loop mechanism
✅ Measure pseudo-labeling effectiveness

---

### 2.1 Cross-Validation (Statistical)

**Method**: 5-Fold Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor

# Load 10 students
X = normalized_features  # 10 × 4 feature matrix
y = success_rates        # 10 × 1 label vector

# Initialize KNN
knn = KNeighborsRegressor(
    n_neighbors=3,
    weights='distance',
    metric='euclidean'
)

# 5-fold cross-validation
n_folds = 5  # 2 samples per fold
mae_scores = cross_val_score(
    knn, X, y,
    cv=n_folds,
    scoring='neg_mean_absolute_error'
)

# Calculate metrics
mae = -mae_scores.mean()
std = mae_scores.std()
r2 = cross_val_score(knn, X, y, cv=n_folds, scoring='r2').mean()

# Expected results:
print(f"MAE: {mae:.2f} ± {std:.2f}")  # Target: <15 ± <5
print(f"R²: {r2:.2f}")                # Target: >0.4
```

**Metrics**:
| Metric | Target | Expected Result | Pass Criteria |
|--------|--------|-----------------|---------------|
| MAE | <15 | 14.2 ± 3.5 | ✅ Within target |
| R² | >0.4 | 0.42 | ✅ Moderate correlation |
| Std Dev | <5 | 3.5 | ✅ Stable across folds |

**Pass Criteria**:
- ✅ MAE within target range (<15)
- ✅ R² indicates moderate correlation (>0.4)
- ✅ Consistent performance across folds (std <5)

---

### 2.2 Feedback Loop Validation (Students 11-20)

**Method**: Real-world testing with feedback ratings

**Process**:
```
For each student #11-20:
  1. Complete factor survey
  2. Show KNN prediction
  3. Collect feedback rating (1-5 stars)
  4. IF rating <4: Request target survey (correction)
  5. Calculate prediction error
```

**Metrics**:
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Avg feedback rating | >3.5/5.0 | Mean of all ratings |
| Pseudo-label rate | >50% | % of students rating ≥4 |
| MAE (corrected cases) | <12 | Error on rating <4 cases |
| Survey time reduction | >50% | Avg time vs. traditional |

**Example Results** (projected):
```
Students 11-20 Feedback:

Student #11: Predicted 79%, Rating ⭐⭐⭐⭐⭐ (5) → Pseudo-label
Student #12: Predicted 68%, Rating ⭐⭐ (2) → Corrected to 52% (Error: 16)
Student #13: Predicted 82%, Rating ⭐⭐⭐⭐⭐ (5) → Pseudo-label
Student #14: Predicted 55%, Rating ⭐⭐⭐ (3) → Corrected to 48% (Error: 7)
Student #15: Predicted 74%, Rating ⭐⭐⭐⭐ (4) → Pseudo-label
Student #16: Predicted 88%, Rating ⭐⭐⭐⭐⭐ (5) → Pseudo-label
Student #17: Predicted 62%, Rating ⭐⭐ (2) → Corrected to 54% (Error: 8)
Student #18: Predicted 76%, Rating ⭐⭐⭐⭐ (4) → Pseudo-label
Student #19: Predicted 40%, Rating ⭐⭐⭐ (3) → Corrected to 35% (Error: 5)
Student #20: Predicted 85%, Rating ⭐⭐⭐⭐⭐ (5) → Pseudo-label

Results:
  Avg rating: 3.8/5.0 ✅
  Pseudo-label rate: 60% (6/10) ✅
  MAE (corrected cases): 9.0 ✅
  Survey time: 7 min avg ✅ (vs 18 min traditional)
```

**Analysis**:
- Compare pseudo-labeled vs. corrected students
- Identify patterns: "Which students disagree with predictions?"
- Adjust model if systematic bias detected

---

### 2.3 Correlation Validation (Multi-Question Targets Only)

**Applicable if**: Using multi-question target surveys

```python
# After 10 students complete multi-question target survey
correlation_data = [
    {"studentId": "001", "calculatedRate": 87, "presumedRate": 85},
    {"studentId": "002", "calculatedRate": 62, "presumedRate": 68},
    {"studentId": "003", "calculatedRate": 73, "presumedRate": 70},
    # ... 7 more students
]

# Send to Model Server
response = await fetch('http://model-server/api/v1/calculate_correlation', {
    method: 'POST',
    body: JSON.stringify({
        modelName: 'model_quiz_ABC123',
        correlationType: 'target_survey',
        dataPoints: correlation_data
    })
});

# Expected response:
{
    "pearson_r": 0.89,                    # Target: >0.85 (excellent)
    "mean_absolute_difference": 3.2,      # Target: <5 (excellent)
    "spearman_rho": 0.92,
    "quality_assessment": "excellent",
    "recommendation": {
        "use": "calculated",
        "confidence": "high"
    }
}
```

**Quality Thresholds**:
| Quality | Pearson r | Mean Abs Diff | Action |
|---------|-----------|---------------|--------|
| **Excellent** | >0.85 | <5 | ✅ Use calculated rates confidently |
| **Good** | 0.70-0.85 | 5-10 | ✅ Use calculated, monitor closely |
| **Fair** | 0.50-0.70 | 10-15 | ⚠️ Review formula, adjust priorities |
| **Poor** | <0.50 | >15 | ❌ Revise survey, recalibrate |

---

## Phase 3: Neural Network Validation (Students 100+)

**Status**: 🔴 Pending (projected: Fall 2026 - Spring 2027)
**Estimated Timeline**: After 100 NEIU transfer students enroll

### Objectives

✅ Validate GAN synthetic data quality
✅ Validate NN prediction accuracy (real validation set)
✅ Compare NN vs. KNN performance

---

### 3.1 GAN Quality Validation

**Method**: Statistical tests on synthetic vs. real data

```python
# Load real and synthetic data
real_features = load_real_students(100)        # 100 real
synthetic_features = gan.generate(400)         # 400 synthetic

# Metric 1: Correlation Similarity
real_corr = np.corrcoef(real_features.T)
synthetic_corr = np.corrcoef(synthetic_features.T)
corr_diff = np.abs(real_corr - synthetic_corr).mean()

print(f"Correlation difference: {corr_diff:.3f}")  # Target: <0.2
assert corr_diff < 0.2, "Correlation mismatch"

# Metric 2: Distribution Match (Kolmogorov-Smirnov Test)
from scipy.stats import ks_2samp

for feature in ['gpa', 'sat', 'support', 'duration']:
    statistic, p_value = ks_2samp(
        real_features[feature],
        synthetic_features[feature]
    )
    print(f"{feature}: KS statistic={statistic:.3f}, p={p_value:.3f}")
    assert p_value > 0.05, f"Distribution mismatch for {feature}"

# Metric 3: Feature Mean Similarity
real_means = real_features.mean(axis=0)
synthetic_means = synthetic_features.mean(axis=0)
mean_diff = np.abs(real_means - synthetic_means)

print(f"Mean differences: {mean_diff}")  # Target: all <0.1
assert (mean_diff < 0.1).all(), "Mean feature mismatch"
```

**Pass Criteria**:
- ✅ Correlation similarity <0.2
- ✅ KS test p-value >0.05 (distributions match)
- ✅ Feature means within 0.1 per feature

**If quality checks fail** → Retrain GAN with adjusted hyperparameters

---

### 3.2 Neural Network Validation (CRITICAL: Real-Only)

**Method**: Train on mixed data, validate on REAL students only

```python
# Step 1: Split REAL students FIRST
X_real, y_real = load_real_students()  # 100 students
X_real_train, X_real_val, y_real_train, y_real_val = train_test_split(
    X_real, y_real,
    test_size=0.2,
    random_state=42
)  # 80 train, 20 validation

# Step 2: Generate synthetic
X_synthetic, y_synthetic = gan.generate(400)

# Step 3: Train on mixed data
X_train = np.vstack([X_real_train, X_synthetic])  # 480
y_train = np.concatenate([y_real_train, y_synthetic])

# Step 4: Validate on REAL ONLY
model.fit(
    X_train, y_train,
    validation_data=(X_real_val, y_real_val),  # 20 real students
    epochs=100,
    callbacks=[EarlyStopping(patience=10)]
)

# Step 5: Evaluate
predictions = model.predict(X_real_val)
mae = mean_absolute_error(y_real_val, predictions)
r2 = r2_score(y_real_val, predictions)

print(f"MAE: {mae:.2f}")  # Target: <10
print(f"R²: {r2:.2f}")    # Target: >0.6
```

**Metrics**:
| Metric | Target | Expected Result | Pass Criteria |
|--------|--------|-----------------|---------------|
| MAE | <10 | 8.7 | ✅ Better than KNN |
| R² | >0.6 | 0.73 | ✅ Strong correlation |
| No overfitting | train_loss ≈ val_loss | Δ <0.05 | ✅ Generalizes well |

---

### 3.3 Model Comparison (A/B Testing)

**Method**: Randomly assign students to KNN or NN predictions

```python
# For students #101-120
for student in students_101_to_120:
    # Random assignment
    model_type = random.choice(['knn', 'nn'])
    
    # Get prediction
    if model_type == 'knn':
        prediction = knn.predict(student.features)
    else:
        prediction = nn.predict(student.features)
    
    # Show prediction, collect feedback
    rating = show_prediction_and_get_feedback(prediction)
    
    # Store for analysis
    results.append({
        'model': model_type,
        'prediction': prediction,
        'rating': rating,
        'actual': student.actual_success_rate  # If available
    })

# Statistical comparison
knn_results = [r for r in results if r['model'] == 'knn']
nn_results = [r for r in results if r['model'] == 'nn']

# Compare ratings
knn_avg_rating = mean([r['rating'] for r in knn_results])
nn_avg_rating = mean([r['rating'] for r in nn_results])

# T-test for significance
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(
    [r['rating'] for r in knn_results],
    [r['rating'] for r in nn_results]
)

print(f"KNN avg rating: {knn_avg_rating:.2f}")
print(f"NN avg rating: {nn_avg_rating:.2f}")
print(f"T-test p-value: {p_value:.4f}")
```

**Expected Results**:
| Metric | KNN | NN | Significance |
|--------|-----|-----|--------------|
| Avg rating | 3.5/5.0 | 4.1/5.0 | p <0.05 ✅ |
| MAE | 11.2 | 8.7 | p <0.05 ✅ |
| Confidence | 0.68 | 0.79 | p <0.05 ✅ |

---

## Phase 4: Long-Term Impact Validation (Transfer Student Outcomes)

**Status**: 🔴 Pending (future work)
**Estimated Timeline**: 2027-2028 (longitudinal tracking)

### Objectives

✅ Validate predicted success rates against actual outcomes
✅ Measure intervention effectiveness
✅ Calculate ROI for institution

---

### 4.1 Predictive Validity (Longitudinal Study)

**Timeline**: After 1-2 semesters
**Focus**: Transfer student-specific validation

```
Transfer Student Enrollment (Week 1)
    ↓
Prediction Made (Week 2)
    ↓
Intervention Assigned (Week 3)
    ↓
Semester 1 Ends (Week 16)
    ↓
Collect Actual Outcomes:
  - Semester GPA (track for "transfer shock")
  - Course completion rate
  - Retention (still enrolled? - critical for transfer students)
  - Transfer-specific metrics: GPA change from community college
    ↓
Calculate Actual Success Rate
    ↓
Compare: Predicted vs. Actual
```

**Actual Success Rate Calculation**:
```python
def calculate_actual_success_rate(student):
    """
    Calculate actual success rate from real outcomes
    """
    # Component 1: GPA (30% weight)
    gpa_score = (student.semester_gpa / 4.0) * 100
    
    # Component 2: Completion rate (25% weight)
    completion_score = (student.courses_completed / student.courses_enrolled) * 100
    
    # Component 3: Retention (20% weight)
    retention_score = 100 if student.still_enrolled else 0
    
    # Component 4: Engagement (15% weight)
    engagement_score = student.attendance_rate * 100
    
    # Component 5: Career readiness (10% weight)
    career_score = student.career_readiness_score  # From advisor assessment
    
    # Weighted composite
    actual_success_rate = (
        gpa_score * 0.30 +
        completion_score * 0.25 +
        retention_score * 0.20 +
        engagement_score * 0.15 +
        career_score * 0.10
    )
    
    return actual_success_rate

# Example:
# Student #15 (predicted 74%)
# Actual outcomes after semester 1:
#   GPA: 3.2/4.0 = 80%
#   Completed: 4/5 courses = 80%
#   Still enrolled: Yes = 100%
#   Attendance: 85%
#   Career readiness: 70%
#
# Actual = 80*0.3 + 80*0.25 + 100*0.2 + 85*0.15 + 70*0.1 = 86%
# Predicted: 74%
# Error: |74 - 86| = 12 points ✅ (within MAE <15)
```

**Validation Metrics**:
| Metric | Target | Pass Criteria |
|--------|--------|---------------|
| Correlation (r) | >0.6 | Moderate-strong correlation |
| MAE | <15 | Acceptable for long-term prediction |
| R² | >0.35 | Explains >35% variance in outcomes |

---

### 4.2 Intervention Effectiveness

**Study Design**: Compare transfer student intervention vs. control groups

```
Group A (Intervention):
  - Transfer students with ACOSUS predictions
  - Risk-based support assignments
  - Early intervention (Week 3)
  - Transfer-specific resources (e.g., credit transfer advising)

Group B (Control):
  - Historical transfer student data (previous cohorts)
  - Standard advising only
  - Late intervention (after midterm failures)
```

**Additional Transfer-Specific Validation**:
- Compare transfer vs. native student prediction accuracy
- Validate on transfer-specific metrics:
  - Retention post-transfer (37% of transfers don't return for year 2)
  - GPA change (transfer shock: 0.2-0.5 GPA drop)
  - Time-to-degree from transfer point
- Test advisor satisfaction with centralized transfer student data platform

**Metrics**:
| Outcome | Intervention Group | Control Group | Improvement | Statistical Test |
|---------|-------------------|---------------|-------------|------------------|
| Retention rate | 85% | 75% | +10% | Chi-square, p <0.05 |
| Avg GPA | 3.2 | 2.9 | +0.3 | T-test, p <0.05 |
| Time-to-degree | 4.2 years | 4.7 years | -0.5 years | T-test, p <0.05 |
| Graduation rate | 78% | 68% | +10% | Chi-square, p <0.05 |

**Pass Criteria**:
- ✅ Retention rate improvement >10%
- ✅ GPA improvement >0.3 points
- ✅ Statistical significance (p <0.05)

---

## Summary: Expected Performance Targets

### By Phase

| Phase | Students | Model | MAE Target | R² Target | Avg Feedback | Status |
|-------|----------|-------|------------|-----------|--------------|--------|
| **Bootstrap** | 10 | KNN | <15 | >0.4 | >3.0/5.0 | 🔴 Pending |
| **Growth** | 20-99 | KNN | <12 | >0.5 | >3.5/5.0 | 🔴 Pending |
| **Mature** | 100+ | NN | <10 | >0.6 | >4.0/5.0 | 🔴 Pending |
| **Longitudinal** | 100+ | NN | <15 | >0.35 | N/A | 🔴 Future |

### Validation Timeline (NEIU Transfer Students)

```
Nov 2025:        System deployed, recruiting transfer students (0/10)
Spring 2026:     Phase 1 - Usability testing (target: 10 transfer students)
Summer 2026:     Phase 2 - KNN validation (10-20 transfer students enrolled)
Fall 2026:       Phase 2 - Feedback loop analysis (20-50 transfer students)
Spring 2027:     Phase 3 - NN validation (target: 100 transfer students)
Fall 2027-2028:  Phase 4 - Long-term impact (longitudinal outcomes)
```

**Note**: Timeline depends on NEIU transfer student enrollment rates. Estimates assume 10-20 transfer students per semester in computing programs.

---

## Speaking Points Summary

**Key Messages**:

1. **Multi-Phase Approach**: "We validate in four phases - usability, model accuracy, comparison testing, and long-term impact."

2. **Real-Only Validation**: "Critically, we validate neural networks ONLY on real students, never synthetic, ensuring generalization."

3. **No Results Yet**: "System deployed Nov 18, 2025. We're transparent: no validation results yet, waiting on first 10 students."

4. **Clear Targets**: "We have specific targets for each phase - MAE <15 for KNN, <10 for NN, based on literature."

5. **Longitudinal Study**: "Long-term validation compares predicted vs. actual outcomes after 1-2 semesters."

6. **Intervention Impact**: "We'll measure if early intervention improves retention by >10% compared to historical data."
