# Introduction & Background

## Slide 1: Title Slide (30 seconds)

### Visual Layout
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         ACOSUS                                              │
│         AI-Driven Counseling System for                     │
│         Underrepresented Transfer Students                  │
│                                                             │
│         Progressive Machine Learning for                    │
│         Transfer Student Success Prediction                 │
│         System Design & ML Component                        │
│                                                             │
│         Deep Mandloi                                        │
│         Master's in Computer Science                        │
│         Northeastern Illinois University (NEIU)             │
│         Advisor: Dr. Xiwei Wang (Principal Investigator)    │
│         November 18, 2025                                   │
│                                                             │
│         NSF Grant IIS-2219623 (CISE-MSI)                    │
│         Multi-Institutional Research (5 Universities)       │
│                                                             │
│         🟢 System Status: Live at acosus.neiu.edu           │
│                                                             │
│         [NEIU Logo]                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Speaking Points
- **Opening**: "Good morning/afternoon, committee members. I'm presenting my master's thesis on ACOSUS - an AI-Driven Counseling System for Underrepresented Transfer Students."
- **Context**: "This thesis is part of a larger NSF-funded multi-institutional research project. NEIU's responsibility is the system design and ML prediction component, which is the focus of this defense."
- **Highlight**: "This is not a prototype - the system is deployed live at acosus.neiu.edu and is currently recruiting NEIU transfer students."
- **Hook**: "What makes ACOSUS unique is that it serves as both an advisor tool - centralizing student data for personalized guidance - and as a predictive system that can work with just 10 transfer students and progressively improve as the cohort grows."

---

## Slide 2: The Transfer Student Challenge (2 minutes)

### The Problem: Transfer Students Face Unique Challenges

#### Alarming Transfer Student Statistics
- **10-15%** lower graduation rates than native students (NSCRC, 2022)
- **37%** of transfer students do not return for second year (NSCRC, 2021)
- **Average 13 credits lost** during transfer process (U.S. GAO, 2017)
- **"Transfer shock"**: 0.2-0.5 GPA drop in first semester post-transfer (Townsend & Wilson, 2006)

#### Underrepresentation in Computing
- Only **15%** of computing workers are Black/Hispanic
- Only **25%** of computing workers are female
- **Community college → university pathway** is critical for diversity in STEM
- Transfer students often come from underrepresented backgrounds

#### The Advising Challenge
**Current Pain Points for Advisors**:
- Student data **scattered across multiple systems**:
  - SIS (Student Information System) for GPA and course history
  - Financial aid portal for scholarships and loans
  - LMS (Learning Management System) for engagement metrics
  - Manual notes and email conversations
- **40-60% of advising time** spent gathering information (Wan et al., AMCIS 2023)
- Difficult to **remember details for 100+ advisees**
- Hard to provide **personalized guidance** without complete picture

**Impact on Transfer Students**:
- Generic advising that doesn't account for transfer-specific challenges
- Missed early intervention opportunities
- Lack of proactive support for at-risk students

---

### The ACOSUS Solution: Three Objectives

#### Objective 1: For Advisors - Centralize Student Data
**What Advisors Need**:
- ✅ Single platform with complete student profile
- ✅ Academic, financial, personal circumstances in one view
- ✅ Customizable surveys to gather transfer-specific information
- ✅ Enables personalized advising before meetings

**How ACOSUS Helps**:
```
Before ACOSUS:
  1. Check SIS for GPA → 3 minutes
  2. Check financial aid portal → 2 minutes
  3. Review LMS for engagement → 3 minutes
  4. Search emails for notes → 5 minutes
  5. Prepare for meeting → 10 minutes
  Total prep time: 23 minutes per student

With ACOSUS:
  1. Open ACOSUS dashboard → 1 minute
  2. View complete student profile → 2 minutes
  3. Review ML prediction & similar students → 1 minute
  4. Prepare for meeting → 3 minutes
  Total prep time: 7 minutes per student

Time Saved: 70% reduction
```

---

#### Objective 2: For Predictions - New Transfer Cohort Problem
**The Challenge**: Small transfer cohorts each semester
- Typical NEIU transfer cohort: **10-20 students** per semester in computing
- Need predictions **immediately**, can't wait years to collect data
- Traditional ML systems require 1000+ students

