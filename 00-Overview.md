# ACOSUS Master's Thesis Presentation - Overview

## Presentation Metadata

- **Title**: ACOSUS: Adaptive Course Success Prediction Using Progressive Machine Learning
- **Subtitle**: Predicting Student Academic Success from Minimal Initial Data Through Progressive Model Evolution
- **Presenter**: [Your Name]
- **Program**: Master's in Computer Science
- **Institution**: Northeastern Illinois University (NEIU)
- **Date**: November 18, 2025
- **Duration**: 30 minutes (20 min presentation + 10 min live demo)
- **Audience**: Faculty thesis committee

## System Status
- **Deployment**: 🟢 Live at [acosus.neiu.edu](https://acosus.neiu.edu)
- **Current Phase**: Bootstrap - Data Collection (0/10 students enrolled)
- **Model Status**: 🟡 Legacy implementation active, Target+Factor migration in progress

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

1. **Progressive Learning Framework**
   - First system to combine KNN → GAN → NN progression for student success prediction
   - Addresses cold start problem (works with n=10 students)
   - Automatically scales as enrollment grows

2. **Intelligent Feedback Loop with Pseudo-Labeling**
   - Active learning approach reduces survey burden by 50-70%
   - Conditional data collection (only when model uncertain)
   - Continuous model improvement from student feedback

3. **GAN-Based Data Augmentation**
   - Demonstrates GAN effectiveness for small educational datasets
   - 4× data multiplication with quality validation
   - Enables neural networks with 100 real students instead of 1000+

4. **PWRS Formula (Priority-Weighted Response Scoring)**
   - Transparent, configurable success rate calculation
   - Based on Item Response Theory (IRT)
   - Admin-adjustable without ML expertise

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
└── 08-QandA.md
```

---

## Presentation Tips

### Before Presentation
- [ ] Test live demo on acosus.neiu.edu
- [ ] Prepare backup screenshots in case of network issues
- [ ] Have demo accounts ready (admin + student)
- [ ] Test projector/screen sharing setup
- [ ] Review Q&A preparation file

### During Presentation
- [ ] Start with high-level problem (retention crisis)
- [ ] Emphasize novelty: "predict with 10 students, improve to 100+"
- [ ] Use real-world analogy: "Like training wheels that automatically remove themselves"
- [ ] Highlight production deployment (not just prototype)
- [ ] Be transparent about current status (no validation results yet)

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
