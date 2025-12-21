# ACOSUS Survey Scoring Methodology

## Overview

This document provides a comprehensive reference for the scoring methodology used in ACOSUS surveys, including data type definitions, priority score assignment, option weightage guidelines, and justification approaches for academic publication.

---

## 1. Data Type Definitions

ACOSUS surveys collect data across multiple types, each requiring specific handling for machine learning ingestion.

### 1.1 Ordinal Data

**Definition:** Categorical variables where the categories have a meaningful order or ranking. While the order is important, the intervals between the categories are not necessarily equal or known.

**Examples in ACOSUS:**
- Confidence levels: "Not confident" < "Somewhat confident" < "Very confident" < "Extremely confident"
- GPA ranges: "Below 2.0" < "2.0-3.0" < "3.0-3.5" < "Above 3.5"
- Readiness scales: "Not ready" < "Moderately ready" < "Very ready" < "Completely ready"

**Normalization:** Option weightage directly mapped to 0-10 scale.

### 1.2 Cardinal (Nominal) Data

**Definition:** Categorical variables where the categories have no intrinsic order or ranking. The values are labels for different groups, and any numerical representation is purely for identification.

**Examples in ACOSUS:**
- Career aspiration: "Academia / Research", "Industry / Corporate", "Entrepreneurship", "Public Sector"
- Scholarship status: "Yes", "No"
- Employment type: "Full-time", "Part-time", "Not employed"

**Normalization:** Sum-of-selected over sum-of-total scaling, or expert-assigned impact values.

### 1.3 Continuous Data

**Definition:** Variables that can take any value within a range, typically measured rather than counted.

**Examples in ACOSUS:**
- Work hours per week (0-40+)
- Commute distance in miles
- Numeric GPA (0.0-4.0)

**Normalization:** Min-max normalization with domain-specific bounds.

### 1.4 Label (Y): Readiness/Success Rate

**Definition:** The dependent variable that the system predicts—a continuous random variable in the range [0, 1] representing the student's likelihood of academic success.

**Collection Methods:**
1. **Single-Question:** Direct self-assessment (0-100 scale) → normalized to [0, 1]
2. **Multi-Question:** Aggregated via PWRS algorithm → produces value in [0, 1]

---

## 2. Priority Score (1-10)

### 2.1 Definition

**Priority Score** represents the importance of a question in determining the overall success/readiness construct. Higher priority scores give more weight to questions that are theoretically or empirically more predictive of student success.

| Score | Level | Description |
|-------|-------|-------------|
| 10 | Critical | Core indicators directly measuring success likelihood |
| 9 | Very High | Strong predictors based on literature (e.g., academic confidence, commitment) |
| 8 | High | Important factors with established relationships to outcomes |
| 7 | Moderate-High | Contributing factors with moderate predictive value |
| 6 | Moderate | Relevant but less direct indicators |
| 4-5 | Low-Moderate | Contextual factors with limited direct impact |
| 1-3 | Low | Background information with minimal predictive weight |

### 2.2 Justification Approach

Priority scores in ACOSUS are assigned through a **hybrid approach combining domain expertise and literature-informed weighting**:

#### A. Literature-Based Foundation

Priority assignments are informed by prior research on transfer student success factors:

1. **Factor Analysis Studies:** Our 2023 preliminary factor analysis identified clusters of variables (academic confidence, time management, financial stability, support systems) that distinguish successful transfer students [REF: 2023 Factor Analysis Paper].

2. **Social-Cognitive Research:** Investigation of social-cognitive factors affecting computing transfer students established theoretical basis for which psychological constructs predict persistence [REF: 2022 Social Cognitive Paper].

3. **Transfer Student Literature:** Established research on transfer shock, belonging uncertainty, and institutional integration informs which factors receive higher priority (Laanan, 2007; Townsend & Wilson, 2006; Tinto, 1993).

#### B. Expert Calibration

Domain experts (academic advisors, education researchers) review and adjust priority scores based on:
- Observed patterns in advising sessions
- Institutional context and student population characteristics
- Practical relevance for intervention planning

#### C. Iterative Refinement

The system is designed for **dynamic calibration**—as pilot data is collected, priority scores are refined based on:
- Correlation between individual question responses and overall outcomes
- Feature importance from trained ML models
- Student feedback on prediction accuracy

### 2.3 Example Priority Assignments

| Question Category | Example Question | Priority | Justification |
|------------------|------------------|----------|---------------|
| Self-Assessment | "Rate your overall readiness (1-10)" | 10 | Direct measure of construct |
| Self-Assessment | "Predict your own success likelihood" | 10 | Meta-cognitive self-assessment |
| Academic | "How confident in your ability to succeed?" | 9 | Academic self-efficacy (Bandura, 1997) |
| Commitment | "How committed to completing this program?" | 9 | Persistence indicator (Tinto, 1993) |
| Career | "How clear are your career goals?" | 9 | Goal clarity predicts motivation |
| Academic | "Rate your time management skills" | 8 | Strongly predicts academic performance |
| Financial | "Expected financial stress impact" | 8 | Financial precarity affects persistence |
| Personal | "How adaptable to new environments?" | 8 | Transfer adjustment factor |
| Support | "Strength of support system" | 7 | Social integration matters |
| Logistics | "Commute distance to university" | 6 | Practical barrier, moderate impact |
| Interest | "Interest level in courses" | 4 | Contextual, less predictive alone |

