# ACOSUS Research Paper - Study Guide for Complex Terms

This document explains the complex terminology, academic phrasing, and technical concepts used in the ACOSUS research paper. Use this guide to prepare for discussions with your professor.

---

## Section 3: Introduction

### "structurally infeasible"
**Meaning:** Not just difficult, but fundamentally impossible given how the system is built.

**Example:** If you only have 20 transfer students per year, training a neural network that needs 10,000 examples isn't just hard—it's structurally infeasible. The structure of the problem (small cohorts) makes the solution (big-data ML) impossible.

---

### "pre-transfer trajectories"
**Meaning:** The academic path a student took BEFORE transferring—their community college courses, grades, major changes, etc.

**Example:** Student A took all their math prerequisites at a community college over 3 years while working full-time. Student B completed an associate's degree in 2 years full-time. These are different pre-transfer trajectories.

---

### "articulation outcomes"
**Meaning:** What happens to a student's credits when they transfer—how many credits were accepted, rejected, or changed.

**Example:** A student earned 60 credits at community college, but only 45 transferred to the university. The articulation outcome is "45 of 60 credits accepted" (25% credit loss).

---

### "psychosocial adjustment factors"
**Meaning:** The emotional and social challenges of adapting to a new environment—feeling like you belong, making friends, dealing with stress.

**Example:** A transfer student might have excellent grades but struggle with psychosocial adjustment: feeling like an outsider because everyone else has friend groups from freshman year.

---

## Section 3.1: Architectural Philosophy

### "Big Data approaches"
**Meaning:** Machine learning methods that require massive datasets (thousands or millions of records) to work properly.

**Example:** Netflix's recommendation system learns from billions of viewing records. That's a Big Data approach—it only works because they have so much data.

---

### "transfer shock"
**Meaning:** The documented phenomenon where transfer students experience a GPA drop in their first semester at the new institution, even if they were strong students before.

**Example:** A student with a 3.8 GPA at community college drops to 3.2 in their first semester after transfer. This temporary decline is transfer shock—it usually recovers, but it's a real pattern.

---

### "belonging uncertainty"
**Meaning:** A student's doubt about whether they truly fit in or are welcome at their institution.

**Example:** A first-generation transfer student might think: "Everyone here seems to know each other. The professors assume we all took the same intro courses. Do I really belong here?"

---

### "financial precarity"
**Meaning:** Being in an unstable financial situation where unexpected expenses could derail your education.

**Example:** A student who can afford tuition but has no savings. If their car breaks down or they get sick, they might have to drop out. That's financial precarity—not poverty, but instability.

---

### "latency between data collection and outcome observation"
**Meaning:** The time gap between when you gather data and when you can see the result you're trying to predict.

**Example:** You survey a student today about their readiness. But you won't know if they actually graduated successfully for 2-4 years. That delay is the latency problem—you can't train a model on outcomes you haven't observed yet.

---

### "heuristic scoring"
**Meaning:** Using expert-defined rules and weights to calculate scores, rather than learning patterns from data.

**Example:** An advisor says "GPA is very important (weight: 9/10), commute time matters somewhat (weight: 5/10)." Using these human-assigned weights to calculate a score is heuristic scoring—no machine learning involved.

---

### "instance-based learning"
**Meaning:** A type of machine learning that makes predictions by finding similar examples in the training data, rather than learning abstract patterns.

**Example:** KNN is instance-based: to predict your success rate, it finds the 5 students most similar to you and averages their success rates. It doesn't learn "rules"—it just remembers examples and finds similar ones.

---

## Section 3.1.1: Advisor Data Fragmentation

### "latent factors"
**Meaning:** Important variables that influence outcomes but are hidden/not directly observable in standard data systems.

