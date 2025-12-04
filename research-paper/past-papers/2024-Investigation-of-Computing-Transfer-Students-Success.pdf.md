

# Investigation of Computing Transfer Students Success \*

Cheyenne Ty<sup>1</sup>, Kay Vargas<sup>1</sup>,  
Yun Wan<sup>4</sup>, Xiwei Wang<sup>5</sup>, Palvi Aggarwal<sup>3</sup>,  
Shebuti Rayana<sup>2</sup> and Sherrene Bogle<sup>1</sup>

<sup>1</sup>Dept. of Computer Science  
California State Polytechnic University Humboldt  
Arcata, CA 95521

{cjt101,kv111,sab30}@humboldt.edu

<sup>2</sup>Dept. of Mathematics, Computer & Information Sciences  
SUNY Old Westbury  
Old Westbury, NY 11568

rayanas@oldwestbury.edu

<sup>3</sup>Dept. of Computer and Information Sciences  
University of Texas At El Paso  
El Paso, TX 79968

paggarwal@utep.edu

<sup>4</sup>Dept. of Computer & Information Sciences  
University of Houston-Victoria  
Victoria, TX 77901

wany@uhv.edu

<sup>5</sup>Dept. of Computer Science  
Northeastern Illinois University  
Chicago, IL 60625

xwang9@neiu.edu

\*Copyright ©2024 by the Consortium for Computing Sciences in Colleges. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage, the CCSC copyright notice and the title of the publication and its date appear, and notice is given that copying is by permission of the Consortium for Computing Sciences in Colleges. To copy otherwise, or to republish, requires a fee and/or specific permission.

## Abstract

Community colleges provide accessibility in the pursuit of higher education, especially for women, underrepresented minority (URM) students, and first-generation college students (FGCS). This is especially true for majors within the STEM field, such as computer science (CS). However, there is a disconnect between the rates of enrollment at community colleges and the prevalence of these underrepresented demographics in 4-year institutions and the CS industry. The literature suggests that social and institutional factors affect transferring CS majors. This study aims to provide an empirical analysis on the different factors affecting the academic performance of transferring CS students. The study found that although all measured demographics impacted post-transfer GPA, the largest disparities are attributed to race/ethnicity, especially among URM students. These results will help inform an AI-driven counseling system that caters towards transfer students in CS.

## 1 Research Problem

Community colleges (CCs) allow higher education to be more accessible to underrepresented students, and transfer systems allow these students to continue their education at 4-year institutions. In particular, women, underrepresented minority (URM), and first-generation college students (FGCS) have been the focus in the impact that the transfer pathway has. Jackson et al. (2013) notes that in 2008, around 49% of female bachelor's and master's degree recipients in STEM attended a CC, with similar percentages reported for multiple URM ethnicities [11]. Additionally, FGCS are more likely to start upper education at a CC in the hopes of transferring [7]. Considering the accessibility that CCs provide women, URM students, and FGCS, supporting them through their post-transfer academics may help to decrease the disparities in representation within the STEM workforce.

In particular, these disparities can be seen in the field of computer science (CS). Between 2017 and 2019, 25% of people working in the U.S. CS industry were women [9]. This report also notes that only 7% and 8% of CS workers in the U.S. were Black or Hispanic, compared to these groups making up 11% and 17% of workers across all fields. Intersections between underrepresented groups may also heighten disparities; less than 10% of CS Bachelor's degrees were handed to URM women in 2006 [8], while first-generation women in CS often display a greater lack of support and self-efficacy during their undergraduate years [3]. To foster a workforce representative of the overall population, it's important to focus on factors that may influence the academic success of these three underrepresented groups: women, underrepresented minorities, and first-generation students. This includes unique barriers that may exist for un-

derrepresented transfer students, or the differences that are inherent between different transfer institutions. The current paper aims to provide a quantitative analysis of the impact that gender, URM, first-generation status, and transfer institution may have on the academic success of underrepresented transfer students in the CS field.

## 2 Review of Related Literature

### 2.1 Transfer Impact

