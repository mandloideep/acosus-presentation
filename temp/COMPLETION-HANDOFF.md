# Presentation Update - Session Handoff Document

## Session Summary

**Date**: Current session
**Work Completed**: 6 out of 13 files updated (46% complete)
**Remaining Work**: 7 files need updates
**Token Budget Used**: ~50K of 200K

---

## ✅ Completed Files (6/13)

### 1. **00-Overview.md** ✅
**Status**: Fully updated with transfer student context

**Changes Made**:
- Updated title: "ACOSUS: AI-Driven Counseling System for Underrepresented Transfer Students"
- Added subtitle: "Progressive Machine Learning for Transfer Student Success Prediction - System Design & ML Component"
- Added advisor: Dr. Xiwei Wang (Principal Investigator, NEIU)
- Added NSF Grant: IIS-2219623 (CISE-MSI)
- Added multi-institutional context (5 universities)
- Updated target population: "Underrepresented transfer students in computing majors"
- Updated key contributions to include "Advisor-Centric System Design" as #1
- Updated file organization to include new files (09, 10)
- Enhanced presentation tips with transfer student framing

**No further action needed**

---

### 2. **03-SurveyMethodology.md** ✅
**Status**: Minor updates completed

**Changes Made**:
- Added context: "Surveys are designed by advisors to gather both ground truth (target) and predictive factors for transfer student success"
- Added note: "Current surveys use generic readiness assessments, but system supports dynamic addition of transfer-specific factors"
- Updated purpose: "Collect actual/perceived success rates from transfer students"
- Added advisor context: "Provides baseline understanding of student confidence and readiness before offering guidance"
- Added reference to actual surveys: `backend/src/init/data/quiz.json`
- Updated frequency note: "First 10 transfer students: REQUIRED"

**No further action needed**

---

### 3. **04-ProgressiveLearning.md** ✅
**Status**: Minor updates completed

**Changes Made**:
- Added context at top: "This progressive ML approach replaces the legacy NLP + recommender system. The cold start problem is framed as: 'How do we predict transfer student success with only 10 students in a new cohort?'"
- Updated Phase 1 duration: "2-4 weeks (depending on NEIU transfer student enrollment rate)"
- Updated Phase 1 goal: "Collect initial training data from first transfer student cohort"
- Updated Phase 1 action: "All transfer students complete Target + Factor surveys"
- Added note: "ML models will be trained after 10 NEIU transfer students enroll. Implementation is pending data collection (currently 0/10 students)."

**No further action needed**

---

### 4. **05-FeedbackLoop.md** ✅
**Status**: Minor update completed

**Changes Made**:
- Added advisor benefit at top: "Advisor Benefit: Reduces survey burden on transfer students while maintaining high-quality data for personalized advising decisions."

**No further action needed**

---

### 5. **09-RelatedWork.md** ✅ NEW FILE
**Status**: Fully created

**Contents**:
- All 4 ACOSUS publications with full citations, relevance, and key findings:
  1. "A Survey of Student Counseling Systems" (AMCIS 2023)
  2. "A Preliminary Factor Analysis on Computing Transfer Students" (ASEE 2023)
  3. "Exploratory Analysis of Personality Traits and Success" (NCCiT 2023)
  4. "Deciding on a College Transfer via Reddit Topic Modeling" (DSI 2024)
- Transfer student success literature with statistics
- Existing advising systems (Starfish, Civitas, EAB Navigate)
- Progressive ML in education
- GAN-based data augmentation research
- Pseudo-labeling & active learning literature
- Comparison table showing ACOSUS contributions vs prior work

**No further action needed**

---

### 6. **10-TeamAndAcknowledgments.md** ✅ NEW FILE
**Status**: Fully created

