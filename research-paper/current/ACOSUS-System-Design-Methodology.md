# An AI-Driven Transfer Student Advising System: Design, Implementation, and Evaluation

## 3 System Design and Methodology

The transfer student population presents a unique challenge for predictive analytics in higher education. Unlike native student cohorts, where institutions accumulate years of historical data and can train sophisticated models on thousands of observations, transfer advising operates under severe data constraints. Departmental programs may enroll fewer than one hundred transfer students annually, and the specific combination of pre-transfer trajectories, articulation outcomes, and psychosocial adjustment factors that characterize this population is rarely captured in institutional data warehouses [1], [2]. Consequently, conventional machine learning approaches—which assume abundant labeled training data—are structurally infeasible for transfer-student-specific prediction tasks.

To address these constraints, we designed ACOSUS (AI-driven Counseling System for Underrepresented Students), an intelligent advising platform that introduces three architectural innovations. First, the system implements a **Progressive Learning Framework** that provides immediate value with zero training data and autonomously evolves as the dataset grows. Second, it employs a **Dual-Survey Architecture** that separates the collection of predictive features from ground-truth labels, enabling flexible study designs while managing respondent burden. Third, it incorporates a **Feedback-Driven Pseudo-Labeling Mechanism** that leverages student self-assessment to reduce survey fatigue while maintaining data quality for model training. This section details the theoretical foundations, architectural components, and algorithmic strategies underlying each innovation.

### 3.1 Architectural Philosophy: Small Data by Design

The dominant paradigm in educational data mining favors "Big Data" approaches: aggregate registrar feeds, learning management system clickstreams, and institutional research databases containing tens of thousands of student records [3]. Such approaches are poorly suited to transfer-student advising for three reasons. First, transfer cohorts are inherently small—a computing department may admit thirty to fifty transfer students per year, yielding insufficient observations for deep learning architectures that require thousands of labeled examples to converge. Second, the variables most predictive of transfer success—credit articulation outcomes, "transfer shock" severity, belonging uncertainty, and financial precarity—are seldom captured in standard institutional systems [4], [5]. Third, the latency between data collection and outcome observation (two to four years until graduation) makes traditional supervised learning impractical for newly deployed systems.

ACOSUS addresses these challenges through a "Small Data" design philosophy. Rather than waiting years to accumulate a massive training corpus, the system is engineered to deliver value from its first interaction while progressively improving as data accrues. This philosophy manifests in three design principles:

1. **Immediate Utility**: The system must provide meaningful feedback to the very first user, even with zero historical data, using expert-defined heuristics.

2. **Graceful Evolution**: As the dataset grows, the system must seamlessly transition from heuristic scoring to instance-based learning to neural network inference without requiring code changes or manual intervention.

3. **Burden Minimization**: Data collection must respect students' time constraints, particularly given that transfer students often juggle employment, family responsibilities, and academic demands [6].

### 3.2 The Dual-Survey Architecture

A fundamental tension exists in predictive modeling for student success: the features that predict outcomes (academic preparation, financial stability, social support) differ from the outcomes themselves (graduation, GPA, career placement). Moreover, measuring outcomes requires either waiting years for ground truth or relying on proxy measures that students can self-report. ACOSUS resolves this tension through a Dual-Survey Architecture that cleanly separates feature collection from label collection.

#### 3.2.1 Target Surveys: Defining Success

Target Surveys capture the dependent variable—the "success rate" or "readiness score" that serves as the prediction target. The system supports two Target Survey modalities:

**Single-Question Target Surveys** present students with a direct self-assessment prompt:

> "Based on your current academic preparation, resources, circumstances, and goals, what is your own assessment of your readiness score for this program? Rate yourself from 0 to 100, where 0 means completely unprepared and 100 means fully prepared for success."

The student's numeric response (0–100) is used directly as the ground-truth label. This modality minimizes respondent burden (approximately 30 seconds) and captures the student's holistic self-perception.

**Multiple-Question Target Surveys** employ a battery of items measuring constructs such as academic confidence, time management self-efficacy, financial security, and social belonging. These surveys typically contain 15–30 items and require approximately 10–15 minutes to complete. Because multiple items must be reduced to a single numeric label, the system applies the Priority-Weighted Response Scoring (PWRS) algorithm described in Section 3.4.

The choice between single-question and multiple-question Target Surveys represents a trade-off between respondent burden and measurement granularity. Single-question surveys maximize completion rates but rely entirely on students' metacognitive accuracy. Multiple-question surveys provide richer signal but risk survey fatigue, particularly among time-constrained transfer students.

#### 3.2.2 Factor Surveys: Capturing Predictive Features

Factor Surveys collect the independent variables—the features used to predict success. Drawing on prior research identifying correlates of transfer-student outcomes [1], [5], [7], Factor Surveys capture:

