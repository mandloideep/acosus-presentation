# **An AI-Driven Transfer Student Advising System: Design, Implementation, and Evaluation**

## **3\. System Design and Architecture**

### **3.1 Architectural Philosophy and Design Rationales**

The architectural foundation of the ACOSUS (AI-driven Counseling System for Underrepresented Students) platform represents a significant divergence from contemporary trends in educational data mining, which predominantly favor "Big Data" approaches requiring massive, pre-existing data lakes. The design philosophy governing this system is predicated on a "Small Data" paradigm, necessitated by the specific operational constraints of departmental advising for transfer students. In this context, historical data is frequently fragmented, inconsistent, or statistically insignificant due to small cohort sizes—often fewer than 100 students per year in specific majors like Computer Science.1 Consequently, deploying a traditional deep learning architecture, which requires thousands of labeled examples to converge, would be structurally impossible.

To address this "Cold Start" problem, the system employs a **Progressive Learning Framework**.1 This framework is not merely a feature but the central architectural thesis: the system must be capable of providing immediate, heuristic-based value from "Day One" (zero training data) and autonomously evolve into a sophisticated, data-driven predictive engine as the dataset organically grows. This necessitates a highly modular, state-driven architecture capable of seamlessly hot-swapping inferential engines—transitioning from deterministic expert systems to stochastic machine learning models—without disrupting the user experience or requiring code deployments.1

Furthermore, the design is deeply rooted in the socio-academic realities of the transfer student experience, specifically the phenomenon of "Transfer Shock"—a transient but critical decline in academic performance and psychosocial well-being immediately following matriculation.1 The architecture explicitly rejects the "registrar-only" view of student success (which looks solely at GPA and credits) in favor of a holistic data model. This model ingests unstructured, qualitative signals regarding "belonging uncertainty," financial anxiety, and social integration—factors identified in the literature as having higher predictive power for attrition among underrepresented minority (URM) students than academic metrics alone.1 This requirement for high-dimensional qualitative data drives the implementation of the system's unique **Dual-Survey Architecture**, which separates the collection of predictive features from the collection of ground-truth validation data to manage user cognitive load.1

### **3.2 High-Level System Architecture**

The system utilizes a robust Three-Tier Architecture, strictly separating presentation, business logic, and data/computation layers. This separation of concerns is critical not only for maintainability and scalability but for compliance with strict student data privacy regulations (e.g., FERPA), ensuring that no direct access to the data layer is possible from the client-side presentation layer.1

#### **3.2.1 Presentation Layer (Client)**

The user interface is engineered as a Single Page Application (SPA) using the React framework and TypeScript.1 The choice of an SPA architecture is deliberate, prioritizing the responsiveness required for complex, multi-step survey instruments where page reloads would degrade user completion rates. The presentation layer is further segmented into distinct functional portals based on user roles, guarded by strict client-side routing logic:

* **Student Portal:** Designed for minimal friction and maximum clarity. It hosts the Survey Rendering Engine and the Prediction Visualization dashboard. The design prioritizes "Progressive Disclosure," revealing complex data entry requirements in stages to prevent survey fatigue.1  
* **Advisor Portal:** Focuses on aggregate visibility and intervention management. It includes distinct views for roster management and an "Act-As" capability, allowing advisors to input data on behalf of students during in-person sessions—a requirement derived from the need for "relationship-rich" advising.1  
* **Administrative Console:** Provides system configuration capabilities, user role management, and the dashboard for triggering asynchronous model training jobs.

#### **3.2.2 Business Logic Layer (Backend API)**

The core orchestration logic resides in a Node.js/Express environment.1 This layer serves as the secure gateway and traffic controller for the entire system. It implements the RESTful API endpoints (versioned as /api/v2/) that handle authentication, user profile management, and survey submission. Crucially, this layer implements the **Finite State Machine (FSM)** that governs the user's progression through the system's various phases (e.g., forcing a user to complete the "Factor Survey" before seeing a prediction).1 By centralizing this logic in the API layer, the system ensures that business rules are enforced consistently regardless of the client (web browser, mobile, or future third-party integrations).

#### **3.2.3 Data and Machine Learning Layer**

