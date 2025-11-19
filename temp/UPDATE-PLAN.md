# ACOSUS Presentation Update Plan

## Critical Misalignment Identified

### Current Presentation Focus
Your slides describe a **success prediction system** using progressive machine learning (KNN → GAN → NN) for predicting individual student success rates with minimal data.

### Actual ACOSUS Research Focus
The ACOSUS project (based on cs.neiu.edu/acosus) is an **AI-driven counseling/advising system** for underrepresented transfer students in computing majors.

---

## Key Differences Analysis

| Aspect | Current Slides | Actual ACOSUS Research |
|--------|---------------|------------------------|
| **Full Name** | Adaptive Course Success Prediction Using Progressive Machine Learning | An AI-driven COunseling System for Underrepresented Transfer Students |
| **Primary Goal** | Predict student success rate (0-100%) | Provide personalized counseling/advising for transfer students |
| **Target Population** | General students in any program | **Underrepresented transfer students** (community college → 4-year university) in STEM/computing |
| **Technical Approach** | Progressive ML (KNN → GAN → NN) with cold start | NLP + ML + Recommender systems |
| **Research Focus** | Cold start problem, pseudo-labeling, minimal data training | Transfer decision-making, social factors, personality traits, advising technologies |
| **NSF Grant** | Not mentioned | NSF IIS-2219623 (CISE-MSI) |
| **Team Structure** | Single presenter | Multi-institutional (NEIU, SUNY, Cal Poly Humboldt, UH-Victoria, UTEP) with 5 PIs + 11 RAs |
| **Publications** | None mentioned | 3+ papers (AMCIS 2023, ASEE 2023, NCCiT 2023, DSI 2024) |
| **System Type** | Prediction engine | Counseling/advising system with personalized guidance |

---

## Critical Questions for You

Before I can update the presentation, I need your clarification on these questions:

### Question 1: Is Your Thesis Part of the ACOSUS Project?
- **Option A**: Your thesis is a **component/module** of the larger ACOSUS project
  - Example: "Success prediction component within ACOSUS counseling system"
  - In this case, we need to show how your work fits into the larger ACOSUS ecosystem

- **Option B**: Your thesis is **separate** from ACOSUS but uses the same name
  - This would be problematic (naming conflict with NSF-funded project)

- **Option C**: Your thesis **IS** the ACOSUS project
  - This seems unlikely given the multi-institutional, multi-PI structure

### Question 2: What Does Your System Actually Do?
Based on your codebase exploration (backend, frontend, model), your system appears to:
- Collect student data via surveys (target + factor)
- Predict success rates using ML models
- Use progressive learning (KNN → GAN → NN)
- Deploy at acosus.neiu.edu

**Is this system intended to:**
- **A)** Predict transfer student success specifically (aligned with ACOSUS mission)?
- **B)** Provide counseling/advising recommendations to transfer students?
- **C)** Predict general student success (any student, not just transfers)?
- **D)** Something else?

### Question 3: What Is the Relationship to Dr. Xiwei Wang's ACOSUS Project?
- Are you a research assistant on the ACOSUS team? (You're listed as Deep Mandloi on the team page)
- Is your thesis supervised by Dr. Wang?
- Is your ML component being integrated into the larger ACOSUS counseling system?
- Or is this a separate implementation of "success prediction" under the ACOSUS umbrella?

### Question 4: Transfer Students vs General Students
The actual ACOSUS project focuses specifically on:
- **Transfer students** (community college → 4-year university)
- **Underrepresented backgrounds** (Hispanic, Black, first-generation)
- **Computing majors** specifically

Does your system:
- **A)** Focus exclusively on transfer students in computing?
- **B)** Work for any student (transfer or native)?
- **C)** Something in between?

### Question 5: Publications Alignment
Your slides don't reference the existing ACOSUS publications:
1. "A Survey of Student Counseling Systems" (AMCIS 2023)
2. "A Preliminary Factor Analysis on the Success of Computing Major Transfer Students" (ASEE 2023)
3. "Exploratory Analysis of Correlation between Personality Traits and Success" (NCCiT 2023)