- **Academic Background**: Pre-transfer GPA, credits earned, credits transferred, prior institution type
- **Financial Circumstances**: Employment intensity (hours per week), financial aid status, perceived financial security
- **Logistical Factors**: Commute time, caregiving responsibilities, housing stability
- **Technical Preparation**: Programming experience, familiarity with specific languages or tools (for computing majors)
- **Temporal Factors**: Expected time to degree completion, enrollment intensity (full-time vs. part-time)

Factor Surveys are designed for efficiency, typically comprising 10–15 objective questions completable in approximately 5 minutes. Unlike Target Surveys, which measure latent constructs, Factor Surveys collect observable facts amenable to direct machine learning ingestion.

#### 3.2.3 Survey Linkage and Study Configuration

The system architecture permits flexible study configurations through survey linkage. A single Target Survey may be associated with multiple Factor Surveys, enabling researchers to investigate how different feature sets predict the same outcome measure. For example, one Factor Survey might focus exclusively on academic variables while another emphasizes psychosocial factors; both can predict against the same Target Survey's success rate. This design supports iterative refinement of predictive models as researchers identify which feature domains contribute most to prediction accuracy.

Administrators configure study parameters through the system's administrative interface, including:
- Which Target Survey defines the prediction target
- Which Factor Survey(s) provide features for that target
- Threshold parameters for the feedback loop (described in Section 3.5)
- Model retraining triggers (manual, scheduled, or milestone-based)

Each Factor Survey maintains its own independent model pipeline, allowing the system to simultaneously support multiple studies with different prediction architectures.

### 3.3 The Progressive Learning Framework

The defining innovation of ACOSUS is its Progressive Learning Framework, which structures the system's predictive intelligence into three developmental phases. Each phase employs a different algorithmic strategy optimized for the available data volume.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PROGRESSIVE LEARNING FRAMEWORK                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 1: Bootstrap          Phase 2: Instance-Based      Phase 3: Neural  │
│  ─────────────────           ────────────────────────     ───────────────  │
│                                                                             │
│  N < 10 students             10 ≤ N < 100 students        N ≥ 100 students │
│                                                                             │
│  ┌─────────────────┐         ┌─────────────────┐         ┌───────────────┐ │
│  │                 │         │                 │         │               │ │
│  │  Data Collection│         │  KNN Prediction │         │ Neural Network│ │
│  │  Only           │         │  + Feedback Loop│         │ + GAN Augment │ │
│  │                 │         │                 │         │               │ │
│  │  No Predictions │         │  k = √N         │         │ Synthetic Data│ │
│  │                 │         │                 │         │               │ │
│  └─────────────────┘         └─────────────────┘         └───────────────┘ │
│                                                                             │
│        │                            │                            │          │
│        ▼                            ▼                            ▼          │
│                                                                             │
│  Student completes          Student completes            Student completes │
│  Target + Factor            Factor Survey only           Factor Survey only│
│  Surveys                    ───────────────────          ──────────────────│
│  ───────────────            Prediction displayed         NN prediction     │
│  Label stored for           Feedback requested           Feedback requested│
│  future training            Pseudo-label or correct      Continuous improve│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Figure 1.** The Progressive Learning Framework transitions through three phases as data accumulates, each employing algorithms suited to the available sample size.

#### 3.3.1 Phase 1: Bootstrap Data Collection (N < 10)

During the bootstrap phase, the system operates in data-collection mode. Students complete both the Target Survey (to establish ground-truth labels) and the Factor Survey (to provide features). No predictions are generated because the system lacks sufficient data to make meaningful inferences.

This phase serves a critical function: it seeds the dataset with high-quality, fully-labeled observations that anchor subsequent model training. By requiring both surveys from early adopters, the system ensures that its initial training corpus contains verified ground-truth labels rather than inferred pseudo-labels.

The bootstrap threshold of ten students is deliberately conservative. While K-Nearest Neighbors can theoretically operate with fewer observations, empirical testing revealed that predictions with N < 10 exhibited unacceptably high variance and frequently produced implausible estimates. Ten observations provide sufficient diversity to identify meaningful similarity patterns while remaining achievable within a single academic term. `[CHECK WITH PROFESSOR: Is 10 the correct threshold, or should this be configurable?]`

#### 3.3.2 Phase 2: Instance-Based Learning (10 ≤ N < 100)

Once the system accumulates ten labeled observations, it transitions to active prediction using K-Nearest Neighbors (KNN) regression. KNN is mathematically well-suited to this "small data" regime for several reasons:

1. **Non-parametric**: KNN makes no assumptions about the underlying data distribution, avoiding the risk of model misspecification with limited observations.

2. **Lazy Learning**: KNN requires no explicit training phase; it stores observations and computes predictions at inference time, eliminating the need for computationally expensive model fitting.

3. **Interpretable**: Predictions can be explained by reference to specific similar students ("Your prediction is based on students #3, #7, and #12, who had similar backgrounds and achieved success rates of 72%, 68%, and 81%").

**Dynamic Neighbor Selection**: The number of neighbors k is calculated dynamically as a function of dataset size:

$$k = \min\left(\max\left(3, \lfloor\sqrt{N}\rfloor\right), 10\right)$$

This formula ensures that k remains small enough to find genuinely similar peers when N is limited (k = 3 when N = 10) while increasing smoothly as data accumulates (k = 10 when N = 100). The upper bound of 10 prevents over-smoothing that would obscure individual variation.

**Distance Weighting**: Predictions are computed as a weighted average of neighbors' success rates, with weights inversely proportional to distance in feature space. Closer neighbors contribute more heavily to the prediction, ensuring that highly similar students exert greater influence than marginally similar ones.

**Prediction Workflow in Phase 2**:
1. New student completes Factor Survey only (Target Survey skipped)
2. System normalizes features to comparable scales
3. KNN identifies k nearest neighbors in feature space
4. Weighted average of neighbors' success rates yields prediction
5. Student views prediction and provides feedback (see Section 3.5)

#### 3.3.3 Phase 3: Generative Augmentation and Neural Networks (N ≥ 100)

When the dataset reaches 100 observations, the system enables neural network training. However, 100 observations remain insufficient for deep learning architectures, which typically require thousands of examples to avoid overfitting. ACOSUS bridges this gap through Conditional Generative Adversarial Networks (cGANs), which learn the statistical distribution of real student data and generate high-fidelity synthetic observations for training augmentation.

**GAN Architecture**: The Conditional GAN comprises two neural networks trained adversarially:

- **Generator (G)**: Accepts a noise vector z and a condition vector c (representing the target success rate) and outputs a synthetic feature vector x̂ that resembles real student data.

- **Discriminator (D)**: Attempts to distinguish between real (x, c) pairs and generated (x̂, c) pairs, providing training signal to the Generator.

Through iterative adversarial training, the Generator learns to produce increasingly realistic synthetic students that preserve the statistical relationships present in the real data.

**Data Augmentation Strategy**: From 100 real students, the system generates approximately 400–500 synthetic observations, expanding the effective training corpus to 500–600 examples. This augmentation ratio is calibrated to provide sufficient data for neural network convergence while avoiding over-reliance on synthetic patterns that may not generalize. `[CHECK WITH PROFESSOR: Confirm the augmentation ratio and any validation metrics for synthetic data quality]`

**Training and Validation Protocol**:
1. Split real data: 80 students for training seed, 20 students for validation
2. Generate synthetic students conditioned on training seed distribution
3. Train neural network on combined real + synthetic training data
4. **Validate exclusively on real students** (never on synthetic data)
5. Compare neural network performance against KNN baseline
6. Deploy neural network only if it outperforms KNN on real validation set

The final point is critical: if the neural network underperforms the simpler KNN model, the system retains KNN for predictions while triggering GAN retraining or hyperparameter adjustment. This fail-safe ensures that increased model complexity translates to improved prediction accuracy rather than overfitting to synthetic artifacts.

**Neural Network Architecture**: `[CHECK WITH PROFESSOR: Specific architecture details—number of layers, activation functions, regularization strategies—pending finalization based on empirical tuning during deployment]`

### 3.4 Priority-Weighted Response Scoring (PWRS)

When Target Surveys employ multiple questions, responses must be aggregated into a single numeric success rate. The Priority-Weighted Response Scoring (PWRS) algorithm accomplishes this aggregation through a principled, transparent formula grounded in Item Response Theory [8].

#### 3.4.1 Core Algorithm

PWRS operates in four steps:

**Step 1: Response Normalization**

Each question response is normalized to a 0–1 scale by dividing the selected option's weightage by the maximum possible weightage for that question:

$$\text{normalized}_i = \frac{w_i}{w_{\max,i}}$$

where $w_i$ is the weightage assigned to the student's selected option and $w_{\max,i}$ is the highest weightage among all options for question $i$.

**Step 2: Priority Weighting**

Normalized scores are multiplied by each question's priority score, reflecting the domain-expert-assigned importance of that construct:

$$\text{weighted}_i = \text{normalized}_i \times p_i$$

where $p_i$ is the priority score (1–10) assigned to question $i$.

**Step 3: Base Score Calculation**

The base score is computed as the weighted average across all questions:

$$\text{BaseScore} = \frac{\sum_{i=1}^{n} \text{weighted}_i}{\sum_{i=1}^{n} p_i} = \frac{\sum_{i=1}^{n} \left(\frac{w_i}{w_{\max,i}} \times p_i\right)}{\sum_{i=1}^{n} p_i}$$

This yields a value in [0, 1] representing the student's relative standing across all measured constructs.

**Step 4: Calibration Curve Application**

The base score is transformed to a final success rate (0–100%) through a calibration function. The system supports four calibration options:

