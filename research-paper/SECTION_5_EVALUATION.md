# Section 5: Evaluation and User Study

## 5.1 Overview

This section presents the evaluation framework for ACOSUS, encompassing the user study design, survey instruments, and analysis methodology. The evaluation addresses two complementary objectives: (1) assessing the usability and user experience of the system, and (2) validating the effectiveness of the progressive learning approach for transfer student success prediction.

The evaluation employs a mixed-methods approach combining quantitative usability metrics with qualitative feedback to provide comprehensive insights into system effectiveness. As ACOSUS is currently in the alpha testing phase, this section presents both the completed evaluation methodology and preliminary results where available, with placeholders for data pending collection.

## 5.2 Research Questions

The evaluation addresses five primary research questions aligned with the system's design objectives:

[TABLE 9: Research Questions and Evaluation Focus]

| ID | Research Question | Focus Area |
|----|-------------------|------------|
| RQ1 | How do transfer students perceive the usability and user experience of the ACOSUS system? | User Experience & Usability |
| RQ2 | What is the completion rate and data quality of the dual-survey system (Target + Factor surveys)? | Survey Completion & Data Quality |
| RQ3 | How do students perceive the accuracy and helpfulness of ML-generated success predictions? | Prediction Accuracy Perception |
| RQ4 | Does the informed consent and onboarding process effectively communicate study objectives and data usage? | Consent & Privacy Understanding |
| RQ5 | What is the advisor experience with the centralized student data platform? | Advisor Usability |

These research questions are mapped to specific metrics and data collection methods as detailed in subsequent sections.

## 5.3 Study Design

### 5.3.1 Study Overview

The evaluation follows a single-group, within-subjects design appropriate for alpha testing of a novel system where no comparable baseline exists within the target institution.

[TABLE 10: Study Design Parameters]

| Parameter | Value |
|-----------|-------|
| Study Type | Alpha Testing / Usability Study |
| Design | Single-group, within-subjects |
| Target Sample Size | 10 transfer students + 2 academic advisors |
| Study Phase | Prototype Testing (Bootstrap Phase) |
| Timeline | Spring 2026 |
| Session Duration | 30-45 minutes per participant |
| Follow-up | Optional longitudinal tracking (6-12 months) |

The sample size of 10 students aligns with the system's bootstrap phase requirement, where the first 10 students provide the training data necessary for initial model deployment. This creates a natural evaluation cohort that simultaneously validates the system and enables its core functionality.

### 5.3.2 Participant Recruitment

**Target Population**: Underrepresented transfer students enrolled in computing programs (Computer Science, Information Technology) at Northeastern Illinois University (NEIU).

**Inclusion Criteria**:
- Currently enrolled as a transfer student OR transferred within the past 2 years
- Majoring in Computer Science, Information Technology, or related computing field
- Currently enrolled at NEIU
- Age 18 years or older
- English proficiency sufficient to complete surveys
- Access to computer/device with internet connection

**Exclusion Criteria**:
- Non-transfer students
- Non-computing majors
- Students under 18 years of age
- Prior participation in ACOSUS studies

**Recruitment Channels**:
- Direct email outreach via registrar-provided lists
- Academic advisor referrals
- Classroom announcements in CS courses (with instructor permission)
- Physical flyers in CS department and student center
- Outreach through CS clubs and transfer student organizations

**Incentives**: Participants receive a $10 Amazon gift card upon completion of each data collection session, consistent with the IRB-approved compensation structure.

### 5.3.3 Ethical Approval

The study operates under IRB-approved protocol:

| Attribute | Value |
|-----------|-------|
| Protocol Number | NEIU Protocol #202 |
| Approval Date | January 25, 2023 |
| Review Type | Expedited (45 CFR 46.110) |
| Institution | Northeastern Illinois University |
| Principal Investigator | Dr. Xiwei Wang |
| IRB Contact | IRB@neiu.edu, (773) 442-4674 |

The informed consent process requires participants to read the complete consent document, scroll to the bottom (enforced by the interface), and explicitly click "I Consent" before account creation. Consent records include timestamp, consent version, and content snapshot for audit purposes.

## 5.4 Participant Tasks

Participants complete a structured sequence of tasks designed to exercise all major system functions while collecting evaluation data:

[TABLE 11: Participant Task Sequence]

