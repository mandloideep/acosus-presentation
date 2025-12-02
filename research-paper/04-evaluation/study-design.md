# User Study Design: Alpha Testing Phase

## Document Purpose
This document details the user study design for ACOSUS alpha testing, including research questions, participant recruitment, consent procedures, and evaluation methodology for the initial 10-student cohort.

---

## 1. Research Questions

### Primary Research Questions

| ID | Research Question | Focus Area |
|----|-------------------|------------|
| **RQ1** | How do transfer students perceive the usability and user experience of the ACOSUS system? | User Experience & Usability |
| **RQ2** | What is the completion rate and data quality of the dual-survey system (Target + Factor surveys)? | Survey Completion & Data Quality |
| **RQ3** | How do students perceive the accuracy and helpfulness of ML-generated success predictions? | Prediction Accuracy Perception |
| **RQ4** | Does the informed consent and onboarding process effectively communicate study objectives and data usage? | Consent & Privacy Understanding |
| **RQ5** | What is the advisor experience with the centralized student data platform? | Advisor Usability |

### Research Question Mapping to Metrics

| RQ | Primary Metrics | Data Collection Method |
|----|-----------------|----------------------|
| RQ1 | SUS score, task completion rate, completion time | SUS survey, system logs, observation |
| RQ2 | Survey completion rate, missing data rate, response patterns | Backend analytics, data quality checks |
| RQ3 | Feedback rating (1-5 stars), qualitative feedback | In-app rating, exit interview |
| RQ4 | Consent comprehension, withdrawal rate | Post-consent quiz (optional), tracking |
| RQ5 | Advisor SUS score, data access time reduction | SUS survey, time-on-task |

---

## 2. Study Design

### 2.1 Study Overview

| Attribute | Value |
|-----------|-------|
| **Study Type** | Alpha Testing / Usability Study |
| **Design** | Single-group, within-subjects |
| **Sample Size** | 10 transfer students + 2 advisors |
| **Study Phase** | Prototype Testing (Bootstrap Phase) |
| **Timeline** | Spring 2026 |
| **Duration per Participant** | ~30-45 minutes (single session) |
| **Follow-up** | Optional longitudinal tracking (6-12 months) |

### 2.2 Recruitment Timeline

| Phase | Timeline | Activities |
|-------|----------|------------|
| **Initial Outreach** | November 2025 | First recruitment emails sent |
| **Active Recruitment** | Spring 2026 | Continued outreach, advisor referrals, classroom announcements |
| **Study Sessions** | Spring 2026 | Self-paced survey completion with facilitator support |
| **Data Analysis** | Ongoing | Quantitative analysis as data is collected |
| **Follow-up** | As agreed | Contact students who opt-in for longitudinal tracking |

### 2.3 Study Context

| Context | Description |
|---------|-------------|
| **Setting** | Remote or in-person at NEIU campus |
| **Platform** | ACOSUS web application (acosus.neiu.edu) |
| **Facilitator Support** | Research team member available for questions during survey completion |
| **Session Type** | Self-paced (no think-aloud protocol; facilitator assists only when needed) |

---

## 3. Recruitment

### 3.1 Target Population

**Primary Population**: Underrepresented transfer students in computing programs at Northeastern Illinois University (NEIU).

### 3.2 Inclusion Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Transfer Status** | Currently enrolled as a transfer student OR transferred within past 2 years |
| **Major** | Computer Science, Information Technology, or related computing field |
| **Institution** | Currently enrolled at NEIU |
| **Age** | 18 years or older |
| **Language** | English proficiency sufficient to complete surveys |
| **Technology Access** | Access to computer/device with internet connection |

**Note**: No additional recruitment criteria beyond the above. **[CHECK WITH PROFESSOR]** - Confirm if any additional criteria should be added.

### 3.3 Exclusion Criteria

| Criterion | Rationale |
|-----------|-----------|
| Students who are not transfer students | Study specifically targets transfer population |
| Non-computing majors | System designed for computing program predictions |
| Students under 18 | IRB protocol requires adult participants |
| Students who have participated in prior ACOSUS studies | Avoid learning effects |

### 3.4 Recruitment Channels

