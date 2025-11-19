# Survey Methodology: Target + Factor System

## Slide 8: Dual-Survey Innovation (3 minutes)

### Why Two Survey Types?

**The Innovation**: Most ML systems collect features and outcomes together in ONE survey.
ACOSUS separates them to enable **progressive learning**.

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

---

### Target Survey: Ground Truth Collection

**Purpose**: Collect actual/perceived success rates from students

**Frequency**:
- First 10 students: REQUIRED (everyone takes target survey)
- Students 11+: CONDITIONAL (only if prediction rating <4 stars)

---

#### Type 1: Single-Question Target Survey

**Design Philosophy**: Simple, direct self-assessment

```
┌─────────────────────────────────────────────────────────────┐
│  Success Rate Self-Assessment                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  On a scale of 0-100%, what is your self-assessed          │
│  likelihood of excelling in your academic and career        │
│  journey?                                                   │
│                                                             │
│  This includes:                                             │
│  • Completing courses successfully                          │
│  • Maintaining a strong GPA (>3.0)                          │
│  • Graduating on time                                       │
│  • Developing career-ready skills                           │
│  • Engaging actively in your program                        │
│                                                             │
│  0% ────────────────●──────────────── 100%                  │
│  (No chance)       75%         (Absolutely will)            │
│                                                             │
│  [Submit Success Rate]                                      │
└─────────────────────────────────────────────────────────────┘

Result: Direct success rate = 75%
Source: "self_reported"
```

**Advantages**:
- ✅ Fast (30 seconds)
- ✅ Simple to understand
- ✅ High completion rate (~98%)
- ✅ Direct ground truth

**Disadvantages**:
- ❌ Subject to individual bias (overconfidence/underconfidence)
- ❌ No validation mechanism
- ❌ Single data point (no redundancy)

---

#### Type 2: Multi-Question Target Survey (with PWRS)

**Design Philosophy**: Comprehensive assessment with validation

**Question Structure**: Each question has TWO key attributes:

1. **Priority Score (1-10)**: How important is this question?
2. **Option Weightage (1-10)**: Value assigned to each answer choice

---

### Understanding Priority Scores

**Priority Score**: Indicates the **importance** of a question in determining success.

**Scale**: 1-10 (admin-configurable)
- **10**: Critical factor (e.g., "Academic confidence")
- **7-9**: Very important (e.g., "Support systems")
- **4-6**: Moderately important (e.g., "Work hours")
- **1-3**: Minor factor (e.g., "Commute time")

**Theoretical Foundation**: Item Response Theory (IRT)
- Questions with higher "discrimination parameters" (our priority scores)
- Contribute more to the overall assessment
- Standard in educational testing (SAT, GRE, TOEFL)

**Example Questions with Priority Scores**:

```typescript
Question 1: "How confident are you in your academic preparation?"
Priority: ⭐⭐⭐⭐⭐⭐⭐⭐⭐ (9/10)
Rationale: Academic confidence strongly predicts success
Literature: Bandura (1997) - Self-efficacy theory

Question 2: "What support systems do you have?"
Priority: ⭐⭐⭐⭐⭐⭐⭐⭐ (8/10)
Rationale: Social support crucial for retention
Literature: Tinto (1993) - Student integration model

Question 3: "How many hours per week do you work?"
Priority: ⭐⭐⭐⭐⭐⭐ (6/10)
Rationale: Work hours impact study time
Literature: Correlational, not causal

Question 4: "How far is your commute?"
Priority: ⭐⭐⭐ (3/10)
Rationale: Minor convenience factor
Literature: Weak correlation with outcomes
```

---

### Understanding Option Weightages

**Option Weightage**: Indicates the **value** of selecting a particular answer.

**Scale**: Typically 1-10, but flexible (admin-configurable)
- Higher weightage = more favorable for success
- Lower weightage = less favorable for success

**Measurement Scales**:

#### 1. Ordinal Scale (Ordered Categories)

**Example**: Academic Confidence