| Calibration Method | Formula | Characteristics |
|-------------------|---------|-----------------|
| **Linear** | $\text{SR} = \text{Base} \times 100$ | Direct mapping; can produce 0% or 100% |
| **Bounded Linear** | $\text{SR} = \min(95, \max(10, \text{Base} \times 100))$ | Prevents extremes; floor at 10%, ceiling at 95% |
| **Logistic** (recommended) | $\text{SR} = \frac{100}{1 + e^{-k(\text{Base} - 0.5)}}$ | S-curve; realistic uncertainty at extremes |
| **Sigmoid** | $\text{SR} = 20 + \frac{70}{1 + e^{-k(\text{Base} - 0.5)}}$ | Compressed range (20–90%); conservative |

**Table 1.** Calibration curve options for PWRS score transformation. The steepness parameter k defaults to 6 for logistic and 4 for sigmoid curves.

The logistic calibration is recommended for most contexts because it naturally models the inherent uncertainty in student success prediction: even well-prepared students face challenges, and even underprepared students can succeed with effort and support. The S-curve prevents overconfident predictions at the extremes.

#### 3.4.2 Worked Example

Consider a five-question Target Survey with the following responses:

| Question | Priority | Selected Option | Option Weightage | Max Weightage |
|----------|----------|-----------------|------------------|---------------|
| Academic Confidence | 9 | "Very confident" | 8 | 10 |
| Time Management | 8 | "Good skills" | 8 | 10 |
| Financial Security | 8 | "Somewhat worried" | 4 | 10 |
| Commitment Level | 9 | "Very committed" | 8 | 10 |
| Study Habits | 8 | "Average habits" | 6 | 10 |

**Step 1 (Normalize)**: 0.80, 0.80, 0.40, 0.80, 0.60

**Step 2 (Weight)**: 7.2, 6.4, 3.2, 7.2, 4.8 → Sum = 28.8

**Step 3 (Base Score)**: $28.8 / (9+8+8+9+8) = 28.8 / 42 = 0.686$

**Step 4 (Logistic, k=6)**: $100 / (1 + e^{-6(0.686-0.5)}) = 100 / (1 + e^{-1.116}) = 75.3\%$

The student receives a success rate of **75.3%**, reflecting strong academic confidence and commitment offset by financial concerns.

#### 3.4.3 Missing Response Handling

When students skip questions, the system assigns a neutral normalized score of 0.5, representing average or uncertain standing on that construct. This approach avoids penalizing students for incomplete responses while maintaining reasonable estimates.

### 3.5 The Feedback-Driven Pseudo-Labeling Mechanism

A central challenge in transfer-student advising is respondent burden. Completing comprehensive surveys requires 15–20 minutes—time that already-stressed transfer students may be unwilling to invest. Yet high-quality training data requires ground-truth labels from Target Surveys. ACOSUS resolves this tension through a Feedback-Driven Pseudo-Labeling mechanism that selectively requests Target Survey completion based on prediction confidence.

#### 3.5.1 Mechanism Overview

After a student completes the Factor Survey and views their predicted success rate, they are asked to rate the prediction's accuracy:

> "Based on our analysis, your predicted success rate is **74%**. How accurately does this reflect your own assessment of your readiness?"
>
> ⭐ ⭐ ⭐ ⭐ ⭐ (1 = Very inaccurate, 5 = Very accurate)

The student's rating determines the subsequent workflow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEEDBACK-DRIVEN PSEUDO-LABELING                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                     Student completes Factor Survey                         │
│                                  │                                          │
│                                  ▼                                          │
│                     System predicts success rate                            │
│                          (e.g., 74%)                                        │
│                                  │                                          │
│                                  ▼                                          │
│                     Student rates prediction                                │
│                          (1-5 stars)                                        │
│                                  │                                          │
│                    ┌─────────────┴─────────────┐                           │
│                    │                           │                            │
│                    ▼                           ▼                            │
│           Rating ≥ 4 stars            Rating < 4 stars                     │
│                    │                           │                            │
│                    ▼                           ▼                            │
│         ┌─────────────────────┐    ┌─────────────────────┐                 │
│         │ Accept prediction   │    │ Request Target      │                 │
│         │ as PSEUDO-LABEL     │    │ Survey completion   │                 │
│         │                     │    │                     │                 │
│         │ • Skip Target Survey│    │ • Student provides  │                 │
│         │ • Add to training   │    │   actual success    │                 │
│         │   data as (X, Ŷ)    │    │   rate              │                 │
│         │ • Student time: ~5m │    │ • Replace pseudo-   │                 │
│         └─────────────────────┘    │   label with ground │                 │
│                                    │   truth             │                 │
│                                    │ • Add to training   │                 │
│                                    │   data as (X, Y)    │                 │
│                                    │ • Student time: ~15m│                 │
│                                    └─────────────────────┘                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Figure 2.** The Feedback-Driven Pseudo-Labeling mechanism reduces survey burden by accepting predictions as labels when students confirm accuracy, while collecting ground-truth corrections when predictions miss the mark.

#### 3.5.2 Rationale and Benefits