**The Cold Start Question**:
> **"How can we predict underrepresented transfer student success with only 10 students in a new cohort?"**

**Why This Matters**:
```
Scenario: Fall 2025 Transfer Cohort - 10 Students

Traditional ML Approach:
  Fall 2025 (10 students)   → Collect data, no predictions ❌
  Spring 2026 (8 students)  → Collect data, no predictions ❌
  Fall 2026 (12 students)   → Collect data, no predictions ❌
  Spring 2027 (11 students) → Collect data, no predictions ❌
  Fall 2027 (15 students)   → Still not enough data ❌

  Result: First 56 transfer students received NO early support

ACOSUS Approach:
  Week 2 (10 students)   → Train KNN model, start predictions ✅
  Week 6 (10 students)   → Predictions for all students ✅
  Spring 2026 (18 total) → Improved predictions ✅
  Fall 2026 (30 total)   → Better predictions ✅

  Result: ALL transfer students receive personalized support
```

---

#### Objective 3: For Students - Reduce Survey Burden
**The Survey Problem**:
- Comprehensive surveys take **15-20 minutes**
- Students overwhelmed with questionnaires
- **40-60% dropout rate** on lengthy surveys

**ACOSUS Feedback Loop Solution**:
```
Transfer Student #11 enrolls:
  1. Complete factor survey (7 questions, ~4 min) ✅
  2. ACOSUS predicts success rate: 74%
  3. Student rates prediction: "How accurate? (1-5 stars)"

  IF student rates ≥4 stars (accurate):
    → Use prediction as training label (pseudo-label)
    → Skip target survey ✅ (save 12 minutes)
    → Total survey time: 4 minutes

  IF student rates <4 stars (inaccurate):
    → Request target survey for correction
    → Student provides actual success rate
    → Model learns from mistake ✅
    → Total survey time: 16 minutes

Expected: 50-70% of students rate ≥4 stars
Average survey time: 8 minutes (vs 18 minutes traditional)
```

---

### Visual Description
- **Infographic**: Transfer student challenges (GPA drop, credit loss, lower graduation rates)
- **Comparison Chart**: Traditional advising (scattered data) vs ACOSUS (centralized)
- **Timeline**: Late intervention (after failure) vs Early intervention (week 2)

---

## Slide 3: Four Core Challenges ACOSUS Addresses (2 minutes)

### Challenge 1: New Transfer Cohort Problem (The Cold Start)

**The Scenario**:
- Fall 2025: 10 transfer students enroll in CS program at NEIU
- Need to predict their success and provide guidance **immediately**
- No historical transfer student data available

**Why Traditional ML Fails**:
| Approach | Minimum Samples Needed | Works at 10 Students? |
|----------|------------------------|----------------------|
| Deep Neural Networks | 1000-10000 samples | ❌ No |
| Random Forest, SVM | 100-1000 samples | ❌ No |
| Existing Systems (Starfish, Civitas) | 500-10000 samples | ❌ No |
| **ACOSUS (KNN)** | **10 samples** | **✅ Yes** |

**ACOSUS Solution**:
- Use K-Nearest Neighbors (KNN) - designed for small datasets
- Instance-based learning (no parameter fitting required)
- Effective with as few as 10 training samples
- Interpretable: "You're similar to transfer students #3, #7, #12"

**Real-World Impact**:
```
Traditional System:
  Academic advisor meets with 10 transfer students
  No data-driven guidance available
  Generic recommendations based only on GPA

ACOSUS:
  Academic advisor meets with 10 transfer students
  Each has personalized success prediction
  Recommendations based on similar transfer students
  Targeted interventions for at-risk students
```

---

### Challenge 2: Advisor Data Gathering Burden

**Current Advisor Workflow** (Without ACOSUS):
1. **Check SIS** for GPA, courses, enrollment status → 3 min
2. **Check Financial Aid Portal** for scholarships, loans → 2 min
3. **Check LMS** for engagement, assignments → 3 min
4. **Search email** for previous conversations → 5 min
5. **Review manual notes** from last meeting → 3 min
6. **Prepare meeting agenda** → 7 min

**Total**: 23 minutes per student × 100 advisees = **38 hours per week just gathering data**

