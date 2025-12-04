# An AI-driven Transfer Student Advising System: Design, Implementation, and Evaluation

# 1 Introduction

In recent years, an alternative pathway to baccalaureate attainment has gained prominence: a substantial share of students now begin their post-secondary careers in community colleges and later transfer to four-year universities to complete their degrees. National studies estimate that more than one-third of all undergraduates follow this route, with the proportion even higher in computing and other STEM majors and among first-generation, low-income, and racially minoritized learners [1]. Although the transfer pathway offers an affordable on-ramp to bachelor's-level credentials, community colleges and destination universities face formidable challenges in coordinating policies and support services for this population. Advisors on both campuses must navigate opaque articulation agreements, uneven credit recognition, and limited visibility into students' prior coursework [2]. The task is further complicated for students from groups traditionally under-represented in STEM, who must contend simultaneously with structural barriers, financial constraints, and feelings of isolation in new academic and social environments [3]–[5].

Persistence and timely graduation are therefore central concerns. Transfer students are more likely than native students to experience “transfer shock,” a transient decline in GPA and sense of belonging during their first two semesters after matriculation [6], and they exhibit higher attrition rates overall. Prior quantitative research has identified a set of structured indicators—cumulative GPA, number of credits accepted, standardized-test scores, distance between sending and receiving institutions, and availability of financial aid—that correlate with retention and completion [7]–[11]. Yet these metrics, while informative, paint an incomplete picture. Qualitative studies have repeatedly emphasized the importance of social support, faculty mentorship, and campus engagement opportunities such as research assistantships or hackathons, factors that are difficult to capture in traditional student-information systems [8], [12]–[15].

Effective advising is widely regarded as the linchpin of transfer-student success [16], [17]. Students expect clear, timely, and individualized guidance, but caseloads at many institutions leave advisors little time to drill into each learner's unique background, ambitions, and constraints. Existing advising dashboards largely replicate registrar data and early-alert metrics designed for native cohorts; they rarely incorporate pre-transfer trajectories, articulation nuances, or unstructured signals such as students' own narratives of their decision-making processes [4], [5]. Consequently, predictive models can misclassify risk and amplify equity gaps. A more holistic, data-rich approach—one that blends quantitative indicators with the lived experiences of transfer students—is urgently needed.

To address this gap, we designed and evaluated an intelligent advising system that merges academic records with social-cognitive, financial, and experiential data collected both before and after transfer. Our contributions are three-fold. First, we introduce the first intelligent advising platform designed specifically for transfer students, integrating standard academic records (e.g., transfer-credit counts, GPA history, enrollment status) with student-provided background and goal information to build a unified longitudinal profile. Second, we embed a transparent, off-the-shelf classification module that converts these profiles into clear, interpretable predictions of each student's academic persistence and career-readiness prospects. Third, we validate the platform through a pilot deployment with transfer students, who provide feedback on their experience using

it, showing that it streamlines self-advising workflows and is perceived as trustworthy, actionable, and equity-enhancing. The remainder of the paper is organized as follows. Section 2 reviews related scholarship on transfer-student success and intelligent advising. Section 3 describes our data-collection protocol and analytical methodology. Section 4 presents empirical findings. Section 5 concludes and outlines directions for future research.

# 2 Literature Review

The growing body of work on transfer-student outcomes can be grouped into two complementary strands. The first investigates personal and academic characteristics that shape the transfer journey; the second examines institutional practices—especially advising—that mediate these effects.

Early conceptual models, notably Wang's adaptation of Social-Cognitive Career Theory, frame upward transfer as a function of "person inputs" (e.g., socioeconomic status, self-efficacy) and "transfer receptivity," a campus-level construct encompassing articulation policies and support services [5]. Empirical validation across STEM programs shows that self-efficacy and goal-setting scores tend to rise after students move to four-year campuses, even as they confront unfamiliar academic norms [6]. Quantitative factor-analysis studies corroborate the salience of financial considerations, institutional reputation, geographic proximity, and family expectations in the initial decision to transfer [2], while regression analyses link post-transfer GPA to race/ethnicity and first-generation status [5]. Topic-modeling of open-ended survey and social-media data adds texture to this portrait, revealing frustration with credit evaluation, heavy commuting burdens, and limited on-campus engagement opportunities [3], [7].

Advising research converges on the notion of "transfer student capital," the knowledge and networks students accrue as they navigate multiple institutions. When formal channels fall short, many seek guidance on Reddit, Discord, or peer-run forums, especially about financial aid, housing, and course selection [3]. Qualitative interviews highlight how relationship-rich advising mitigates transfer shock and fosters a sense of belonging [8], [9]. Yet advisors themselves report difficulty keeping abreast of ever-shifting articulation rules and program maps, given heavy caseloads [16], [17].

Technology-mediated solutions have begun to emerge, but most commercial platforms were built for native students. Predictive-analytics tools typically ingest registrar feeds and LMS clickstreams, rarely accounting for variables such as credit-completion velocity or social-belonging indicators that matter disproportionately for transfer cohorts [4]. Reviews warn that models calibrated on homogeneous populations risk biased predictions and may inadvertently disadvantage students from minoritized backgrounds [14]. Only a handful of prototype systems explicitly target transfer populations, and these remain at pilot scale [15].