**Example:** GPA is directly observable (it's in the SIS). But "how supported does this student feel by their family?" is a latent factor—it affects success but isn't captured anywhere unless you specifically ask.

---

### "disparate sources"
**Meaning:** Multiple separate, disconnected systems that don't share information with each other.

**Example:** The SIS, financial aid portal, LMS, and email are disparate sources. They each have useful information, but an advisor has to log into each one separately—they don't talk to each other.

---

### "ad-hoc conversations"
**Meaning:** Informal, unstructured discussions that happen as needed, without a systematic process.

**Example:** An advisor asking a student "So, how are things going financially?" during a meeting is ad-hoc. The answer might be valuable, but it's not recorded consistently or available to other advisors.

---

### "intervention opportunities"
**Meaning:** Chances to help a student before a problem becomes serious.

**Example:** If an advisor notices a student's work hours increased from 10 to 35 per week, that's an intervention opportunity—they can proactively discuss time management before grades suffer.

---

## Section 3.2: Dual-Survey Architecture

### "dependent variable"
**Meaning:** The thing you're trying to predict (the output/outcome).

**Example:** In ACOSUS, the dependent variable is "success rate." Everything else (GPA, work hours, confidence) are independent variables used to predict it.

---

### "ground-truth labels"
**Meaning:** The actual, verified correct answers used to train a machine learning model.

**Example:** If a student says their readiness is 72%, that's the ground-truth label. The model learns by comparing its predictions against these known-correct values.

---

### "proxy measures"
**Meaning:** Indirect measurements used when you can't measure the real thing directly.

**Example:** We can't measure "will this student graduate successfully?" directly (it takes years to find out). So we use proxy measures like "how ready do you feel?" as stand-ins for the real outcome.

---

### "metacognitive accuracy"
**Meaning:** How good someone is at accurately assessing their own knowledge, skills, or situation.

**Example:** A student with high metacognitive accuracy knows when they truly understand material vs. when they're fooling themselves. If they say "I'm 70% ready," that estimate is probably close to reality.

---

### "respondent burden"
**Meaning:** The effort, time, and mental energy required to complete a survey.

**Example:** A 5-minute survey has low respondent burden. A 45-minute survey with complex questions has high respondent burden—and higher dropout rates.

---

### "survey fatigue"
**Meaning:** When people get tired of surveys and either stop responding or give low-quality answers.

**Example:** If students are asked to complete 3 surveys per week, by week 4 they'll either stop participating or just click through without reading. That's survey fatigue.

---

## Section 3.3: Progressive Learning Framework

### "cold start problem"
**Meaning:** The challenge of making useful predictions when you have little or no historical data to learn from.

**Example:** Day 1 of deploying ACOSUS: zero students have used it. How do you make predictions? Traditional ML can't—that's the cold start problem. ACOSUS solves it with the progressive approach.

---

### "neural network inference"
**Meaning:** Using a trained neural network to make predictions on new data.

**Example:** After the neural network learns patterns from 500 students, using it to predict a new student's success rate is "inference"—applying what it learned to new cases.

---

### "non-parametric"
**Meaning:** A model that doesn't assume the data follows a specific mathematical distribution (like a bell curve).

**Example:** Linear regression assumes a straight-line relationship (parametric). KNN makes no such assumption—it just finds similar examples. That flexibility makes it non-parametric.

---

### "lazy learning"
**Meaning:** A learning approach that doesn't build a model during training—it just stores the data and does all the work at prediction time.

**Example:** KNN doesn't "train" in the traditional sense. It stores all examples, and when you ask for a prediction, it searches for similar ones on the spot. The "learning" is lazy—deferred until needed.

---

### "distance weighting"
**Meaning:** Giving more influence to closer/more similar examples when making predictions.

**Example:** If your 3 nearest neighbors have success rates of 80%, 75%, and 60%, but the first two are very similar to you and the third is only somewhat similar, distance weighting might give you a prediction of 77% (closer to 80% and 75%) rather than a simple average of 72%.

---

### "generative augmentation"
**Meaning:** Creating synthetic (fake but realistic) data to expand a small dataset.

**Example:** You have 100 real students. A GAN generates 400 synthetic students with similar characteristics. Now you have 500 training examples—enough for a neural network. That's generative augmentation.

---

### "Conditional Generative Adversarial Networks (cGANs)"
**Meaning:** A type of AI that learns to generate realistic fake data, where you can specify conditions (like "generate a student with 75% success rate").

**Example:** A regular GAN generates random fake students. A cGAN lets you say "generate a student who would have a 60% success rate" and it creates features that match that outcome.

**How it works (simplified):**
- **Generator:** Tries to create fake data that looks real
- **Discriminator:** Tries to detect which data is fake
- They compete, and the Generator gets better at fooling the Discriminator
- Eventually, the Generator creates highly realistic synthetic data

---

### "adversarially trained"
**Meaning:** Trained through competition between two models trying to outsmart each other.

**Example:** The Generator tries to make fakes good enough to fool the Discriminator. The Discriminator tries to get better at catching fakes. This competition (adversarial training) makes both improve.

---

### "synthetic observations"
**Meaning:** Artificially generated data points that mimic real data patterns.

**Example:** Real student: GPA 3.2, works 20 hrs/week, commutes 30 min, 68% success rate. Synthetic student: GPA 3.1, works 22 hrs/week, commutes 25 min, 65% success rate. The second is fake but statistically plausible.

---

### "overfitting"
**Meaning:** When a model learns the training data too perfectly, including its noise and quirks, and fails to generalize to new data.

**Example:** A model trained on 50 students might "memorize" their specific patterns (like "student #23 had GPA 3.4 and success 78%"). It performs perfectly on those 50 but terribly on new students. That's overfitting.

---

### "distribution shift"
**Meaning:** When the patterns in your training data don't match the patterns in real-world data.

**Example:** If synthetic students generated by the GAN have slightly different characteristics than real students, a model trained mostly on synthetic data might not work well on real students. That difference is distribution shift.

---

## Section 3.4: PWRS (Priority-Weighted Response Scoring)

### "Item Response Theory"
**Meaning:** A framework from psychometrics (the science of measuring psychological traits) for understanding how people respond to survey questions.

**Example:** IRT recognizes that not all questions are equally important or difficult. A hard question that a student gets "right" tells you more than an easy question. PWRS borrows this idea through priority weighting.

---

### "calibration curve"
**Meaning:** A mathematical function that adjusts raw scores to produce more realistic final scores.

**Example:** A student's raw calculation gives 0.95 (95%). But is anyone really 95% certain to succeed? A calibration curve might adjust this to 85%, reflecting that even well-prepared students face uncertainty.

---

### "logistic function / S-curve"
**Meaning:** A mathematical function that creates an S-shaped curve, where extreme inputs are compressed toward the middle.

**Example:**
- Input 0.1 → Output ~15% (low stays low)
- Input 0.5 → Output ~50% (middle stays middle)
- Input 0.9 → Output ~85% (high is compressed down from 90%)

The S-shape prevents overconfident predictions at the extremes.

---

### "steepness parameter k"
**Meaning:** A number that controls how sharply the S-curve transitions from low to high values.

**Example:**
- k = 2: Gentle slope, scores spread out more evenly
- k = 10: Sharp slope, most scores cluster around 50% unless inputs are extreme

Higher k = more dramatic differentiation between high and low performers.

---

## Section 3.5: Feedback Loop

### "pseudo-labeling"
**Meaning:** Using a model's prediction as if it were a ground-truth label (when the student confirms it's accurate).