| Task | Description | Expected Duration | Success Criterion |
|------|-------------|-------------------|-------------------|
| Task 1 | System onboarding and account creation | 5-7 minutes | Account created, consent recorded |
| Task 2 | Complete Target Survey | 8-10 minutes | Success rate calculated and stored |
| Task 3 | Complete Factor Survey | 5-7 minutes | All questions answered |
| Task 4 | Review prediction/readiness score | 3-5 minutes | Prediction viewed, feedback provided |
| Task 5 | Complete Qualtrics feedback survey | 10-15 minutes | SUS and qualitative feedback collected |
| Task 6 | Optional follow-up agreement | 2-3 minutes | Longitudinal participation confirmed |

**Total Session Duration**: 30-45 minutes

### 5.4.1 Task 1: System Onboarding

Participants navigate to the registration page, read and accept the informed consent form, create an account with email verification, and complete the initial demographic profile. Success is measured by consent timestamp recording and account creation completion.

### 5.4.2 Task 2: Target Survey Completion

Participants complete the Comprehensive Student Readiness Assessment (Target Survey), which measures self-reported readiness across five categories:

[TABLE 12: Target Survey Categories]

| Category | Questions | Focus Areas |
|----------|-----------|-------------|
| Academic Confidence & Preparation | 6 | Academic readiness, commitment, time management, study habits |
| Motivation & Career Goals | 5 | Career clarity, industry awareness, professional development |
| Personal Attributes & Skills | 7 | Stress management, adaptability, problem-solving |
| Resources & Support | 4 | Financial confidence, support systems, technology access |
| Self-Assessment & Expectations | 8 | Success prediction, grade expectations, anticipated challenges |

The survey comprises 27 total questions (22 active, 5 reserved for future activation). Responses are processed through the Priority-Weighted Response Scoring (PWRS) formula to generate a readiness score (0-100%).

### 5.4.3 Task 3: Factor Survey Completion

Participants complete the Student Background & Demographics Assessment (Factor Survey), providing objective background information used as ML features:

[TABLE 13: Factor Survey Categories]

| Category | Questions | Feature Examples |
|----------|-----------|------------------|
| Academic Background | 4 | GPA, SAT score, credits completed, course load |
| Financial Support | 2 | Scholarship status, family income support |
| Logistics & Commitment | 2 | Distance to university, employment status |
| Interest & Experience | 3 | Career aspiration, course interest, prior experience |

All 11 Factor Survey questions are active for all participants to ensure consistent feature collection across the training cohort.

### 5.4.4 Task 4: Prediction Review and Feedback

Following survey completion, participants view their readiness score with contextual interpretation. For the bootstrap cohort (first 10 students), predictions are calculated directly from Target Survey responses using PWRS rather than ML inference, as the model requires this initial data for training.

Participants provide feedback through:
1. 5-star rating of perceived accuracy
2. Optional free-text comments
3. Indication of whether the score aligns with self-assessment

### 5.4.5 Task 5: Qualtrics Feedback Survey

Participants complete a comprehensive feedback survey administered via Qualtrics, encompassing usability assessment and qualitative feedback collection.

## 5.5 Evaluation Instruments

### 5.5.1 System Usability Scale (SUS)

The System Usability Scale [CITATION NEEDED] provides a standardized measure of perceived usability on a 0-100 scale. The instrument comprises 10 items with 5-point Likert response scales:

[TABLE 14: System Usability Scale Items]

| # | Statement | Scale |
|---|-----------|-------|
| 1 | I think that I would like to use this system frequently | Strongly Disagree (1) - Strongly Agree (5) |
| 2 | I found the system unnecessarily complex | Strongly Disagree (1) - Strongly Agree (5) |
| 3 | I thought the system was easy to use | Strongly Disagree (1) - Strongly Agree (5) |
| 4 | I think that I would need the support of a technical person to use this system | Strongly Disagree (1) - Strongly Agree (5) |
| 5 | I found the various functions in this system were well integrated | Strongly Disagree (1) - Strongly Agree (5) |
| 6 | I thought there was too much inconsistency in this system | Strongly Disagree (1) - Strongly Agree (5) |
| 7 | I would imagine that most people would learn to use this system very quickly | Strongly Disagree (1) - Strongly Agree (5) |
| 8 | I found the system very cumbersome to use | Strongly Disagree (1) - Strongly Agree (5) |
| 9 | I felt very confident using the system | Strongly Disagree (1) - Strongly Agree (5) |
| 10 | I needed to learn a lot of things before I could get going with this system | Strongly Disagree (1) - Strongly Agree (5) |