Transfer students often face challenges that native (non-transfer) students in the institution do not. This can result in transfer students feeling less satisfied with their post-transfer institution, which is further amplified for students who are also both URM and FGCS [10]. One such challenge is the struggle to socially integrate into a post-transfer student body. Social circles among native students may already exist, making establishing social connections more challenging. Simultaneously, stigma within the native student body against transfer students' academic abilities may further reinforce feelings of social isolation and work to prevent integration [2]. These challenges can be further complicated by the intersectionality of transfer status and being underrepresented in their field, as is the case with women, URM students, and FGCS [2, 4, 16]. Transferring into an environment that lacks adequate support for social integration and academic goals for underrepresented students may hinder academic success in the post-transfer institution.

### 2.2 Institutional Differences

The different ways 4-year institutions treat transfer students may impact how well they integrate into the native student body. Institutions focusing on socialization among native, freshman students can have the unintended consequence of isolating transfer students [2, 4]. Opportunities for research and internships are also scarcer for transfer students, since faculty may not form as close of a relationship with transfer students compared to native students [18]. Conversely, providing unique transfer experiences or facilities catered towards underrepresented populations can help foster integration amongst the native population. Majka et al. (2021) details a boot-camp experience that helped develop communication and acceptance between transferring STEM students and native upperclassmen and faculty [13]. Spaces or facilities on campus that provide support for women, URM students, or FGCS can also help said students feel more integrated and reduce feelings of isolation in their new institution [14]. Hence, the programs and facilities that different 4-year institutions provide can have significant impact on the experience of underrepresented transfer students in both positive and negative regards.

### 2.3 Conceptual Framework

Wang's STEM Transfer Model [21] aims to identify the factors that influence upward STEM transfer into 4-year institutions. The model depicted in Figure 1, is also applicable to the persistence and performance of transfer students after successfully transferring. Wang's STEM Transfer Model was chosen instead of models like the Social Cognitive Theory (SCT) or Social Cognitive Career Theory (SCCT) since it provides a more specific framework for understanding the potential institutional, social, and personal factors in STEM transfer success. Its scope is also specific to CC transfer students, aligning with our research demographic. We focus on two aspects of the STEM Transfer Model: Person Inputs and Transfer Receptivity.

**Person Inputs** refers to characteristics such as demographics and previous academic success. Perceived stereotypes related to these characteristics can impact a student's self-efficacy within STEM, both before and after transferring. This can be seen in Cheryan et al. (2020), where perceived threats to one's identity may be enough to deter women from pursuing or continuing to pursue a CS degree [6].

**Transfer Receptivity** refers to the amount of support that an institution provides STEM students post-transfer. Institutional support can influence a transfer student in continuing their education and obtaining a Bachelor's degree, while a lack in institutional support can hinder or even halt this pursuit.

![](b7251436a2a3c0d1c00c3e935df2a8f5_img.jpg)

Figure 1 is a flowchart illustrating Wang's STEM Transfer Model, showing the progression of factors leading to upward STEM transfer and subsequent outcomes over time (indicated by a horizontal arrow).

The model starts with inputs and contextual factors:

- **Person Inputs** (Demographics; Prior academic abilities; Initial attitudes) and **Distal Contextual Factors** (Individual; Programs; Institutions) influence **STEM Momentum: STEM Course Taking and Learning Experiences**.
- **Proximal Contextual Factors** (STEM Transfer Capital (objective and perceived)) and **Transfer Receptivity at 4-Year Institutions** also influence **STEM Momentum: STEM Course Taking and Learning Experiences**.

**STEM Momentum: STEM Course Taking and Learning Experiences** influences:

- **Self-Efficacy in Math and Science & STEM Transfer**
- **Interest in STEM Transfer**
- **Outcome Expectations Regarding STEM Learning & Transfer**

**Self-Efficacy in Math and Science & STEM Transfer** and **Interest in STEM Transfer** influence **Intent to Transfer in STEM**.

**Outcome Expectations Regarding STEM Learning & Transfer** and **Intent to Transfer in STEM** influence **Upward STEM Transfer** (the central outcome).

**Upward STEM Transfer** leads to **Post-Transfer Learning in STEM**.

**Post-Transfer Learning in STEM** leads to **Post-Transfer Persistence & Aspirations in STEM**.

**Post-Transfer Persistence & Aspirations in STEM** leads to two final outcomes:

- **Baccalaureate and Career Attainment in STEM** (Solid box)
- **Alternative Educational and Occupational Attainment in STEM** (Dashed box)

The legend defines the box types:

- Upward STEM transfer outcome (Red box)
- Person inputs (Orange box)
- Contextual factors (Green box)
- Learning experiences in STEM (Yellow box)
- Motivational factors (Blue box)
- Post-transfer factors and outcomes in STEM (White box)
- Alternative and post-transfer outcomes (Dashed box)

Figure 1: The STEM Transfer Model, as seen in Wang 2016 [21]. The horizontal arrow throughout the entire diagram represents time.

## 3 Methodology

This study uses data derived from five different U.S. institutions: University of Houston-Victoria (Texas), Cal Poly Humboldt (California), Northeastern Illinois University (Illinois), University of Texas El Paso (Texas), and SUNY Old Westbury (New York). They are referred to as Institutions 1 through 5 within this paper, in the order of their appearance.

### 3.1 Integration of Framework

The data consists of CS students who have successfully transferred into a 4-year institution, aligning with the group of people the STEM Transfer Model is aimed at. The statistical analysis takes into account information such as gender, race/ethnicity, first-generation status, and earned transfer credits, reflecting Person Inputs prior to transferring. The institution a student transferred into is included as another variable in our models, highlighting potential institutional differences in Transfer Receptivity.

![Figure 2 displays two histograms showing student distribution. The left histogram, titled 'Distribution by Earned Credits', shows the number of students (Y-axis, 0 to 600) versus Earned Credits (X-axis, 0 to 175). The distribution is highly skewed right, peaking around 50-75 credits. The right histogram, titled 'Distribution by Transfer GPA', shows the number of students (Y-axis, 0 to 350) versus Transfer GPA (X-axis, 0.0 to 4.0). The distribution is also skewed right, peaking around 3.5-4.0 GPA.](b15e3860e0c96ed16ce77f032da6f107_img.jpg)

Figure 2 displays two histograms showing student distribution. The left histogram, titled 'Distribution by Earned Credits', shows the number of students (Y-axis, 0 to 600) versus Earned Credits (X-axis, 0 to 175). The distribution is highly skewed right, peaking around 50-75 credits. The right histogram, titled 'Distribution by Transfer GPA', shows the number of students (Y-axis, 0 to 350) versus Transfer GPA (X-axis, 0.0 to 4.0). The distribution is also skewed right, peaking around 3.5-4.0 GPA.

Figure 2: Student distribution based on earned transfer credits and transfer GPA. Five students with more than 175 earned credits are omitted in the first histogram, but are included in the final dataset.

### 3.2 Data Collection Method

The institutional data was obtained from the five institutions' respective registrar offices. The data was anonymized and filtered to only include CS and CS-related majors, with the most recent data for each student being kept. The comprehensive dataset was narrowed down to the following predictors: Transfer credits, gender, race/ethnicity, and post-transfer GPA. Only students who identified as either male

or female were kept in the final dataset. Gender is not a binary label; however, the data had a small number of non-binary students ( $N = 14$ ) and all of these students belonged to the same institution. Hence, to prevent bias we omitted them from this study. Additionally, post-transfer GPA refers to the GPA calculated using courses across all semesters and institutions.

Race/ethnicity was generalized into three categories: URM, non-URM, and Other. Non-URM consists of students who identified as only White or only Asian, since there is an overrepresentation of these ethnicities in CS [9]. URM consists of all other recorded races/ethnicities, which include African American, Hawaiian Pacific, Indigenous, and Hispanic/Latinx. Although the experiences of each URM group are unique in their own right, there is evidence suggesting that academic disparities exist that are consistent across races/ethnicities that fall under the URM category [1]. The URM category also includes undocumented students; although this is not a race or ethnicity, some institutions recorded it as such and the experiences that undocumented students face are very similar to the experiences that URM students face [14]. The Other category consists of students who either identified as being part of two or more races, of an unknown race/ethnicity, or students who put "Other" as their race/ethnicity. This grouping serves to represent the sample student population more accurately, accounting for the unique experiences of students who do not clearly fall under URM or non-URM. There also exists evidence that disparities URM students face may not be identical to the experience that students with unknown ethnicity have, as seen the large differences in attrition rates between URM and unknown ethnicity students in STEM [5]. The final dataset totals to 2056 students. Distributions of students by earned credits and transfer GPA can be seen in Figure 2, and a table of student demographics can be seen in Table 1.