**Example:** The model predicts 74%. The student says "yes, that feels right" (4+ stars). Instead of making them take another survey, we accept 74% as the label. It's not verified ground truth, but it's "pseudo" (approximately) correct.

---

### "active learning"
**Meaning:** A machine learning approach where the system strategically chooses which examples to get labels for, focusing on cases where it's uncertain.

**Example:** Instead of randomly asking students to complete surveys, ACOSUS specifically asks students who rated predictions poorly (< 4 stars). These are the cases where the model needs to learn, so it's "actively" choosing where to collect data.

---

### "implicit validation"
**Meaning:** Getting feedback about model quality as a byproduct of normal system use, without running a separate evaluation study.

**Example:** If 80% of students rate predictions 4+ stars, that implicitly validates the model is working well. If suddenly only 40% rate highly, something is wrong. You learn this just from normal usage.

---

## Section 3.6: Feature Normalization

### "ordinal data"
**Meaning:** Categories that have a meaningful order, but the gaps between them aren't necessarily equal.

**Example:** "Not confident" < "Somewhat confident" < "Very confident" is ordinal. We know the order, but the difference between "not" and "somewhat" might not equal the difference between "somewhat" and "very."

---

### "nominal/cardinal data"
**Meaning:** Categories with no inherent order—just different labels.

**Example:** "Institution type: Community College, State University, Private University" is nominal. None is inherently "higher" than another—they're just different categories.

---

### "one-hot encoding"
**Meaning:** Converting a category into multiple yes/no columns, one for each possible value.

**Example:** "Institution type" with 3 options becomes:
- Is_CommunityCollege: 1 or 0
- Is_StateUniversity: 1 or 0
- Is_PrivateUniversity: 1 or 0

A community college student would be [1, 0, 0].

---