---

## 3. Option Weightage (1-10)

### 3.1 Definition

**Option Weightage** represents the value assigned to each answer choice within a question, reflecting how favorable that response is for predicting success. Higher weightages indicate responses associated with better outcomes.

### 3.2 Justification Approach: Likert-Scale Methodology

Option weightages follow established **Likert scale scoring conventions** adapted for success prediction:

#### A. Semantic Mapping

Answer choices are mapped to numerical values based on their semantic strength:

**Standard 5-Point Ordinal Scale:**
```
"Not at all / Never"           → 1-2  (Unfavorable)
"Slightly / Rarely"            → 3-4  (Below average)
"Moderately / Sometimes"       → 5-6  (Neutral/Average)
"Very / Often"                 → 7-8  (Above average)
"Extremely / Always"           → 9-10 (Highly favorable)
```

**Reference:** This approach aligns with Likert scale interpretation guidelines as described in psychometric literature. For comprehensive discussion of Likert scale analysis and appropriate weighting schemes, see Sullivan & Artino (2013) and the systematic review by Joshi et al. (2015). For visual presentation of Likert-type data, see Robbins & Heiberger (2011).

#### B. Non-Linear Adjustments

Some scales require non-linear weightage to reflect real-world impact:

**Work Hours Example (Inverse Relationship):**
```
0-15 hours/week      → 10 (Ideal: minimal conflict with studies)
16-25 hours/week     → 7  (Manageable)
26-35 hours/week     → 4  (Significant impact)
36+ hours/week       → 2  (Severe impact on academics)
```

**Difficulty Perception Example (Inverted):**
```
"Much easier than expected"    → 5  (May indicate overconfidence)
"About the same difficulty"    → 8  (Realistic expectations)
"Much more challenging"        → 10 (Prepared for challenge)
"Not sure what to expect"      → 3  (Lack of preparation)
```

### 3.3 Literature Support

The Likert-type scaling approach used in ACOSUS is grounded in established psychometric methodology:

1. **Likert, R. (1932).** "A technique for the measurement of attitudes." *Archives of Psychology*, 22(140), 1-55.
   - Original development of summated rating scales

2. **Sullivan, G. M., & Artino Jr, A. R. (2013).** "Analyzing and interpreting data from Likert-type scales." *Journal of Graduate Medical Education*, 5(4), 541-542.
   - Guidelines for appropriate analysis of Likert-type data

3. **Joshi, A., Kale, S., Chandel, S., & Pal, D. K. (2015).** "Likert scale: Explored and explained." *British Journal of Applied Science & Technology*, 7(4), 396-403.
   - Comprehensive review of Likert scale properties and applications

4. **Norman, G. (2010).** "Likert scales, levels of measurement and the 'laws' of statistics." *Advances in Health Sciences Education*, 15(5), 625-632.
   - Discussion of parametric analysis with ordinal data

5. **PMC Article Reference:** For additional context on Likert scale methodology in health and education research, see https://pmc.ncbi.nlm.nih.gov/articles/PMC12482090/

### 3.4 Example Option Weightages

**Academic Confidence Question:**
| Option | Weightage | Rationale |
|--------|-----------|-----------|
| "Extremely confident" | 10 | Highest self-efficacy |
| "Very confident" | 8 | Strong confidence |
| "Moderately confident" | 6 | Average level |
| "Somewhat confident" | 4 | Below average |
| "Not confident at all" | 1 | Significant concern |

**GPA Range Question:**
| Option | Weightage | Rationale |
|--------|-----------|-----------|
| "Above 3.5" | 9-10 | Strong academic record |
| "3.0-3.5" | 8 | Good standing |
| "2.0-3.0" | 4-6 | Adequate |
| "Below 2.0" | 2 | Academic concern |

**Career Aspiration (Cardinal/Nominal):**
| Option | Weightage | Rationale |
|--------|-----------|-----------|
| "Academia / Research" | 9 | Clear direction |
| "Industry / Corporate" | 9 | Clear direction |
| "Entrepreneurship" | 9 | Clear direction |
| "Public Sector" | 9 | Clear direction |
| "Other" | 9 | Has a goal |

*Note: For nominal data where no option is inherently "better," weightages may be equal, with priority score determining overall question importance.*

---

## 4. PWRS Algorithm Summary

The **Priority-Weighted Response Scoring (PWRS)** algorithm aggregates multi-question Target Survey responses into a single readiness score:

### 4.1 Formula