| Channel | Method | Responsible Party |
|---------|--------|------------------|
| **Email Outreach** | Direct email to eligible transfer students via registrar list | Research team |
| **Advisor Referrals** | Academic advisors identify and recommend eligible students | NEIU CS advisors |
| **Classroom Announcements** | Brief announcements in CS courses (with instructor permission) | Research team |
| **Flyers/Posters** | Physical postings in CS department and student center | Research team |
| **Student Organizations** | Outreach through CS clubs and transfer student groups | Research team |

### 3.5 Recruitment Materials

Recruitment communications will include:
- Study title and brief description
- Time commitment (~30-45 minutes)
- Eligibility criteria summary
- Compensation details (if applicable)
- Contact information for questions
- IRB approval statement

### 3.6 Incentives

| Incentive Type | Amount | Distribution |
|----------------|--------|--------------|
| **Compensation** | $10 Amazon gift card | Per data update/session |
| **Additional** | Opportunity for future compensation with periodic updates | Per consent form |

**Note**: Compensation details per IRB-approved consent form.

---

## 4. Consent Process

### 4.1 IRB Approval Status

| Attribute | Details |
|-----------|---------|
| **Protocol Number** | NEIU Protocol #202 |
| **Approval Date** | January 25, 2023 |
| **Review Type** | Expedited (45 CFR 46.110) |
| **Institution** | Northeastern Illinois University |
| **IRB Contact** | IRB@neiu.edu, (773) 442-4674 |
| **Principal Investigator** | Dr. Xiwei Wang |

**Note**: **[CHECK WITH PROFESSOR]** - Confirm IRB renewal status for Spring 2026 (original approval was January 2023).

### 4.2 Informed Consent Form

The IRB-approved consent form includes:

**Study Information**:
- Title: "AN AI-DRIVEN COUNSELING SYSTEM FOR UNDERREPRESENTED TRANSFER STUDENTS"
- Purpose: Develop and validate an AI-driven counseling system
- Procedures: Complete surveys, receive predictions, provide feedback

**Key Disclosures**:
| Disclosure | Description |
|------------|-------------|
| **Data Types** | Demographic, academic, social/behavioral, career goals |
| **Data Use** | Research purposes only, not shared beyond study team |
| **Periodic Updates** | Participants may be asked to update data periodically |
| **Compensation** | $10 Amazon gift card per data update |
| **Duration** | Ongoing participation optional |

**Confidentiality Statement**:
> "The data will only be used for research purposes and will not be shared with anyone beyond the study team. The computers that host these data will be password protected and the login credentials will not be shared with anyone other than the investigator him/herself. All personal identifiers will be stored in a separate file."

### 4.3 Consent Flow (In-System)