**ACOSUS Advisor Workflow**:
1. **Open ACOSUS dashboard** → 1 min
2. **View complete student profile**:
   - Academic: GPA, courses, enrollment status
   - Financial: Scholarships, work hours, family support
   - Personal: Commute distance, previous institution, confidence levels
   - ML Prediction: Success rate + similar students
3. **Prepare personalized guidance** → 3 min

**Total**: 4 minutes per student × 100 advisees = **7 hours per week**

**Time Saved**: 31 hours per week (81% reduction)

---

### Challenge 3: Progressive Accuracy Improvement

**The Dilemma**:
- Initial model (10 transfer students): Acceptable but **limited accuracy** (MAE ~14)
- Goal: Automatically improve as transfer cohort grows (20, 50, 100+ students)
- Challenge: How to transition between models without service interruption?

**ACOSUS Solution**: Progressive Model Evolution
```
Phase 1: KNN Bootstrap (10 transfer students)
  - MAE: ~14 points
  - R²: ~0.42
  - Inference: <10ms
  - Use case: Initial cohort predictions

Phase 2: KNN Refinement (11-99 transfer students)
  - MAE: ~12 points (improving)
  - R²: ~0.54 (improving)
  - More transfer students → better neighbor matching

Phase 3: GAN Augmentation (100 transfer students)
  - Generate 400 synthetic transfer student profiles
  - Total training data: 500 samples
  - Enables neural network training

Phase 4: Neural Network (100+ transfer students)
  - MAE: ~9 points (best performance)
  - R²: ~0.71 (best performance)
  - Captures complex transfer-specific patterns
```

**Key Innovation**:
- Automatic model selection based on transfer cohort size
- Seamless transitions (no downtime)
- Each phase maintains or improves accuracy
- **Replaces legacy NLP + recommender system approach**

---

### Challenge 4: Survey Burden vs. Data Quality

**The Trade-off**:
```
More Questions = Better Predictions BUT Higher Dropout

Survey Length vs Completion Rate:
  5 questions  (3 min)  → 95% completion ✅
  10 questions (7 min)  → 85% completion ✅
  20 questions (15 min) → 60% completion ⚠️
  40 questions (30 min) → 30% completion ❌
```

**Traditional Approach**:
- Every transfer student completes full survey (20-40 questions)
- Result: High dropout, missing data, lower model quality

**ACOSUS Feedback Loop** (Pseudo-Labeling + Active Learning):
```
Transfer Student #11 enrolls:
  1. Complete factor survey (questions about background)
  2. ACOSUS predicts: "Your success rate: 74%"
  3. Student rates: "How accurate is this? (1-5 stars)"

  IF rating ≥4 stars:
    → Prediction is accurate enough
    → Use 74% as training label (pseudo-label)
    → Skip detailed target survey ✅
    → Survey time: 4 minutes

  IF rating <4 stars:
    → Prediction needs correction
    → Request detailed target survey
    → Model learns from mistake ✅
    → Survey time: 16 minutes
```

**Expected Impact**:
- 50-70% of transfer students rate predictions ≥4 stars
- Average survey time: 8 minutes (vs 18 minutes)
- **Advisor benefit**: Maintains high-quality data for personalized advising
- Higher completion rates (92% vs 60%)

---

### Visual Description

**Four Quadrants Graphic**:
```
┌──────────────────────┬──────────────────────┐
│  Challenge 1:        │  Challenge 2:        │
│  New Transfer Cohort │  Advisor Burden      │
│                      │                      │
│  [Icon: 10 Students] │  [Icon: Scattered    │
│  Need: Predict with  │        Data]         │
│        only 10       │  Solution: Centralize│
│  Solution: KNN       │            Platform  │
├──────────────────────┼──────────────────────┤
│  Challenge 3:        │  Challenge 4:        │
│  Progressive         │  Survey Fatigue      │
│  Improvement         │                      │
│  [Icon: Upward       │  [Icon: Frustrated   │
│   Arrow Chart]       │   Student]           │
│  Solution: KNN→GAN→NN│  Solution: Pseudo-   │
│  (10→100→1000+)      │  labeling Feedback   │
└──────────────────────┴──────────────────────┘
```

---

## Slide 4: ACOSUS Project Context (1.5 minutes)

### Multi-Institutional NSF-Funded Research

