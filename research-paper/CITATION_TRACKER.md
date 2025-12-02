# Citation Tracker for ACOSUS Research Paper

This document tracks all citations needed across Sections 3, 4, and 5, categorized by type and priority.

---

## Summary Statistics

| Section | Total Citations Needed |
|---------|------------------------|
| Section 3: System Design | 6 |
| Section 4: Implementation | 5 |
| Section 5: Evaluation | 6 |
| **Total** | **17** |

---

## Section 3: System Design and Architecture

### 3.1 Overview

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S3-01 | "Traditional machine learning approaches requiring large training datasets are impractical" for small cohorts | Methodology paper / Survey | High | Look for papers on cold start problem in ML, small dataset challenges, or educational data mining with limited samples. Key terms: "cold start", "small sample learning", "few-shot learning" |

### 3.2.1 Functional Requirements

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S3-02 | "Needs analysis conducted with academic advisors and transfer student success research" | Transfer student research | High | Foundation for system requirements. Look for: (1) Transfer student challenges literature, (2) Academic advising best practices, (3) NISTS (National Institute for the Study of Transfer Students) reports |

### 3.5.2 Progressive Learning Framework

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S3-03 | KNN "effective with small datasets" and provides "interpretable results" | Methodology paper | Medium | Classic ML textbooks (Hastie et al., Bishop) or papers on KNN for small datasets. Could also cite instance-based learning surveys |
| S3-04 | "Conditional GAN generates synthetic training data... enabling neural network training that would otherwise require 1000+ samples" | GAN / Data augmentation paper | High | Papers on: (1) Conditional GANs (Mirza & Osindero), (2) GAN for tabular data augmentation, (3) SMOTE alternatives. Look for medical/education ML with small datasets using GAN augmentation |

### 3.5.4 Priority-Weighted Response Scoring (PWRS)

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S3-05 | PWRS formula "inspired by Item Response Theory" | Methodology paper | High | Classic IRT references: Rasch model, 2PL/3PL models. Authors: Lord & Novick (1968), Hambleton et al. (1991), Embretson & Reise (2000) |
| S3-06 | "S-shaped distribution reflecting empirical success rate patterns" | Statistical methods / Educational research | Medium | Papers on grade distributions, success rate normalization, or logistic calibration in educational assessment |

---

## Section 4: Implementation

### 4.2.3 Auto-Save Implementation

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S4-01 | Debouncing patterns for web applications | Software engineering best practices | Low | Could cite: Lodash documentation, web performance articles, or UX research on auto-save patterns. May be optional - common practice |

### 4.4.3 K-Nearest Neighbors Implementation

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S4-02 | KNN algorithm for small dataset prediction | Methodology paper | Medium | scikit-learn documentation, or classic ML papers. Cover (1967) for NN classification, or textbook reference |

### 4.4.4 GAN-Augmented Neural Network

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S4-03 | Conditional GAN architecture for data augmentation | Methodology paper | High | Mirza & Osindero (2014) "Conditional Generative Adversarial Nets". Also: CTGAN (Xu et al., 2019) for tabular data |

### 4.4.4 Synthetic Data Validation

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S4-04 | Kolmogorov-Smirnov test for distribution validation | Statistical methods | Medium | Classic statistics reference. Massey (1951) or any statistical methods textbook. scipy.stats documentation is also acceptable |

### 4.5.2 Role-Based Access Control

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S4-05 | Role-based access control patterns | Software engineering / Security | Low | Ferraiolo & Kuhn (1992) original RBAC paper, or NIST RBAC standard. May be optional - industry standard practice |

---

## Section 5: Evaluation and User Study

### 5.5.1 System Usability Scale (SUS)

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-01 | System Usability Scale instrument | Methodology paper | High | **Brooke, J. (1996)**. "SUS: A 'quick and dirty' usability scale." In Usability Evaluation in Industry. This is the canonical reference |

### 5.5.1 SUS Interpretation

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-02 | "SUS ≥ 68 (industry average for acceptable usability)" | Benchmark study | High | **Bangor, A., Kortum, P., & Miller, J. (2009)**. "Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale." JUS. Also: Sauro (2011) for percentile rankings |

### 5.5.2 Technology Acceptance Model (TAM)

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-03 | Technology Acceptance Model constructs | Methodology paper | High | **Davis, F.D. (1989)**. "Perceived usefulness, perceived ease of use, and user acceptance of information technology." MIS Quarterly. The foundational TAM paper |

### 5.7.2 Qualitative Analysis

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-04 | Thematic analysis methodology (Braun & Clarke, 2006) | Methodology paper | High | **Braun, V., & Clarke, V. (2006)**. "Using thematic analysis in psychology." Qualitative Research in Psychology. The standard reference for thematic analysis |

### 5.10.2 Feature Importance (SHAP)

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-05 | SHAP values for ML interpretability | Methodology paper | Medium | **Lundberg, S.M., & Lee, S.I. (2017)**. "A Unified Approach to Interpreting Model Predictions." NeurIPS. The original SHAP paper |

### 5.2 Research Questions (Implicit)

| ID | Context | Citation Type | Priority | Notes |
|----|---------|---------------|----------|-------|
| S5-06 | Transfer student success research foundations | Survey / Background paper | High | Needed for introduction and literature review. Look for: (1) Jenkins & Fink (2016) on transfer student outcomes, (2) NISTS reports, (3) Papers on underrepresented students in computing |

---

## Citation Categories Summary

### By Type

| Citation Type | Count | IDs |
|---------------|-------|-----|
| Methodology paper | 9 | S3-03, S3-04, S3-05, S4-02, S4-03, S5-01, S5-03, S5-04, S5-05 |
| Survey / Background | 3 | S3-01, S3-02, S5-06 |
| Statistical methods | 2 | S3-06, S4-04 |
| Software engineering / Best practices | 2 | S4-01, S4-05 |
| Benchmark study | 1 | S5-02 |

