Here is the complete Markdown file content based on your request. You can copy the content below directly into a `.md` file to use as context for future AI interactions.

---

# BibTeX Citation

```bibtex
@inproceedings{Wali2025Transfer,
  author    = {Wali, Nawar and Hooshangi, Sara},
  title     = {Transfer Students in Computer Science: Examining Barriers, Success Metrics, and Research Gaps},
  booktitle = {Proceedings of the 30th ACM Conference on Innovation and Technology in Computer Science Education V. 1 (ITICSE 2025)},
  year      = {2025},
  publisher = {ACM},
  address   = {Nijmegen, Netherlands},
  doi       = {10.1145/3724363.3729118},
  pages     = {86--92}
}

```

# Executive Summary

**Paper Overview:**
This paper is a systematic literature review analyzing 38 peer-reviewed papers (from ACM, IEEE, and ASEE) to explore the specific experiences of transfer students in Computer Science (CS). The authors argue that while research exists for STEM transfer students generally, CS students face unique curriculum and professional dynamics that require specific study.

**Key Findings:**

- **Barriers:** CS transfer students often experience "transfer shock" (a temporary GPA drop). Major hurdles include financial needs, lack of background knowledge in gateway courses (like Data Structures), and credit loss due to misalignment between community colleges and universities.

- **Success Metrics:** Financial aid is the most critical factor for retention. Effective support strategies include "near-peer" mentoring (students mentoring students), summer bridge programs (specifically for math/foundational gaps), and early advising.

- **Diversity:** Transfer pathways are a primary entry point for underrepresented groups (URG), including women, minorities, and first-generation students. However, despite being more diverse, these students often report lower levels of departmental support compared to "native" four-year students.

**Conclusion & Research Gaps:**
The authors conclude that while institutional support (mentorship, financial aid) helps, there is a significant gap in global research (most studies are US-centric). They recommend future research use mixed methods (qualitative and quantitative) to better understand the "lived experience" of these students and to look beyond the US education system.

---

# Full Paper Content

## Abstract

Transfer students play an important role in enhancing diversity within computer science programs. As first-generation college students, minorities, rural residents, and individuals from low-income backgrounds, transfer students represent a demographic critical to fostering innovation and inclusion in the field. However, while significant research has been conducted on transfer students in STEM disciplines, studies specifically addressing their experiences in computer science remain limited. This paper presents a preliminary systematic review of the literature to explore the challenges, successes, and gaps in the support of transfer students in computer science.

## 1. Introduction and Motivation

Diversity in computer science remains a critical and widely discussed topic. Although Diversity, Equity and Inclusion (DEI) initiatives have been heavily discussed, their outcomes often vary [19]. Some initiatives achieve measurable success, while others fall short of their intended goals. Governments and universities recognize the importance of fostering diversity, as evidenced by various government projects aimed at increasing representation in STEM fields [2] [17].

Many institutions globally are committed to increasing the diversity of computer science programs. A method to achieve this goal is by creating more accessible pathways for transfer students transitioning from community colleges or two-year institutions to four-year universities. These institutions are not unique to the United States; they exist worldwide, including in countries like Canada, Japan, India, and Thailand, where they serve as bridges between secondary education and higher education or workforce training [37].

Transfer students often represent underserved demographics, including minorities, first-generation college students, rural students, and those from low-income backgrounds. By facilitating their entry into computer science programs, we can leverage the inclusive potential of community colleges worldwide, significantly enhancing diversity and inclusion in the field.

Research has extensively documented the challenges facing these students, particularly in STEM disciplines. Common barriers include the need for financial aid, the phenomenon of 'transfer shock' (a temporary drop in GPA after transferring) [13], low retention rates [33], and inadequate institutional support [29]. Although many studies have explored these struggles in engineering and other STEM fields, there is a significant gap and lack of research specifically addressing computer science transfer students.

This gap is critical to address because computer science has unique educational and professional dynamics that differ from challenges seen in other fields. Understanding the current landscape, identifying gaps, and building on existing research is essential to develop targeted solutions.

## 2. Methodology

Our study is guided by the Kitchenham et al. [22] process on systematic literature reviews in software engineering. We began by defining the purpose of this review, then articulated research questions, followed by developing a review protocol, we concluded by analyzing the data and synthesizing results.

### Data Sources and Inclusion Criteria

This review focuses on papers from global education- and computer science-related conferences hosted by **ACM, IEEE, and ASEE**. These venues were chosen to ensure relevance to computing education research while excluding those with broader applications or less direct focuses on computer science education.