#### Project Overview
- **Full Name**: AI-Driven Counseling System for Underrepresented Transfer Students
- **NSF Grant**: IIS-2219623 (CISE-MSI)
- **Duration**: 2022-2025
- **Total Funding**: [Amount from NSF records]
- **Lead Institution**: Northeastern Illinois University (NEIU)

#### Five Partner Institutions
1. **Northeastern Illinois University (NEIU)** - Lead
   - **Responsibility**: System design + ML prediction component
   - **PI**: Dr. Xiwei Wang
   - **This Thesis**: Complete system architecture + Progressive ML framework

2. **SUNY College at Old Westbury**
   - **Responsibility**: NLP analysis of transfer decision factors
   - **Focus**: Reddit topic modeling, social media influence

3. **Cal Poly Humboldt**
   - **Responsibility**: Personality traits & student success correlation
   - **Focus**: Psychometric assessments

4. **University of Houston-Victoria**
   - **Responsibility**: Student counseling systems survey
   - **Focus**: Existing system analysis, advisor workflows

5. **University of Texas at El Paso (UTEP)**
   - **Responsibility**: Factor analysis on transfer student success
   - **Focus**: Predictive factors identification

---

### NEIU's Role: System Design + ML Component (This Thesis)

**Thesis Scope**:
- ✅ **Full-stack system architecture** (Frontend + Backend + Model Server)
- ✅ **Progressive ML framework** (KNN → GAN → Neural Network)
- ✅ **Advisor-centric platform** (centralized data, customizable surveys)
- ✅ **Feedback loop implementation** (pseudo-labeling + active learning)
- ✅ **Production deployment** at acosus.neiu.edu
- ✅ **NEIU transfer student pilot** (currently recruiting 10 students)

**What This Thesis DOES Include**:
- Complete system implementation
- ML model design and validation strategy
- Advisor workflow design
- Survey methodology (dual-survey system)

**What This Thesis DOES NOT Include**:
- Multi-institutional deployment (NEIU only)
- NLP topic modeling (handled by SUNY)
- Personality trait analysis (handled by Cal Poly Humboldt)
- Large-scale factor analysis (handled by UTEP)

---

### ACOSUS Publications (Building on Prior Work)

This thesis builds on findings from four ACOSUS publications:

1. **"A Survey of Student Counseling Systems"** (AMCIS 2023)
   - Identifies gaps: scattered data, manual processes, lack of ML
   - **Informs**: Advisor-centric system design in ACOSUS

2. **"A Preliminary Factor Analysis on Computing Transfer Students"** (ASEE 2023)
   - Key predictors: financial support, GPA, institutional fit
   - **Informs**: Factor survey design and priority scores

3. **"Personality Traits and Transfer Student Success"** (NCCiT 2023)
   - Personality factors: adaptability, stress management, self-discipline
   - **Informs**: Target survey questions (Personal Attributes category)

4. **"Reddit Topic Modeling for Transfer Decisions"** (DSI 2024)
   - NLP analysis of transfer student concerns
   - **Complements**: This thesis's ML prediction approach

**See [09-RelatedWork.md](./09-RelatedWork.md) for complete literature review**

---

### Visual Description

**Multi-Institutional Collaboration Diagram**:
```
┌─────────────────────────────────────────────────────┐
│         NSF Grant IIS-2219623 (CISE-MSI)            │
│              ACOSUS Project                         │
└──────────────────────┬──────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   ┌────▼────┐    ┌───▼────┐    ┌───▼────┐
   │  NEIU   │    │  SUNY  │    │ Cal Poly│
   │ System  │    │  NLP   │    │Personality│
   │   +ML   │    │Analysis│    │  Traits │
   └─────────┘    └────────┘    └─────────┘
        │              │              │
   ┌────▼────┐    ┌───▼────┐
   │   UHV   │    │  UTEP  │
   │Counseling│    │ Factor │
   │ Systems  │    │Analysis│
   └──────────┘    └────────┘
```

---

## Slide 5: The Research Problem (1 minute)

### Primary Research Question

> **"How can we predict underrepresented transfer student success with only 10 students in a new cohort, and serve advisors with a centralized platform for personalized guidance?"**

### Problem Decomposition

#### Sub-Problem 1: New Transfer Cohort Prediction
**Challenge**: Train a reliable model with only 10 transfer student records