**SUS Scoring**: For odd-numbered items, score = response - 1. For even-numbered items, score = 5 - response. Sum all scores and multiply by 2.5 to obtain a 0-100 scale score.

**Interpretation Benchmarks**:

| Score Range | Grade | Adjective Rating |
|-------------|-------|------------------|
| 90-100 | A+ | Best Imaginable |
| 80-89 | A | Excellent |
| 70-79 | B | Good |
| 60-69 | C | OK |
| 50-59 | D | Poor |
| < 50 | F | Awful |

**Target Threshold**: SUS ≥ 68 (industry average for acceptable usability) [CITATION NEEDED]

### 5.5.2 Technology Acceptance Model (TAM) Constructs

The feedback survey incorporates questions derived from the Technology Acceptance Model [CITATION NEEDED] to assess perceived usefulness and perceived ease of use:

**Perceived Usefulness (6 items)**:

| ID | Statement |
|----|-----------|
| Q1 | Using this AI counseling system in my academic planning enables me to accomplish tasks more quickly than other advising methods. |
| Q2 | Using this AI counseling system improves my academic planning performance. |
| Q3 | Using this AI counseling system in my academic planning increases my productivity. |
| Q4 | Using this AI counseling system enhances my effectiveness in transfer planning. |
| Q5 | Using this AI counseling system makes it easier to plan my academic path. |
| Q6 | I have found this AI counseling system useful for my transfer journey. |

**Perceived Ease of Use (6 items)**:

| ID | Statement |
|----|-----------|
| Q7 | Learning to operate this AI counseling system was easy for me. |
| Q8 | I found it easy to get this AI counseling system to do what I want it to do. |
| Q9 | My interaction with this AI counseling system has been clear and understandable. |
| Q10 | I found this AI counseling system to be flexible to interact with. |
| Q11 | It was easy for me to become skillful at using this AI counseling system. |
| Q12 | I found this AI counseling system easy to use. |

All TAM items use 5-point Likert scales (Strongly Disagree to Strongly Agree).

### 5.5.3 Prediction Quality Assessment

Questions assessing the quality of system predictions and recommendations:

| ID | Question | Scale |
|----|----------|-------|
| Q19 | How accurate did you find the system's assessment of your academic success factors? | 5-point (Not accurate at all - Extremely accurate) |
| Q20 | Did the success probability estimates align with your own assessment of your academic situation? | 5-point (Not at all aligned - Perfectly aligned) |
| Q21 | How relevant were the recommendations provided by the system to your specific situation? | 5-point (Not relevant at all - Extremely relevant) |
| Q22 | How actionable were the recommendations provided? | 5-point (Not actionable at all - Easily actionable) |

### 5.5.4 Behavioral Intention

Questions measuring future use intent and recommendation likelihood:

| ID | Question | Scale |
|----|----------|-------|
| Q25 | How likely are you to continue using this system for academic planning? | 5-point (Extremely unlikely - Extremely likely) |
| Q26 | How likely are you to recommend this system to other transfer students? | 5-point (Extremely unlikely - Extremely likely) |

Q26 enables Net Promoter Score (NPS) calculation using standard methodology.

### 5.5.5 Open-Ended Questions

Qualitative feedback is collected through open-ended questions:

| ID | Question | Purpose |
|----|----------|---------|
| Q16 | What specific elements of the interface were difficult to navigate or understand? | Interface issues identification |
| Q18 | What technical issue you faced while using this system? | Technical problem documentation |
| Q23 | What was the most helpful feature of the system? | Positive attribute identification |
| Q24 | What feature or capability was missing that would have improved your experience? | Feature gap analysis |
| Q29 | Can you specify what accessibility issue was there in the system? | Accessibility assessment |
| Q30 | What additional features would make this system more valuable to transfer students? | Enhancement suggestions |
| Q32 | If you could redesign one aspect of the system, what would it be? | Priority improvement identification |
| Q33 | Please provide any additional feedback or suggestions that could help improve the system for future students. | General feedback |

## 5.6 Data Collection

### 5.6.1 Quantitative Measures

[TABLE 15: Quantitative Data Collection]

