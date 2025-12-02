# Readiness Score Calculation: Complete Documentation

## Overview

The ACOSUS system calculates student readiness scores using the **Priority-Weighted Response Scoring (PWRS)** formula. This methodology is inspired by Item Response Theory (IRT), the same statistical framework used in standardized testing (SAT, GRE, TOEFL).

The readiness score provides a single, interpretable metric (0-100%) that represents a transfer student's self-reported likelihood of academic success.

### Scope and Application

The PWRS formula applies specifically to the **Target Survey** when configured as a **multi-question survey**. ACOSUS supports two target survey modes:

| Mode | Description | Score Calculation |
|------|-------------|-------------------|
| **Single-Question** | Directly asks student their presumed readiness score (0-100%) | Direct input, no calculation needed |
| **Multi-Question** | Collects responses across multiple readiness dimensions | PWRS formula aggregates into single score |

This document focuses on the **multi-question** approach where PWRS converts diverse responses into a unified readiness score.

---

## Mathematical Formula

### Complete PWRS Formula (LaTeX Notation)

The readiness score calculation follows a 4-step process:

#### Step 1: Response Normalization

$$
s_i^{norm} = \frac{w_i^{selected}}{w_i^{max}}
$$

Where:
- $s_i^{norm}$ = Normalized score for question $i$ (range: 0-1)
- $w_i^{selected}$ = Weightage of the selected answer option
- $w_i^{max}$ = Maximum possible weightage for that question

#### Step 2: Priority Weighting

$$
s_i^{weighted} = s_i^{norm} \times p_i
$$

Where:
- $s_i^{weighted}$ = Priority-weighted score for question $i$
- $p_i$ = Priority score for question $i$ (range: 1-10)

#### Step 3: Base Score Calculation

$$
S_{base} = \frac{\sum_{i=1}^{n} s_i^{weighted}}{\sum_{i=1}^{n} p_i} = \frac{\sum_{i=1}^{n} (s_i^{norm} \times p_i)}{\sum_{i=1}^{n} p_i}
$$

Where:
- $S_{base}$ = Base readiness score (range: 0-1)
- $n$ = Total number of questions answered

#### Step 4: Calibration (Logistic Transform)

$$
S_{final} = \frac{100}{1 + e^{-k(S_{base} - 0.5)}}
$$

Where:
- $S_{final}$ = Final readiness score (range: 0-100%)
- $k$ = Steepness parameter (default: 6)
- $e$ = Euler's number (≈ 2.71828)

### Consolidated Formula

The complete formula in a single expression:

$$
\boxed{S_{final} = \frac{100}{1 + e^{-k\left(\frac{\sum_{i=1}^{n} \left(\frac{w_i^{selected}}{w_i^{max}} \times p_i\right)}{\sum_{i=1}^{n} p_i} - 0.5\right)}}}
$$

---

## Variable Definitions

### Input Variables

| Variable | Symbol | Range | Description |
|----------|--------|-------|-------------|
| **Selected Weightage** | $w_i^{selected}$ | 1-10 | Value assigned to the student's selected answer |
| **Max Weightage** | $w_i^{max}$ | 10 | Maximum possible weightage for the question |
| **Priority Score** | $p_i$ | 1-10 | Importance of question in determining success |
| **Steepness Parameter** | $k$ | 4-8 | Controls calibration curve shape (default: 6) |

### Priority Score Guidelines

Priority scores indicate the **importance** of a question in determining student success:

| Priority | Level | Example Questions |
|----------|-------|-------------------|
| **10** | Critical | Overall readiness, Success self-prediction |
| **9** | Very High | Academic confidence, Commitment, Career motivation |
| **8** | High | Time management, Study habits, Financial confidence, Adaptability |
| **7** | Moderate-High | Stress management, Career specificity, Industry awareness |
| **6** | Moderate | Study time, Technology resources, Distance to university |
| **4** | Low-Moderate | Scholarship status, Course interest |

> **Note on Priority Scores**: Current priority values are initial configurations set by domain expertise. These are **not derived from empirical research** but are designed to work within the PWRS calculation framework. The system is designed to be **dynamic**—as pilot data is collected and validated against actual outcomes, priority scores will be refined based on observed correlations with student success.

### Option Weightage Guidelines

Option weightages indicate the **favorability** of each answer choice:

**For Ordinal Scales (e.g., Confidence)**:
```
"Not at all confident"     → 1
"Slightly confident"       → 3
"Somewhat confident"       → 5
"Very confident"           → 8
"Extremely confident"      → 10
```

**For Support Systems (Nominal)**:
```
"No support"                        → 1
"Family support only"               → 5
"Institutional support only"        → 7
"Both family and institutional"     → 10
```