**Constraints**:
- No pre-training data (NEIU-specific cohort)
- No transfer learning (domain-specific to transfer students)
- No seed/synthetic data initially

**Success Criteria**:
- MAE (Mean Absolute Error) < 15 points
- R² (Coefficient of Determination) > 0.4
- Cross-validation stability (std < 5)

---

#### Sub-Problem 2: Advisor Tool Design
**Challenge**: Centralize scattered student data for advisors

**Requirements**:
- Integrate academic, financial, and personal data
- Customizable surveys for transfer-specific factors
- Intuitive dashboard for 100+ advisees

**Success Criteria**:
- Reduce data gathering time by >70%
- Advisor satisfaction rating >4.0/5.0
- Survey completion rate >85%

---

#### Sub-Problem 3: Progressive Scaling
**Challenge**: Seamlessly transition from KNN (10 students) → Neural Network (100+ students)

**Requirements**:
- Maintain or improve accuracy during transitions
- No service interruption
- Automatic model selection

**Success Criteria**:
- KNN → NN transition improves MAE by ≥15%
- Zero downtime during model upgrades
- Student-facing API remains unchanged

---

#### Sub-Problem 4: Intelligent Data Collection
**Challenge**: Reduce redundant surveys through feedback loops

**Approach**:
- Use pseudo-labeling when model confidence is high (rating ≥4/5)
- Request correction only when uncertain (rating <4/5)
- Continuous learning from feedback

**Success Criteria**:
- 50-70% pseudo-label rate
- Survey completion rate >90%
- Average time per student <8 minutes

---

### Visual Description

**Side-by-Side Comparison Flowchart**:

```
Traditional Approach              ACOSUS Approach
──────────────────               ───────────────

New Transfer Cohort Arrives      New Transfer Cohort Arrives
         ↓                                ↓
   Need 1000 students              10 transfer students enroll
         ↓                                ↓
    Wait 4-5 years                 Advisors create surveys
         ↓                                ↓
    Train ML model                 Students complete surveys
         ↓                                ↓
  Deploy predictions               Train KNN model (Week 2)
         ↓                                ↓
  Early cohorts missed ❌          Make predictions (Week 3)
                                          ↓
                                   Personalized advising ✅

Timeline: 5 YEARS                Timeline: 3 WEEKS
First 1000 students: No support  ALL students: Full support
```

---

## Slide 6: Research Objectives & Success Criteria (1.5 minutes)

### Primary Objectives

#### Objective 1: Build Advisor-Centric Data Platform
**Goal**: Centralize student data for personalized transfer student advising

**Deliverables**:
- ✅ Admin portal for advisors to create customizable surveys
- ✅ Student portal for survey completion
- ✅ Complete student profile dashboard (academic, financial, personal)
- ✅ Reduce advisor data gathering time by >70%

**Validation**:
- Advisor feedback surveys (target: >4.0/5.0 satisfaction)
- Time tracking study (before/after ACOSUS adoption)

---

#### Objective 2: Build Minimal-Data Prediction System
**Goal**: Train initial model with only 10 transfer student records

**Deliverables**:
- ✅ KNN model trained on 10 samples
- ✅ Achieve MAE <15 points, R² >0.4
- ✅ Provide actionable predictions for students 11+
- ✅ Explainable predictions (similar transfer students)

**Validation**:
- 5-fold cross-validation on 10 transfer students
- Compare against baseline (random prediction: MAE ~25)

---

#### Objective 3: Implement Progressive Learning Architecture
**Goal**: Automatic model evolution as transfer cohort grows

**Stages**:
- **Stage 1** (10-99 transfer students): K-Nearest Neighbors
- **Stage 2** (100+ transfer students): GAN-augmented Neural Network
- **Automatic trigger**: Model selection based on enrollment count

**Deliverables**:
- ✅ Seamless transitions without service interruption
- ✅ Performance improvement at each stage
- ✅ Model versioning and rollback capability

**Validation**:
- Longitudinal tracking of MAE/R² as cohort grows
- A/B testing during model transitions

---

#### Objective 4: Intelligent Feedback Loop System
**Goal**: Reduce survey burden by 50-70%

**Mechanism**:
- **Pseudo-labeling**: Use high-confidence predictions as training labels
- **Feedback collection**: 1-5 star rating system
- **Conditional survey**: Only request detailed surveys if rating <4