| Measure | Source | Collection Point | RQ Addressed |
|---------|--------|-----------------|--------------|
| Task completion rate | System logs | During session | RQ1, RQ2 |
| Task completion time | System logs | During session | RQ1 |
| Survey completion rate | Backend analytics | Post-session | RQ2 |
| Missing data rate | Data quality checks | Post-session | RQ2 |
| SUS score | Qualtrics survey | End of session | RQ1 |
| TAM composite scores | Qualtrics survey | End of session | RQ1 |
| Prediction accuracy rating (1-5) | In-app feedback | Task 4 | RQ3 |
| Consent timestamp | User model | Task 1 | RQ4 |
| Withdrawal rate | User model | Ongoing | RQ4 |

### 5.6.2 Qualitative Measures

| Measure | Source | Collection Point | RQ Addressed |
|---------|--------|-----------------|--------------|
| Open-ended survey responses | Qualtrics | End of session | RQ1, RQ3, RQ5 |
| Facilitator observations | Research team notes | During session | RQ1, RQ4 |
| Technical issue reports | Q17, Q18 | End of session | RQ1 |
| Feature requests | Q24, Q30 | End of session | RQ1, RQ5 |

### 5.6.3 System-Logged Metrics

The backend automatically captures behavioral metrics:

- Page view sequences and navigation patterns
- Time spent on each survey question
- Auto-save trigger frequency
- Error occurrences and recovery actions
- Prediction viewing duration
- Feedback submission timing

## 5.7 Analysis Methodology

### 5.7.1 Quantitative Analysis

**Descriptive Statistics**:
- Mean, median, and standard deviation for all Likert-scale items
- Frequency distributions for categorical responses
- Completion rate percentages with confidence intervals

**Composite Score Construction**:
- Perceived Usefulness Score: Mean of Q1-Q6 (range: 1-5)
- Perceived Ease of Use Score: Mean of Q7-Q12 (range: 1-5)
- Prediction Quality Score: Mean of Q19-Q22 (range: 1-5)
- Net Promoter Score: Derived from Q26 using standard calculation

**Reliability Analysis**:
- Cronbach's alpha for internal consistency of TAM constructs (target: α ≥ 0.70)
- Item-total correlations to identify potentially problematic items

**Statistical Tests** (sample size permitting):
- Mann-Whitney U / Kruskal-Wallis for group comparisons
- Spearman's rho for correlations between constructs
- Wilcoxon signed-rank for any pre/post comparisons

Non-parametric tests are preferred due to the expected small sample size and ordinal nature of Likert data.

### 5.7.2 Qualitative Analysis

**Thematic Analysis Approach** (following Braun & Clarke, 2006 [CITATION NEEDED]):

1. **Familiarization**: Initial read-through of all open-ended responses
2. **Initial Coding**: Line-by-line coding to generate discrete concepts
3. **Theme Search**: Grouping codes into candidate themes
4. **Theme Review**: Checking themes against coded data and entire dataset
5. **Theme Definition**: Refining theme names and definitions
6. **Report Production**: Selecting representative quotes for each theme

**Expected Theme Categories**:
- Interface/Navigation Issues
- Technical Problems
- Positive System Attributes
- Feature Requests
- Personalization Needs
- Accessibility Concerns
- Trust and Prediction Perception

**Coding Reliability**:
- Dual-coder approach for inter-rater reliability
- Cohen's Kappa calculation (target: κ ≥ 0.70)

### 5.7.3 Pain Point Prioritization

Identified issues are categorized using a prioritization matrix:

| Priority | Criteria | Action |
|----------|----------|--------|
| Critical | High frequency + High severity | Address immediately |
| Important | High frequency + Low severity | Plan for next iteration |
| Monitor | Low frequency + High severity | Investigate edge cases |
| Minor | Low frequency + Low severity | Document for future |

## 5.8 Success Criteria

### 5.8.1 Required Criteria (Pass/Fail)

[TABLE 16: Alpha Testing Success Criteria]

| Metric | Target | Rationale |
|--------|--------|-----------|
| Task completion rate | > 90% | Core functionality must be accessible |
| Average completion time | < 45 minutes | Session must fit within reasonable timeframe |
| SUS score | ≥ 68 | Industry-standard usability threshold |
| Critical errors | 0 | No blocking issues |
| Survey completion rate | 100% (both surveys) | Complete data required for model training |
| Missing data rate | < 5% | Data quality threshold |
| Consent completion | 100% | IRB compliance requirement |