**Inclusion Criteria:** Papers were included if they met all of the following conditions:

1. **Specific Focus on Transfer Students in Computer Science:** The study must explicitly address transfer students as a key demographic within computer science education. This includes research analyzing their academic performance, pathways, retention, or challenges specific to the computer science context.

2. **Primary or Comparative Treatment of Transfer Students:** The paper must directly address transfer students either as the primary population of interest or as a significant comparative group. Examples include studies exploring interventions aimed at improving transfer student outcomes or understanding how their experiences differ from non-transfer students.

**Exclusion Criteria:**

- **Peripheral Mentions of Transfer Students:** Studies that only mentioned transfer students as part of a broader dataset without substantive analysis or focus on their experiences were excluded.

- **Focus on General Undergraduate Populations:** Papers that addressed broader issues in computer science education (e.g., curriculum design for all undergraduates) but did not analyze transfer students as a distinct group were excluded.

- **Non-Transfer-Specific Initiatives:** Studies that discussed general diversity initiatives in computer science education without focusing on transfer students as a targeted group were excluded.

- **Different Disciplines:** Papers that focused on transfer students in non-computing disciplines, such as general STEM or humanities fields, were excluded.

### Dataset

The final dataset, compiled after applying the search and inclusion criteria, consists of 38 papers published across the three venues: IEEE, ASEE, and ACM.

**Table 1: Number of Papers Published by each Venue**
| Venue and Conference | Papers |
| :--- | :--- |
| **IEEE** | |
| Frontiers in Education (FIE) | 3 |
| RESPECT | 1 |
| **ASEE** | |
| Annual Conference | 21 |
| Virtual Annual Conference | 2 |
| **ACM** | |
| Inroads | 1 |
| TOCE | 1 |
| ITICSE | 1 |
| SIGCSE | 4 |
| SIGITE | 1 |
| ICER | 1 |
| Learning @ Scale (L-AT-S) | 2 |
| **Grand Total** | **38** |

### Codebook

To systematically address our research questions, we organized the papers into distinct groups using a set of codes. The final set of codes is presented in Table 2.

**Table 2: Codebook for Categorizing Selected Papers**
| Code Group | Code | Description |
| :--- | :--- | :--- |
| **Transfer Pathways in CS Education** | **Pathways** | Papers on frameworks and initiatives to ease the transition from two-year to four-year CS programs. Focus areas: articulation agreements, transfer processes, program alignment. |
| **Underrepresented Groups in CS Transfer** | **URG** | Studies on the experiences of underrepresented groups (e.g., minorities, women) in CS transfers. Focus areas: equity, inclusion, support mechanisms. |
| **Institutional Support for CS Transfers** | **IS** | Research on institutional support and resources impacting transfer student success. Focus areas: financial aid, advising, mentoring, community building. |
| **Career Readiness and Professional Development** | **CRPD** | Papers on career preparation for transfer students via industry collaborations and experiential learning. Focus areas: internships, industry partnerships, curriculum enhancement. |
| **Assessment and Success Metrics** | **ASST** | Studies on evaluating transfer programs. Focus areas: assessments, retention, program replication. |
| **Academic Performance and Challenges** | **PERF** | Papers on GPA shock, academic readiness, and transition challenges. Focus areas: performance gaps, academic support. |
| **Equity in Education Access** | **EQ-ED** | Papers on broadening access to education for disadvantaged students. Focus areas: access pathways, systemic inequalities, democratization strategies. |

## 4. Results

### 4.1 Transfer Pathways and Success Metrics

Financial aid has emerged as a critical factor in both transfer student retention and their decision to transfer in the first place [10]. Collaboration between institutions, particularly between two-year and four-year colleges, plays a vital role in fostering transfer student success. Programs that focus on peer mentoring, industry advising, scholarships, online resources, orientation sessions, and tutoring provide essential support. However, a persistent challenge remains: many students lack the necessary background knowledge to excel in gateway courses, which hinders retention efforts [1].

One example is a transition program emphasizing networking and program standards through workshops, mentoring, and student empowerment activities. These initiatives have proven effective in helping transfer students adjust to new academic environments [2]. While both transfer and native students face similar course-specific difficulties [11], gaps in academic preparation are a significant concern. For instance, students transferring with a C average in prerequisite courses often struggle more in subsequent courses compared to peers with higher grades [14]. This underscores the importance of transfer credit policies that ensure prerequisite courses adequately prepare students.