**For Work Hours (Continuous)**:
```
0-15 hours/week (Ideal)      → 10
16-25 hours/week (Moderate)  → 7
26-35 hours/week (Heavy)     → 4
36+ hours/week (Extreme)     → 2
```

**For GPA (Ratio Scale)**:
```
Below 2.0   → 2
2.0-2.5     → 4
2.5-3.0     → 6
3.0-3.5     → 8
Above 3.5   → 10
```

> **Note on Option Weightages**: Similar to priority scores, option weightages are initial configurations based on domain expertise rather than empirical research. These values are designed to integrate with the PWRS calculation and will be refined through the pilot validation process.

---

## Calibration Curves

ACOSUS supports four calibration options to transform base scores:

| Curve Type | Formula | Range | Use Case |
|------------|---------|-------|----------|
| **Logistic** (default) | $\frac{100}{1 + e^{-k(s - 0.5)}}$ | 2%-98% | S-shaped, prevents extremes |
| **Linear** | $s \times 100$ | 0%-100% | Direct 1:1 mapping |
| **Bounded Linear** | $\min(95, \max(10, s \times 100))$ | 10%-95% | Linear with floor/ceiling |
| **Sigmoid** | $20 + \frac{70}{1 + e^{-k(s - 0.5)}}$ | 20%-90% | Conservative, compressed |

### Calibration Comparison Table

| Base Score | Linear | Logistic (k=6) | Bounded | Sigmoid (k=4) |
|------------|--------|----------------|---------|---------------|
| 0.0 | 0% | 2% | 10% | 20% |
| 0.2 | 20% | 17% | 20% | 28% |
| 0.4 | 40% | 38% | 40% | 45% |
| 0.5 | 50% | 50% | 50% | 55% |
| 0.6 | 60% | 62% | 60% | 65% |
| 0.8 | 80% | 78% | 80% | 82% |
| 0.9 | 90% | 82% | 90% | 88% |
| 1.0 | 100% | 98% | 95% | 90% |

**Recommendation**: Use Logistic (k=6) as default. The S-shaped curve:
- Prevents unrealistic extremes (rarely 0% or 100%)
- Reflects real-world success distributions
- Provides intuitive score interpretation

---

## Score Range Interpretation

### Readiness Score Bands

| Score Range | Classification | Description |
|-------------|----------------|-------------|
| **0-30%** | **At-Risk** | Student exhibits significant barriers to success. Multiple risk factors present. Requires intensive intervention. |
| **30-40%** | **High Concern** | Substantial challenges identified. Early intervention recommended. Close monitoring essential. |
| **40-60%** | **Moderate Readiness** | Mixed indicators. Some strengths and some concerns. Standard support with targeted interventions. |
| **60-70%** | **Prepared** | Solid foundation with minor concerns. Standard advising pathway appropriate. |
| **70-85%** | **High Readiness** | Strong preparation across most factors. Enrichment opportunities recommended. |
| **85-100%** | **Exceptional Readiness** | Excellent preparation. Candidate for honors/accelerated programs. Minimal intervention needed. |

### Visual Score Distribution

```
0%        30%        40%        60%        70%        85%       100%
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│  AT-RISK │  HIGH    │ MODERATE │ PREPARED │   HIGH   │EXCEPTIONAL│
│          │ CONCERN  │          │          │ READINESS│          │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
   ████       ████        ████       ████        ████       ████
 Intensive  Early     Targeted   Standard   Enrichment  Honors/
 Intervention Support  Intervention Advising Recommended Accelerated
```

---

## Advisor Usage Guide

### How Advisors Use the Readiness Score

#### Pre-Meeting Preparation (4 minutes total)

1. **Open ACOSUS Dashboard** (1 min) - View student profile
2. **Review Readiness Score** (1 min) - Note score band and key factors
3. **Check Similar Students** (1 min) - Compare to successful transfer peers
4. **Prepare Talking Points** (1 min) - Identify areas for discussion

#### Score-Based Intervention Framework

**At-Risk (0-40%): Intensive Intervention Protocol**

| Action | Description |
|--------|-------------|
| Reduced course load | Recommend 9-12 credits maximum |
| Financial aid referral | Connect to scholarship/emergency aid |
| Weekly check-ins | Schedule recurring meetings |
| Tutoring enrollment | Mandatory tutoring center registration |
| Counseling referral | Address stress/personal barriers |
| Peer mentoring | Match with successful transfer student |

**Moderate (40-70%): Standard Support with Monitoring**

