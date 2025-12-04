

# Target Survey Success Rate Calculation

## Dynamic Success Rate Calculation

## Priority-Weighted Response Scoring (PWRS) Model

**Purpose:** Universal formula for calculating student success rates from survey responses

Define: Success Rate or Readiness Score

## Executive Summary

This document presents a transparent formula for calculating student success rates that works dynamically with any number of questions (from 1 to 50+). The system uses only two configurable parameters per question:

- **Priority Score** (1-10): Importance of the question
- **Option Weightage** (numeric): Value assigned to each answer choice

The formula produces realistic success rates (0-100%) without hardcoded assumptions or machine learning models.

## Survey Types

### Single-Question Surveys

For surveys with a single question (target type: `single`), the student's selected option weightage **directly maps** to their success rate. These questions ask students to self-assess their readiness.

#### **Example:**

- Question: "What is your own assessment of your readiness score?"
- Student provide the success rate numeric value

### Multiple-Question Surveys

For surveys with multiple questions (target type: `multiple`), the PWRS formula calculates success rate by combining all responses with priority-based weighting.

## The PWRS Formula

### Core Calculation (4 Steps)

```
1 # Step 1: Normalize each answer to 0-1 scale
2 normalized_score_i = selected_option_weightage / max_option_weightage_for_question_i
3 # Step 2: Apply priority weighting
4 weighted_score_i = normalized_score_i x priority_score_i
5 # Step 3: Calculate base score (0-1 range)
```

```
6 base_score = sum(weighted_score_i) / sum(priority_score_i)
7 # Step 4: Apply calibration curve
8 success_rate = calibration_function(base_score)
```

#### Mathematical Notation

$$\text{Base Score} = \frac{\sum_{i=1}^{n} \left( \frac{w_i}{w_{max,i}} \times p_i \right)}{\sum_{i=1}^{n} p_i}$$

Where:

- $w_i$  = selected option weightage for question  $i$
- $w_{max,i}$  = maximum option weightage for question  $i$
- $p_i$  = priority score for question  $i$
- $n$  = total number of questions

#### Foundation

##### 1. Item Response Theory (IRT)

Questions with higher "discrimination parameters" (our priority scores) contribute more to the overall assessment. This is standard in educational testing (SAT, GRE, etc.).

##### 2. Weighted Portfolio Assessment

Different assessment components receive different weights based on their importance—used in academic grading systems worldwide.

##### 3. Logistic Transformation

Converts linear scores to probability scales, preventing unrealistic extremes. Used in statistical modeling, credit scoring, and medical risk assessment.

**Why this matters:** We're not inventing a new approach—we're applying proven measurement principles in a transparent way.

## Calibration Curves

The calibration curve transforms the base score (0-1) into a final success rate (0-100%). Different curves produce different distributions.

### Option 1: Logistic Curve (RECOMMENDED)

#### Formula:

$$\text{Success Rate} = \frac{100}{1 + e^{-k(B-0.5)}}$$

Where:

- $B$  = base score (0-1)
- $k$  = steepness factor (recommended: 6)
- $e$  = Euler's number (2.718...)

#### Characteristics:

- Produces S-shaped distribution
- Prevents extreme values (rare 0% or 100%)
- Most scores fall in 20-85% range
- Realistic: mirrors real-world success distributions

**Why Logistic?** Real academic success is rarely 0% or 100%. Students with very poor preparation still have some chance of success (persistence, improvement), and even well-prepared students face uncertainties. The logistic curve naturally models this reality.

#### Impact:

- Base score 0.3  $\to$  ~33% success rate
- Base score 0.5  $\to$  ~50% success rate
- Base score 0.7  $\to$  ~67% success rate
- Base score 0.9  $\to$  ~82% success rate

```
1 def logistic_curve(base_score, k=6):  
2     return 100 / (1 + math.exp(-k * (base_score - 0.5)))
```

### Option 2: Linear (No Curve)

#### Formula:

$$\text{Success Rate} = B \times 100$$

#### Characteristics:

- Direct 1:1 mapping
- Simplest calculation
- Can produce 0% and 100% easily
- Full range of scores used

#### **Impact:**

- Base score 0.3 → 30% success rate
- Base score 0.5 → 50% success rate
- Base score 0.7 → 70% success rate
- Base score 0.9 → 90% success rate

**When to use:** If you want absolute transparency with no adjustments, or if your validation data shows linear relationship.

```
1 def linear_curve(base_score):  
2 return base_score * 100
```

### Option 3: Bounded Linear (Clipped)

#### **Formula:**

$$\text{Success Rate} = \min(95, \max(10, B \times 100))$$

#### **Characteristics:**