### "min-max normalization"
**Meaning:** Scaling numbers to a fixed range (like 0-10) based on the minimum and maximum possible values.

**Example:** GPA ranges 0.0 to 4.0. To normalize to 0-10:
- GPA 4.0 → 10
- GPA 2.0 → 5
- GPA 3.2 → 8

Formula: (value - min) / (max - min) × 10

---

## Section 3.7: Model Selection

### "model versioning"
**Meaning:** Keeping track of different versions of trained models so you can compare them or roll back if needed.

**Example:** Model v1 was trained on 50 students (MAE: 12). Model v2 was trained on 100 students (MAE: 9). Model versioning lets you compare them and keeps v1 available in case v2 has problems.

---

### "validation protocol"
**Meaning:** A defined process for testing whether a model is good enough to use in production.

**Example:** ACOSUS validation protocol: Hold out 20 real students, test both old and new models on them, only deploy the new model if it performs better. This systematic process is the validation protocol.

---

### "MAE (Mean Absolute Error)"
**Meaning:** The average size of prediction errors, ignoring whether they're too high or too low.

**Example:** Predictions: [70, 75, 80]. Actual: [72, 70, 85]. Errors: [2, 5, 5]. MAE = (2+5+5)/3 = 4 points. On average, predictions are off by 4 percentage points.

---

### "RMSE (Root Mean Square Error)"
**Meaning:** Like MAE, but larger errors are penalized more heavily.

**Example:** Same errors [2, 5, 5]. RMSE = √((4+25+25)/3) = √18 = 4.24. The squaring makes big errors count more than small ones.

---

### "R² (R-squared)"
**Meaning:** How much of the variation in outcomes your model explains, from 0 (none) to 1 (all).