```typescript
Question: "How confident are you in your academic preparation?"
Type: Ordinal (ordered from low to high)
Priority Score: 9/10

Options:
┌────────────────────────────────────────────────────────┐
│ ○ Not confident at all                                 │
│   Weightage: 1                                         │
│   Interpretation: Very low self-efficacy               │
├────────────────────────────────────────────────────────┤
│ ○ Somewhat confident                                   │
│   Weightage: 4                                         │
│   Interpretation: Moderate uncertainty                 │
├────────────────────────────────────────────────────────┤
│ ● Very confident                                       │
│   Weightage: 8                                         │
│   Interpretation: Strong self-belief                   │
├────────────────────────────────────────────────────────┤
│ ○ Extremely confident                                  │
│   Weightage: 10                                        │
│   Interpretation: Exceptional self-efficacy            │
└────────────────────────────────────────────────────────┘

Selected: "Very confident" (weightage: 8)
Normalized: 8/10 = 0.80
```

**Why these weightages?**
- Non-linear progression (1, 4, 8, 10) reflects real-world impact
- Gap between "Not confident" (1) and "Somewhat" (4) is significant
- Smaller gap between "Very" (8) and "Extremely" (10) - diminishing returns

---

#### 2. Nominal Scale (Unordered Categories)

**Example**: Support Systems

```typescript
Question: "What support systems do you have?"
Type: Nominal (no inherent order, but ranked by impact)
Priority Score: 8/10

Options:
┌────────────────────────────────────────────────────────┐
│ ○ None                                                 │
│   Weightage: 1                                         │
│   Interpretation: At-risk, isolated                    │
├────────────────────────────────────────────────────────┤
│ ○ Family support only                                  │
│   Weightage: 5                                         │
│   Interpretation: External support, limited campus     │
├────────────────────────────────────────────────────────┤
│ ○ Institutional support only (tutoring, advising)      │
│   Weightage: 7                                         │
│   Interpretation: Strong academic resources            │
├────────────────────────────────────────────────────────┤
│ ● Both family and institutional support                │
│   Weightage: 10                                        │
│   Interpretation: Optimal support network              │
└────────────────────────────────────────────────────────┘

Selected: "Both family and institutional" (weightage: 10)
Normalized: 10/10 = 1.00
```

**Rationale for Weightages**:
- Research shows combined support is multiplicative, not additive
- Institutional support (7) > Family support (5) for academic outcomes
- Both (10) is maximum because of synergy effect

---

#### 3. Continuous Scale (Numeric Input)

**Example**: Work Hours per Week

```typescript
Question: "How many hours per week do you work?"
Type: Numeric (continuous, 0-60 hours)
Priority Score: 6/10

Input: [Text box: _25_ hours/week]

Normalization:
  Ideal range: 0-15 hours → score 10.0 (minimal impact on studies)
  Moderate: 16-25 hours → score 7.0 (some impact, manageable)
  Heavy: 26-35 hours → score 4.0 (significant impact)
  Extreme: 36+ hours → score 2.0 (severe impact on studies)

  Student input: 25 hours
  Normalized score: 7.0
```

**Normalization Formula**:
```python
def normalize_work_hours(hours):
    if hours <= 15:
        return 10.0
    elif hours <= 25:
        return 10.0 - ((hours - 15) / 10) * 3.0  # 10 → 7
    elif hours <= 35:
        return 7.0 - ((hours - 25) / 10) * 3.0   # 7 → 4
    else:
        return max(2.0, 4.0 - ((hours - 35) / 10) * 2.0)
```

---

#### 4. Ratio Scale (True Zero Point)

**Example**: GPA (0.0 - 4.0)

```typescript
Question: "What is your high school GPA?"
Type: Ratio (true zero, meaningful ratios)
Priority Score: 9/10

Options (categorical approximation):
┌────────────────────────────────────────────────────────┐
│ ○ Below 2.0                                            │
│   Weightage: 2                                         │
│   Interpretation: Academic struggles, high risk        │
├────────────────────────────────────────────────────────┤
│ ○ Between 2.0 and 3.0                                  │
│   Weightage: 4                                         │
│   Interpretation: Below average, needs support         │
├────────────────────────────────────────────────────────┤
│ ● Between 3.0 and 3.5                                  │
│   Weightage: 8                                         │
│   Interpretation: Strong academic foundation           │
├────────────────────────────────────────────────────────┤
│ ○ More than 3.5                                        │
│   Weightage: 10                                        │
│   Interpretation: Excellent academic preparation       │
└────────────────────────────────────────────────────────┘

Selected: "Between 3.0 and 3.5" (weightage: 8)
Normalized: 8/10 = 0.80

Alternative (numeric input):
  Input: 3.25 (exact GPA)
  Normalized: (3.25 / 4.0) * 10 = 8.125
```

