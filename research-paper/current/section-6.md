## 6 Conclusion and Future Work

This paper presented ACOSUS, an AI-driven counseling system designed specifically for transfer students in computing majors. We addressed the dual challenges of data scarcity inherent in departmental-level advising and the fragmented information landscape that advisors must navigate when supporting transfer populations.

### 6.1 Summary of Contributions

Our work makes three primary contributions to the literature on intelligent advising systems:

**First**, we introduced a Dual-Survey Architecture that cleanly separates label collection from feature collection (§3.1). Target Surveys capture success indicators through either direct self-assessment or priority-weighted multi-question instruments, while Factor Surveys systematically gather academic, financial, and logistical variables identified in prior research as predictive of transfer outcomes. This separation serves a dual purpose: it enables the progressive learning framework described below, and it addresses the data fragmentation problem by providing advisors with structured, standardized student profiles through a unified dashboard. The survey linkage mechanism further supports longitudinal adaptability, allowing researchers to deploy alternative feature sets without disrupting existing data collection.

**Second**, we designed a progressive learning framework that treats data scarcity as a fundamental design constraint rather than a limitation to overcome (§3.2). The three-stage pipeline—foundation, augmentation, and refinement—enables predictions to begin with as few as ten labeled observations, a threshold achievable within the first weeks of a new cohort. The algorithm-agnostic architecture permits substitution of any similarity-based method, generative technique, or deep learning architecture at each stage, positioning ACOSUS as a generalizable framework rather than a fixed implementation. As methodological advances emerge in few-shot learning and data augmentation, institutions can integrate these improvements without structural modification.

**Third**, we validated the platform through a pilot deployment during the foundation phase (§5). With N=4 transfer students from a public urban university, we assessed usability and data collection quality prior to model training. Perceived Ease of Use achieved a perfect score (M=5.00), indicating that the survey workflow successfully balanced comprehensiveness with accessibility—a critical requirement for time-constrained transfer students. The priority-weighted success rate calculations aligned with participants' self-assessments (M=4.50), validating the PWRS approach for generating training labels. The absence of reported technical or accessibility issues indicates deployment readiness for broader recruitment.

### 6.2 Current Status and Limitations

The system is currently operational and collecting labeled observations during the foundation phase. The pilot evaluation validated the data collection workflow and established that the PWRS formula produces labels that resonate with student self-perceptions. However, the predictive components of the framework—similarity-based predictions in the foundation stage, synthetic data generation in the augmentation stage, and deep learning in the refinement stage—remain to be evaluated as the training corpus grows.

The pilot findings are subject to the limitations detailed in §5.5: small sample size (N=4) precludes statistical generalization, self-selection bias may over-represent technology-positive students, and single-institution recruitment limits external validity. Furthermore, the evaluation captured immediate post-use perceptions rather than longitudinal academic outcomes. These constraints are appropriate for a formative usability study but insufficient for effectiveness claims.

### 6.3 Future Work

Several directions extend the current work:

**Continued Recruitment and Multi-Institutional Deployment.** The immediate priority is recruiting additional participants to reach the augmentation stage threshold, enabling evaluation of the full progressive pipeline. Concurrent deployment across partner institutions—including community colleges and regional universities—will assess generalizability across diverse transfer pathways and institutional contexts.

**Longitudinal Outcome Tracking.** The pilot captured perceptions at a single time point. Future work will track participants' academic trajectories (GPA changes, persistence, time-to-degree) to correlate predicted readiness scores with actual outcomes once sufficient training data enables predictions.

**Advisor Perspective Evaluation.** The current evaluation focused on student-facing workflows. A complementary study will assess whether the unified advisor dashboard reduces information-gathering burden and improves advising efficiency, addressing the data fragmentation problem identified in prior research [8], [17].

**Comparative Effectiveness Study.** With sufficient sample size, a controlled study comparing ACOSUS-assisted advising against traditional advising will establish whether the system improves outcomes beyond what structured advising interactions alone provide.

**Algorithm Comparison Studies.** The pluggable architecture enables systematic comparison of alternative algorithms within each pipeline stage. Future work will evaluate which specific similarity metrics, generative techniques, and neural architectures perform best for transfer student prediction, contributing empirical guidance to the broader educational data mining community.

### 6.4 Broader Implications

Beyond the immediate application to transfer student advising, ACOSUS demonstrates a template for deploying intelligent systems in small-data educational contexts. Many prediction problems in higher education—success of students in newly launched programs, outcomes for specialized populations, retention in departments with limited enrollment—share the cold-start challenge that motivated this work. The progressive learning framework, with its emphasis on immediate advisor utility during data collection and adaptive survey burden based on model confidence, offers a generalizable approach for these settings.

The explicit separation of concerns—data collection instruments from prediction algorithms, advisor-facing dashboards from student-facing workflows, configuration from core infrastructure—positions the architecture for adaptation across diverse institutional contexts. As the educational technology field increasingly emphasizes equity and transparency, systems designed from the ground up for underrepresented populations provide a model for responsible AI deployment in higher education.

---

*End of Section 6*