| Dem.              | Inst. |     |      |     |     | Total |
|-------------------|-------|-----|------|-----|-----|-------|
|                   | 1     | 2   | 3    | 4   | 5   |       |
| Male              | 48    | 93  | 946  | 121 | 473 | 1681  |
| Female            | 14    | 19  | 208  | 27  | 107 | 375   |
| White             | 17    | 58  | 269  | 40  | 54  | 438   |
| Asian American    | 12    | 9   | 227  | 32  | 13  | 293   |
| African American  | 12    | 3   | 81   | 36  | 19  | 151   |
| Hispanic/Latinx   | 7     | 22  | 328  | 33  | 469 | 859   |
| Indigenous        | 0     | 1   | 2    | 2   | 1   | 6     |
| Hawaiian Pacific  | 0     | 0   | 6    | 0   | 0   | 6     |
| Undocumented      | 0     | 1   | 70   | 0   | 0   | 71    |
| Two or More Races | 10    | 12  | 22   | 1   | 8   | 53    |
| Unknown           | 4     | 6   | 149  | 4   | 9   | 172   |
| Other Ethnicity   | 0     | 0   | 0    | 0   | 7   | 7     |
| Total             | 62    | 112 | 1154 | 148 | 580 | 2056  |

Table 1: Student demographics across all five institutions.

### 3.3 Data Analysis

Two sets of models were created using this data. For Set 1, a factorial ANOVA and a least-squares linear regression were performed. Post-transfer GPA was the response variable for both models, and predictor variables were race/ethnicity, gender, and institution. The linear regression also includes earned transfer credits as a predictor variable to represent past academic success, which has been shown to predict STEM persistence [8, 7]. Both models use all 2056 students from the final dataset.

Set 2 is similar to the models from the first set, but also includes first-generation status. Data used for this analysis only comes from Institutions 1 through 3, since first-generation status was only recorded for these three institutions. Since approximately one third ( $N = 387$ ) of the data points report an unknown first-generation status, data imputation was performed using the k-nearest neighbors algorithm. A value of  $k = 1$  was used to preserve the binary categories of first-generation and continuing-generation. This subset of the data includes 1169 students.

Factorial ANOVAs were conducted through the Pingouin Python package [20], and least-squares linear regressions were performed using the ISLP and statsmodels packages [12, 17]. The k-nearest neighbors algorithm was conducted using the scikit-learn package [15]. Significance was evaluated at the  $p < 0.05$  level.

## 4 Results

### 4.1 Set 1

The ANOVA found that all main effects are significant on post-transfer GPA for the predictors of gender ( $F(1, 2027) = 8.152, p = 0.0043$ ), institution ( $F(4, 2027) = 205.937, p < 0.0005$ ), and race/ethnicity ( $F(2, 2027) = 13.488, p < 0.0005$ ). The interaction between institution and race/ethnicity was also significant,  $F(8, 2027) = 2.274, p = 0.0202$ . The main effect of institution accounts for 28.25% of the variance ( $\eta^2 = 0.2825$ ). The main effects of gender, race/ethnicity, and interaction between institution and race/ethnicity each account for less than 1% of the variance in GPA.

The conducted linear regression found that being a URM student significantly predicted post-transfer GPA ( $\beta = -0.2211, p < 0.0005$ ). The amount of earned transfer credits also significantly predicted GPA ( $\beta = 0.0035, p < 0.0005$ ). All other variables and interactions were deemed insignificant at the  $p < 0.05$  level.

Earned transfer credits were significant in the linear regression as expected, since previous academic success may predict STEM persistence and achievement [8, 7]. Although race/ethnicity accounted for 1% of the variance in the ANOVA, its statistical significance alongside URM status being significant in the linear regression imply that race/ethnicity impacts post-transfer GPA to a degree. Furthermore, a URM student's GPA is predicted to be 0.22 points lower than a non-URM student's GPA, with all other variables constant. Institution having a high effect on post-transfer GPA in the ANOVA may be attributed to the uneven sample sizes for each institution, as seen in Table 1. As outlined in Figure 2, earned credits has inherent bias since most transfer students will have around two years of credits before transferring,