| Action | Description |
|--------|-------------|
| Study skills workshops | Recommend time management training |
| Regular advising | Bi-weekly to monthly meetings |
| Resource awareness | Ensure awareness of campus resources |
| Academic planning | Create detailed degree pathway |
| Early alert monitoring | Flag for instructor check-ins |

**High Readiness (70%+): Enrichment Pathway**

| Action | Description |
|--------|-------------|
| Advanced coursework | Recommend challenging courses |
| Research opportunities | Connect to faculty research |
| Leadership roles | Suggest student organization involvement |
| Internship referrals | Career services connection |
| Honors consideration | Evaluate for honors program eligibility |

### Using Component Scores

Advisors should examine individual component scores to identify specific intervention areas:

| Low-Scoring Component | Recommended Action |
|----------------------|-------------------|
| Academic Confidence (< 5) | Pair with successful peer mentor |
| Financial Stress (< 5) | Immediate financial aid referral |
| Time Management (< 5) | Time management workshop enrollment |
| Support Systems (< 5) | Connect to student support services |
| Study Habits (< 5) | Learning center assessment |
| Career Clarity (< 5) | Career counseling appointment |

---

## Connection to Transfer Student Success Factors

### Research-Based Factor Categories

The PWRS formula incorporates factors identified in transfer student success research:

#### 1. Academic Preparation (Weight: High)
- Prior GPA and academic performance
- Course load capacity
- Study habits and time management
- **Research Support**: Laanan (2007), Townsend & Wilson (2006)

#### 2. Psychological Readiness (Weight: High)
- Self-efficacy and confidence
- Commitment to completion
- Stress management capability
- **Research Support**: Bandura (1997), Tinto (1993)

#### 3. Support Systems (Weight: Moderate-High)
- Family support
- Institutional support awareness
- Peer connections
- **Research Support**: Kuh et al. (2006), Pascarella & Terenzini (2005)

#### 4. Financial Stability (Weight: Moderate)
- Scholarship/financial aid status
- Work hours and employment impact
- Financial stress levels
- **Research Support**: Perna (2006), Chen (2008)

#### 5. Career Motivation (Weight: Moderate)
- Goal clarity and specificity
- Industry awareness
- Professional development commitment
- **Research Support**: Deci & Ryan (2000), Lent et al. (1994)

### Transfer-Specific Considerations

The formula accounts for unique transfer student challenges:

1. **Credit Articulation Uncertainty** - Questions about course transferability
2. **Institutional Navigation** - Familiarity with new campus systems
3. **Social Reintegration** - Building new peer networks
4. **Time Compression** - Accelerated timeline to degree completion

---

## Worked Example

### Student Profile: Maria Chen

**Survey Responses**:

| Question | Response | Weightage | Max | Priority |
|----------|----------|-----------|-----|----------|
| Overall Readiness | "8 out of 10" | 8 | 10 | 10 |
| Academic Confidence | "Very confident" | 8 | 10 | 9 |
| Commitment | "Strongly committed" | 9 | 10 | 9 |
| Support Systems | "Both family & institutional" | 10 | 10 | 7 |
| Work Hours | "20 hours/week" | 7 | 10 | 8 |
| Financial Confidence | "Somewhat confident" | 6 | 10 | 8 |

### Step-by-Step Calculation

**Step 1: Normalize**
```
Q1: 8/10 = 0.80
Q2: 8/10 = 0.80
Q3: 9/10 = 0.90
Q4: 10/10 = 1.00
Q5: 7/10 = 0.70
Q6: 6/10 = 0.60
```

**Step 2: Apply Priority Weights**
```
Q1: 0.80 × 10 = 8.0
Q2: 0.80 × 9 = 7.2
Q3: 0.90 × 9 = 8.1
Q4: 1.00 × 7 = 7.0
Q5: 0.70 × 8 = 5.6
Q6: 0.60 × 8 = 4.8
```

**Step 3: Calculate Base Score**
```
Sum of weighted scores: 8.0 + 7.2 + 8.1 + 7.0 + 5.6 + 4.8 = 40.7
Sum of priorities: 10 + 9 + 9 + 7 + 8 + 8 = 51

Base Score = 40.7 / 51 = 0.798
```

**Step 4: Apply Logistic Calibration (k=6)**
```
S_final = 100 / (1 + e^(-6 × (0.798 - 0.5)))
        = 100 / (1 + e^(-1.788))
        = 100 / (1 + 0.167)
        = 100 / 1.167
        = 85.7%
```

**Result**: Maria's readiness score is **85.7%** (High Readiness)

**Advisor Interpretation**:
- Classification: **High Readiness**
- Pathway: Enrichment track
- Concern Areas: Financial confidence slightly below average
- Recommended Actions:
  - Discuss advanced course options
  - Connect to research opportunities
  - Provide information about emergency financial resources (preventive)