$$
S_{final} = \frac{100}{1 + e^{-k\left(\frac{\sum_{i=1}^{n} \left(\frac{w_i^{selected}}{w_i^{max}} \times p_i\right)}{\sum_{i=1}^{n} p_i} - 0.5\right)}}
$$

Where:
- $w_i^{selected}$ = Weightage of selected option for question $i$
- $w_i^{max}$ = Maximum possible weightage for question $i$
- $p_i$ = Priority score for question $i$
- $k$ = Steepness parameter (default: 6)
- $n$ = Number of questions answered

### 4.2 Steps

1. **Normalize:** $s_i^{norm} = \frac{w_i^{selected}}{w_i^{max}}$ (produces 0-1 value)
2. **Weight:** $s_i^{weighted} = s_i^{norm} \times p_i$
3. **Aggregate:** $S_{base} = \frac{\sum s_i^{weighted}}{\sum p_i}$
4. **Calibrate:** Apply logistic transformation to produce final 0-100% score

*For detailed PWRS documentation, see [readiness-score-calculation.md](./readiness-score-calculation.md)*

---

## 5. Feature Normalization (Factor Surveys)

Factor Survey responses are normalized to a common 0-10 scale before ML ingestion:

| Data Type | Normalization Method | Example |
|-----------|---------------------|---------|
| **Ordinal** | Direct option weightage | "Very confident" (w=8) → 8.0 |
| **Cardinal** | Sum-of-selected / Sum-of-total × 10 | Multi-select: 2 of 4 selected → 5.0 |
| **Continuous** | Min-max: $(x - min) / (max - min) \times 10$ | GPA 3.2: $(3.2-0)/(4.0-0) \times 10 = 8.0$ |
| **Temporal** | Duration scoring curve | 2 years to degree → literature-informed score |

---

## 6. Validation Framework

### 6.1 Current Status

Priority scores and option weightages are **initial configurations based on domain expertise**. The system is designed for iterative refinement through pilot validation.

### 6.2 Validation Metrics

| Metric | Target | Action if Not Met |
|--------|--------|-------------------|
| Pearson correlation (PWRS vs ML prediction) | > 0.70 | Adjust priority weights |
| Mean Absolute Error | < 15 points | Review option weightages |
| Student feedback rating | > 3.5/5.0 | Investigate systematic errors |

### 6.3 Refinement Process

1. Collect pilot data (N ≥ 10 students)
2. Compare PWRS scores with ML predictions and student feedback
3. Identify under/over-weighted questions via feature importance analysis
4. Adjust priority scores and option weightages
5. Retrain and validate

---

## 7. References

### Transfer Student Success Literature
- Laanan, F. S. (2007). Studying transfer students: Part II: Dimensions of transfer students' adjustment. *Community College Journal of Research and Practice*, 31(1), 37-59.
- Townsend, B. K., & Wilson, K. (2006). "A hand hold for a little bit": Factors facilitating the success of community college transfer students to a large research university. *Journal of College Student Development*, 47(4), 439-456.
- Tinto, V. (1993). *Leaving college: Rethinking the causes and cures of student attrition* (2nd ed.). University of Chicago Press.

### Psychometric and Measurement Literature
- Bandura, A. (1997). *Self-efficacy: The exercise of control*. W.H. Freeman.
- Likert, R. (1932). A technique for the measurement of attitudes. *Archives of Psychology*, 22(140), 1-55.
- Sullivan, G. M., & Artino Jr, A. R. (2013). Analyzing and interpreting data from Likert-type scales. *Journal of Graduate Medical Education*, 5(4), 541-542.
- Joshi, A., Kale, S., Chandel, S., & Pal, D. K. (2015). Likert scale: Explored and explained. *British Journal of Applied Science & Technology*, 7(4), 396-403.
- Norman, G. (2010). Likert scales, levels of measurement and the "laws" of statistics. *Advances in Health Sciences Education*, 15(5), 625-632.

### ACOSUS Research Papers
- [REF: 2022 Social Cognitive Paper] Investigation of social-cognitive factors affecting computing transfer students.
- [REF: 2023 Factor Analysis Paper] A preliminary factor analysis on the success of computing major transfer students.
- [REF: 2024 Transfer Students Success Paper] Investigation of computing transfer students' success.

---

## 8. Summary

| Component | Definition | Range | Assignment Method |
|-----------|------------|-------|-------------------|
| **Priority Score** | Importance of question to success construct | 1-10 | Literature + expert judgment |
| **Option Weightage** | Favorability of answer choice | 1-10 | Likert-scale methodology |
| **Label (Y)** | Readiness/Success Rate | [0, 1] | Single-Q or PWRS aggregation |
| **Features (X)** | Normalized factor responses | 0-10 | Type-aware normalization |

The scoring methodology enables:
- **Transparent** calculation with documented variables
- **Configurable** weights adjustable by administrators
- **Validated** through iterative pilot refinement
- **Literature-grounded** justification for academic publication