The persistence strategy utilizes MongoDB, a NoSQL database chosen for its schema flexibility.1 This flexibility is paramount in a research context where the specific "risk factors" (survey questions) collected from students may need to evolve rapidly as new literature on transfer student success emerges. A rigid SQL schema would impose significant migration overhead for every change in the survey instrument.

The Machine Learning components are decoupled into a dedicated Model Server built with Python and Flask.1 This separation is a critical architectural decision for performance and stability. While the Node.js backend handles high-concurrency, I/O-bound web traffic, the Python server handles CPU-intensive computational tasks—such as training K-Nearest Neighbors (KNN) models or generating synthetic data via Generative Adversarial Networks (GANs). Communication between the Business Logic Layer and the ML Layer occurs via asynchronous HTTP requests and job queues, ensuring that long-running training tasks do not block the main application thread or degrade the responsiveness of the student-facing interface.1

### **3.3 The Progressive Learning Framework**

The defining innovation of the ACOSUS architecture is the **Progressive Learning Framework**. This framework provides a structured lifecycle for the system's predictive intelligence, solving the "Small Cohort" constraint.1 It divides the system's maturity into three distinct phases, each employing a different algorithmic strategy.

| Phase | Cohort Size (N) | Algorithmic Strategy | Primary Goal | Mechanism |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Bootstrap** | $N \< 10$ | **Heuristic Scoring (PWRS)** | Data Collection & Cold Start | Uses expert-defined weights to calculate a deterministic readiness score. No ML involved. |
| **2\. Instance-Based** | $10 \\leq N \< 100$ | **K-Nearest Neighbors (KNN)** | Personalized Prediction | Finds $k$ similar peers in the database and aggregates their ground-truth scores. |
| **3\. Generative** | $N \\geq 100$ | **Neural Network \+ cGAN** | Generalization & Scale | Uses synthetic data augmentation to train deep learning classifiers without overfitting. |

**Phase 1: The Heuristic Bootstrap (Priority-Weighted Response Scoring)**  
In the absence of historical training data, traditional supervised learning is impossible. To provide immediate value to the first cohort of users, the system utilizes the Priority-Weighted Response Scoring (PWRS) algorithm.1 This is a deterministic expert system inspired by Item Response Theory (IRT).1 Domain experts (academic advisors and researchers) assign distinct priority weights to specific survey questions. For example, "Do you have secured financial aid?" might be assigned a priority of 10, while "Do you commute via public transit?" might be assigned a 5\. The system calculates a normalized readiness score based on these pre-configured weights. This ensures that the very first student receives a scientifically grounded assessment of their transfer readiness, incentivizing them to use the system and thereby contributing data for future models.  
**Phase 2: Instance-Based Learning (KNN)**  
Once the system accumulates a small dataset ($10 \\leq N \< 100$), it automatically transitions to a K-Nearest Neighbors (KNN) regression model.1 KNN is mathematically ideal for this "small data" phase because it is a non-parametric "lazy learner"—it does not require a training phase to estimate parameters. Instead, it predicts a student's success by locating the $k$ most similar historical profiles in the feature space and aggregating their known outcomes. The parameter $k$ is dynamic, calculated as $k \= \\sqrt{N}$ 1, ensuring the model adapts its sensitivity as the dataset grows. This phase shifts the system from "what experts think matters" (PWRS) to "what actually happened to similar students."  
**Phase 3: Generative Augmentation (Neural Networks \+ cGAN)**  
As the dataset matures ($N \\geq 100$), the system enables the training of neural networks. However, $N=100$ is still insufficient for deep learning. To bridge this gap, the architecture incorporates Conditional Generative Adversarial Networks (cGANs).1 The cGAN learns the complex, non-linear distribution of the real student data and generates high-fidelity synthetic student profiles. This synthetic data augmentation expands the training set by orders of magnitude, allowing for the training of robust neural network classifiers that can detect subtle, non-linear interactions between risk factors (e.g., the compounded risk of "working full-time" \+ "first-generation status") that simple linear models like KNN might miss.

### **3.4 The Dual-Survey Architecture and Feedback Loop**