---

#### 5. Interval Scale (Date Ranges → Duration)

**Example**: Program Duration

```typescript
Question 1: "When did you start your program?"
Type: Date (MM/YYYY format)
Priority Score: 6/10

Input: [08/2021]

Question 2: "When do you expect to graduate?"
Type: Date (MM/YYYY format)
Priority Score: 8/10

Input: [05/2025]

Calculation:
  Duration = 05/2025 - 08/2021 = 3.75 years

Duration Scoring Logic:
  Ideal: 3.5-4.5 years → score 10.0 (standard 4-year degree)
  Too short: <2 years → score 3.0 (accelerated, high stress)
  Too long: >6 years → score 4.0 (extended, potential struggles)

  Student duration: 3.75 years
  Normalized score: 10.0 (within ideal range)
```

**Duration Scoring Curve**:
```python
def calculate_duration_score(years):
    if years <= 0:
        return 0.0
    elif years < 2:
        return years * 2.5  # Linear: 2 years = 5.0
    elif 3.5 <= years <= 4.5:
        return 10.0  # Ideal range
    elif 2 <= years < 3.5:
        return 5.0 + ((years - 2) / 1.5) * 5.0  # 2→3.5: 5→10
    elif 4.5 < years <= 6:
        return 10.0 - ((years - 4.5) / 1.5) * 5.0  # 4.5→6: 10→5
    else:
        return max(2.0, 10.0 - (years - 4) * 1.5)  # Decay
```

**Visual Curve**:
```
Score
10 ┤           ╭────╮
 9 ┤         ╭─╯    ╰─╮
 8 ┤       ╭─╯        ╰─╮
 7 ┤     ╭─╯            ╰─╮
 6 ┤   ╭─╯                ╰─╮
 5 ┤  ╭╯                    ╰─╮
 4 ┤ ╭╯                       ╰─────
 3 ┤╭╯
 2 ┼╯
 1 ┤
 0 ┤────┬────┬────┬────┬────┬────┬────
   0    2   3.5  4.5   6    8   10  Years
        │    │    │    │
        │    └────┴────┘ Ideal Range
        │  Too Short   Too Long
```

---

### PWRS Formula: Priority-Weighted Response Scoring

**Complete 4-Step Process**:

#### Step 1: Normalize Each Answer (0-1 Scale)

```python
normalized_score_i = selected_option_weightage / max_option_weightage
```

**Example**:
```
Question 1: Academic Confidence
  Student selected: "Very confident" (weightage: 8)
  Max weightage: 10
  Normalized: 8/10 = 0.80

Question 2: Support Systems
  Student selected: "Both family & institutional" (weightage: 10)
  Max weightage: 10
  Normalized: 10/10 = 1.00

Question 3: Financial Stability
  Student selected: "Partial scholarship" (weightage: 6)
  Max weightage: 10
  Normalized: 6/10 = 0.60

Question 4: Work Hours
  Student input: 25 hours/week
  Normalized via curve: 7.0/10 = 0.70

Question 5: Program Duration
  Calculated: 3.75 years
  Score: 10.0
  Normalized: 10.0/10 = 1.00
```

---

#### Step 2: Apply Priority Weighting

```python
weighted_score_i = normalized_score_i × priority_score_i
```

**Example**:
```
Q1: 0.80 × 9 = 7.2
Q2: 1.00 × 8 = 8.0
Q3: 0.60 × 7 = 4.2
Q4: 0.70 × 6 = 4.2
Q5: 1.00 × 8 = 8.0

Total weighted: 7.2 + 8.0 + 4.2 + 4.2 + 8.0 = 31.6
```

---

#### Step 3: Calculate Base Score (0-1 Range)

