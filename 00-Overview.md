# ACOSUS Master's Thesis Presentation - Overview

## Presentation Metadata

- **Title**: ACOSUS: AI-Driven Counseling System for Underrepresented Transfer Students
- **Subtitle**: Progressive Machine Learning for Transfer Student Success Prediction - System Design & ML Component
- **Presenter**: Deep Mandloi
- **Advisor**: Dr. Xiwei Wang (Principal Investigator, NEIU)
- **Program**: Master's in Computer Science
- **Institution**: Northeastern Illinois University (NEIU)
- **Date**: November 18, 2025
- **Duration**: 30 minutes (20 min presentation + 10 min live demo)
- **Audience**: Faculty thesis committee

## Project Context

- **NSF Grant**: IIS-2219623 (CISE-MSI)
- **Project Type**: Multi-institutional research collaboration (5 universities)
- **NEIU Responsibility**: System design + ML prediction component
- **Thesis Scope**: Complete system architecture + Progressive ML framework
- **Target Population**: Underrepresented transfer students in computing majors

## System Status
- **Deployment**: 🟢 Live at [acosus.neiu.edu](https://acosus.neiu.edu)
- **Target Users**: NEIU transfer students (system designed for broader use)
- **Current Phase**: Bootstrap - Recruiting first 10 transfer students
- **Enrollment**: 0/10 students (actively recruiting)
- **Model Status**: 🟡 Legacy implementation active, Progressive ML (KNN→GAN→NN) pending data collection

---

## Presentation Structure (30 Minutes Total)

### Part 1: Presentation (20 minutes)

| Section | Duration | File Reference |
|---------|----------|----------------|
| **1. Title & Introduction** | 2 min | [01-Introduction.md](./01-Introduction.md) |
| - Problem statement | | |
| - Research objectives | | |
| **2. Background & Motivation** | 3 min | [01-Introduction.md](./01-Introduction.md) |
| - Student retention challenges | | |
| - Current system limitations | | |
| - ACOSUS opportunity | | |
| **3. System Architecture** | 3 min | [02-SystemArchitecture.md](./02-SystemArchitecture.md) |
| - Three-component design | | |
| - Technology stack | | |
| - Data flow | | |
| **4. Survey Methodology** | 3 min | [03-SurveyMethodology.md](./03-SurveyMethodology.md) |
| - Target vs Factor surveys | | |
| - PWRS formula explanation | | |
| - Question types & weightages | | |
| **5. Progressive Learning Strategy** | 4 min | [04-ProgressiveLearning.md](./04-ProgressiveLearning.md) |
| - KNN bootstrap (10 students) | | |
| - GAN augmentation (100 students) | | |
| - Neural Network training | | |
| **6. Feedback Loop & Pseudo-Labeling** | 2 min | [05-FeedbackLoop.md](./05-FeedbackLoop.md) |
| - Active learning approach | | |
| - Survey burden reduction | | |
| **7. Expected Results & Validation** | 3 min | [06-ValidationPlan.md](./06-ValidationPlan.md) |
| - Performance targets | | |
| - Validation methodology | | |

### Part 2: Live Demo (10 minutes)

| Section | Duration | File Reference |
|---------|----------|----------------|
| **1. Admin Portal** | 3 min | [07-DemoScript.md](./07-DemoScript.md) |
| - Create target survey | | |
| - Create factor survey | | |
| - Configure model settings | | |
| **2. Student Portal** | 4 min | [07-DemoScript.md](./07-DemoScript.md) |
| - Student enrollment | | |
| - Take surveys | | |
| - View predictions (future state) | | |
| **3. Analytics Dashboard** | 3 min | [07-DemoScript.md](./07-DemoScript.md) |
| - Bootstrap progress | | |
| - Data tracking | | |
| - Model performance metrics (future) | | |

---

## Key Research Contributions

1. **Advisor-Centric System Design**
   - Centralizes scattered student data (GPA, financial, personal circumstances) in one platform
   - Enables personalized advising through customizable surveys
   - Replaces manual data gathering and note-taking for advisors

2. **Progressive Learning Framework for Transfer Students**
   - First system to combine KNN → GAN → NN progression for transfer student success prediction
   - Addresses cold start problem (works with n=10 transfer students)
   - Automatically scales as cohort enrollment grows
   - Replaces legacy NLP + recommender system approach

3. **Intelligent Feedback Loop with Pseudo-Labeling**
   - Active learning approach reduces survey burden by 50-70%
   - Conditional data collection (only when model uncertain)
   - Continuous model improvement from student feedback
   - Benefits both students (less time) and advisors (maintains data quality)

4. **GAN-Based Data Augmentation for Small Cohorts**
   - Demonstrates GAN effectiveness for small educational datasets (transfer cohorts)
   - 4× data multiplication with quality validation
   - Enables neural networks with 100 real students instead of 1000+

5. **PWRS Formula (Priority-Weighted Response Scoring)**
   - Transparent, configurable success rate calculation
   - Based on Item Response Theory (IRT)
   - Advisors can adjust priorities without ML expertise
   - Provides explainable predictions for advising decisions

---

## File Organization

```
PresentationPlan/
├── 00-Overview.md (this file)
├── 01-Introduction.md
├── 02-SystemArchitecture.md
├── 03-SurveyMethodology.md
├── 04-ProgressiveLearning.md
├── 05-FeedbackLoop.md
├── 06-ValidationPlan.md
├── 07-DemoScript.md
├── 08-QandA.md
├── 09-RelatedWork.md (ACOSUS publications & literature)
├── 10-TeamAndAcknowledgments.md (NSF grant, multi-institutional team)
├── PRESENTATION-SUMMARY.md (condensed single-file version)
└── UPDATE-PLAN.md (alignment analysis)
```

---

## Presentation Tips

### Before Presentation
- [ ] Test live demo on acosus.neiu.edu
- [ ] Prepare backup screenshots in case of network issues
- [ ] Have demo accounts ready (admin + student)
- [ ] Test projector/screen sharing setup
- [ ] Review Q&A preparation file (08-QandA.md)
- [ ] Review ACOSUS publications for related work discussion

### During Presentation
- [ ] Start with transfer student challenges (lower graduation rates, unique obstacles)
- [ ] Emphasize ACOSUS project context (NSF-funded, multi-institutional)
- [ ] Clarify thesis scope: "System design + ML component for NEIU"
- [ ] Frame as advisor tool first: "Centralizes student data for personalized guidance"
- [ ] Emphasize novelty: "Predict transfer success with 10 students, improve to 100+"
- [ ] Use real-world analogy: "Like training wheels that automatically remove themselves"
- [ ] Highlight production deployment (not just prototype)
- [ ] Be transparent about current status (recruiting students, models pending data)

### Demo Best Practices
- [ ] Keep browser tabs pre-opened
- [ ] Narrate actions clearly ("Now I'm clicking...")
- [ ] Show both admin and student perspectives
- [ ] Explain what will happen when 10 students enroll
- [ ] Point out feedback loop UI elements

---

## Visual Aids Needed

1. **Architecture Diagram**: Three-layer system (Frontend → Backend → Model Server)
2. **Progressive Learning Timeline**: 10 students → 100 students → 1000+ students
3. **Feedback Loop Flowchart**: Rating ≥4 (pseudo-label) vs Rating <4 (correction)
4. **PWRS Formula Visualization**: Step-by-step calculation example
5. **Performance Target Chart**: MAE and R² targets by phase

---

## Backup Slides (If Time Permits or Asked)

- Detailed GAN architecture (Generator + Discriminator networks)
- Data normalization examples (heterogeneous → 0-10 scale)
- Cross-validation methodology (5-fold CV for KNN)
- Correlation validation metrics (Pearson r, KS test)
- Literature review and theoretical foundations

---

## Success Metrics for Presentation

✅ **Clear Problem Statement**: Audience understands retention crisis + cold start problem
✅ **Novel Contribution**: Audience recognizes progressive learning innovation
✅ **Technical Rigor**: Demonstrates ML expertise (KNN, GAN, NN, validation)
✅ **Practical Impact**: Shows production deployment, not just research
✅ **Future Work**: Clear roadmap for validation and scaling

---

## Next Steps After Defense

1. **Immediate** (Next 2 months)
   - Recruit 10 students for bootstrap phase
   - Train initial KNN model
   - Validate cross-validation metrics

2. **Short-term** (3-6 months)
   - Deploy feedback loop (students 11-99)
   - Measure pseudo-labeling effectiveness
   - Refine survey questions based on correlation

3. **Long-term** (6-12 months)
   - Scale to 100+ students for GAN/NN training
   - Longitudinal validation (predicted vs actual outcomes)
   - Multi-institution deployment

---

## Contact Information

- **System URL**: https://acosus.neiu.edu
- **Demo Accounts**:
  - Admin: admin@neiu.edu
  - Student: student1@neiu.edu
- **Repository**: [Internal NEIU GitLab]
- **Documentation**: [System docs portal]