A fundamental challenge in predictive modeling for student success is the latency of the target variable. In a live advising scenario, the true "label" (Did the student graduate?) is not known for 2-4 years. To train a model *now*, the system requires a proxy for success. ACOSUS addresses this via a novel **Dual-Survey Architecture** coupled with a **Pseudo-Labeling Feedback Loop**.1

#### **3.4.1 The Factor Survey (Input Features \- $X$)**

This instrument is designed to be lightweight (approx. 5 minutes) to minimize friction. It collects the independent variables used for prediction—the "Factors." It consists of 11 objective questions covering Academic Background (GPA, credits), Financial Support (aid status, employment), Logistics (commute, caregiving duties), and Technical Experience.1 These objective facts form the feature vector for the ML model.

#### **3.4.2 The Target Survey (Ground Truth \- $Y$)**

This instrument is more extensive (approx. 15 minutes) and collects the dependent variables—the "Targets." It consists of 27 subjective questions derived from "Transfer Student Capital" literature 1, measuring self-reported "Academic Confidence," "Sense of Belonging," "Motivation," and "Perceived Support." The responses to this survey are processed via the PWRS formula to calculate a precise "Readiness Score" (0-100), which serves as the ground-truth label for training.1

#### **3.4.3 The Pseudo-Labeling Feedback Mechanism**

Requiring every student to complete the long Target Survey would likely result in high abandonment rates. The system utilizes a feedback loop to optimize this trade-off:

1. **Prediction Generation:** A student completes the short **Factor Survey**. The system (using KNN/Neural models) predicts their Readiness Score.  
2. **User Verification:** The student is shown the prediction and asked to rate its accuracy on a 5-star scale ("Does this score accurately reflect your current confidence?").  
3. **Branching Logic:**  
   * **High Agreement ($\\geq 4$ Stars):** The system infers the prediction is accurate. It accepts the predicted score as a "Pseudo-Label" ($Y'$). The student's Factor data ($X$) and this pseudo-label are added to the training set. The student is *exempt* from the long Target Survey.  
   * **Low Agreement ($\< 4$ Stars):** The system infers the prediction was inaccurate. The student is then redirected to complete the full **Target Survey** to establish a true Ground Truth ($Y$). This serves a dual purpose: it corrects the individual student's record and provides a high-quality, verified error-correction data point for the next model training cycle.1

This mechanism creates a self-correcting system that selectively imposes the burden of ground-truth collection only when the model is uncertain or inaccurate, thereby optimizing data quality while respecting user time.

### **3.5 Data Privacy and Security Framework**

Given the sensitive nature of educational records and the inclusion of potentially stigmatizing data (e.g., financial insecurity, belonging uncertainty), the architecture implements a rigorous security framework.

* **Role-Based Access Control (RBAC):** Access to data is strictly governed by middleware that enforces scope checks at the API level. Students may only access their own records (verified via JWT claims). Advisors are restricted to accessing records of students explicitly assigned to their roster or who have granted temporary "Act-As" permissions.  
* **Data Anonymization Pipeline:** The Machine Learning pipeline is architecturally isolated from the PII (Personally Identifiable Information) store. Before data is extracted for model training, a transformation layer strips all direct identifiers (Names, IDs, Emails), replacing them with hashed surrogate keys. The ML models are trained exclusively on anonymized feature vectors, ensuring that the AI cannot memorize or leak specific student identities.1

## **4\. Implementation Details**

### **4.1 Frontend Engineering and User Experience**

The client-side application is a complex piece of engineering, comprising approximately 45,000 lines of TypeScript code.1 It is structured not merely to display forms, but to manage the complex state transitions of the progressive learning workflow while ensuring a highly responsive user experience.

#### **4.1.1 Feature-Based Modular Architecture**

Unlike traditional layered architectures (grouping files by type: components/, services/, utils/), the ACOSUS frontend adopts a **Feature-Based Directory Structure**.1 Code is organized by domain context: features/survey/, features/dashboard/, features/auth/, and features/admin/.

* **Rationale:** This colocation strategy significantly enhances maintainability. All logic required for the survey subsystem—Redux state slices, API hooks, validation utilities, and UI components—resides in a single directory. This allows for the "Survey Rendering Engine" to be treated as a self-contained module that can be tested or refactored in isolation from the rest of the application.

#### **4.1.2 The Survey Rendering Engine**

A core component of the frontend is the **Survey Rendering Engine**, which implements the **Registry Pattern** to manage the complexity of dynamic form generation.

* **Implementation:** A central registry maps specific QuestionType strings (e.g., multiple-choice, scale, date-range, multi-select) to their corresponding React components.1 The engine consumes a JSON configuration defining the 11 Factor questions and 27 Target questions. This configuration drives the UI rendering at runtime.  
* **Dynamic capabilities:** This architecture allows the application to render complex, nested questions without hard-coding the DOM structure. It supports features like conditional branching (showing Question B only if Question A is answered a certain way) and strictly enforces validation rules (e.g., ensuring "GPA" is between 0.0 and 4.0) before allowing navigation.

#### **4.1.3 Robust State Management: Auto-Save and Debouncing**

To support students who may be completing surveys on mobile devices or unstable campus Wi-Fi, data persistence is a critical requirement. The implementation utilizes a custom useAutoSave hook that manages the synchronization of local form state with the backend database.

* **Debouncing Strategy:** To prevent saturating the network and database with write operations on every keystroke, the implementation applies a **Debouncing Pattern**. State changes trigger a timer; the actual API write request is dispatched only after 2000ms of user inactivity.  
* **Reconciliation Logic:** Simultaneously, the state is persisted to the browser's localStorage. On application reload (e.g., if the user accidentally refreshes the page), the hook implements a reconciliation strategy: it compares the timestamps of the local state versus the fetched server state and hydrates the form with the most recent version, ensuring zero data loss.

#### **4.1.4 Prediction Visualization and Contextualization**

The "Student Portal" implementation focuses on interpreting the raw probabilistic output of the ML models. The backend returns a raw float (0.0 \- 1.0) representing the success probability. The frontend implements a transformation layer that maps these values to semantic bands for display:

* **At-Risk (0% \- 40%):** Rendered with urgency indicators, prompting the student to seek advising.  
* **Moderate (40% \- 70%):** Rendered as a neutral state, highlighting specific areas for improvement.  
* High Readiness (70% \- 100%): Rendered with positive reinforcement.1  
  This logic includes a visual gauge component that animates the score, providing immediate, accessible feedback that contextualizes the abstract probability.

### **4.2 Backend Services and Orchestration Logic**

The backend, built on Node.js 20 LTS, is the nervous system of the platform. It implements the rigorous business logic required to maintain the integrity of the data collection process.

#### **4.2.1 Finite State Machine (FSM) for Survey Workflow**

The logic governing which survey a student sees is not a simple set of if/else statements but a formally implemented **Finite State Machine**.1 The explicit states include:

* created  
* target\_in\_progress / target\_completed  
* factor\_in\_progress / factor\_completed  
* prediction\_shown  
* feedback\_provided

The FSM strictly enforces the research protocol. For example, for a user in the "Bootstrap Cohort" (User ID \< 10), the valid transition from created is *only* to target\_in\_progress. Any attempt to bypass the Target Survey and jump to the Factor Survey is rejected by the state machine logic. Conversely, for a "Prediction Cohort" user (User ID \> 10), the transition flows from created to factor\_in\_progress. The transition from prediction\_shown is conditional: if the user submits a feedback rating $\< 4$, the machine transitions to target\_in\_progress, forcing the corrective loop. This robust implementation guarantees that the dataset structure remains consistent with the progressive learning design.

#### **4.2.2 PWRS Calculation Service**

The Priority-Weighted Response Scoring service is a dedicated module that executes the mathematical logic for the heuristic phase.

* Scoring Algorithm: The service iterates through the user's responses. For each question, it looks up the configured priority ($P\_q$) and the normalized score ($S\_a$) of the selected answer option. The base score is calculated as the weighted average:

  $$\\text{BaseScore} \= \\frac{\\sum (S\_a \\times P\_q)}{\\sum P\_q}$$  
* **Logistic Calibration:** The raw weighted average often clusters around the mean (0.5), resulting in "muddy" signals. To fix this, the implementation applies a **Logistic Calibration Strategy**.1 The raw score is passed through a sigmoid function with a configurable steepness parameter ($k=6$). This non-linear transformation pushes scores towards the extremes (high readiness or high risk), increasing the distinctiveness of the signal and making the feedback more actionable for students.

#### **4.2.3 Asynchronous Job Queue for Model Training**

Training machine learning models is a blocking, CPU-intensive operation. To prevent this from degrading the performance of the web server (which creates the latency perceived by users), the implementation utilizes an asynchronous Job Queue architecture.1

1. **Trigger:** An administrator clicks "Retrain Model."  
2. **Dispatch:** The Node.js server aggregates the training data and dispatches a payload to the Python Model Server via a private internal API.  
3. **Process:** The Node.js server immediately returns a "202 Accepted" response to the client, preventing a timeout.  
4. Callback: The Python server processes the training job in the background. Upon completion, it hits a webhook on the Node.js server to update the system status and deploy the new model version.  
   This architecture allows the system to scale, handling heavy training workloads without impacting the responsiveness of the student dashboard.

### **4.3 Machine Learning Pipeline Engineering**

The Machine Learning layer, implemented in Python using scikit-learn and PyTorch, handles the intelligent aspects of the system.

#### **4.3.1 Feature Engineering and Domain-Specific Normalization**

Raw survey data is categorical and often ordinal. The feature engineering pipeline transforms this into numerical vectors suitable for ML ingestion. A key innovation in the implementation is the **Non-Linear Duration Scoring** function.1

* **Context:** Literature suggests that both "rushing" a degree and taking too long are correlated with attrition.1  
* **Implementation:** Instead of a linear normalization of "Years to Degree," the system implements a curve function.  
  * 2-4 Years: Scored as 1.0 (Optimal).  
  * \< 2 Years: Penalized to 0.4 (Risk of burnout/unrealistic planning).  
  * 6 Years: Penalized to 0.3 (Risk of stagnation/life interference).  
  * 4-6 Years: Scaled linearly from 1.0 down to 0.5.  
    This domain-aware feature engineering embeds expert knowledge directly into the input data, improving the model's ability to detect realistic risk patterns.

#### **4.3.2 K-Nearest Neighbors (KNN) Implementation**

For Phase 2, the system uses KNeighborsRegressor. A critical implementation detail is the dynamic calculation of $k$, the number of neighbors. A static $k$ would fail as the dataset grows from 10 to 100\. The implementation defines $k$ dynamically:

$$k \= \\min(\\max(3, \\sqrt{N}), 10)$$

This logic ensures that for very small datasets ($N=10$), $k$ is small enough (3) to find meaningful matches, but as the dataset grows ($N=100$), $k$ increases (to 10\) to smooth out noise, preventing overfitting.1

#### **4.3.3 Conditional GAN Architecture**

For Phase 3 ($N \\geq 100$), the implementation deploys a Conditional GAN to augment the training data.

* **Generator:** A neural network that takes a noise vector $z$ and a condition vector $c$ (the desired Readiness Score label) and outputs a synthetic feature vector $\\hat{x}$.  
* **Discriminator:** A network that attempts to distinguish between real pairs $(x, c)$ and generated pairs $(\\hat{x}, c)$.  
* **Implementation Detail:** The loss function is carefully tuned to penalize the generation of "impossible" students (e.g., a student with "0 credits" but "Senior" status), ensuring the synthetic data respects the logical constraints of the academic domain.

### **4.4 Technical Stack Summary**

| Layer | Component | Technology | Role |
| :---- | :---- | :---- | :---- |
| **Frontend** | Framework | React (TypeScript) | Component-based UI rendering |
|  | State | Redux Toolkit | Global state management |
|  | Routing | React Router | Role-based navigation guards |
| **Backend** | Runtime | Node.js / Express | API endpoint orchestration |
|  | Database | MongoDB | Flexible document storage |
|  | Auth | JWT (JSON Web Tokens) | Stateless authentication |
| **ML Layer** | Language | Python 3.9 | Scientific computing |
|  | Frameworks | scikit-learn, PyTorch | KNN and GAN implementation |
|  | Interface | Flask | Internal REST API for ML jobs |

## **5\. Survey Design and Experimental Study**

### **5.1 Empirical Foundations of Survey Instrumentation**

The validity of any predictive system relies entirely on the quality of its input data. The design of the ACOSUS survey instruments is not arbitrary; it is a direct translation of the qualitative findings from recent transfer student literature into quantitative metrics. The survey items function as sensors, detecting the specific friction points—financial, academic, and social—that characterize the "Transfer Student Experience".1

#### **5.1.1 The "Factor Survey": Detecting Structural Risk**

The **Factor Survey** serves as the feature extraction mechanism ($X$). Its design prioritizes objective, structural variables identified as high-impact predictors in the literature.

* **Financial & Economic Pressure:** Previous studies utilizing Reddit topic modeling and surveys of computing students identified "Cost," "Tuition," and "Financial Aid" as the dominant stressors influencing transfer decisions.1 Ty et al. 1 further quantified that employment status (working full-time vs. part-time) has a statistically significant correlation with GPA outcomes.  
  * *Instrument Design:* Consequently, the survey includes high-priority, weighted questions regarding **Employment Intensity** (Hours/Week) and **Financial Security** (Aid status). These features are not merely demographic trivia; they are weighted heavily in the initial PWRS algorithm to reflect their proven impact on retention.  
* **Academic Logistics:** Literature highlights that "Transfer Shock" is often exacerbated by logistical friction, such as commuting burdens and credit transfer disputes.1  
  * *Instrument Design:* The survey captures **Commute Time** and **Credit Transfer Percentage**, allowing the model to identify students whose time-to-degree is threatened by logistical overhead rather than academic ability.

#### **5.1.2 The "Target Survey": Measuring Psychosocial Readiness**

The **Target Survey** serves as the ground-truth mechanism ($Y$). It measures the latent variables of "success" that grades alone cannot capture.

* **Transfer Shock & Belonging:** The concept of "Transfer Shock" describes a dip in performance driven by psychosocial factors like "belonging uncertainty" and isolation.1 Reddit analysis reveals pervasive themes of "Loneliness" and difficulty "Adjusting to a New School".1  
  * *Instrument Design:* This instrument includes Likert-scale items derived from validated scales for **Sense of Belonging**, **Academic Confidence**, and **Perceived Support**. By quantifying these subjective states, the system can define "Readiness" holistically. A student with a 4.0 GPA who reports extreme isolation and zero support is correctly identified as "At-Risk" by this model, whereas a registrar-based model would miss them.  
* **Technical Self-Efficacy:** Specific to computing majors, "Programming Proficiency" (e.g., skill gaps in C++ or Java) was identified as a major source of anxiety and academic stumbling blocks.1  
  * *Instrument Design:* The survey includes specific self-assessments of technical preparedness, ensuring the AI can distinguish between general academic risk and specific curriculum misalignment.

### **5.2 Evaluation Methodology: The Alpha Bootstrap Study**

Because ACOSUS utilizes a Progressive Learning Framework that begins with $N=0$, the initial evaluation is designed as an **Alpha Testing / Usability Study** targeting the "Bootstrap Phase." The primary objective is not to validate a mature neural network (which requires $N\>100$), but to validate the feasibility of the data collection mechanism and the usability of the system for the first cohort of users who will "bootstrap" the intelligence.

#### **5.2.1 Research Questions**

The study is structured to answer five specific Research Questions (RQs) 1:

| ID | Research Question | Focus |
| :---- | :---- | :---- |
| **RQ1** | How do transfer students perceive the usability/UX of ACOSUS? | **Usability** |
| **RQ2** | What is the completion rate and data quality of the dual-survey system? | **Feasibility** |
| **RQ3** | How do students perceive the accuracy of the PWRS-generated predictions? | **Trust/Validity** |
| **RQ4** | Is the informed consent process effective in communicating privacy usage? | **Ethics/Privacy** |
| **RQ5** | How do advisors experience the roster management and "Act-As" tools? | **Advisor Utility** |

#### **5.2.2 Experimental Design**

The study utilizes a **single-group, within-subjects design**.1 Since no baseline AI advising system exists at the target institution, a control group comparison is not feasible for this alpha stage.

* **Participants:** The study targets a recruitment sample of **10 Transfer Students** (Computing Majors) and **2 Academic Advisors**. This sample size is statistically deliberate: it corresponds exactly to the threshold ($N=10$) required to transition the system from Phase 1 (Heuristic) to Phase 2 (KNN). Thus, the study participants are not just testing the system; they are physically executing the "Bootstrap" transition of the live architecture.  
* **Recruitment:** Participants are recruited from Computer Science and IT programs at Northeastern Illinois University (NEIU), specifically targeting underrepresented transfers.  
* **Incentive:** Recognizing the cognitive burden of the "Bootstrap" workflow (completing both Target and Factor surveys), participants are compensated with a $10 Amazon Gift Card.1

### **5.3 Study Protocol and Task Analysis**

The data collection follows a structured, task-based protocol designed to simulate the complete user journey from onboarding to value realization. The session is estimated to take 30-45 minutes per participant.

| Task | Description | Metric Captured |
| :---- | :---- | :---- |
| **Task 1** | **Onboarding:** Account creation and Informed Consent review. | Time-on-Task, Consent/Drop-off Rate |
| **Task 2** | **Ground Truth Collection:** Completion of the 27-question Target Survey. | Completion Rate, Missing Data Rate |
| **Task 3** | **Feature Collection:** Completion of the 11-question Factor Survey. | Time-on-Task (Efficiency comparison) |
| **Task 4** | **Prediction Review:** Viewing the calculated "Readiness Score" and visualization. | Dwell Time, Click-through |
| **Task 5** | **Feedback Loop:** Providing the 5-star accuracy rating and text feedback. | Prediction Alignment Score (1-5) |
| **Task 6** | **Debrief:** Completing the SUS and TAM evaluation questionnaires. | SUS Score, TAM Construct Scores |

### **5.4 Instrumentation and Success Metrics**

To quantify the user experience, the study employs standard psychometric instruments widely recognized in Human-Computer Interaction (HCI) research.

#### **5.4.1 System Usability Scale (SUS)**

To address **RQ1**, participants complete the standard 10-item System Usability Scale (e.g., "I thought the system was easy to use," "I found the system unnecessarily complex").

* **Scoring:** Responses are converted to a 0-100 scale.  
* **Benchmark:** The success criterion for the Alpha release is a mean SUS score of **$\\geq 68$**, which represents the industry standard for "Average" or "Acceptable" usability. A score below 68 would indicate that the complexity of the dual-survey workflow is too high and requires redesign before wider rollout.

#### **5.4.2 Technology Acceptance Model (TAM) Constructs**

To assess potential adoption and address **RQ3**, the study measures constructs from the Technology Acceptance Model:

* **Perceived Usefulness (PU):** 6 items measuring whether the student believes the system improves their academic planning.  
* Perceived Ease of Use (PEOU): 6 items measuring the effort required to use the system.  
  Distinguishing between these constructs is vital. A system might be "easy to use" (high PEOU) but "useless" (low PU). For ACOSUS to succeed, it must demonstrate high Perceived Usefulness, validating that the "Readiness Score" provides actionable insight to the student.

#### **5.4.3 Prediction Quality Assessment**

Since we cannot wait 4 years to verify if the prediction was "accurate" (i.e., if the student graduated), we measure **Perceived Accuracy**. In Task 5, students rate the extent to which the system's assessment aligns with their own internal sense of confidence.

* **Metric:** Mean User Rating (1-5 stars).  
* **Implication:** A high correlation between the system's score and the student's self-assessment validates the **Pseudo-Labeling Feedback Loop**. If students consistently rate the predictions as "Accurate" (4 or 5 stars), it empirically justifies the architectural decision to use user feedback as valid training labels for the ML model.1

### **5.5 Analytic Strategy**

The analysis of the study data will employ a convergent mixed-methods approach.1

* **Quantitative Analysis:** Descriptive statistics (Mean, Standard Deviation) will be computed for SUS and TAM scores. Completion rates will be analyzed to calculate the "drop-off" funnel, identifying if specific survey sections cause abandonment.  
* **Thematic Analysis:** Qualitative data from open-ended feedback fields and facilitator observations will undergo Thematic Analysis.1 This process involves coding responses to identify recurring semantic themes (e.g., "Confusion about Financial Terminology," "Desire for Course Recommendations"). These themes will directly inform the engineering backlog for the Beta release, ensuring that the Phase 2 rollout addresses real-world user friction points.

## **6\. Conclusion and Future Work**

### **6.1 Summary of Contributions**

This research documents the design, implementation, and initial evaluation of ACOSUS, a platform that represents a paradigm shift in how higher education institutions can leverage AI for student success. By moving away from "Big Data" dependency, this work offers a scalable, equitable, and technically feasible path forward for departmental advising.

1. Architectural Contribution: The Progressive Learning Framework.  
   We introduced a novel architectural pattern that specifically solves the "Cold Start" problem in educational data mining. By engineering a system that fluidly transitions from heuristic scoring (PWRS) to instance-based learning (KNN) and finally to generative deep learning (cGANs), ACOSUS provides a blueprint for institutions to deploy intelligent tools immediately, without needing to wait years to build a massive data warehouse.  
2. Methodological Contribution: The Sustainable Data Ecosystem.  
   The Dual-Survey Architecture combined with the Pseudo-Labeling Feedback Loop offers a sustainable solution to the "Ground Truth" problem. By decoupling feature collection from label collection, and using the user's own feedback to validate predictions, the system drastically reduces the cognitive burden on students while maintaining the high data quality necessary for machine learning training.  
3. Domain Contribution: Socio-Technical Alignment.  
   The system is not a generic analytics tool; it is deeply embedded in the sociology of the transfer student experience. By explicitly engineering the feature set to capture "Transfer Shock," "Belonging Uncertainty," and "Financial Anxiety"—factors derived directly from URM student literature—ACOSUS addresses the specific equity gaps that traditional, GPA-focused systems ignore.1

### **6.2 Limitations of the Current Work**

While the Alpha phase represents a significant milestone, several limitations frame the current scope.

* **Heuristic Bias:** During the initial "Bootstrap Phase," the system relies on the PWRS algorithm, which is inherently subjective. The weights assigned to factors (e.g., the impact of "Working Full Time") are based on expert opinion and literature, which may not perfectly reflect the local reality of every student population until the data-driven models take over.  
* **Domain Specificity:** The current feature engineering is highly tuned to **Computing Majors** (e.g., questions about C/Java proficiency). While the *architecture* is generalizable, the *survey instruments* would require significant adaptation to be effective for students in Humanities or Nursing.  
* **Sample Size:** The reported evaluation is an Alpha study ($N=10$). While sufficient for usability validation and system bootstrapping, it does not provide statistical proof of the model's long-term predictive validity.

### **6.3 Future Directions and Research Roadmap**

The roadmap for ACOSUS involves three primary vectors of expansion, evolving the system from a departmental pilot to a robust institutional platform.

6.3.1 Longitudinal Validation and "True Accuracy"  
Following the Alpha study, a longitudinal cohort study will track the initial users over a 12-18 month period. This will allow for the correlation of the system's "Readiness Scores" with actual academic outcomes (Retention Rates, Semester GPA, Graduation). This is the "Gold Standard" validation: transforming the metric from Perceived Accuracy (Student thinks the score is right) to True Accuracy (The score correctly predicted attrition).  
6.3.2 Advanced Generative Augmentation  
As the dataset surpasses the $N=100$ threshold, research will focus on optimizing the Conditional GAN architecture. Future work will involve experimenting with distinct loss functions (e.g., Wasserstein loss) to ensure that the synthetic students generated for training perfectly mirror the complex, multi-modal distributions of the real underrepresented student population, further reducing the risk of bias in the neural network classifiers.1  
6.3.3 Cross-Institutional Federated Learning  
Perhaps the most ambitious future direction is the move towards Federated Learning. Many departments face the "Small Data" problem. Future iterations of ACOSUS could support a federated architecture where multiple institutions run local instances of the model. These instances could share model weights (learned patterns) without ever sharing raw student data, creating a privacy-preserving "Collective Intelligence." This would allow a small college with only 50 transfer students to benefit from the predictive insights learned from thousands of students across the entire consortium, democratizing access to high-quality AI advising.  
By synthesizing rigorous software engineering patterns with deep educational insights, ACOSUS demonstrates that "Small Data" is not a barrier to innovation, but a constraint that drives smarter, more human-centric design.

#### **Works cited**

1. Introduction\_script.pdf