```python
base_score = sum(weighted_score_i) / sum(priority_score_i)
```

**Example**:
```
Sum of priorities: 9 + 8 + 7 + 6 + 8 = 38

Base score = 31.6 / 38 = 0.832
```

**Interpretation**: Student scores 83.2% on a linear scale BEFORE calibration.

---

#### Step 4: Apply Calibration Curve

**Four Calibration Options** (admin-selectable):

##### Option A: Logistic Curve (Recommended)

```python
def logistic_curve(base_score, k=6):
    return 100 / (1 + math.exp(-k * (base_score - 0.5)))

Final success rate = logistic_curve(0.832) = 82.7%
```

**Why Logistic?**
- S-shaped distribution mirrors real-world success patterns
- Prevents extreme values (rarely 0% or 100%)
- Students with poor prep still have SOME chance (motivation)
- Well-prepared students face uncertainties (realistic)

**Calculation Breakdown**:
```
base_score = 0.832
k = 6 (steepness parameter)

exponent = -6 * (0.832 - 0.5)
         = -6 * 0.332
         = -1.992

denominator = 1 + e^(-1.992)
            = 1 + 0.137
            = 1.137

success_rate = 100 / 1.137 = 87.9%
```

---

##### Option B: Linear (No Curve)

```python
def linear_curve(base_score):
    return base_score * 100

Final success rate = 0.832 * 100 = 83.2%
```

**When to use**: Maximum transparency, direct 1:1 mapping

---

##### Option C: Bounded Linear (Clipped)

```python
def bounded_linear_curve(base_score, min_rate=10, max_rate=95):
    return min(max_rate, max(min_rate, base_score * 100))

Final success rate = min(95, max(10, 83.2)) = 83.2%
```

**When to use**: Linear simplicity but avoid absolute certainty (0% or 100%)

---

##### Option D: Sigmoid (Softer S-Curve)

```python
def sigmoid_curve(base_score, k=4):
    return 20 + 70 / (1 + math.exp(-k * (base_score - 0.5)))

Final success rate = 20 + 70 / (1 + e^(-1.328)) = 78.4%
```

**When to use**: Conservative approach, avoiding strong statements at extremes

---

### Calibration Curve Comparison

| Base Score | Linear | Logistic (k=6) | Sigmoid (k=4) | Bounded Linear |
|------------|--------|----------------|---------------|----------------|
| 0.0 | 0% | 2% | 20% | 10% |
| 0.2 | 20% | 17% | 28% | 20% |
| 0.4 | 40% | 38% | 45% | 40% |
| 0.5 | 50% | 50% | 55% | 50% |
| 0.6 | 60% | 62% | 65% | 60% |
| 0.8 | 80% | 78% | 82% | 80% |
| 0.9 | 90% | 82% | 88% | 90% |
| 1.0 | 100% | 98% | 90% | 95% |

**Visual Representation**:
```
Success Rate (%)
100 ┤                        ╭── Bounded (95% cap)
 90 ┤                  ╭─────╯
 80 ┤             ╭────╯   ╭─── Sigmoid (k=4)
 70 ┤        ╭────╯    ╭───╯
 60 ┤    ╭───╯     ╭───╯  ╭─── Logistic (k=6)
 50 ┤╭───╯     ╭───╯  ╭───╯
 40 ┼╯     ╭───╯  ╭───╯ ╭─── Linear
 30 ┤  ╭───╯  ╭───╯ ╭───╯
 20 ┤──╯  ╭───╯ ╭───╯ ← Sigmoid floor (20%)
 10 ┤ ╭───╯ ╭───╯ ← Bounded floor (10%)
  0 ┤─╯─────╯───────────────
    0.0   0.5   1.0  Base Score
```

---

### Complete Example: Multi-Question Target Survey

**Student: Jane Doe**

**Survey Questions & Responses**:

```
Q1: "How confident are you in your academic preparation?"
    Priority: 9/10
    Selected: "Very confident" (weightage: 8)
    Normalized: 8/10 = 0.80
    Weighted: 0.80 × 9 = 7.2

Q2: "What support systems do you have?"
    Priority: 8/10
    Selected: "Both family & institutional" (weightage: 10)
    Normalized: 10/10 = 1.00
    Weighted: 1.00 × 8 = 8.0

Q3: "What is your financial situation?"
    Priority: 7/10
    Selected: "Partial scholarship" (weightage: 6)
    Normalized: 6/10 = 0.60
    Weighted: 0.60 × 7 = 4.2

Q4: "How many hours per week do you work?"
    Priority: 6/10
    Input: 25 hours
    Normalized: 0.70 (via curve)
    Weighted: 0.70 × 6 = 4.2

Q5: "What is your expected program duration?"
    Priority: 8/10
    Calculated: 3.75 years (08/2021 → 05/2025)
    Normalized: 1.00 (ideal range)
    Weighted: 1.00 × 8 = 8.0
```

**PWRS Calculation**:
```
Total weighted score: 7.2 + 8.0 + 4.2 + 4.2 + 8.0 = 31.6
Total priority: 9 + 8 + 7 + 6 + 8 = 38

Base score: 31.6 / 38 = 0.832
```

**Calibration** (Logistic, k=6):
```
Success rate = 100 / (1 + e^(-6 * (0.832 - 0.5)))
             = 100 / (1 + e^(-1.992))
             = 100 / 1.137
             = 87.9%
```

**Validation**:
```
Calculated success rate: 87.9%
Student's presumed rate: 85.0% (self-assessment)

Difference: |87.9 - 85.0| = 2.9 points
Agreement: Excellent (within 5 points)
```

**Final Result**:
```json
{
  "studentId": "student_008",
  "label": {
    "success_rate": 88,  // Rounded calculated rate
    "source": "calculated",
    "collectedAt": "2025-11-18T14:20:00Z"
  },
  "correlationData": {
    "calculatedRate": 88,
    "presumedRate": 85,
    "difference": 3,
    "agreementLevel": "excellent"
  }
}
```

---

### Correlation Validation (After 10 Students)

**Purpose**: Validate that PWRS formula produces accurate success rates

**Process**:
```
After 10 students complete multi-question target survey:

1. Backend collects correlation data points:
   {
     "student_001": { calculated: 91, presumed: 90 },
     "student_002": { calculated: 45, presumed: 50 },
     "student_003": { calculated: 73, presumed: 70 },
     ...
   }

2. Backend calls Model Server:
   POST /api/v1/calculate_correlation
   {
     "modelName": "model_quiz_ABC123",
     "correlationType": "target_survey",
     "dataPoints": [...]
   }

3. Model Server calculates:
   - Pearson correlation coefficient (r)
   - Spearman rank correlation (ρ)
   - Mean absolute difference (MAD)
   - Root mean square error (RMSE)

4. Model Server returns quality assessment:
   {
     "pearson_r": 0.89,
     "mean_absolute_difference": 3.2,
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

### Factor Survey: Feature Collection

**Purpose**: Collect predictive features WITHOUT asking about success rate

**Key Principle**: Factor surveys are used to PREDICT success; they don't ask about it.

**Frequency**: ALL students, every enrollment

**Categories**:

#### 1. Demographics (Categorical)
```
Age Group:
  Priority: 3/10
  Options:
    - "18-22" (weightage: 8)  # Traditional age, high engagement
    - "23-30" (weightage: 7)  # Mature, motivated
    - "31-40" (weightage: 6)  # Balancing work/life
    - "40+" (weightage: 5)    # Time constraints

Gender:
  Priority: 2/10 (low priority, included for diversity tracking)
  Options:
    - "Male" (weightage: 5)
    - "Female" (weightage: 5)
    - "Non-binary" (weightage: 5)
    - "Prefer not to say" (weightage: 5)
  Note: Equal weightage (no gender bias in predictions)

Ethnicity:
  Priority: 2/10 (diversity tracking, not predictive)
  Options: All equal weightage (5/10)

First-Generation Student:
  Priority: 5/10
  Options:
    - "No" (weightage: 7)   # Family experience with college
    - "Yes" (weightage: 4)  # Less family guidance