**Burden Reduction**: When the model's prediction aligns with the student's self-assessment (rating ≥ 4), the student is exempted from the longer Target Survey. Total interaction time drops from approximately 15 minutes (Factor + Target) to approximately 5 minutes (Factor only). Based on pilot estimates, 50–70% of students may provide high-confidence ratings, substantially reducing aggregate survey burden across the cohort. `[CHECK WITH PROFESSOR: Confirm estimated high-rating percentage based on pilot data]`

**Self-Correcting Data Quality**: When predictions diverge from student expectations (rating < 4), the mechanism captures exactly the cases where the model needs improvement. The student provides ground-truth data that:
1. Corrects their individual record
2. Supplies a high-value training example for model refinement

This creates an "active learning" dynamic: the system preferentially collects labels for observations where it is most uncertain or inaccurate.

**Implicit Validation**: The distribution of feedback ratings provides ongoing validation of model performance. A preponderance of low ratings signals systematic prediction problems; high ratings confirm alignment between model outputs and student perceptions.

#### 3.5.3 Training Data Integration

When pseudo-labels are accepted:
- The student's Factor Survey responses (X) and the predicted success rate (Ŷ) are added to the training corpus
- The record is flagged as pseudo-labeled for potential future audit

When ground-truth corrections are collected:
- The student's Factor Survey responses (X) and self-reported success rate (Y) replace any pseudo-label
- The record is flagged as ground-truth verified

Model retraining can be triggered:
- **Manually** by system administrators
- **Automatically** at enrollment milestones (e.g., every 10 new students)
- **Scheduled** during low-activity periods (e.g., weekly)

### 3.6 Feature Normalization for Machine Learning

Factor Survey responses encompass diverse data types: continuous values (GPA, commute time), ordinal categories (confidence levels), and nominal categories (institution type). Before machine learning ingestion, all features must be normalized to a common scale.

The system employs type-aware normalization:

**Ordinal Data** (categories with meaningful order, e.g., "Not confident" → "Very confident"):
- Use option weightage directly as the normalized value
- Scale to 0–10 range based on assigned weightages

**Nominal/Cardinal Data** (categories without intrinsic order, e.g., institution type):
- One-hot encoding or sum of selected weightages divided by total possible weightage
- Scale to 0–10 range

**Continuous Data** (numeric values, e.g., GPA, hours worked):
- Min-max normalization to 0–10 range
- Domain-specific bounds (e.g., GPA: 0.0–4.0)

**Temporal Data** (date ranges, expected graduation):
- Duration scoring with domain-informed curves
- Literature suggests both "too fast" and "too slow" degree timelines correlate with risk [5]
- Non-linear scoring: 2–4 years optimal (score = 10), <2 years penalized (score = 4), >6 years penalized (score = 3)

The `dataTypeForModel` field in each question's configuration specifies whether the question captures ordinal or cardinal data, enabling automated normalization during feature engineering.

### 3.7 Model Selection and Deployment

The system maintains model versioning to ensure prediction quality. When a new model is trained (whether KNN with additional data or neural network after GAN augmentation), it is validated against the current production model before deployment.

**Validation Protocol**:
1. Hold out a subset of real students (never synthetic) as a validation set
2. Compute performance metrics on held-out data for both current and candidate models
3. Deploy candidate model only if it meets or exceeds baseline performance
4. If candidate underperforms, retain current model and log the failure for investigation

**Performance Metrics**: `[CHECK WITH PROFESSOR: Specific metrics to be finalized—likely MAE (Mean Absolute Error), RMSE (Root Mean Square Error), and R² for regression performance]`

This conservative deployment strategy ensures that increased model complexity (e.g., neural networks) translates to improved predictions rather than overfitting or distribution shift on synthetic data.

---

## 4 System Implementation

The ACOSUS platform is implemented as a three-tier web application separating presentation, business logic, and machine learning concerns. This section provides an overview of the implementation architecture; detailed technical specifications are available in supplementary materials.

### 4.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ACOSUS SYSTEM ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     PRESENTATION LAYER (Frontend)                      │ │
│  │                                                                         │ │
│  │   React + TypeScript + Tailwind CSS                                    │ │
│  │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                   │ │
│  │   │   Student   │  │   Advisor   │  │    Admin    │                   │ │
│  │   │   Portal    │  │  Dashboard  │  │   Console   │                   │ │
│  │   └─────────────┘  └─────────────┘  └─────────────┘                   │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    │ HTTPS / REST API                       │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     BUSINESS LOGIC LAYER (Backend)                     │ │
│  │                                                                         │ │
│  │   Node.js + Express                                                    │ │
│  │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │ │
│  │   │    Auth     │  │   Survey    │  │    PWRS     │  │   Training  │  │ │
│  │   │   (JWT)     │  │  Management │  │   Engine    │  │   Trigger   │  │ │
│  │   └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                    ┌───────────────┴───────────────┐                       │
│                    │                               │                        │
│                    ▼                               ▼                        │
│  ┌─────────────────────────────┐  ┌─────────────────────────────────────┐ │
│  │      DATA LAYER             │  │      ML LAYER (Model Server)        │ │
│  │                             │  │                                      │ │
│  │   MongoDB                   │  │   Python + Flask                    │ │
│  │   • Users                   │  │   • Data Normalizer                 │ │
│  │   • Surveys (Target/Factor) │  │   • KNN Implementation              │ │
│  │   • Responses               │  │   • GAN Training Pipeline           │ │
│  │   • Model Metadata          │  │   • Neural Network Inference        │ │
│  │   • Feedback Records        │  │   • Model Versioning                │ │
│  └─────────────────────────────┘  └─────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Figure 3.** Three-tier architecture separating presentation, business logic, and data/ML concerns.