To address these gaps, initiatives with robust support frameworks, such as mandatory tutoring and professional mentoring, have shown success in boosting transfer rates and degree completion [16]. For example, summer bridge programs have been particularly effective in addressing foundational gaps in mathematics, with one study reporting that 60% of participants eliminated the need for remedial math. Expanding such models to a broader range of students—not just those in specific pathways—could further promote equitable access to engineering and computer science education.

Strengthening transfer pathways between community colleges and four-year institutions has been identified as a key strategy to increase participation in fields like engineering and computer science. Effective articulation agreements and curriculum alignment can reduce credit loss and facilitate smoother transitions for students [20, 21]. Programs that integrate early advising, cohort-building, and financial support highlight the value of intentional interventions in improving transfer student outcomes [15]. By offering scholarships, tailored advising, and extracurricular opportunities, these programs help students adapt both academically and socially to their new environment.

Near-peer instruction is another promising approach, where students are mentored by individuals only a few years ahead of them academically. For instance, in an NSF S-STEM (Scholarships in Science, Technology, Engineering, and Mathematics) Award program, graduate students mentor undergraduate transfer students through research-oriented courses. Near-peer mentorship provides: psychological and emotional support, assistance in setting goals, exploring career paths, academic knowledge support, and access to relatable role models.

Despite these successes, challenges persist. Research shows that transfer students often struggle to adapt to new academic systems, especially when transitioning from semester-based community colleges to quarter-based four-year institutions [34]. Additionally, discrepancies in preparation and performance metrics, such as Basic Data Structures Inventory (BDSI) scores in computer science courses, highlight the need for targeted support to ensure equitable outcomes for transfer students [34].

### 4.2 Equity and Diversity in Transfer Pathways

Community colleges have become an entry point for students transitioning to four-year universities. This pathway is especially significant for underrepresented students who often face challenges related to transfer decision-making, access to academic and non-academic support, and job placement opportunities. These barriers disproportionately affect minority groups and underscore the importance of equity-focused initiatives [35]. A study using the Laanan-Transfer Student Questionnaire found that transfer students are often first-generation college students (44%), older than traditional students (two-thirds are 21 years or older), and from lower socioeconomic backgrounds. In addition, proximity to home plays a significant role in their decision to transfer [24].

In response to these challenges, institutions have developed programs aimed at increasing diversity in engineering and computer science. For example, the College of Engineering and Computer Science at one university received an NSF (National Science Foundation) S-STEM Scholarship grant to support students with high financial need and underrepresented minority (URM) students in computer science [38]. Similarly, financial, family support, and geographical factors remain the most common reasons for transfer, with women and minorities comprising approximately 61% of transfer students [5].

A survey conducted nationwide in the United States by the BRAID Research team revealed that upward transfer students tend to be more diverse in terms of race/ethnicity, socioeconomic status, and other demographic factors compared to native computing students. However, these students report lower levels of peer, mentor, and departmental support. This represents a missed opportunity for computing programs to better serve and support this diverse group of students [12].

Despite these initiatives, gender disparities remain stark. While more women than men transfer from community colleges to four-year universities, women are far less likely to select engineering and computer science as their major. In a study done in Texas, data from a ten-year cohort study showed that only 2% of female transfer students chose engineering or computer science compared to 11% of male transfers [30].

## 5. Discussion

### 5.1 Transfer Pathways and Success Metrics

**RQ1: What frameworks and institutional strategies best support transfer students' successful transition from two-year to four-year computer science programs?**
We found that in our literature review, financial aid is a critical factor in transfer student retention and success post-transfer [10]. Students who were able to obtain financial aid were able to focus more on their studies as well as reduced the need for getting secondary jobs. Beyond financial aid, early advising, cohort-based models, and structured pathways have proven effective in helping students adapt to new academic environments [15]. These strategies not only ease the struggles of transferring but also help to create a sense of belonging to the community.

**RQ2: How can these strategies address challenges such as GPA shock, retention, and academic performance?**
The GPA disparity of 0.2 to 0.3 points between transfer and native students highlights the support needed by transfer students [4]. To address this, institutions should focus on targeted interventions, such as summer bridge programs that tackle foundational gaps, especially in high-demand areas like mathematics [16]. Additionally, clear transfer credit policies can prevent students from being unprepared for advanced courses. For example, ensuring that prerequisite courses taken at community colleges are similar in rigor to those at four-year institutions can reduce academic shock and improve outcomes.