---

## Validation Framework

### Current Status: Pilot Phase

This system is currently in the **pilot validation phase**. The PWRS formula and its parameters (priority scores, option weightages) have been configured based on domain expertise but have **not yet been empirically validated**.

### Validation Approach

The validation strategy involves:

1. **Collecting Pilot Data** - First 10+ students complete both Target and Factor surveys
2. **Comparing Predictions** - ML-generated predictions compared against PWRS-calculated scores
3. **Student Feedback** - Students rate prediction accuracy (1-5 stars)
4. **Iterative Refinement** - Priority scores and weightages adjusted based on:
   - Correlation between calculated scores and student self-assessments
   - Prediction accuracy feedback
   - Observed patterns in student success outcomes

### Validation Quality Thresholds

Once sufficient data is collected, the PWRS formula will be validated using these metrics:

| Quality Level | Pearson Correlation (r) | Mean Absolute Difference | Action |
|---------------|------------------------|--------------------------|--------|
| **Excellent** | > 0.85 | < 5 points | Use calculated rates confidently |
| **Good** | 0.70 - 0.85 | 5-10 points | Use calculated rates, monitor |
| **Fair** | 0.50 - 0.70 | 10-15 points | Review formula, adjust priorities |
| **Poor** | < 0.50 | > 15 points | Revise survey, recalibrate |

### Dynamic Calibration

The system architecture supports **continuous improvement**:

```
┌─────────────────────────────────────────────────────────────┐
│                    VALIDATION CYCLE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Student completes survey → PWRS calculates score        │
│                    ↓                                        │
│  2. ML model makes prediction (after 10+ students)          │
│                    ↓                                        │
│  3. Compare: PWRS score vs ML prediction vs actual outcome  │
│                    ↓                                        │
│  4. If discrepancy detected:                                │
│     • Adjust priority scores for under/over-weighted items  │
│     • Refine option weightages based on outcome correlation │
│     • Consider adding/removing survey questions             │
│                    ↓                                        │
│  5. Retrain model, repeat cycle                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Administrative Configuration

### Adjustable Parameters

Administrators can modify the following to tune the formula:

1. **Priority Scores** - Increase/decrease importance of specific questions
2. **Option Weightages** - Adjust values for answer choices
3. **Calibration Curve** - Select between logistic, linear, bounded, or sigmoid
4. **Steepness Parameter (k)** - Adjust curve steepness (4-8 range)

### Configuration Guidance

| Scenario | Adjustment |
|----------|------------|
| Scores too extreme | Use Sigmoid or increase k |
| Scores too compressed | Use Linear or decrease k |
| Certain factors matter more | Increase priority scores |
| Answer options incorrectly valued | Revise weightages |

---

## References

- Bandura, A. (1997). Self-efficacy: The exercise of control.
- Chen, R. (2008). Financial aid and student dropout in higher education.
- Deci, E. L., & Ryan, R. M. (2000). Self-determination theory.
- Kuh, G. D., et al. (2006). What matters to student success.
- Laanan, F. S. (2007). Studying transfer students.
- Lent, R. W., et al. (1994). Social cognitive career theory.
- Pascarella, E. T., & Terenzini, P. T. (2005). How college affects students.
- Perna, L. W. (2006). Understanding the relationship between information and college access.
- Tinto, V. (1993). Leaving college: Rethinking the causes of student attrition.
- Townsend, B. K., & Wilson, K. (2006). Transfer students' academic and social experiences.

---

## Summary

The PWRS formula provides a mathematically structured approach to calculating transfer student readiness scores from multi-question Target Surveys. By combining normalized response values with priority weighting and calibration curves, the system produces interpretable scores that guide advisor interventions.

Key features:
- **Transparent**: Clear formula with documented variables
- **Configurable**: Administrators can adjust priorities and weightages dynamically
- **Designed for Validation**: Built-in correlation checks with student self-assessments
- **Actionable**: Score bands map directly to intervention protocols
- **Iterative**: System designed to refine parameters as pilot data is collected

### Current Limitations

As a pilot system:
- Priority scores and option weightages are based on domain expertise, not empirical research
- Validation thresholds are theoretical targets pending real-world data collection
- Score interpretation bands may be adjusted based on observed distributions

### Next Steps

1. Complete pilot data collection (10+ transfer students)
2. Analyze correlation between PWRS scores and ML predictions
3. Gather student feedback on prediction accuracy
4. Refine priority scores and weightages based on outcomes
5. Establish institution-specific calibration parameters