### 5.8.2 Stretch Goals

| Metric | Target |
|--------|--------|
| SUS score | ≥ 80 (excellent usability) |
| Average prediction feedback rating | ≥ 3.5/5.0 |
| Follow-up opt-in rate | ≥ 70% |
| Recommendation intent (Q26) | ≥ 4.0/5.0 |

## 5.9 Preliminary Results

> **Note**: This section presents the analysis framework with placeholder values. Results will be populated following data collection completion in Spring 2026.

### 5.9.1 Participant Demographics

[TABLE 17: Participant Demographics (Pending)]

| Characteristic | n | % |
|----------------|---|---|
| **Total Participants** | -- | -- |
| **Gender** | | |
| - Male | -- | -- |
| - Female | -- | -- |
| - Non-binary/Other | -- | -- |
| - Prefer not to say | -- | -- |
| **Age Group** | | |
| - 18-24 | -- | -- |
| - 25-34 | -- | -- |
| - 35+ | -- | -- |
| **First Generation Student** | | |
| - Yes | -- | -- |
| - No | -- | -- |
| **Transfer Institution Type** | | |
| - Community College | -- | -- |
| - 4-Year Institution | -- | -- |
| - Other | -- | -- |

### 5.9.2 Task Completion Metrics

[TABLE 18: Task Completion Results (Pending)]

| Task | Completion Rate | Mean Time | SD |
|------|-----------------|-----------|-----|
| Task 1: Onboarding | --% | -- min | -- |
| Task 2: Target Survey | --% | -- min | -- |
| Task 3: Factor Survey | --% | -- min | -- |
| Task 4: Prediction Review | --% | -- min | -- |
| Task 5: Feedback Survey | --% | -- min | -- |
| **Overall** | --% | -- min | -- |

### 5.9.3 System Usability Scale Results

[TABLE 19: SUS Item Scores (Pending)]

| Item | Mean | SD |
|------|------|-----|
| 1. Would use frequently | -- | -- |
| 2. Unnecessarily complex | -- | -- |
| 3. Easy to use | -- | -- |
| 4. Need technical support | -- | -- |
| 5. Functions well integrated | -- | -- |
| 6. Too much inconsistency | -- | -- |
| 7. Quick to learn | -- | -- |
| 8. Cumbersome to use | -- | -- |
| 9. Felt confident using | -- | -- |
| 10. Needed to learn a lot | -- | -- |
| **Overall SUS Score** | -- | -- |

**Interpretation**: [To be completed based on results]

### 5.9.4 TAM Construct Scores

[TABLE 20: Technology Acceptance Model Results (Pending)]

| Construct | Mean | SD | Cronbach's α |
|-----------|------|-----|--------------|
| Perceived Usefulness (Q1-Q6) | -- | -- | -- |
| Perceived Ease of Use (Q7-Q12) | -- | -- | -- |
| Prediction Quality (Q19-Q22) | -- | -- | -- |
| Behavioral Intention (Q25-Q26) | -- | -- | -- |

### 5.9.5 Prediction Accuracy Perception

[TABLE 21: Prediction Feedback Results (Pending)]

| Metric | Value |
|--------|-------|
| Mean accuracy rating (1-5 stars) | -- |
| % Rating ≥ 4 stars (high confidence) | --% |
| % Rating < 4 stars (requiring correction) | --% |
| Mean alignment with self-assessment (Q20) | -- |

### 5.9.6 Qualitative Themes

[TABLE 22: Preliminary Theme Analysis (Pending)]

| Theme | Frequency | Representative Quote |
|-------|-----------|---------------------|
| [Theme 1] | -- | "..." |
| [Theme 2] | -- | "..." |
| [Theme 3] | -- | "..." |
| [Theme 4] | -- | "..." |

## 5.10 Survey Instrument Validation

### 5.10.1 Target Survey Validation Framework

The Target Survey (readiness assessment) employs the Priority-Weighted Response Scoring (PWRS) formula to calculate success rates. Validation of this instrument involves:

**Internal Consistency**: Cronbach's alpha for each category to assess whether questions within a category measure the same construct.

**Convergent Validity**: Correlation between calculated PWRS scores and direct self-assessment questions (Q23: "success-predict" with priority 10).