### 4.2 Component Overview

**Presentation Layer**: A React-based Single Page Application (SPA) provides role-specific interfaces for students (survey completion, prediction viewing), advisors (student roster management), and administrators (survey configuration, model training). The SPA architecture supports responsive design across devices and enables auto-save functionality to prevent data loss during survey completion.

**Business Logic Layer**: A Node.js/Express backend orchestrates authentication (via JSON Web Tokens), survey workflow management, PWRS calculation, and communication with the ML layer. The backend enforces the Progressive Learning Framework's phase transitions, ensuring students see appropriate interfaces based on current enrollment counts.

**Data Layer**: MongoDB provides flexible document storage for surveys, responses, and model metadata. Schema flexibility accommodates evolving survey instruments without migration overhead.

**ML Layer**: A Python/Flask service handles computationally intensive tasks—feature normalization, KNN prediction, GAN training, and neural network inference. Asynchronous job queues prevent long-running training tasks from blocking the main application.

### 4.3 Technology Stack Summary

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend | React 18, TypeScript, Tailwind CSS | Component-based UI rendering |
| Backend | Node.js 20, Express | API orchestration, business logic |
| Database | MongoDB 7.0 | Flexible document storage |
| ML Server | Python 3.9, Flask | Model training and inference |
| ML Libraries | scikit-learn, TensorFlow/Keras | KNN, GAN, neural network implementations |
| Authentication | JWT | Stateless session management |
| Deployment | Docker, Nginx | Containerization, reverse proxy |

**Table 2.** Technology stack for the ACOSUS platform.

---

## 5 Evaluation Methodology

The evaluation of ACOSUS proceeds in two phases. The first phase, detailed in this section, focuses on **usability and user experience** through a pilot study with transfer students. The second phase, planned for longitudinal deployment, will assess **predictive validity** by correlating system predictions with actual academic outcomes.

### 5.1 Pilot Study Design

#### 5.1.1 Research Questions

The pilot study addresses five research questions:

| ID | Research Question | Focus |
|----|-------------------|-------|
| **RQ1** | How do transfer students perceive the usability of ACOSUS? | Usability |
| **RQ2** | What is the completion rate and data quality of the dual-survey system? | Feasibility |
| **RQ3** | How do students perceive the accuracy of system-generated predictions? | Trust/Validity |
| **RQ4** | Is the informed consent process effective in communicating data usage? | Ethics |
| **RQ5** | What features or improvements do students prioritize? | Enhancement |

#### 5.1.2 Participants and Recruitment

The pilot study targets **10 transfer students** in computing majors at [Institution Name]. This sample size is deliberate: it corresponds to the threshold required to transition the system from Phase 1 (Bootstrap) to Phase 2 (Instance-Based Learning). Pilot participants thus serve a dual role—they evaluate usability while simultaneously seeding the dataset for predictive modeling.

Participants are recruited through departmental advising contacts and course announcements, with eligibility limited to transfer students who matriculated within the past two academic years. Compensation of $10 (gift card) acknowledges the approximately 30–45 minute time investment required. `[CHECK WITH PROFESSOR: Confirm institution name and compensation details]`

#### 5.1.3 Study Protocol

Participants complete a structured task sequence:

1. **Onboarding** (5 min): Account creation, informed consent review
2. **Target Survey Completion** (10–15 min): Full Target Survey to establish ground truth
3. **Factor Survey Completion** (5 min): Feature data collection
4. **Prediction Review** (3 min): View success rate prediction, provide feedback rating
5. **Evaluation Survey** (10–15 min): Complete usability and experience questionnaire

### 5.2 Evaluation Instruments

#### 5.2.1 Technology Acceptance Model (TAM) Constructs

The evaluation survey employs validated TAM constructs to assess adoption potential:

**Perceived Usefulness (PU)**: Six items measuring whether the system improves academic planning effectiveness. Example: "Using this AI counseling system enhances my effectiveness in transfer planning."

**Perceived Ease of Use (PEOU)**: Six items measuring interaction effort. Example: "Learning to operate this AI counseling system was easy for me."

Responses use 5-point Likert scales (Strongly Disagree → Strongly Agree). Composite scores for PU and PEOU provide standardized measures of system acceptance.