| Variable                                 | DF | F       | p       | $\eta^2$ |
|------------------------------------------|----|---------|---------|----------|
| Institution                              | 2  | 9.921   | <0.0005 | 0.0091   |
| Ethnicity                                | 2  | 382.430 | <0.0005 | 0.3513   |
| Gender                                   | 1  | 6.607   | 0.0103  | 0.0030   |
| Institution * Ethnicity                  | 4  | 7.030   | <0.0005 | 0.0129   |
| Ethnicity * Gender                       | 2  | 69.858  | <0.0005 | 0.0642   |
| Institution * Ethnicity * Gender         | 4  | 8.079   | <0.0005 | 0.0148   |
| First Gen. * Ethnicity * Gender          | 2  | 11.398  | <0.0005 | 0.0105   |
| Institution * First Gen. * Eth. * Gender | 4  | 3.354   | 0.0097  | 0.0062   |

Table 2: Variables with significant effects for Set 2's ANOVA, evaluated at the  $p < 0.05$  level. The residual degrees of freedom was 1134.

especially among CC transfers. To better determine the effects of the post-transfer institution, more even sample sizes may be preferred. Additionally, pre-transfer GPA may provide a better measure of previous academic success, if it is available.

### 4.2 Set 2

With the inclusion of first-generation as a predictor, Table 2 shows all predictors that were deemed significant at the  $p < 0.05$  level. Of note is that the main effect of ethnicity accounts for 35.13% of the variance ( $\eta^2 = 0.3513$ ). Additionally, the interaction between race/ethnicity and gender yields a moderate effect size, accounting for 6.42% of the variance ( $\eta^2 = 0.0642$ ). Two interactions involving first-generation status were significant, but the main effect was not ( $F(1, 1134) = 0.104, p = 0.7468$ ).

The conducted linear regression found that being a URM student significantly predicted post-transfer GPA ( $\beta = -0.1802, p = 0.005$ ). Earned transfer credits were also significant in predicting post-transfer GPA ( $\beta = 0.0046, p < 0.0005$ ). The interactions that significantly predicted GPA were between URM ethnicity and first-generation status ( $\beta = -0.1424, p = 0.025$ ) and between gender, first-generation status, and URM ethnicity ( $\beta = -0.1789, p = 0.005$ ).

The results indicate that although first-generation status may not have a significant effect on post-transfer GPA by itself, its intersection with other underrepresented groups can amplify effects on post-transfer GPA. Race/ethnicity is of significance in this set of models as well, accounting for a high percentage of the variance in the ANOVA and URM status being significant in the linear regression. This consistency further indicates that race/ethnicity is of importance when considering the factors we have taken into account, though intersectionalities between underrepresented groups can still be worth noting.

## 5 Conclusion

This paper first reports on the effects that institution, gender, first-generation status, and race/ethnicity can have on transfer student success, and why certain groups

are underrepresented in the CS academic field. Using themes from Wang's STEM Transfer Model, two sets of ANOVA and linear regression models were created to analyze the effects that these demographics can have on post-transfer GPA. The results suggest that although every demographic analyzed had some effect on a student's post-transfer GPA, URM status had the greatest effect. Intersectionality between being URM and another underrepresented group further amplifies gaps in GPA. Based on these results, more support towards URM students in particular may bridge the largest gaps in GPA for the transfer student population. Future analyses using pre-transfer GPA or additional data on students' pre-transfer academic success may yield clearer results on the effects of each demographic. Ultimately, these results will help design an AI-driven counseling system catered towards transfer students and tailored to their specific needs [19]. We expect that this system will allow CS transfer students to realize their full potential within higher education.

## 6 Acknowledgments

This material is based upon work supported by the National Science Foundation under CNS-2219623. Any opinions, findings and conclusions, or recommendations expressed in this material are those of the authors, and do not necessarily reflect the views of the National Science Foundation.

## References