**Predictive Validity** (longitudinal): Correlation between initial readiness scores and actual academic outcomes (GPA, retention) at semester end.

[TABLE 23: Target Survey Validation Thresholds]

| Quality Level | Pearson Correlation (r) | Mean Absolute Difference | Action |
|---------------|------------------------|--------------------------|--------|
| Excellent | > 0.85 | < 5 points | Use calculated rates confidently |
| Good | 0.70 - 0.85 | 5-10 points | Use calculated rates, monitor |
| Fair | 0.50 - 0.70 | 10-15 points | Review formula, adjust priorities |
| Poor | < 0.50 | > 15 points | Revise survey, recalibrate |

### 5.10.2 Factor Survey Feature Importance

Following model training, feature importance analysis will assess the predictive contribution of each Factor Survey question:

**For KNN**: Contribution assessed through leave-one-feature-out analysis
**For Neural Network**: SHAP (SHapley Additive exPlanations) values for feature attribution [CITATION NEEDED]

Low-importance features may be candidates for removal in future survey iterations to reduce participant burden.

### 5.10.3 Feedback Loop Effectiveness

The pseudo-labeling feedback loop is evaluated through:

1. **Pseudo-Label Accuracy**: For students who receive predictions and subsequently complete Target Surveys (low-confidence cases), the difference between the prediction and calculated Target Survey score indicates pseudo-label quality.

2. **Model Improvement Trajectory**: MAE (Mean Absolute Error) tracked across model retraining cycles to assess whether feedback-driven data collection improves prediction accuracy.

[TABLE 24: Expected Feedback Loop Progression]

| Phase | Students | Expected MAE | Pseudo-Label Rate | Avg Rating |
|-------|----------|--------------|-------------------|------------|
| Initial | 10-20 | 14 pts | 50% | 3.2/5.0 |
| Growing | 21-50 | 12 pts | 60% | 3.5/5.0 |
| Maturing | 51-99 | 11 pts | 70% | 3.8/5.0 |
| Neural Network | 100+ | 9 pts | 75% | 4.1/5.0 |

## 5.11 Limitations

### 5.11.1 Study Design Limitations

**Sample Size**: The 10-student cohort, while aligned with system requirements, limits statistical power and generalizability. Results should be interpreted as formative evaluation findings rather than definitive conclusions.

**Single Institution**: Recruitment from a single institution (NEIU) limits generalizability to other contexts. Transfer student populations vary significantly across institution types and geographic regions.

**Self-Selection Bias**: Participants who volunteer for the study may be more motivated or technologically comfortable than the general transfer student population.

**No Control Group**: The single-group design precludes comparison with alternative advising approaches or baseline conditions.

### 5.11.2 Measurement Limitations

**Self-Reported Data**: Reliance on self-reported success predictors introduces potential response bias. Students may overestimate or underestimate their readiness based on social desirability or lack of self-awareness.

**Prediction Validation**: During the bootstrap phase, "predictions" are calculated from Target Survey responses rather than ML inference, limiting evaluation of actual model accuracy until subsequent cohorts.

**Short-Term Assessment**: The initial evaluation captures immediate usability and satisfaction but cannot assess long-term prediction accuracy without longitudinal follow-up.

### 5.11.3 Mitigation Strategies

| Limitation | Mitigation |
|------------|------------|
| Small sample size | Qualitative depth to complement quantitative breadth |
| Single institution | Clear documentation of institutional context for future replication |
| Self-selection | Diverse recruitment channels to broaden participant pool |
| Self-reported data | Multiple questions per construct for triangulation |
| Short-term focus | Optional longitudinal follow-up with consenting participants |

## 5.12 Ethical Considerations

### 5.12.1 Risk Minimization

| Risk | Mitigation Strategy |
|------|---------------------|
| Data breach | Password protection, role-based access, encryption at rest and in transit |
| Coercion | Voluntary participation explicitly stated; no penalty for withdrawal |
| Privacy violation | Anonymization for research outputs; consent for all data use |
| Algorithmic bias | Transparent ML methods; feedback loop enables correction |
| Psychological harm | Score interpretation framed constructively; support resources provided |

### 5.12.2 Participant Benefits