**RQ3: How does institutional support influence the academic and career outcomes of computer science transfer students?**
Institutional support plays an important role in shaping both academic and career outcomes. Programs that integrate mentoring with industry exposure, such as NSF-funded initiatives, help students understand a diverse set of pathways post-graduation [3]. Near-peer mentoring programs have been shown to have success in offering relatable role models and tailored academic guidance, fostering both academic success and a sense of belonging for their students [32].

### 5.2 Equity and Diversity in Transfer Pathways

**RQ1: How do transfer pathways contribute to increasing diversity and inclusion in computer science?**
Transfer pathways are crucial for diversifying computer science programs, as they serve as a gateway for first-generation, older, and socioeconomically disadvantaged students [24]. However, these students often lack access to resources such as peer networks and mentoring, which can limit their sense of belonging and academic success [12]. This disparity suggests an opportunity for computing programs to better leverage the diversity of transfer students by developing inclusive practices that address their unique needs.

**RQ2: What specific barriers and support mechanisms affect underrepresented groups in their transfer journey?**
Underrepresented groups, including women and minority students, face intersecting barriers such as inadequate academic preparation, financial constraints, and limited exposure to career pathways [35]. Programs that can combine academic and professional mentoring with research opportunities, such as summer research initiatives, can potentially bridge academic gaps and bring more interest in CS from underrepresented groups [28]. Institutions must also address structural barriers, such as proximity to campus and inflexible program requirements, which disproportionately affect these students.

## 6. Research Gaps and Future Directions

Challenges extend beyond academic performance to social integration. Although native freshmen and transfer students rated their overall social experiences similarly, native freshmen were nearly twice as likely to develop close personal friendships on campus (55%) compared to transfer students (29%) [26]. Additionally, at least one in five native freshmen had participated in student organizations related to their major or intramural sports, highlighting higher engagement in extracurricular and co-curricular activities compared to transfer students. These disparities emphasize the importance of interventions to support transfer students' academic and social integration.

Improving transfer student outcomes requires institutional partnerships that extend beyond individual campuses [27]. Effective strategies include organizing students into cohorts to foster peer support, providing support that is both timely and accessible, defining clear pathways that guarantee graduation within a set timeframe, and helping students develop a clear post-graduation vision early in their academic journey.

While these challenges have been well-documented in the U.S., there is a noticeable lack of global literature on transfer students in computer science and other fields. The majority of existing studies focus on the U.S. context, which may not fully represent the diverse experiences of transfer students worldwide. Future research should explore the unique challenges and support systems for transfer students in varying educational systems globally, ensuring that findings can inform policies and practices across different cultural and institutional contexts.

Finally, capturing a broader understanding of transfer student challenges and success requires expanding methodological approaches. This involves integrating qualitative insights with quantitative data to better capture the lived experiences of transfer students. For instance, analyzing participation in co-curricular activities, sense of belonging, and engagement with support services could provide a holistic understanding of the transfer student experience. Additionally, employing predictive modeling to identify at-risk students early could inform targeted interventions, ensuring that resources are allocated efficiently to those who need them most.

## 7. Conclusion and Future Work

Addressing the systemic barriers faced by transfer students requires a multi-faceted approach that combines financial, academic, and social support. Institutions must collaborate to develop streamlined transfer pathways, equitable policies, and inclusive support frameworks. By focusing on these areas, policymakers and educators can create more effective and accessible pathways for transfer student success, especially in computer science.

This review represents a preliminary step toward a more comprehensive examination of the computer science transfer student experience. While our focus on conference papers from ACM, IEEE, and ASEE ensures alignment with computing education venues, it may exclude relevant journal articles, poster papers, and global studies. In subsequent work, we plan to broaden our scope to include more diverse sources, incorporate additional CS-specific constructs such as curriculum alignment, and more clearly delineate CS-specific themes versus generalizable STEM insights.

## References