1. David J. Asai. "Race matters". In: *Cell* 181.4 (2020), pp. 754–757.
2. Peter Riley Bahr et al. "A review and critique of the literature on community college students' transition processes and outcomes in four-year institutions". In: *Higher Education: Handbook of Theory and Research: Volume 28* (2013), pp. 459–511.
3. Jennifer M. Blaney and Jane G. Stout. "Examining the relationship between introductory computing course experiences, self-efficacy, and belonging among first-generation college women". In: *Proceedings of the 2017 ACM SIGCSE technical symposium on computer science education*. 2017, pp. 69–74.
4. Jennifer M. Blaney et al. "Transfer Student Receptivity in Patriarchal STEM Contexts: Evidence of Gendered Transfer Student Stigma in Computer Science From a Mixed Methods Study". In: *Community College Review* (2024), p. 00915521231218233.
5. Marguerite Bonous-Hammarth. "Pathways to success: Affirming opportunities for science, mathematics, and engineering majors". In: *Journal of Negro Education* (2000), pp. 92–111.

[6] Sapna Cheryan et al. "Double isolation: Identity expression threat predicts greater gender disparities in computer science". In: *Self and Identity* 19.4 (2020), pp. 412–434.

[7] Sandra L. Dika and Mark M. D'Amico. "Early experiences and integration in the persistence of first-generation college students in STEM and non-STEM majors". In: *Journal of Research in Science Teaching* 53.3 (2016), pp. 368–383.

[8] Lorelle Espinosa. "Pipelines and pathways: Women of color in undergraduate STEM majors and the college experiences that contribute to persistence". In: *Harvard Educational Review* 81.2 (2011), pp. 209–241.

[9] Richard Fry, Brian Kennedy, and Cary Funk. "STEM jobs see uneven progress in increasing gender, racial and ethnic diversity". In: *Pew Research Center* 1 (2021).

[10] Melissa Hawthorne and Adena Young. "First-Generation Transfer Students' Perceptions: Implications for Retention and Success". In: *Journal of College Orientation, Transition, and Retention* 17.2 (2010).

[11] Dimitra Lynette Jackson, Soko S. Starobin, and Frankie Santos Lanaan. "The Shared Experiences: Facilitating Successful Transfer of Women and Underrepresented Minorities in STEM Fields." In: *New directions for higher education* 162 (2013), pp. 69–76.

[12] Gareth James et al. *An introduction to statistical learning: With applications in python*. Springer Nature, 2023.

[13] Elizabeth A. Majka, Merrilee F. Guenther, and Stacey L. Raimondi. "Science bootcamp goes virtual: a compressed, interdisciplinary online CURE promotes psychosocial gains in STEM transfer students". In: *Journal of Microbiology & Biology Education* 22.1 (2021), pp. 10–1128.

[14] Mayra Nuñez Martinez. "Cultivating transfer receptivity for undocumented and DACAmented Latina/o/x students at 4-year institutions." In: *Journal of Diversity in Higher Education* (2023).

[15] Fabian Pedregosa et al. "Scikit-learn: Machine Learning in Python". In: *Journal of Machine Learning Research* 12 (2011), pp. 2825–2830.

[16] Marie-Elena Reyes. "Unique challenges for women of color in STEM transferring from community colleges to universities". In: *Harvard Educational Review* 81.2 (2011), pp. 241–263.

[17] Skipper Seabold and Josef Perktold. "statsmodels: Econometric and statistical modeling with python". In: *9th Python in Science Conference*. 2010.

[18] Bertin Solis and Richard P. Durán. “Latinx community college students’ transition to a 4-year public research-intensive university”. In: *Journal of Hispanic Higher Education* 21.1 (2022), pp. 49–66.

[19] Northeastern Illinois University. *AI-driven Counseling System for Transfer Students*. URL: <https://cs.neiu.edu/acosus/Home.html>.

[20] Raphael Vallat. “Pingouin: statistics in Python”. In: *The Journal of Open Source Software* 3.31 (Nov. 2018), p. 1026.

[21] Xueli Wang. “Upward transfer in STEM fields of study: A new conceptual framework and survey instrument for institutional research”. In: *New Directions for Institutional Research* 2016.170 (2016), pp. 49–60.