Should your presentation:
- **A)** Build on these prior works (cite them as related work)?
- **B)** Ignore them (separate research)?
- **C)** Extend them (your thesis continues this research)?

---

## Proposed Update Scenarios

Based on your answers, here are potential update paths:

### Scenario 1: Your Thesis IS Part of ACOSUS Project
**If true**, the presentation should be updated to:

#### Title Slide
- **Current**: "ACOSUS: Adaptive Course Success Prediction Using Progressive Machine Learning"
- **Updated**: "ACOSUS: AI-Driven Counseling for Underrepresented Transfer Students - Success Prediction Component"
- **Subtitle**: "Progressive Machine Learning for Transfer Student Success Prediction with Minimal Data"

#### Introduction Changes
- Add context about transfer students (community college → university challenges)
- Emphasize underrepresented populations (Hispanic Serving Institutions)
- Cite existing ACOSUS publications as foundation
- Position your work as **one component** of the larger system

#### Background Section
- **Add**: Transfer student statistics (lower graduation rates, unique challenges)
- **Add**: Underrepresentation in computing (15% Black/Hispanic, 25% female)
- **Modify**: Frame "cold start" as "new transfer cohort" challenge
- **Add**: NSF grant context (IIS-2219623)

#### System Architecture
- Show how your prediction component fits into larger ACOSUS ecosystem
- Reference other components (counseling recommendations, NLP for decision-making, etc.)
- Clarify: "This thesis focuses on the ML prediction component"

#### Related Work Section (NEW)
- Cite the 3 ACOSUS publications
- Show how your work extends "Preliminary Factor Analysis" paper
- Reference "Survey of Counseling Systems" as motivation

#### Target Population
- **Current**: Generic "students"
- **Updated**: "Underrepresented transfer students in computing majors"
- **Add**: Transfer-specific factors (transfer shock, credit loss, institutional fit)

---

### Scenario 2: Your Thesis Extends ACOSUS to General Prediction
**If true**, the presentation should:

#### Title
- Keep "ACOSUS" but clarify it's an extension/generalization
- Subtitle: "Extending Transfer Student Counseling to General Success Prediction"

#### Introduction
- Start with ACOSUS project context (NSF-funded, transfer students)
- **Your contribution**: "We generalize this approach to any student population"
- Position as "transferable framework" (pun intended)

#### Acknowledgments
- Credit Dr. Wang and ACOSUS team
- Note: "This work builds on the ACOSUS project..."

---

### Scenario 3: Different System, Same Name (Problem!)
**If true**, you have a naming conflict:

- **Issue**: Using "ACOSUS" for a different system than the NSF-funded project
- **Solution**: Either align with actual ACOSUS or rename your system
- **Recommendation**: Align with ACOSUS mission if possible

---

## Specific Slide Updates Needed (Pending Your Answers)

### Slide 1: Title
- **Current**: Too generic
- **Needs**: Clarify relationship to ACOSUS project and transfer student focus

### Slide 2: Background
- **Missing**: Transfer student context
- **Missing**: Underrepresented populations statistics
- **Missing**: NSF grant acknowledgment

### Slide 4: "How a Course Works"
- **Title is confusing**: Should be "How ACOSUS Works" or "Student Journey in ACOSUS"
- **Missing**: Transfer-specific context (previous institution, transfer credits, etc.)

### Slide 6: Research Objectives
- **Missing**: Connection to ACOSUS project goals
- **Missing**: How this helps underrepresented transfer students specifically

### Slide 7: System Architecture
- **Missing**: Where this fits in larger ACOSUS ecosystem
- **Missing**: Integration with other ACOSUS components

### NEW Slide: Related Work
- Should cite the 3 existing ACOSUS publications
- Should cite literature on transfer student success
- Should position your ML approach vs. existing counseling systems

### NEW Slide: Team & Acknowledgments
- Dr. Xiwei Wang (advisor?)
- ACOSUS team (5 PIs, 11 RAs)
- NSF IIS-2219623
- Partner institutions

---

## Research Questions for Context

To help me update the slides accurately, please clarify:

### About Your Data Collection
1. Are you collecting data from **transfer students only** or **all students**?
2. Do you track transfer-specific factors like:
   - Previous institution (community college name)
   - Credits transferred vs. lost
   - "Transfer shock" (GPA drop after transfer)
   - Institutional fit/social integration
3. Do your surveys include questions about transfer decision-making?

### About Your Success Definition
1. Is "success rate" defined differently for transfer students?
2. Do you predict:
   - **A)** Overall academic success (GPA, graduation)
   - **B)** Transfer-specific success (adjustment, retention post-transfer)
   - **C)** Career readiness (job placement after graduation)
   - **D)** All of the above

### About Your Model
1. Does your KNN/GAN/NN model specifically account for transfer student patterns?
2. Have you validated on transfer student data?
3. Do transfer students have different prediction accuracy than native students?

### About Your Deployment
1. Is acosus.neiu.edu:
   - **A)** Exclusively for NEIU transfer students?
   - **B)** Multi-institutional (SUNY, UTEP, Cal Poly Humboldt)?
   - **C)** Open to any institution?

---

## Recommended Next Steps

### Step 1: You Answer the 5 Critical Questions Above
This will determine the update strategy.

### Step 2: I'll Create Updated Slide Content
Based on your answers, I'll revise:
- Title and positioning
- Background and motivation (add transfer student context)
- Research objectives (align with ACOSUS mission)
- Related work (cite existing publications)
- Target population (clarify transfer vs. general)
- Team and acknowledgments

### Step 3: Verify Factual Accuracy
You review the updated slides to ensure:
- Correct relationship to ACOSUS project
- Accurate representation of your system
- Proper citations and acknowledgments

---

## Key Points to Address in Updated Presentation

### Must Include (if your work is part of ACOSUS)
1. ✅ NSF Grant acknowledgment (IIS-2219623)
2. ✅ Multi-institutional collaboration (5 institutions)
3. ✅ Transfer student focus (community college → university)
4. ✅ Underrepresented populations (Hispanic, Black, first-generation)
5. ✅ Computing major specificity
6. ✅ Citations to existing ACOSUS publications
7. ✅ Dr. Xiwei Wang as PI/advisor
8. ✅ Position your ML work as component of larger system

### Must Clarify
1. ❓ Is your system for transfer students only or general students?
2. ❓ How does your prediction component integrate with counseling/advising?
3. ❓ What is your relationship to the ACOSUS research team?
4. ❓ Is your thesis supervised by Dr. Wang or another faculty?

---

## Example Updated Title Slide (Scenario 1)

**Current**:
```
ACOSUS: Adaptive Course Success Prediction Using Progressive Machine Learning
Predicting Student Academic Success from Minimal Initial Data
```

**Updated (if part of ACOSUS project)**:
```
ACOSUS: AI-Driven Counseling System for Underrepresented Transfer Students
Progressive ML Component for Transfer Student Success Prediction

Master's Thesis Presentation
Deep Mandloi
Advisor: Dr. Xiwei Wang
Northeastern Illinois University

NSF Award IIS-2219623
Multi-Institutional Collaboration:
NEIU | SUNY Old Westbury | Cal Poly Humboldt | UH-Victoria | UTEP
```

---

## Summary

**Before I can update the presentation files, I need you to clarify:**

1. **Is your thesis part of the ACOSUS project or separate?**
2. **What does your system actually do (prediction only, or counseling/advising)?**
3. **What is your relationship to Dr. Wang's ACOSUS team?**
4. **Does your system focus on transfer students or general students?**
5. **Should you cite the existing ACOSUS publications?**

**Once you answer these questions, I can provide specific update recommendations for each slide.**

**My Assessment:**
Based on the evidence:
- You're listed on the ACOSUS team page (Deep Mandloi, NEIU)
- Your system is deployed at acosus.neiu.edu
- The domain suggests this IS the ACOSUS project

**Most likely scenario:** Your thesis is the ML/prediction component of the larger ACOSUS project, and your slides need to be updated to reflect:
- Transfer student focus
- Underrepresented populations
- NSF grant context
- Multi-institutional collaboration
- Connection to existing ACOSUS research

**Please confirm or correct this assessment so I can update the slides accordingly.**