| Benefit | Description |
|---------|-------------|
| Self-awareness | Insight into factors affecting academic success |
| Personalized guidance | Tailored score interpretation based on individual profile |
| Early intervention | Identification of potential risk factors before academic difficulties |
| Advisor connection | Facilitated communication with academic advisors |
| Compensation | $10 gift card for participation |

### 5.12.3 Data Governance

All collected data adheres to the following governance principles:

- **Purpose Limitation**: Data used exclusively for research purposes as specified in consent
- **Data Minimization**: Only data necessary for study objectives collected
- **Storage Security**: MongoDB Atlas with AES-256 encryption; access restricted to research team
- **Retention**: Data retained per IRB protocol; participants may request deletion
- **Anonymization**: Published results use anonymized aggregate data only

## 5.13 Timeline and Current Status

[TABLE 25: Evaluation Timeline]

| Phase | Target Date | Status |
|-------|-------------|--------|
| IRB Protocol Approval | January 2023 | Complete |
| Survey Instrument Development | November 2024 | Complete |
| System Implementation | December 2024 | Complete |
| Recruitment Materials Preparation | January 2025 | Complete |
| Pilot Testing | February 2025 | Complete |
| Active Recruitment | Spring 2026 | Planned |
| Data Collection | Spring 2026 | Planned |
| Quantitative Analysis | Following collection | Planned |
| Qualitative Coding | Following collection | Planned |
| Results Synthesis | Following analysis | Planned |

### 5.13.1 Current Data Collection Status

| Milestone | Target | Current | Status |
|-----------|--------|---------|--------|
| Student participants | 10 | 0 | Recruitment pending |
| Advisor participants | 2 | 0 | Recruitment pending |
| Survey completions | 10 | 0 | Awaiting participants |
| Feedback responses | 10 | 0 | Awaiting participants |

## 5.14 Summary

This section presented the comprehensive evaluation framework for ACOSUS, addressing research questions related to usability, survey completion, prediction accuracy, consent understanding, and advisor experience. The mixed-methods approach combines standardized instruments (SUS, TAM) with qualitative feedback collection to provide both benchmarkable metrics and rich contextual insights.

The evaluation design aligns with the system's progressive learning approach, where the initial 10-student cohort simultaneously validates the platform and provides the training data necessary for ML model deployment. Success criteria establish clear thresholds for alpha testing acceptance, with required metrics ensuring core functionality and stretch goals targeting excellent user experience.

Key evaluation contributions include:
- Integration of usability evaluation with ML training data collection
- Validation framework for the Priority-Weighted Response Scoring formula
- Feedback loop effectiveness metrics connecting user ratings to model improvement
- Longitudinal design enabling predictive validity assessment

Results from this evaluation will inform iterative system refinement and provide empirical evidence for the progressive learning approach to transfer student success prediction.

---

## Figures and Tables Summary

| ID | Description | Status |
|----|-------------|--------|
| [TABLE 9] | Research Questions and Evaluation Focus | Complete |
| [TABLE 10] | Study Design Parameters | Complete |
| [TABLE 11] | Participant Task Sequence | Complete |
| [TABLE 12] | Target Survey Categories | Complete |
| [TABLE 13] | Factor Survey Categories | Complete |
| [TABLE 14] | System Usability Scale Items | Complete |
| [TABLE 15] | Quantitative Data Collection | Complete |
| [TABLE 16] | Alpha Testing Success Criteria | Complete |
| [TABLE 17] | Participant Demographics (Pending) | Placeholder |
| [TABLE 18] | Task Completion Results (Pending) | Placeholder |
| [TABLE 19] | SUS Item Scores (Pending) | Placeholder |
| [TABLE 20] | TAM Results (Pending) | Placeholder |
| [TABLE 21] | Prediction Feedback Results (Pending) | Placeholder |
| [TABLE 22] | Preliminary Theme Analysis (Pending) | Placeholder |
| [TABLE 23] | Target Survey Validation Thresholds | Complete |
| [TABLE 24] | Expected Feedback Loop Progression | Complete |
| [TABLE 25] | Evaluation Timeline | Complete |

---

## Citations Needed

- System Usability Scale (Brooke, 1996)
- SUS score interpretation benchmarks (Bangor et al., 2009)
- Technology Acceptance Model (Davis, 1989)
- Thematic analysis methodology (Braun & Clarke, 2006)
- SHAP values for ML interpretability (Lundberg & Lee, 2017)
- Transfer student success research foundations