- Linear but prevents extreme edges
- Minimum success rate: 10%
- Maximum success rate: 95%
- Maintains proportionality within bounds

#### **Impact:**

- Base score 0.0 → 10% (not 0%)
- Base score 0.3 → 30% success rate
- Base score 0.7 → 70% success rate
- Base score 1.0 → 95% (not 100%)

**When to use:** If you want linear simplicity but need to avoid absolute certainty at the extremes.

```
1 def bounded_linear_curve(base_score, min_rate=10, max_rate=95):  
2 return min(max_rate, max(min_rate, base_score * 100))
```

### Option 4: Sigmoid (Softer S-curve)

#### **Formula:**

$$\text{Success Rate} = 20 + 70 \times \frac{1}{1 + e^{-k(B-0.5)}}$$

Where  $k = 4$  (softer than logistic)

#### **Characteristics:**

- S-shaped but gentler than logistic
- Compressed to 20-90% range
- More gradual transitions
- Very rare to see <25% or >85%

#### **Impact:**

- Base score 0.2 → ~28% success rate
- Base score 0.5 → ~55% success rate
- Base score 0.8 → ~82% success rate
- Base score 0.95 → ~88% success rate

**When to use:** If you want to be even more conservative than logistic, avoiding strong judgments at the extremes.

```
1 def sigmoid_curve(base_score, k=4):  
2     return 20 + 70 / (1 + math.exp(-k * (base_score - 0.5)))
```

### Calibration Curve Comparison

| Base Score | Linear | Bounded Linear | Logistic (k=6) | Sigmoid (k=4) |
|------------|--------|----------------|----------------|---------------|
| 0.0        | 0%     | 10%            | 18%            | 24%           |
| 0.2        | 20%    | 20%            | 26%            | 32%           |
| 0.4        | 40%    | 40%            | 43%            | 47%           |
| 0.5        | 50%    | 50%            | 50%            | 55%           |
| 0.6        | 60%    | 60%            | 57%            | 63%           |
| 0.8        | 80%    | 80%            | 74%            | 78%           |
| 1.0        | 100%   | 95%            | 82%            | 86%           |

#### Visual Representation:

![](bc04d002fc79e8a3637b1552ac3361e6_img.jpg)

This step chart visually compares four calibration curves (Bounded Linear, Sigmoid, Logistic, and Linear) showing the mapping from Base Score (X-axis, 0.0 to 1.0) to Success Rate (Y-axis, 0% to 100%).

Success Rate

100%  
90%  
80%  
70%  
60%  
50%  
40%  
30%  
20%  
10%  
0%

0.0 0.5 1.0 Base Score

Bounded Linear  
Sigmoid  
Logistic  
Linear

## Step-by-Step Example

### Scenario: 5-Question Survey

| Question             | Priority | Student Selected   | Weightage | Max Weightage |
|----------------------|----------|--------------------|-----------|---------------|
| Academic Confidence  | 9        | "Very confident"   | 8         | 10            |
| Time Management      | 8        | "Good skills"      | 8         | 10            |
| Financial Confidence | 8        | "Somewhat worried" | 4         | 10            |
| Commitment           | 9        | "Very committed"   | 8         | 10            |
| Study Habits         | 8        | "Average habits"   | 6         | 10            |

### Step 1: Normalize Scores

1 Q1:  $8/10 = 0.80$

2 Q2:  $8/10 = 0.80$

3 Q3:  $4/10 = 0.40$

4 Q4:  $8/10 = 0.80$

5 Q5:  $6/10 = 0.60$

### Step 2: Apply Priority Weighting

1 Q1:  $0.80 \times 9 = 7.2$

2 Q2:  $0.80 \times 8 = 6.4$

3 Q3:  $0.40 \times 8 = 3.2$

4 Q4:  $0.80 \times 9 = 7.2$

5 Q5:  $0.60 \times 8 = 4.8$

6 Total: 28.8

### Step 3: Calculate Base Score

1 Sum of priorities:  $9 + 8 + 8 + 9 + 8 = 42$

2 Base score:  $28.8 / 42 = 0.686$

### Step 4: Apply Calibration

#### Logistic (k=6):

1  $100 / (1 + e^{(-6(0.686-0.5))})$

2  $= 100 / (1 + e^{(-1.116)})$

3  $= 100 / (1 + 0.328)$

4  $= 75.3\%$

#### Linear:

1  $0.686 \times 100 = 68.6\%$

#### Bounded Linear:

1  $\min(95, \max(10, 68.6)) = 68.6\%$

#### Sigmoid (k=4):

```
1 20 + 70 / (1 + e^(-4(0.686-0.5)))
2 = 20 + 70 / (1 + 0.481)
3 = 20 + 47.3
4 = 67.3%
```