**Deliverables**:
- ✅ Feedback loop UI (student rates predictions)
- ✅ Pseudo-label integration into training pipeline
- ✅ Target 50-70% reduction in survey time
- ✅ Advisor benefit: Maintains data quality for guidance

**Validation**:
- Measure pseudo-label rate vs target (50-70%)
- Survey completion rate before/after feedback loop
- Average survey time tracking

---

#### Objective 5: Production Deployment & NEIU Pilot
**Goal**: Deploy full-stack system and recruit NEIU transfer students

**Components**:
- ✅ Frontend: React + TypeScript (Admin + Student portals)
- ✅ Backend: Node.js + Express + MongoDB
- ✅ Model Server: Python Flask (KNN, GAN, NN)
- ✅ Infrastructure: Docker + Nginx

**Deliverables**:
- ✅ Public access via acosus.neiu.edu
- ✅ Recruit 10 NEIU transfer students (0/10 currently)
- ✅ Validation against actual outcomes (longitudinal study planned)
- ✅ FERPA compliance and IRB approval

---

### Success Metrics by Phase

| Phase | Transfer Students | Model | MAE Target | R² Target | Avg Feedback |
|-------|------------------|-------|------------|-----------|--------------|
| **Bootstrap** | 10 | KNN | <15 | >0.4 | >3.0/5.0 |
| **Growth** | 20-99 | KNN | <12 | >0.5 | >3.5/5.0 |
| **Mature** | 100+ | Neural Net | <10 | >0.6 | >4.0/5.0 |

**Current Status** (as of Nov 18, 2025):
- Phase: Bootstrap (0/10 NEIU transfer students)
- Recruitment: Active (targeting Spring 2026 enrollment)
- Model: Pending data collection
- Validation: Planned for Spring-Fall 2026

---

### Current System Status

**What's Deployed**:
- ✅ Full system architecture (Frontend + Backend + Model Server)
- ✅ Dual-survey system (Target + Factor surveys)
- ✅ Admin portal for advisors
- ✅ Student portal with feedback loop UI
- ✅ Survey questions based on ASEE 2023 factor analysis
- ✅ PWRS formula implementation

**Current Surveys** (see `backend/src/init/data/quiz.json`):
- Target survey: 5 categories (Academic Confidence, Motivation, Personal Attributes, Resources, Self-Assessment)
- Factor survey: 5 categories (Academic Background, Program Timeline, Financial Support, Logistics, Interest)
- **Note**: Current surveys use generic readiness assessments; system supports dynamic addition of transfer-specific factors

**What's Pending**:
- ⏳ 10 NEIU transfer student enrollments
- ⏳ KNN model training (after 10 students)
- ⏳ Validation results (Spring-Fall 2026)
- ⏳ Success rate definition refinement (may include GPA maintenance, on-time graduation, career readiness, or composite metric)

---

### Speaking Points Summary

**Key Messages to Emphasize**:

1. **NSF Project Context**: "This thesis is part of a larger multi-institutional NSF project. NEIU's responsibility is the system design and ML component."

2. **Dual Purpose**: "ACOSUS serves two objectives: a centralized platform for advisors AND a predictive system for transfer students."

3. **Transfer Student Focus**: "We specifically target underrepresented transfer students in computing - a population with 10-15% lower graduation rates and unique challenges."

4. **Cold Start Innovation**: "We can start predicting with just 10 transfer students - something existing systems like Starfish and Civitas cannot do."

5. **Progressive Evolution**: "The system automatically evolves from KNN to Neural Networks as the transfer cohort grows, replacing the legacy NLP + recommender approach."

6. **Advisor Tool First**: "In the short-term, this is an advisor tool for centralizing data. Mid-term: ML predictions inform advising. Long-term: Automated student recommendations."

7. **Production Ready**: "This is deployed and running live at acosus.neiu.edu - not a research prototype."

8. **Validation Plan**: "We're currently recruiting 10 NEIU transfer students. Validation is planned for Spring-Fall 2026 with longitudinal tracking."

9. **Transparency**: "The ML models are not yet trained - we have 0/10 students enrolled. The system is ready, and we're actively recruiting."

10. **System Flexibility**: "While designed for transfer students, the system architecture supports any student population."