```
┌─────────────────────────────────────────────────────────────────┐
│                     Consent Process Flow                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Step 1: Pre-Registration                                        │
│    └── Student navigates to registration page                   │
│                                                                   │
│  Step 2: Consent Display                                         │
│    └── Full informed consent form displayed                      │
│    └── Student must scroll to bottom (enforced)                  │
│                                                                   │
│  Step 3: Explicit Agreement                                      │
│    └── Student clicks "I Consent" button                         │
│    └── Checkbox confirmation of understanding                    │
│                                                                   │
│  Step 4: Consent Recording                                       │
│    └── Timestamp recorded (agreedAt)                             │
│    └── Consent version stored (title, content)                   │
│    └── isAgreed flag set to true                                 │
│                                                                   │
│  Step 5: Account Creation                                        │
│    └── Proceed only after consent                                │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 4.4 Data Usage Explanation

Participants are informed that their data will be used for:

| Usage | Description |
|-------|-------------|
| **ML Model Training** | Features used to train success prediction models |
| **Research Analysis** | Anonymized data for academic publications |
| **System Improvement** | Feedback used to improve system usability |
| **Advisor Support** | Data available to assigned academic advisors |

### 4.5 Withdrawal Rights

| Right | Implementation |
|-------|----------------|
| **Voluntary Participation** | Explicitly stated; no penalty for non-participation |
| **Withdrawal at Any Time** | Students can request account deactivation |
| **Data Removal** | Soft delete implemented; hard deletion available upon request |
| **Contact for Questions** | PI contact and IRB contact provided |

### 4.6 Consent Tracking (Technical)

```typescript
// User model consent schema
consent: {
  title: string,           // Consent version identifier
  content: {
    html: string,          // Rendered consent form
    json: object,          // Structured content
    text: string           // Plain text version
  },
  isAgreed: boolean,       // Explicit consent flag
  agreedAt: Date           // Timestamp of agreement
}
```

---

## 5. Participant Tasks

### 5.1 Task Overview

| Task | Description | Expected Time | Success Criterion |
|------|-------------|---------------|-------------------|
| **Task 1** | System onboarding and account creation | 5-7 minutes | Account created, consent recorded |
| **Task 2** | Complete Target Survey | 3-10 minutes | Success rate recorded |
| **Task 3** | Complete Factor Survey | 5-7 minutes | All questions answered |
| **Task 4** | Review prediction/readiness score | 3-5 minutes | Prediction viewed, understood |
| **Task 5** | Provide system feedback (Qualtrics) | 5-10 minutes | SUS + qualitative feedback |
| **Task 6** | Optional follow-up | Variable | Longitudinal data collected |

**Total Session Time**: ~30-45 minutes

### 5.2 Task 1: System Onboarding and Account Creation

**Objective**: Register for ACOSUS and complete informed consent

**Steps**:
1. Navigate to acosus.neiu.edu/register
2. Read informed consent form (scroll to bottom required)
3. Click "I Consent" to agree
4. Enter account details (email, password)
5. Verify email address
6. Complete initial demographic profile

**Success Criteria**:
- [ ] Consent recorded with timestamp
- [ ] Account created successfully
- [ ] Demographic profile 100% complete (required fields)

**Data Collected**:
- Consent agreement (timestamp, version)
- Account creation timestamp
- Demographic data (gender, age group, ethnicity, first-gen status - optional)

### 5.3 Task 2: Complete Target Survey

**Objective**: Provide ground truth success rate for model training

**Survey Type**: Multi-question Target Survey (27 questions, 22 active)

**Categories**:
| Category | Questions | Focus |
|----------|-----------|-------|
| Academic Confidence & Preparation | 6 | Academic readiness |
| Motivation & Career Goals | 5 | Career orientation |
| Personal Attributes & Skills | 7 | Soft skills |
| Resources & Support | 4 | Support systems |
| Self-Assessment & Expectations | 8 | Self-evaluation |

**Output**: Priority-Weighted Response Score (PWRS) → Success Rate (0-100%)

**Success Criteria**:
- [ ] All required questions answered
- [ ] Success rate calculated and stored
- [ ] Completion time recorded

**Note**: Target survey is REQUIRED for first 10 students (bootstrap phase). For students 11+, it is conditional based on prediction feedback rating.

### 5.4 Task 3: Complete Factor Survey

**Objective**: Provide predictive features for ML model input

**Survey Type**: Factor Survey (13 questions)

**Categories**:
| Category | Questions | Purpose |
|----------|-----------|---------|
| Academic Background | 4 | GPA, prior courses, SAT/ACT |
| Financial Support | 2 | Financial stability indicators |
| Logistics & Commitment | 2 | Time availability, commute |
| Interest & Experience | 3 | Motivation, prior experience |

**Success Criteria**:
- [ ] All 13 questions answered
- [ ] Feature vector generated for ML model
- [ ] Data quality validation passed

### 5.5 Task 4: Review Prediction/Readiness Score

**Objective**: View and evaluate ML prediction (if available)

**Process**:
1. Navigate to dashboard after survey completion
2. View predicted success rate (0-100%)
3. View explanation: "Similar students like you..."
4. Rate prediction accuracy (1-5 stars)
5. Optional: View detailed breakdown

**Note for Bootstrap Phase**: Students 1-10 may not receive ML predictions until model is trained. Task may show calculated success rate from Target Survey instead.

**Success Criteria**:
- [ ] Prediction/score displayed correctly
- [ ] Student provides feedback rating
- [ ] Interaction logged

**Data Collected**:
- Prediction displayed (value, timestamp)
- Feedback rating (1-5 stars)
- Time spent on prediction screen

### 5.6 Task 5: Provide System Feedback (Qualtrics Survey)

**Objective**: Collect usability and experience feedback

**Components**:

#### A. System Usability Scale (SUS) - 10 Questions

| # | Statement | Scale |
|---|-----------|-------|
| 1 | I think I would like to use this system frequently | 1-5 |
| 2 | I found the system unnecessarily complex | 1-5 |
| 3 | I thought the system was easy to use | 1-5 |
| 4 | I think I would need support to use this system | 1-5 |
| 5 | I found the various functions well integrated | 1-5 |
| 6 | There was too much inconsistency in this system | 1-5 |
| 7 | I would imagine most people would learn this system quickly | 1-5 |
| 8 | I found the system very cumbersome to use | 1-5 |
| 9 | I felt very confident using the system | 1-5 |
| 10 | I needed to learn a lot before I could get going | 1-5 |

**Target Score**: >70 (acceptable usability)

#### B. Qualitative Feedback Questions

| Question | Type |
|----------|------|
| What did you like most about the system? | Open-ended |
| What was confusing or difficult? | Open-ended |
| How accurate did the prediction feel? | Likert + comment |
| Would you recommend this to other transfer students? | Yes/No + why |
| Any suggestions for improvement? | Open-ended |

**Success Criteria**:
- [ ] SUS completed (10 questions)
- [ ] At least 2 qualitative responses provided

### 5.7 Task 6: Optional Follow-up

**Objective**: Collect longitudinal data for validation

**Follow-up Approach**:
- No structured follow-up sessions are pre-planned
- Students who agree to follow-up during initial session will be contacted
- Follow-up timing and format determined based on participant availability and consent

**Types of Follow-up** (if participant agrees):
| Follow-up | Timeline | Purpose |
|-----------|----------|---------|
| **Data Update Request** | TBD | Update academic progress |
| **Outcome Collection** | End of semester | Collect actual GPA, retention |

**Compensation**: $10 Amazon gift card per data update (per consent form)

**Success Criteria**:
- [ ] Participant agrees to follow-up during initial session
- [ ] Contact information verified
- [ ] Follow-up initiated based on participant agreement

---

## 6. Data Collection Summary

### 6.1 Quantitative Measures

| Measure | Source | Collection Point |
|---------|--------|-----------------|
| Task completion rate | System logs | During session |
| Task completion time | System logs | During session |
| Survey completion rate | Backend analytics | Post-session |
| Missing data rate | Data quality checks | Post-session |
| SUS score | Qualtrics survey | End of session |
| Feedback rating (1-5) | In-app | Task 4 |
| Consent timestamp | User model | Task 1 |

### 6.2 Qualitative Measures

| Measure | Source | Collection Point |
|---------|--------|-----------------|
| Open-ended survey responses | Qualtrics | End of session |
| Facilitator notes | Research team | During session (questions asked) |
| Follow-up responses | Email/survey | If participant agrees |

---

## 7. Success Criteria (Alpha Testing)

### 7.1 Pass Criteria

| Metric | Target | Pass/Fail |
|--------|--------|-----------|
| Task completion rate | >90% | Required |
| Average completion time | <45 minutes | Required |
| SUS score | >70 | Required |
| Critical errors | 0 | Required |
| Survey completion rate | 100% (Target + Factor) | Required |
| Missing data rate | <5% | Required |
| Consent completion | 100% | Required |

### 7.2 Stretch Goals

| Metric | Stretch Target |
|--------|----------------|
| SUS score | >80 (good usability) |
| Avg feedback rating | >3.5/5.0 |
| Follow-up opt-in rate | >70% |

---

## 8. Ethical Considerations

### 8.1 Minimizing Risk

| Risk | Mitigation |
|------|------------|
| **Data breach** | Password protection, role-based access, encryption |
| **Coercion** | Voluntary participation, no penalty for withdrawal |
| **Privacy** | Anonymization for research, consent for data use |
| **Bias** | Transparent ML methods, feedback loop for corrections |

### 8.2 Benefits to Participants

| Benefit | Description |
|---------|-------------|
| **Self-awareness** | Insight into factors affecting academic success |
| **Personalized guidance** | Tailored recommendations based on profile |
| **Early intervention** | Identification of at-risk factors |
| **Compensation** | Gift card for participation |

---

## 9. Items Requiring Professor Confirmation

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Recruitment criteria | **[CHECK WITH PROFESSOR]** | No additional criteria beyond computing transfer students |
| 2 | IRB renewal status | **[CHECK WITH PROFESSOR]** | Original approval 01/25/2023; confirm validity for Spring 2026 |
| 3 | Screen recording consent | **[CHECK WITH PROFESSOR]** | Believed to be covered by main consent form; needs confirmation |

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document Version** | 1.1 |
| **Last Updated** | December 2024 |
| **Author** | Research Team |
| **Status** | Draft - Pending professor confirmation on 3 items |
| **Related Documents** | [data-privacy.md](../03-implementation/data-privacy.md), [06-ValidationPlan.md](../../06-ValidationPlan.md) |