### Result Summary

- **Logistic:** 75% success rate
- **Linear:** 69% success rate
- **Bounded Linear:** 69% success rate
- **Sigmoid:** 67% success rate

## Edge Cases

### Missing Answers

When a student skips a question, assign the **neutral value**:

```
1 normalized_score = 0.5 # 50% of scale
```

This represents "average" or "uncertain" without penalizing heavily.

#### Example:

- Question with priority 8 is skipped
- Weighted score:  $0.5 \times 8 = 4.0$
- Contributes average performance to calculation

### Single Question with Custom Input

For single-question surveys where students provide a custom numeric value (0-100), use the value directly:

```
1 success_rate = student_custom_input # Use as-is
```

No calculation needed—this is direct self-assessment.

## Implementation Guide

### Complete Python Implementation

```
1
```

### Choosing the Right Calibration Curve

**Recommended:** Logistic Curve (k=6)

#### **Use when:**

- You want realistic, research-backed distributions
- You need to prevent extreme confidence (0% or 100%)
- You're assessing predictive readiness (not just current state)

**Rationale:** Student success is probabilistic, not deterministic. Even highly prepared students face challenges; even underprepared students can succeed with effort. The logistic curve models this uncertainty naturally, which is why it's used in credit scoring, medical prognosis, and educational assessment.

#### **Alternative: Linear**

##### **Use when:**

- Maximum transparency is required
- Stakeholders prefer direct calculation
- You have validation data showing linear relationships

#### **Alternative: Bounded Linear**

##### **Use when:**

- You want linear simplicity
- But need to avoid absolute 0% or 100% claims

#### **Alternative: Sigmoid**

##### **Use when:**

- You want to be very conservative
- Avoiding strong statements at extremes is critical
- You're in early pilot phases

## Validation Strategy

To validate the formula with real data:

1. **Collect baseline:** Survey students, record predicted success rates
2. **Track outcomes:** Monitor actual performance (completion, GPA, etc.)
3. **Compare distributions:** Plot predicted vs. actual success rates
4. **Adjust calibration:** If predictions are consistently high/low, adjust k-factor or switch curves
5. **Iterate:** Refine priority scores based on which questions correlate best with outcomes

### **Correlation targets:**

- Good:  $r > 0.5$
- Excellent:  $r > 0.7$

## Configuration Examples

### **Conservative Setting (Sigmoid, k=3)**

```
1 success_rate = calculate_success_rate(
```

```
2 questions, answers,
3 calibration_method="sigmoid",
4 k_factor=3.0
5 )
```

Result: Compressed scores, fewer extreme predictions

### Balanced Setting (Logistic, k=6)

```
1 success_rate = calculate_success_rate(
2 questions, answers,
3 calibration_method="logistic",
4 k_factor=6.0
5 )
```

Result: Realistic S-curve distribution

### Direct Setting (Linear)

```
1 success_rate = calculate_success_rate(
2 questions, answers,
3 calibration_method="linear"
4 )
```

Result: Proportional 1:1 mapping

## Summary

The PWRS model provides a **transparent, flexible, and research-backed** approach to calculating student success rates:

- ✓ Works with any number of questions (1-50+)
- ✓ Uses only priority scores and option weightages
- ✓ No hardcoded assumptions or black-box algorithms
- ✓ Four calibration options for different needs
- ✓ Handles missing data gracefully
- ✓ Produces realistic, actionable predictions

**Recommended configuration:** Logistic curve with k=6 for most educational contexts.

## Appendix: Formula Derivations

### Why Normalize First?

Different questions may have different weightage scales (0-5, 0-10, 1-100). Normalization ensures fair comparison:

$$\text{Normalized} = \frac{\text{Selected}}{\text{Maximum}} \in [0, 1]$$

### Why Divide by Sum of Priorities?

This creates a weighted average, not a sum. A survey with 3 priority-10 questions should produce the same base score as 1 priority-10 question (given identical answers).

### Logistic Function Properties

The logistic function  $f(x) = \frac{1}{1+e^{-x}}$  has:

- Domain:  $(-\infty, +\infty)$
- Range:  $(0, 1)$
- Inflection point at  $x=0$  (value=0.5)
- Symmetric S-shape

Parameter  $k$  controls steepness:

- $k=2$ : Very gradual
- $k=6$ : Moderate (recommended)
- $k=12$ : Very steep

### Logistic Function Properties

The logistic function  $f(x) = \frac{1}{1 + e^{-x}}$  has:

- Domain:  $(-\infty, +\infty)$
- Range:  $(0, 1)$
- Inflection point at  $x=0$  (value=0.5)
- Symmetric S