**Contents**:
- Thesis presenter: Deep Mandloi, Advisor: Dr. Xiwei Wang
- NSF Grant IIS-2219623 details
- All 5 partner institutions (NEIU, SUNY Old Westbury, Cal Poly Humboldt, UH-Victoria, UTEP)
- All 5 Co-PIs with their roles
- All 12 research assistants with their institutions and roles
- NEIU responsibilities: System design + ML prediction component
- Other institutions' responsibilities (NLP, personality traits, factor analysis, etc.)
- Division of work diagram
- All 4 publications listed
- Conference presentations
- Acknowledgments for funding, facilities, support
- Contact information

**No further action needed**

---

## 🔴 Remaining Files (7/13) - NEEDS COMPLETION

### Priority 1: Major Rewrites (3 files)

#### **1. 01-Introduction.md** 🔴 CRITICAL
**Current State**: Generic student success prediction narrative
**Required Changes**: Complete rewrite with transfer student focus

**Must Include**:
- **Slide 1 (Title)**:
  - Title: "ACOSUS: AI-Driven Counseling System for Underrepresented Transfer Students"
  - Subtitle: "Progressive Machine Learning for Transfer Student Success Prediction"
  - System Design & ML Component (NEIU's Responsibility)
  - Presenter: Deep Mandloi, Advisor: Dr. Xiwei Wang
  - NSF Grant IIS-2219623

- **Slide 2 (Background)**:
  - Transfer student statistics:
    - 10-15% lower graduation rates than native students
    - 37% don't return for second year
    - Average 13 credits lost during transfer
    - "Transfer shock": 0.2-0.5 GPA drop in first semester
  - Underrepresentation in computing:
    - Only 15% of computing workers are Black/Hispanic
    - Only 25% are female
    - Community college → university pathway is critical for diversity
  - **Remove**: Generic "40% of students don't graduate" (too broad)

- **Slide 3 (Advisor Pain Points)** - NEW SECTION:
  - Current challenges for advisors:
    - Student data scattered across multiple systems (SIS, financial aid, LMS, manual notes)
    - 40-60% of advising time spent gathering information
    - Difficult to remember details for 100+ students
    - Hard to provide personalized guidance without complete picture
  - ACOSUS solution:
    - Centralizes all student information in one platform
    - Advisors create customizable surveys (beyond just GPA)
    - System collects: academic, financial, personal circumstances, support systems
    - Enables personalized advising before meetings

- **Slide 4 (4 Core Challenges)** - UPDATE:
  - Challenge 1: "New Transfer Cohort Problem" (not "new course")
    - Small transfer cohorts (10-20 students per semester)
    - Need predictions immediately, can't wait years
  - Challenge 2: Advisor data gathering burden
  - Challenge 3: Progressive accuracy improvement as cohort grows
  - Challenge 4: Survey burden vs. accuracy

- **Slide 5 (Research Problem)**:
  - Primary question: "How can we predict underrepresented transfer student success with only 10 students in a new cohort?"
  - Frame as: New transfer cohort → 10 students → Need immediate predictions
  - **Remove**: "New CS program launches" language

- **Slide 6 (Research Objectives)**:
  - Add: "Support advisors with centralized student data platform"
  - Add: "Enable prediction for transfer student success"
  - Update timeline: NEIU transfer student enrollment
  - Add: NSF-funded multi-institutional research context

**Key Messaging**:
- Emphasize transfer students throughout
- Frame as advisor tool first, ML prediction second
- NEIU's role in larger ACOSUS project
- System design + ML component thesis scope

---

#### **2. 08-QandA.md** 🔴 MAJOR REWRITE NEEDED
**Current State**: Generic ML questions
**Required Changes**: Add transfer student, ACOSUS project, and advisor-focused questions

**Must Add These Question Categories**:

**A. Transfer Student Questions** (NEW):
- Q: "Why focus specifically on transfer students?"
  - A: 10-15% lower graduation rates, unique challenges (transfer shock, credit loss, institutional fit), underrepresented in computing

- Q: "What makes transfer students different from native students?"
  - A: Transfer shock (GPA drop), credit articulation issues, social integration challenges, financial pressures

- Q: "Does your system work for non-transfer students?"
  - A: Yes, system is designed for flexibility. Currently focused on transfer students for ACOSUS project, but architecture supports any student population

**B. ACOSUS Project Questions** (NEW):
- Q: "How does your thesis fit into the larger ACOSUS project?"
  - A: ACOSUS is multi-institutional NSF project. NEIU's role: system design + ML prediction. Other institutions: NLP (SUNY), personality traits (Cal Poly), factor analysis (UTEP), counseling systems (UH-Victoria)

- Q: "Why not multi-institutional deployment?"
  - A: Thesis scope = NEIU deployment. Each institution has separate research focuses. Future work: integration across institutions

- Q: "What about the other ACOSUS publications?"
  - A: Build on findings from Factor Analysis (ASEE 2023), Counseling Systems Survey (AMCIS 2023), Personality Traits (NCCiT 2023)

**C. Advisor Use Case Questions** (NEW):
- Q: "How does this help advisors specifically?"
  - A: Centralizes data (GPA, financial, personal circumstances), enables personalized surveys, reduces prep time, provides success predictions for targeted interventions

- Q: "What if advisors don't trust ML predictions?"
  - A: System provides explainable predictions (PWRS formula, similar students), advisors always make final decisions, predictions are advisory not prescriptive

**D. Update Existing Questions**:
- Update Q: "No validation results yet?"
  - Add: "Recruiting 10 NEIU transfer students currently (0/10 enrolled)"

- Update Q: "What if model performs poorly?"
  - Add: "Success rate definition requires further study - may include GPA, graduation, career readiness, or composite"

**E. System Design Questions** (NEW):
- Q: "Why build from scratch instead of using existing systems?"
  - A: Existing systems (Starfish, Civitas) require 500-10,000 students, expensive ($50K-$200K/year), don't support cold start

---

#### **3. PRESENTATION-SUMMARY.md** 🔴 COMPLETE REWRITE NEEDED
**Current State**: Generic student success prediction summary
**Required Changes**: Full rewrite with transfer student focus, advisor use case, NSF context

**New Structure**:

**Title Section**:
- "ACOSUS: AI-Driven Counseling System for Underrepresented Transfer Students"
- NSF Grant IIS-2219623, Multi-institutional (5 universities)
- NEIU Thesis: System Design + ML Component
- Presenter: Deep Mandloi, Advisor: Dr. Xiwei Wang

**The Problem**:
- Transfer students face unique challenges:
  - 10-15% lower graduation rates
  - 37% don't return for second year
  - Average 13 credits lost
  - "Transfer shock" GPA drop
- Underrepresentation in computing (15% Black/Hispanic, 25% female)
- Advisors struggle with scattered data sources

**ACOSUS Solution - Three Objectives**:
1. **For Advisors**: Centralize student data, enable personalized guidance
2. **For Predictions**: Predict transfer student success with minimal data (10 students)
3. **For Students**: Reduce survey burden through feedback loop

**Core Innovation: Progressive Learning**:
- Phase 1 (10 students): KNN
- Phase 2 (100 students): GAN + Neural Network
- Replaces legacy NLP + recommender approach

**Dual-Survey System**:
- Target Survey: Collects success rate
- Factor Survey: Collects predictive features
- Current surveys: Generic readiness (see backend/src/init/data/quiz.json)
- System supports dynamic addition of transfer-specific factors

**System Architecture**:
- Frontend (React) + Backend (Node.js) + Model Server (Python)
- Deployed at acosus.neiu.edu
- Target: NEIU transfer students (system designed for broader use)

**Current Status**:
- System deployed ✅
- Recruiting 10 transfer students (0/10 enrolled)
- ML models pending data collection
- Validation planned for Spring-Fall 2026

**Key Contributions**:
1. Advisor-centric system design
2. Progressive learning for small cohorts
3. Feedback loop with pseudo-labeling
4. GAN augmentation for educational data
5. PWRS formula (explainable predictions)

**ACOSUS Project Context**:
- NSF IIS-2219623 (CISE-MSI)
- 5 institutions: NEIU, SUNY, Cal Poly Humboldt, UH-Victoria, UTEP
- NEIU: System + ML (this thesis)
- Others: NLP, personality traits, factor analysis

---

### Priority 2: Moderate Updates (3 files)

#### **4. 02-SystemArchitecture.md** 🔴 MODERATE UPDATE
**Current State**: Technical architecture only
**Required Changes**: Add advisor workflow section

**Must Add Section** (after "Three-Component Architecture"):

**NEW SECTION: "System Purpose for Advisors"**:
- Replaces scattered data gathering:
  - Before: Check SIS (GPA), financial aid portal (scholarships), LMS (engagement), manual notes
  - After: Single ACOSUS dashboard with complete student profile

- Enables personalized advising:
  - Advisors create custom surveys beyond standard academic questions
  - Can ask: family support, commute distance, work hours, financial independence
  - All responses centralized for meeting preparation

- Advisor workflow:
  1. Admin creates surveys (target + factor)
  2. Students complete before advising meeting
  3. Advisor reviews responses + ML prediction
  4. Personalized guidance based on complete profile

**Update Data Flow Diagram**:
- Show advisor role: Admin creates surveys → Students complete → Advisors view → Personalized guidance

**Add Future Vision**:
- Current: Advisor tool (data centralization)
- Mid-term: ML predictions inform advising
- Long-term: Automated student recommendations

---

#### **5. 06-ValidationPlan.md** 🔴 MODERATE UPDATE
**Current State**: Generic validation plan
**Required Changes**: Add transfer student context, realistic NEIU timeline

**Updates Needed**:

**Update Current Status Section**:
- Change: "Currently recruiting 10 NEIU transfer students (0/10 enrolled)"
- Add: "Validation pending data collection - estimated Spring 2026 for Phase 1"

**Add Note on Success Rate Definition**:
- "Success rate definition requires further study and validation"
- "May include: GPA maintenance, on-time graduation, career readiness, or composite metric"
- "Will be refined based on advisor feedback and empirical validation"

**Update Timeline**:
- Phase 1 (Spring 2026): Recruit 10-20 NEIU transfer students, bootstrap validation
- Phase 2 (Summer-Fall 2026): Grow to 50 students, KNN validation
- Phase 3 (Fall 2026-Spring 2027): 100+ students, GAN/NN validation
- Phase 4 (2027-2028): Longitudinal validation

**Add Transfer-Specific Validation**:
- Compare transfer vs. native student prediction accuracy
- Validate on transfer-specific metrics (retention post-transfer, GPA change)
- Test advisor satisfaction with centralized data platform

---

#### **6. 07-DemoScript.md** 🔴 MODERATE UPDATE
**Current State**: Generic admin demo
**Required Changes**: Frame as advisor creating surveys, add advisor perspective

**Updates Needed**:

**Update Admin Demo Section (Minutes 1-3)**:
- Narrative: "Advisors can create customized surveys to understand transfer student backgrounds"
- Example: "An advisor wants to understand: financial support, commute distance, previous institution experience"
- Show: Creating surveys with questions beyond just GPA

**Add Note About Advisor Portal** (if not implemented):
- "Future enhancement: Advisor dashboard to view all student responses"
- "Currently: Admin can view via student records"

**Update Student Demo Section (Minutes 4-8)**:
- Narrative: "Before meeting with advisor, transfer student completes surveys"
- "This gives advisor complete picture: academic, financial, personal circumstances"

**Update Analytics Demo (Minutes 9-12)**:
- Add: "Advisors can track: survey completion rates, prediction accuracy, student feedback"
- Future: "Advisor-specific dashboards showing their advisee cohort"

---

### Priority 3: Minor Update (1 file)

#### **7. README.md** 🔴 MINOR UPDATE
**Current State**: Generic project README
**Required Changes**: Add NSF grant, new files, transfer student note

**Simple Updates**:

**At Top - Add Context Block** (before "Core Presentation Files"):
```markdown
## Project Context

**ACOSUS Project**: AI-Driven Counseling System for Underrepresented Transfer Students
**NSF Grant**: IIS-2219623 (CISE-MSI)
**Multi-Institutional**: NEIU, SUNY Old Westbury, Cal Poly Humboldt, UH-Victoria, UTEP
**NEIU Thesis**: System Design + ML Prediction Component (Deep Mandloi, Advisor: Dr. Xiwei Wang)

**Website**: https://cs.neiu.edu/acosus/
```

**Update Core Presentation Files List** (add 09, 10):
```
9. **[09-RelatedWork.md](./09-RelatedWork.md)** - ACOSUS publications & literature review
10. **[10-TeamAndAcknowledgments.md](./10-TeamAndAcknowledgments.md)** - NSF grant, multi-institutional team
```

**Update File Status Table** (add 09, 10):
```
| 09-RelatedWork.md | ✅ Complete | 100% |
| 10-TeamAndAcknowledgments.md | ✅ Complete | 100% |
```

**Update Acknowledgments Section** (at bottom):
```markdown
## Acknowledgments

This presentation plan supports the ACOSUS master's thesis defense at NEIU.

**NSF Grant**: IIS-2219623 (CISE-MSI)
**Advisor**: Dr. Xiwei Wang (PI, NEIU)
**Project**: Multi-institutional collaboration (5 universities)
```

---

## 📚 Reference Materials for Next Session

### Key Context Documents

1. **Original slides.md**: `/home/deep/projects/research/ts/slides.md`
   - Contains original presentation content (generic student success)
   - Use for structure reference only, content needs transfer student reframing

2. **Survey Questions**: `/home/deep/projects/research/ts/backend/src/init/data/quiz.json`
   - Actual target and factor survey questions
   - 5 categories: Academic Confidence, Motivation & Career Goals, Personal Attributes, Resources & Support, Self-Assessment
   - Currently generic readiness, not transfer-specific yet

3. **ACOSUS Website**: https://cs.neiu.edu/acosus/
   - Home page: Project overview, goals, NSF grant
   - Our Team: All 5 PIs and 12 research assistants
   - News: Publications and conference presentations

4. **User Clarifications** (from conversation):
   - Thesis is part of ACOSUS project
   - System designed to predict transfer student success AND provide advisor tool for counseling
   - Advisors want centralized student data (GPA, financial, personal circumstances)
   - Short-term: Advisor tool; Mid-term: ML predictions; Long-term: Automated recommendations
   - Target: Underrepresented transfer students, but system works for any student
   - Current surveys: Generic (backend/src/init/data/quiz.json)
   - System supports adding transfer-specific factors dynamically
   - ML models NOT yet trained (0/10 students, pending data collection)
   - Success rate definition needs further study
   - Legacy approach: NLP + recommender → New approach: Progressive ML (KNN→GAN→NN)

### ACOSUS Publications (for citations)

1. Yun Wan et al. (2023). "A Survey of Student Counseling Systems: Functions, Designs, and Interactions." AMCIS 2023.
2. Xiwei Wang et al. (2023). "A Preliminary Factor Analysis on the Success of Computing Major Transfer Students." ASEE 2023.
3. Sherrene Bogle et al. (2023). "Exploratory Analysis of Correlation between Personality Traits and the Success of Computing Major Transfer Students." NCCiT 2023.
4. Shebuti Rayana et al. (2024). "Deciding on a College Transfer: Uncovering Transition Queries and Concerns via Reddit Topic Modeling." DSI 2024.

---

## 🎯 Completion Strategy for Next Session

### Recommended Order

1. **Start with 01-Introduction.md** (CRITICAL - 30 min)
   - Sets foundation for entire presentation
   - Most important file to get right
   - Complete rewrite needed

2. **Update 02-SystemArchitecture.md** (MODERATE - 15 min)
   - Add advisor workflow section
   - Quick update, builds on 01

3. **Update 06-ValidationPlan.md** (MODERATE - 10 min)
   - Update timeline and status
   - Add transfer-specific notes

4. **Update 07-DemoScript.md** (MODERATE - 15 min)
   - Reframe as advisor tool demo
   - Update narrative

5. **Rewrite 08-QandA.md** (MAJOR - 30 min)
   - Add all new question categories
   - Critical for defense preparation

6. **Rewrite PRESENTATION-SUMMARY.md** (MAJOR - 30 min)
   - Single-file condensed version
   - Complete reframe needed

7. **Update README.md** (MINOR - 5 min)
   - Quick final touches

**Total Estimated Time**: ~2.5 hours
**Total Estimated Tokens**: ~40-50K

---

## 📝 Quick Reference: Key Messaging Changes

### ❌ Remove/Replace
- "40% of students don't graduate" → Transfer-specific statistics
- "New course/program launches" → "New transfer cohort"
- Generic student success → Transfer student success
- "Retention crisis" → Transfer student graduation challenges

### ✅ Add/Emphasize
- **Transfer student focus**: 10-15% lower graduation, transfer shock, credit loss
- **Underrepresented populations**: 15% Black/Hispanic in computing, 25% female
- **Advisor use case**: Centralize data, personalized guidance, reduce prep time
- **NSF grant**: IIS-2219623, multi-institutional (5 universities)
- **NEIU role**: System design + ML component
- **Current status**: 0/10 students, recruiting, models pending data
- **System flexibility**: Works for any student, currently focused on transfers
- **Legacy → New**: NLP + recommender → Progressive ML

---

## 🔧 Technical Details

### File Paths
- Presentation files: `/home/deep/projects/research/ts/PresentationPlan/`
- Backend surveys: `/home/deep/projects/research/ts/backend/src/init/data/quiz.json`
- Model documentation: `/home/deep/projects/research/ts/model/`

### Files Already Updated (DO NOT REVERT)
1. 00-Overview.md
2. 03-SurveyMethodology.md
3. 04-ProgressiveLearning.md
4. 05-FeedbackLoop.md
5. 09-RelatedWork.md (NEW)
6. 10-TeamAndAcknowledgments.md (NEW)

### Files Needing Updates (7 remaining)
1. 01-Introduction.md - MAJOR REWRITE
2. 02-SystemArchitecture.md - MODERATE UPDATE
3. 06-ValidationPlan.md - MODERATE UPDATE
4. 07-DemoScript.md - MODERATE UPDATE
5. 08-QandA.md - MAJOR REWRITE
6. PRESENTATION-SUMMARY.md - MAJOR REWRITE
7. README.md - MINOR UPDATE

---

## ✅ Completion Checklist for Next Session

- [ ] Read this COMPLETION-HANDOFF.md file completely
- [ ] Review the 6 completed files to understand the framing
- [ ] Start with 01-Introduction.md (most critical)
- [ ] Follow recommended order above
- [ ] Use key messaging changes (remove generic, add transfer student focus)
- [ ] Reference ACOSUS publications in updated files
- [ ] Maintain consistency with completed files
- [ ] Update README.md last
- [ ] Mark all todos as completed
- [ ] Provide final summary to user

---

## 🎓 Final Notes

**User Goal**: Complete and accurate presentation for master's thesis defense on November 18, 2025

**User Expectation**: All files updated with transfer student focus, advisor use case, NSF context, and ACOSUS project alignment

**Critical Success Factors**:
1. Transfer student focus throughout (not generic students)
2. Advisor use case prominently featured (centralize data, personalized guidance)
3. NSF grant and multi-institutional context (NEIU's role clear)
4. Current status transparency (0/10 students, models pending)
5. System flexibility noted (works for any student, currently transfers)

**User Approved**: The update plan in UPDATE-PLAN.md - all changes align with user's clarifications

---

**Ready for next session to complete the remaining 7 files!**