### By Priority

| Priority | Count | IDs |
|----------|-------|-----|
| High | 10 | S3-01, S3-02, S3-04, S3-05, S5-01, S5-02, S5-03, S5-04, S5-06, S4-03 |
| Medium | 5 | S3-03, S3-06, S4-02, S4-04, S5-05 |
| Low | 2 | S4-01, S4-05 |

---

## Suggested Sources by Category

### Related Work: Systems & Methodologies

1. **Cold Start / Small Dataset ML**
   - Pan, S.J., & Yang, Q. (2010). "A Survey on Transfer Learning." IEEE TKDE
   - Finn, C., Abbeel, P., & Levine, S. (2017). "Model-Agnostic Meta-Learning." ICML (few-shot learning)
   - Romero, C., & Ventura, S. (2010). "Educational Data Mining: A Review of the State of the Art." IEEE SMC

2. **GAN for Tabular Data Augmentation**
   - Mirza, M., & Osindero, S. (2014). "Conditional Generative Adversarial Nets." arXiv
   - Xu, L., et al. (2019). "Modeling Tabular Data using Conditional GAN." NeurIPS (CTGAN)
   - Chawla, N.V., et al. (2002). "SMOTE: Synthetic Minority Over-sampling Technique." JAIR (comparison baseline)

3. **KNN / Instance-Based Learning**
   - Cover, T., & Hart, P. (1967). "Nearest Neighbor Pattern Classification." IEEE IT
   - Aha, D.W., Kibler, D., & Albert, M.K. (1991). "Instance-Based Learning Algorithms." Machine Learning

### Statistical Methods

1. **Item Response Theory**
   - Hambleton, R.K., Swaminathan, H., & Rogers, H.J. (1991). "Fundamentals of Item Response Theory." Sage
   - Embretson, S.E., & Reise, S.P. (2000). "Item Response Theory for Psychologists." Lawrence Erlbaum

2. **Distribution Testing**
   - Massey, F.J. (1951). "The Kolmogorov-Smirnov Test for Goodness of Fit." JASA

### Software / Frameworks

1. **RBAC**
   - Sandhu, R.S., et al. (1996). "Role-Based Access Control Models." IEEE Computer

### Transfer Student Research

1. **Transfer Student Success**
   - Jenkins, D., & Fink, J. (2016). "Tracking Transfer: New Measures of Institutional and State Effectiveness." CCRC
   - Laanan, F.S. (2001). "Transfer Student Adjustment." New Directions for Community Colleges
   - NISTS Annual Reports on Transfer Student Outcomes

2. **Underrepresented Students in Computing**
   - Margolis, J., & Fisher, A. (2002). "Unlocking the Clubhouse: Women in Computing." MIT Press
   - Charleston, L.J., et al. (2014). "Using Culturally Responsive Practices to Broaden Participation in the Educational Pipeline." Journal of Research in Technical Careers

### Usability & Evaluation

1. **SUS**
   - Brooke, J. (1996). "SUS: A Quick and Dirty Usability Scale." In Jordan et al. (Eds.), Usability Evaluation in Industry
   - Bangor, A., Kortum, P., & Miller, J. (2009). "Determining What Individual SUS Scores Mean." JUS
   - Sauro, J., & Lewis, J.R. (2016). "Quantifying the User Experience." Morgan Kaufmann

2. **TAM**
   - Davis, F.D. (1989). "Perceived Usefulness, Perceived Ease of Use, and User Acceptance." MIS Quarterly
   - Venkatesh, V., & Davis, F.D. (2000). "A Theoretical Extension of the Technology Acceptance Model." Management Science

3. **Qualitative Methods**
   - Braun, V., & Clarke, V. (2006). "Using Thematic Analysis in Psychology." Qualitative Research in Psychology

### ML Interpretability

1. **SHAP**
   - Lundberg, S.M., & Lee, S.I. (2017). "A Unified Approach to Interpreting Model Predictions." NeurIPS
   - Ribeiro, M.T., Singh, S., & Guestrin, C. (2016). "Why Should I Trust You? Explaining the Predictions of Any Classifier." KDD (LIME)

---

## Action Items

### Immediate (High Priority)
- [ ] Obtain and verify citations for SUS (S5-01), TAM (S5-03), and thematic analysis (S5-04) - these are well-established instruments
- [ ] Find transfer student success literature for requirements justification (S3-02, S5-06)
- [ ] Locate GAN data augmentation papers for tabular data (S3-04, S4-03)
- [ ] Verify IRT citation for PWRS formula (S3-05)
- [ ] Find cold start / small dataset ML literature (S3-01)

### Secondary (Medium Priority)
- [ ] KNN literature for small datasets (S3-03, S4-02)
- [ ] SHAP paper for interpretability (S5-05)
- [ ] Success rate distribution / logistic calibration papers (S3-06)
- [ ] K-S test statistical reference (S4-04)

### Optional (Low Priority)
- [ ] Debouncing/auto-save UX patterns (S4-01) - may omit as common practice
- [ ] RBAC patterns (S4-05) - may omit as industry standard

---

## Notes

1. Several citations are "canonical" references with well-known authors and years - these should be easy to verify (Brooke 1996, Davis 1989, Braun & Clarke 2006)

2. The transfer student success citations (S3-02, S5-06) may overlap with citations from the Introduction section - coordinate to avoid duplication

3. Consider using recent survey papers where possible to capture state-of-the-art while reducing citation count

4. For software libraries (scikit-learn, TensorFlow), official documentation or JMLR software papers are acceptable

5. The GAN citations (S3-04, S4-03) are the same conceptual need - can use one strong citation in both locations