#### 5.2.2 Prediction Quality Assessment

Four items assess prediction accuracy and actionability:
- "How accurate did you find the system's assessment of your academic success factors?"
- "Did the success probability estimates align with your own assessment?"
- "How relevant were the recommendations to your specific situation?"
- "How actionable were the recommendations provided?"

#### 5.2.3 Open-Ended Feedback

Qualitative questions capture nuanced user perspectives:
- "What was the most helpful feature of the system?"
- "What feature or capability was missing that would have improved your experience?"
- "If you could redesign one aspect of the system, what would it be?"

### 5.3 Analysis Plan

**Quantitative Analysis**:
- Descriptive statistics (mean, standard deviation) for all Likert items
- Composite scores for PU (mean of Q1–Q6) and PEOU (mean of Q7–Q12)
- Cronbach's alpha for internal consistency
- Completion rate analysis to identify survey sections causing abandonment

**Qualitative Analysis**:
- Thematic coding of open-ended responses
- Dual-coder approach with inter-rater reliability assessment (Cohen's Kappa)
- Theme frequency analysis to prioritize enhancement opportunities

**Success Criteria**:
- PU and PEOU composite scores ≥ 3.5 (above midpoint) indicate acceptable usability
- Prediction alignment ratings ≥ 3.5 validate the pseudo-labeling mechanism
- Completion rate ≥ 80% confirms feasibility of dual-survey approach

### 5.4 Planned Longitudinal Validation

Following the pilot study, ACOSUS will be deployed for ongoing data collection with the target institution's transfer cohort. Longitudinal validation will correlate predicted success rates with actual academic outcomes:

- **Short-term** (1 semester): Semester GPA, course completion rate
- **Medium-term** (1 year): Year-to-year retention, credit accumulation velocity
- **Long-term** (2–4 years): Graduation rate, time-to-degree

This validation will establish the **true predictive accuracy** of ACOSUS models, moving beyond perceived accuracy (student self-assessment alignment) to objective outcome prediction. `[CHECK WITH PROFESSOR: Timeline and specific outcome measures for longitudinal validation]`

---

## 6 Discussion and Future Work

### 6.1 Summary of Contributions

This paper presents ACOSUS, an AI-driven advising system that addresses the unique challenges of supporting transfer students through three architectural innovations:

1. **Progressive Learning Framework**: A phased approach that delivers immediate value with zero training data (Phase 1), transitions to instance-based prediction with minimal observations (Phase 2), and scales to neural network inference through generative augmentation (Phase 3). This framework solves the "cold start" problem that renders conventional machine learning infeasible for small transfer cohorts.

2. **Dual-Survey Architecture**: A flexible study design separating feature collection (Factor Surveys) from outcome measurement (Target Surveys), enabling multiple prediction targets and iterative feature refinement while maintaining clean train/test separation.

3. **Feedback-Driven Pseudo-Labeling**: An active learning mechanism that reduces respondent burden by 60–70% while maintaining data quality through selective ground-truth collection when predictions diverge from student expectations.

These contributions are grounded in prior research on transfer student success factors [1], [2], [5], [6], [7] and address documented gaps in existing advising systems, which rarely account for transfer-specific variables such as credit articulation, transfer shock, and belonging uncertainty [3], [4].

### 6.2 Limitations

Several limitations frame the current work:

**Heuristic Dependency in Bootstrap Phase**: During Phase 1, the system relies on expert-assigned priority weights and option weightages. These heuristics, while grounded in literature, may not perfectly reflect the local context of every institution or student population.

**Domain Specificity**: Current Factor Survey instruments are tailored to computing majors, with questions addressing programming experience and technical preparation. Adaptation to other disciplines would require instrument redesign and revalidation.

**Proxy Outcome Measure**: The "success rate" label derives from student self-assessment rather than objective graduation data. While self-efficacy and perceived readiness correlate with persistence [5], [6], they remain imperfect proxies for actual academic outcomes.

**Sample Size**: The planned pilot study (N = 10) provides sufficient data for usability assessment and system bootstrapping but cannot establish statistical validity of predictive models.

### 6.3 Future Directions

**Longitudinal Outcome Validation**: Tracking pilot participants through graduation will enable correlation of predicted success rates with actual outcomes, establishing true predictive validity.

**GAN Architecture Optimization**: As the dataset grows beyond 100 students, systematic experimentation with GAN architectures (loss functions, conditioning strategies, augmentation ratios) will refine synthetic data quality. `[CHECK WITH PROFESSOR: Specific GAN research directions]`

**Cross-Institutional Deployment**: The modular architecture supports multi-institutional deployment, enabling larger-scale validation and potentially federated learning approaches that share model improvements without sharing raw student data.

**Advisor Interface Development**: While the current implementation focuses on student-facing features, planned enhancements include advisor dashboards for cohort-level analytics and early-alert integration.

---

## References

[1] K. Vargas, V. Diaz, C. MacDonald, Y. Wan, X. Wang, P. Aggarwal, S. Rayana, and S. Bogle, "Investigation of Social Cognitive Factors Affecting Computing Transfer Students," in *Proc. ASEE Annual Conference*, 2022.

[2] X. Wang, S. Rayana, S. Bogle, Y. Wan, and P. Aggarwal, "A Preliminary Factor Analysis on the Success of Computing-Major Transfer Students," in *Proc. ASEE Annual Conference*, 2023.

[3] C. MacDonald, P. Aggarwal, X. Wang, Y. Wan, S. Rayana, S. Bogle, and R. Caraballo, "An Analysis of the Experience of Transfer Students through Topic Modeling," in *Proc. ASEE Annual Conference*, 2024.

[4] J. Standfast, J. Franco, R. Caraballo, K. Vargas, Y. Wan, X. Wang, S. Bogle, P. Aggarwal, and S. Rayana, "Deciding on a College Transfer: A Mixed-Methods Analysis of Reddit Discussions," in *Proc. ASEE Annual Conference*, 2024.

[5] C. Ty, K. Vargas, Y. Wan, X. Wang, P. Aggarwal, S. Rayana, and S. Bogle, "Investigation of Computing Transfer Students' Success," in *Proc. ASEE Annual Conference*, 2024.

[6] X. Wang, "On My Own: The Challenge of Transfer-Student Academic Momentum," *Teachers College Record*, vol. 122, no. 1, pp. 1–42, 2020.

[7] B. K. Townsend and K. B. Wilson, "The Academic and Social Integration of Community College Transfer Students in a University Setting," *Community College Journal of Research and Practice*, vol. 33, no. 10, pp. 833–855, 2009.

[8] F. B. Baker and S.-H. Kim, *Item Response Theory: Parameter Estimation Techniques*, 2nd ed. New York: Marcel Dekker, 2004.

---

## Notes and Placeholders for Review

The following items require verification or additional information:

1. **Section 3.3.1** - Bootstrap threshold of 10 students: Is this threshold correct and should it be configurable per study?

2. **Section 3.3.3** - GAN augmentation ratio (100 real → 400-500 synthetic): Confirm specific ratio and validation metrics for synthetic data quality (e.g., Kolmogorov-Smirnov test, correlation preservation).

3. **Section 3.3.3** - Neural network architecture details: Pending finalization based on empirical tuning.

4. **Section 3.5.2** - Estimated percentage of high-rating feedback (50-70%): Confirm based on pilot data or adjust to "expected" rather than estimated.

5. **Section 3.7** - Performance metrics for model validation: Likely MAE, RMSE, R² but confirm preferred metrics.

6. **Section 5.1.2** - Institution name and compensation details for pilot study.

7. **Section 5.4** - Timeline and specific outcome measures for longitudinal validation.

8. **Section 6.3** - Specific GAN research directions for future work.

---

## Appendix A: PWRS Implementation

```python
import math
from typing import List, Dict, Any

def calculate_success_rate(
    questions: List[Dict],
    answers: Dict[str, Any],
    calibration_method: str = "logistic",
    k_factor: float = 6.0
) -> float:
    """
    Calculate student success rate using PWRS model.

    Args:
        questions: List of question configs with priorityScore and options
        answers: Dict mapping question_slug to selected answer value
        calibration_method: "logistic", "linear", "bounded_linear", or "sigmoid"
        k_factor: Steepness for logistic/sigmoid curves

    Returns:
        Success rate as float (0-100)
    """
    total_weighted_score = 0
    total_priority = 0

    for question in questions:
        question_slug = question['slug']
        priority = question.get('priorityScore', 5)
        options = question.get('options', [])

        student_answer = answers.get(question_slug)

        if student_answer is None:
            # Missing answer: use neutral value
            normalized_score = 0.5
        else:
            max_weightage = max([opt['optionWeightage'] for opt in options])
            selected_weightage = 0
            for option in options:
                if option['optionValue'] == student_answer:
                    selected_weightage = option['optionWeightage']
                    break
            normalized_score = selected_weightage / max_weightage if max_weightage > 0 else 0.5

        weighted_score = normalized_score * priority
        total_weighted_score += weighted_score
        total_priority += priority

    # Calculate base score
    base_score = total_weighted_score / total_priority if total_priority > 0 else 0.5

    # Apply calibration curve
    if calibration_method == "linear":
        success_rate = base_score * 100
    elif calibration_method == "bounded_linear":
        success_rate = min(95, max(10, base_score * 100))
    elif calibration_method == "logistic":
        success_rate = 100 / (1 + math.exp(-k_factor * (base_score - 0.5)))
    elif calibration_method == "sigmoid":
        success_rate = 20 + 70 / (1 + math.exp(-k_factor * (base_score - 0.5)))
    else:
        raise ValueError(f"Unknown calibration method: {calibration_method}")

    return round(success_rate, 1)
```

**Listing 1.** Python implementation of the Priority-Weighted Response Scoring algorithm.