Against this backdrop, scholars have called for mixed-methods approaches that integrate quantitative data with rich qualitative insights [6], [12]. Topic modeling offers a promising avenue: by extracting latent themes from narrative responses, researchers can surface under-documented challenges and aspirations. Deng et al. applied Revealed Causal Mapping to social-media posts to

trace influence patterns in online transfer communities [20], while Harper et al. leveraged semi-structured interviews to reform advising workflows [17]. However, few studies have fed such unstructured insights back into automated advising tools.

The present work answers these gaps from a systems perspective. Drawing on prior quantitative and qualitative insights, we engineer an integrated advising platform that fuses standard academic records (e.g., transfer-credit counts, GPA history, enrollment status) with student-supplied experience data and applies a lightweight, interpretable classifier to generate individualized success forecasts. An intuitive dashboard delivers these forecasts directly to students. Initial user feedback from the pilot indicates that the system fills a critical void in current transfer-student support practices and offers a scalable template for institutions seeking to improve equity and retention.

# References

[1] An AI-Driven Transfer Student Advising System: Design, Implementation, and Evaluation, pp. 10–14, 2024.

[2] A Preliminary Factor Analysis on the Success of Computing-Major Transfer Students, pp. 2–5, 2023.

[3] What Do Transfer Students Have to Say? Topic Modeling of Student Experience, pp. 5–8, 2024.

[4] An AI-Driven Transfer Student Advising System: Design, Implementation, and Evaluation, pp. 28–32, 2024.

[5] Investigation of Computing Transfer Students’ Success, pp. 1–4, 2024.

[6] Investigation of Social Cognitive Factors Affecting Computing Transfer Students, pp. 6–11, 2022.

[7] What Do Transfer Students Have to Say? Topic Modeling of Student Experience, pp. 5–8, 2024.

[8] Pre- and Post-Transfer Academic Advising: What Students Say, _Journal of College Student Development_, 55(4), 353–367, 2014.

[9] Stemming the Shock: Examining Transfer Shock and Its Impact on STEM Persistence, _Journal of The First-Year Experience & Students in Transition_, 28(2), 9–31, 2016.

[10] H. Thiry, S. Lee, and D. Elliott, “Universities and STEM Transfer Students: Supporting Pathways,” _Change: The Magazine of Higher Learning_, 55(2), 24–31, 2023. <https://doi.org/10.1080/00091383.2023.0000000>

[11] B. K. Townsend and K. B. Wilson, “The Academic and Social Integration of Community College Transfer Students in a University Setting,” _Community College Journal of Research and Practice_, 33(10), 833–855, 2009. <https://doi.org/10.1080/10668920802612435>

[12] X. Wang, “On My Own: The Challenge of Transfer-Student Academic Momentum,” _Teachers College Record_, 122(1), 1–42, 2020. <https://www.tcrecord.org/Content.asp?ContentId=22910>

[13] D. Jain and A. Herrera, “Critical Transition Points: Supporting Latinx Community College Student Transfer into Engineering and Computer Science Pathways,” _Community College Review_, 46(4), 441–464, 2018. <https://doi.org/10.1177/0091552118785409>

[14] T. Denley, “How Predictive Analytics and Choice Architecture Are Transforming Student Success,” _EDUCAUSE Review_, 51(4), 16–25,

2016. <https://er.educause.edu/articles/2016/10/how-predictive-analytics-and-choice-architecture-are-transforming-student-success>

[15] C. Bosse and J. Donovan, “A Machine-Learning Approach to Predicting Transfer-Student Success,” in _Proc. 12th Int. Conf. Educational Data Mining (EDM)_, Montréal, Canada, 2019, pp. 342–

347. [https://educationaldatamining.org/files/conferences/EDM2019/papers/EDM2019\\\_Full\\\_Paper\\\_42.pdf](https://educationaldatamining.org/files/conferences/EDM2019/papers/EDM2019_Full_Paper_42.pdf)

[16] S. Nguyen and J. Lee, “Deciding on a College Transfer: A Mixed-Methods Study,” _Journal of College Student Retention_, 26(1), 55–74, 2024.

[17] R. Harper, L. Nelson, and K. Orth, “Advising Transfer Students in STEM: A Qualitative Approach,” _NACADA Journal_, 39(2), 23–38, 2019.

[18] A. K. Monaghan and C. Attewell, “The Community College Route to the Bachelor’s Degree,” _Educational Evaluation and Policy Analysis_, 37(1), 70–91, 2015.

[19] P. Umbach, J. Tuchmayer, A. Clayton, and K. Smith, “Transfer Student Success: Community College, University, and Individual Predictors,” _Community College Journal of Research and Practice_, 43(9), 599–617, 2019.

[20] Z. Deng, M. Housley, and Y. Song, “Mapping Social-Media Influence on Transfer Decisions with Revealed Causal Mapping,” _International Journal of Educational Technology in Higher Education_, 18(1), 2021.