```

---

#### 2. Academic Background (Ordinal & Continuous)

```
High School GPA:
  Priority: 9/10 (strongest predictor)
  Options:
    - "Below 2.0" (weightage: 2)
    - "2.0-3.0" (weightage: 4)
    - "3.0-3.5" (weightage: 8)
    - ">3.5" (weightage: 10)

SAT/ACT Score:
  Priority: 8/10
  Type: Numeric (400-1600 for SAT)
  Normalization: (score - 400) / (1600 - 400) * 10

Transfer Credits:
  Priority: 6/10
  Options:
    - "0 credits" (weightage: 5)      # Fresh start
    - "1-30 credits" (weightage: 7)   # Some experience
    - "31-60 credits" (weightage: 10) # Strong foundation
    - "60+ credits" (weightage: 8)    # May have struggles

Previous Institution:
  Priority: 5/10
  Options:
    - "None" (weightage: 5)
    - "Community College" (weightage: 7)
    - "University" (weightage: 8)
```

---

#### 3. Socioeconomic Factors (Categorical & Ordinal)

```
Family Financial Support:
  Priority: 7/10
  Options:
    - "Yes, full support" (weightage: 10)
    - "Partial support" (weightage: 7)
    - "No support" (weightage: 3)

Work Hours per Week:
  Priority: 6/10
  Type: Numeric (0-60 hours)
  Normalization: Via duration curve (ideal: 0-15 hours)

Scholarship Status:
  Priority: 5/10
  Options:
    - "Full scholarship" (weightage: 10)
    - "Partial scholarship" (weightage: 7)
    - "No scholarship" (weightage: 4)
```

---

#### 4. Temporal Features (Dates)

```
Program Start Date:
  Priority: 6/10
  Type: Date (MM/YYYY)
  Combined with graduation date for duration calculation

Expected Graduation Date:
  Priority: 8/10
  Type: Date (MM/YYYY)

Calculated Duration:
  Priority: 8/10 (derived feature)
  Normalization: Via scoring curve (ideal: 3.5-4.5 years)
```

---

### Data Flow: Target + Factor Integration

```
┌─────────────────────────────────────────────────────────────┐
│  Student #1-10 (Bootstrap Phase)                            │
└─────────────┬───────────────────────────────────────────────┘
              │
              ▼
      ┌───────────────────┐
      │ Complete Profile  │
      │ (demographics)    │
      └───────┬───────────┘
              │
              ▼
      ┌────────────────────────────────┐
      │ Complete Target Survey         │
      │ (get success rate)             │
      │                                │
      │ IF single-question:            │
      │   → Direct input: 75%          │
      │                                │
      │ IF multi-question:             │
      │   → Answer 5-10 questions      │
      │   → PWRS calculates: 88%       │
      │   → Validate with presumed: 85%│
      └───────┬────────────────────────┘
              │
              ▼
      ┌───────────────────┐
      │ Complete Factor   │
      │ Survey            │
      │ (features only)   │
      └───────┬───────────┘
              │
              ▼
      ┌────────────────────────────────┐
      │ Backend:                       │
      │ - Store label.success_rate     │
      │ - Store factorAnswers          │
      │ - Check: count == 10?          │
      │   YES → Train KNN model        │
      └────────────────────────────────┘
```

---

### Speaking Points Summary

**Key Messages**:

1. **Dual-Survey Innovation**: "We separate ground truth collection (target) from feature collection (factor) - enabling progressive learning that traditional systems cannot achieve."

2. **PWRS Formula Transparency**: "Our success rate calculation uses Item Response Theory - the same proven method as SAT and GRE exams. It's not a black box."

3. **Priority Scores**: "Admins can configure which questions matter most. Academic confidence (priority 9/10) contributes more than commute time (priority 3/10)."

4. **Option Weightages**: "Each answer has a carefully researched value. 'Very confident' (8/10) is weighted higher than 'Somewhat confident' (4/10) based on literature."

5. **Measurement Scales**: "We handle all data types - ordinal (GPA ranges), nominal (support systems), continuous (work hours), dates (duration) - normalizing everything to a 0-10 scale for the model."

6. **Validation Built-In**: "For multi-question surveys, we validate calculated rates against student self-assessments, ensuring formula accuracy before trusting predictions."