[1] Zilouchian Ali, Romance Nancy, Myers Annie Laurie, Hamadeh Dana, and Vitale Michael. 2019. A University-State College Collaborative Project to Advance Students' Degree Completion and Career Attainment in Engineering and Computer Science. doi:10.18260/1-2-32016
[2] Mary Anderson-Rowland. 2006. Evaluating an Academic Scholarship Program For Engineering and Computer Science Transfer Students. In Proceedings. Frontiers in Education. 36th Annual Conference. IEEE, 18-25. doi:10.1109/fie.2006.322554
[3] Mary Anderson-Rowland. 2009. An academic scholarship program for transfer students in engineering and computer science: A five year summary. In ASEE Annual Conference and Exposition.
[4] Mary R. Anderson-Rowland. 2011. Reducing GPA shock for engineering and computer science community college transfer students. In ASEE Annual Conference and Exposition.
[5] Mary R. Anderson-Rowland. 2012. Understanding the path of engineering and computer science upper division transfer students to a large university. In ASEE Annual Conference and Exposition.
[6] Mary R. Anderson-Rowland. 2013. Critical support for upper division Transfer Students in engineering and computer science. In IEEE Frontiers in Education Conference (FIE) IEEE, 1891-1897. doi:10.1109/fie.2013.6685164
[7] Mary R Anderson-Rowland and Anita Grierson. 2010. Evaluating a university/community college collaboration for encouragement of engineering and computer science transfer students. In ASEE Annual Conference and Exposition.
[8] Mary R. Anderson-Rowland, Armando Rodriguez, and Anita Grierson. 2013. S-STEM programs for transfer and non-transfer upper division and graduate engineering and computer science students. In ASEE Annual Conference and Exposition.
[9] I. Araojo and M. Ayoobi. 2024. IDENTITY DEVELOPMENT AND INTEGRATION PROCESS AMONG TRANSFER STUDENTS IN STEM FIELDS. In ICER12024 Proceedings.
[10] Jasmine Batten, Alexandra Strong, Monique Ross, Elodie Billionniere, and Myrian Herlle. 2022. Exploring the pathways: Using transition theory to understand the strategies undergraduate computing students leverage as transfer students. In ASEE Annual Conference and Exposition.
[11] Frederik Baucks, Robin Schmucker, Conrad Borchers, Zachary A. Pardos, and Laurenz Wiskott. 2024. Gaining Insights into Group-Level Course Difficulty via Differential Course Functioning. In Proceedings of the Eleventh ACM Conference on Learning @ Scale, Vol. 43. ACM, 165-176.
[12] Jennifer M. Blaney. 2020. Broadening Participation in Computing. In Proceedings of the 51st ACM Technical Symposium on Computer Science Education. ACM, 254-260.
[13] Karen Brinkley-Etzkorn and Leigh Cherry. 2022. A lens for transfer: A history of the theoretical frameworks and conceptual models applied to the study of transfer students. Journal of College Student Retention: Research, Theory & Practice 24, 1 (2022), 99-125.
[14] Helen Catanese, Carl Hauser, and Assefaw H. Gebremedhin. 2018. Evaluation of native and transfer students' success in a computer science course. ACM Inroads 9, 2 (2018), 53-57.
[15] B. Knight David, P. E. Amy Richardson, Grote Dustin Michael, C. Lee Walter, A. Watford Bevlee, Hall Janice Leshay, and Glisson Hannah. 2022. Completing the engineering and computer science transfer pathway: Transfer students' post-matriculation experiences through a four-year institution. doi:10.18260/1-2--39108
[16] D. J Espiritu and R. Todorovic. 2020. Increasing Diversity and Student Success in Engineering and Computer Science through Contextualized Practices. ASEE Virtual Annual Conference Content Access (2020).
[17] David M Ford, Paula Rees, and Kathleen G Rubin. 2015. The impact of federally funded scholarship programs on the success of transfer students at a public engineering college. In 2015 ASEE Annual Conference & Exposition.
[18] Jeffrey E Froyd, Julie P Martin, Maura J Borrego, Nathan H Choe, Margaret J Foster, and Xueshu Chen. 2015. What have we learned from a systematic review of literature on Hispanic transfer students in engineering?. In 2015 ASEE Annual Conference & Exposition.
[19] Seval Gündemir, Rouven Kanitz, Floor Rink, Inga J. Hoever, and Michael L. Slepian. 2024. Beneath the surface: Resistance to diversity, equity, and inclusion (DEI) initiatives in organizations. Current Opinion in Psychology 60 (2024), 101922.
[20] Shanna Smith Jaggars, John Fink, Jeffrey Fletcher, and Afet Dundar. 2016. The community college pathway to computer science and other STEM bachelor's degrees. In RESPECT, IEEE, 1-2.
[21] Jinya Jiang, Richa Kafle, Christa Lehr, Simone Wright, Clarissa Guitierrez-Godoy, and Christine Alvarado. 2024. Understanding California's Computer Science Transfer Pathways. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1. ACM, 604-610.
[22] Barbara Kitchenham and Stuart M. Charters. 2007. Guidelines for performing systematic literature reviews in software engineering. Tech. report EBSE-2007-01. EBSE, Keele, UK.
[23] Sophia Krause-Levy, Sander Valstar, Leo Porter, and William G. Griswold. 2022. A Demographic Analysis on Prerequisite Preparation in an Advanced Data Structures Course. In Proceedings of the 53rd ACM Technical Symposium on Computer Science Education. ACM, 661-667.
[24] Harrison Kwik, Benjamin Xie, and Amy J. Ko. 2018. Experiences of Computer Science Transfer Students. In Proceedings of the 2018 ACM Conference on International Computing Education Research. ACM, 115-123.
[25] R. Anderson-Rowland Mary, A. Rodriguez Armando, and Grierson Anita. 2011. Making a Difference: How to Recruit More Community College Women and Underrepresented Minority Students into Engineering and Computer Science. doi:10.18260/1-2--18313
[26] Lisa Massi, Patrice Lancey, Uday Nair, Rachel Straney, Michael Georgiopoulos, and Cynthia Young. 2012. Engineering and computer science community college transfers and native freshmen students: Relationships among participation in extra-curricular and co-curricular activities, connecting to the university campus, and academic success. In Frontiers in Education Conference Proceedings. IEEE, 1-6.
[27] Sathya Narayanan, Kathryn Cunningham, Sonia Arteaga, William J. Welch, Leslie Maxwell, Zechariah Chawinga, and Bude Su. 2018. Upward Mobility for Underrepresented Students. In Proceedings of the 49th ACM Technical Symposium on Computer Science Education. ACM, 705-710.
[28] Norouzi Narges, Robinson Carmen, and Tellez Kip. 2024. Board 266: Enhancing Transfer Pathways in Computing: An NSF Project Progress Report. doi:10.18260/1-2-46839
[29] Andrea M. Ogilvie P.E. 2014. A Review of the Literature on Transfer Student Pathways to Engineering Degrees. In 2014 ASEE Annual Conference & Exposition.
[30] Rincon Roberta. 2018. Women on the Community College Pathway toward a Baccalaureate Degree in Engineering or Computer Science in Texas. doi:10.18260/1-2-31258
[31] Conner Shannon, DiSilvestre Olivia Anne, Ridlehuber Marcus Lee, Averitt Louise, and D. Matthew Boyer. 2023. Examining Student Experiences Related to Transfer from Two-Year Technical Colleges to Engineering and Computer Science Degree Programs at a Four-Year Institution. doi:10.18260/1-2--43499
[32] Conner Shannon, Hubbarth Skylar, and D. Matthew Boyer. 2024. Impacts of Near-Peer Mentoring Between Graduate Students and Undergraduate Transfer Students in Engineering and Computing. doi:10.18260/1-2--47569
[33] Natasha L Smith and Eileen M Van Aken. 2020. Systematic literature review of persistence of engineering transfer students. Journal of Engineering Education 109, 4 (2020), 865-883.
[34] Sander Valstar, Sophia Krause-Levy, Adrian Salguero, Leo Porter, and William G. Griswold. 2021. Proficiency in Basic Data Structures among Various Subpopulations of Students at Different Stages in a CS Program. In Proceedings of the 26th ACM Conference on Innovation and Technology in Computer Science Education V. 1. ACM, 429-435.
[35] Xiwei Wang, Shebuti Rayana, Sherrene Bogle, Palvi Aggarwal, and Yun Wan. 2023. A Preliminary Factor Analysis on the Success of Computing Major Transfer Students. In ASEE Annual Conference and Exposition.
[36] Erica Winterer, Jeffrey E Froyd, Maura J Borrego, Julie P Martin, Nathan Hyungsok Choe, Margaret J Foster, et al. 2017. Board# 153: A Systematic Review of Literature on Latino Transfer Students in Engineering. In 2017 ASEE Annual Conference & Exposition.
[37] Alexander W. Wiseman, Audree M. Chase-Mayoral, Thomas Janis, and Anu Sachdev. 2012. Community Colleges: Where Are They (Not)? International Perspectives on Education and Society 17 (2012), 3-18.
[38] Ali Zilouchian, Nancy Romance, and Hanqi Zhuang. 2022. A Transformative Project between Two-State Colleges and a-4-year Institution for Student Success in STEM. In ASEE Annual Conference Proceedings. doi:10.18260/1-2--41499