**Example:** R² = 0.7 means the model explains 70% of why some students have higher success rates than others. The remaining 30% is unexplained (luck, factors we didn't measure, etc.).

---

## Section 5: Evaluation Methodology

### "Technology Acceptance Model (TAM)"
**Meaning:** A well-established framework for measuring whether users will adopt new technology, based on perceived usefulness and ease of use.

**Example:** TAM predicts that people adopt technology when: (1) they believe it helps them (useful), and (2) they believe it's easy to use. ACOSUS uses TAM constructs to measure student acceptance.

---

### "Perceived Usefulness (PU)"
**Meaning:** A user's belief that the system will help them accomplish their goals.

**Example:** "Using ACOSUS helps me understand my academic situation better" - agreeing with this indicates high perceived usefulness.

---

### "Perceived Ease of Use (PEOU)"
**Meaning:** A user's belief that using the system requires little effort.

**Example:** "Learning to use ACOSUS was easy for me" - agreeing with this indicates high perceived ease of use.

---

### "Likert scale"
**Meaning:** A rating scale with ordered response options, typically 5 or 7 points from "Strongly Disagree" to "Strongly Agree."

**Example:**
1 = Strongly Disagree
2 = Disagree
3 = Neutral
4 = Agree
5 = Strongly Agree

Responses are treated as numbers for statistical analysis.

---

### "Cronbach's alpha"
**Meaning:** A statistical measure of whether multiple survey questions are consistently measuring the same underlying concept (internal consistency).

**Example:** If 6 questions all measure "perceived usefulness," students who agree with one should agree with the others. Cronbach's alpha > 0.7 indicates the questions are reliably measuring the same thing.

---

### "inter-rater reliability"
**Meaning:** How much different people agree when coding or categorizing the same data.

**Example:** Two researchers independently read open-ended survey responses and categorize themes. If they agree 90% of the time, inter-rater reliability is high—the coding is consistent, not subjective.

---

### "Cohen's Kappa"
**Meaning:** A specific statistic measuring inter-rater agreement, accounting for agreement that would happen by chance.

**Example:** If two coders agree 80% of the time, but random guessing would produce 50% agreement, Kappa adjusts for this. Kappa > 0.6 is generally considered acceptable agreement.

---

### "longitudinal validation"
**Meaning:** Testing predictions against real outcomes over an extended time period.

**Example:** We predicted student success rates in Fall 2024. Longitudinal validation means following those students for 2-4 years and checking: did the ones we predicted would succeed actually graduate?

---

### "predictive validity"
**Meaning:** Evidence that predictions actually correlate with real-world outcomes.

**Example:** If students predicted at 80% success rate actually graduate at higher rates than students predicted at 40%, the model has predictive validity—its predictions mean something real.

---

## Section 6: Discussion

### "heuristic dependency"
**Meaning:** Relying on human-defined rules rather than data-learned patterns.

**Example:** In Phase 1 (bootstrap), ACOSUS uses expert-assigned weights for questions. This is heuristic dependency—if experts set weights poorly, predictions suffer. Later phases learn from data and reduce this dependency.

---

### "domain specificity"
**Meaning:** Being designed for one specific field/area and not easily transferable to others.

**Example:** ACOSUS Factor Surveys ask about programming experience (relevant for CS majors). This is domain-specific—a nursing program would need different questions. The system works, but it's specialized.

---

### "federated learning"
**Meaning:** A machine learning approach where multiple institutions train models on their local data and share only the model improvements, not the raw data.

**Example:** NEIU and UTEP both use ACOSUS. Instead of sharing student data (privacy concern), they each train locally and share model weights. The combined model benefits from both datasets without exposing individual students.

---

### "cohort-level analytics"
**Meaning:** Statistics and visualizations about groups of students rather than individuals.

**Example:** "45% of this semester's transfer cohort scored below 50% predicted success" is cohort-level analytics. It helps advisors identify systemic issues, not just individual student problems.

---

### "early-alert integration"
**Meaning:** Connecting the prediction system to notification systems that warn advisors about at-risk students.

**Example:** If a student's predicted success drops below 40%, the system automatically emails their advisor: "Student X may need intervention." That automatic warning is early-alert integration.

---

## Quick Reference: Acronyms

| Acronym | Full Form | What It Is |
|---------|-----------|------------|
| **ACOSUS** | AI-driven Counseling System for Underrepresented Students | The system we built |
| **SIS** | Student Information System | Where GPA, courses, enrollment live |
| **LMS** | Learning Management System | Canvas, Blackboard, etc. |
| **KNN** | K-Nearest Neighbors | ML algorithm that finds similar students |
| **GAN** | Generative Adversarial Network | AI that creates synthetic data |
| **cGAN** | Conditional GAN | GAN where you can specify conditions |
| **PWRS** | Priority-Weighted Response Scoring | Our formula for calculating success rate |
| **TAM** | Technology Acceptance Model | Framework for measuring user adoption |
| **PU** | Perceived Usefulness | Do users think it's helpful? |
| **PEOU** | Perceived Ease of Use | Do users think it's easy? |
| **MAE** | Mean Absolute Error | Average prediction error size |
| **RMSE** | Root Mean Square Error | Prediction error (penalizes big errors) |
| **R²** | R-squared | How much variance the model explains |
| **IRT** | Item Response Theory | Psychometric theory behind PWRS |
| **JWT** | JSON Web Token | Authentication mechanism |

---

## Potential Professor Questions & Quick Answers

### "Why KNN instead of other algorithms for Phase 2?"
KNN is non-parametric (no distribution assumptions), requires no training phase, and works with as few as 10 examples. Other algorithms need more data or make assumptions that may not hold for small, diverse transfer populations.

### "How do you know the GAN-generated students are realistic?"
We validate exclusively on real students. If the neural network (trained on real + synthetic) performs well on held-out real students, the synthetic data preserved meaningful patterns. We can also use statistical tests (Kolmogorov-Smirnov) to compare distributions.

### "What if students game the system by giving dishonest answers?"
Two safeguards: (1) The feedback loop catches misalignment—if predictions consistently miss, students are asked for ground truth. (2) Advisors can verify/correct data during sessions. Longitudinal validation will ultimately reveal if predictions correlate with real outcomes.

### "Why is the bootstrap threshold 10 and not 5 or 20?"
10 is empirically chosen: fewer than 10 produces high-variance KNN predictions (not enough diversity to find meaningful neighbors). More than 10 delays the system's utility unnecessarily. It's also achievable within a single semester.

### "How do you handle the proxy outcome problem?"
Currently, we use student self-assessment as a proxy for success. The planned longitudinal validation (correlating predictions with actual graduation) will establish whether this proxy is valid. If not, we may need to adjust the Target Survey constructs.

### "What makes this different from existing early-alert systems like Starfish?"
Three things: (1) Works with 10 students, not 500+. (2) Captures transfer-specific latent factors that SIS/LMS don't have. (3) Feedback loop actively learns and reduces survey burden. Commercial systems are designed for large populations with existing data.
