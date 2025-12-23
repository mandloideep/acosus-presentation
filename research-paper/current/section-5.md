## 5 Evaluation

To assess the usability and perceived value of the ACOSUS platform, we conducted a pilot study with transfer students at a public urban university. This section describes the study design (§5.1), evaluation instruments (§5.2), quantitative results (§5.3), qualitative findings (§5.4),

### 5.1 Study Design

#### Participants

Four transfer students (N=4) from Northeastern Illinois University participated in the study. Participants were recruited through email invitation and voluntarily enrolled after providing informed consent. All participants were active transfer students in computing-related majors. This evaluation was conducted during the foundation phase of the progressive learning pipeline (§3.2), when the system was actively collecting labeled observations to establish the initial training corpus. At this stage, no predictive model had yet been trained—the system's primary function was structured data collection rather than prediction generation. Participants completed the Factor and Target Survey instruments described in Sections 3.1 and 4.1, followed by a post-hoc feedback survey administered through Qualtrics. The study protocol received Institutional Review Board (IRB) approval prior to data collection.

### 5.2 Evaluation Instruments

The feedback survey was designed based on the Technology Acceptance Model (TAM) framework [Davis, 1989] to assess participants' perceptions of the data collection experience. The instrument comprised Likert-scale items (5-point scale) measuring Perceived Usefulness, Perceived Ease of Use, and Behavioral Intention, along with open-ended questions capturing qualitative feedback on interface difficulties, helpful features, missing capabilities, and redesign suggestions. Table 4 presents the constructs and example items.

**Table 4.** Feedback survey constructs and items.

| Construct                        | Example Item                                                                                               |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Perceived Usefulness (PU)**    | "Using this AI counseling system enables me to accomplish tasks more quickly than other advising methods." |
| **Perceived Ease of Use (PEOU)** | "Learning to operate this AI counseling system was easy for me."                                           |
| **Behavioral Intention**         | "How likely are you to continue using this system for academic planning?"                                  |

Open-ended questions captured qualitative feedback on interface difficulties, helpful features, missing capabilities, and redesign suggestions.

### 5.3 Quantitative Results

#### 5.3.1 TAM Construct Scores

Analysis of the TAM-based constructs revealed strong positive perceptions across all dimensions.

**Table 5.** Summary statistics for evaluation metrics (5-point Likert scale).

| Metric                       | Mean | SD   | Min | Max |
| ---------------------------- | ---- | ---- | --- | --- |
| Perceived Usefulness (PU)    | 4.46 | 0.85 | 3   | 5   |
| Perceived Ease of Use (PEOU) | 5.00 | 0.00 | 5   | 5   |
| Likelihood to Continue       | 4.75 | 0.50 | 4   | 5   |
| Likelihood to Recommend      | 4.25 | 1.50 | 2   | 5   |

![Figure 7. TAM construct scores showing Perceived Usefulness and Perceived Ease of Use.](../04-evaluation/figs/fig1_tam_metrics.png)

**Figure 7.** TAM construct scores. Perceived Ease of Use achieved a perfect score (M=5.00), while Perceived Usefulness showed strong agreement (M=4.46) with slightly more variance.

Perceived Ease of Use achieved a perfect mean score (M=5.00, SD=0.00), indicating that all participants found the system straightforward to learn and operate. Perceived Usefulness was rated highly (M=4.46, SD=0.85), though with greater variance reflecting individual differences in how participants valued the system's utility for their specific situations.

#### 5.3.2 Behavioral Intention

![Figure 10. Behavioral intention metrics showing likelihood to continue and recommend.](../04-evaluation/figs/fig4_behavioral_intention.png)

**Figure 10.** Behavioral intention. Likelihood to Continue (M=4.75) exceeded Likelihood to Recommend (M=4.25), with the latter showing greater variance.

Likelihood to Continue using the system was high (M=4.75, SD=0.50), suggesting strong personal adoption intent. Likelihood to Recommend showed more variance (M=4.25, SD=1.50), with one participant providing a lower rating (2/5). This discrepancy may reflect individual differences in social recommendation behavior rather than system satisfaction.

### 5.4 Qualitative Findings

Thematic analysis of open-ended responses revealed four primary themes.

![Figure 16. Qualitative theme distribution from open-ended responses.](../04-evaluation/figs/fig6_qualitative_themes.png)

**Figure 16.** Qualitative theme distribution. Usability and Satisfaction were the most frequently occurring themes (3 mentions each), followed by Efficiency and Personalization.

**Table 6.** Qualitative themes and representative responses.

| Theme               | Count | Representative Quote                                                                        |
| ------------------- | ----- | ------------------------------------------------------------------------------------------- |
| **Usability**       | 3     | "UI navigation is very user friendly"; "User interface was easy to understand and navigate" |
| **Satisfaction**    | 3     | "No feature was missing, experience was great"; "None, everything was clear"                |
| **Efficiency**      | 1     | "Faster and more compatible"                                                                |
| **Personalization** | 1     | "Make it tailored more towards individual users"                                            |

Thematic analysis of open-ended responses revealed four primary themes. Usability emerged most frequently, with participants consistently praising the interface design—one noted "UI navigation is very user friendly" while another described the system as "easy to understand and navigate," corroborating the quantitative PEOU results (M=5.00). Satisfaction was equally prominent; when asked about missing features or interface difficulties, participants responded with "No feature was missing, experience was great" and "None, everything was clear." One participant highlighted efficiency, noting the system was "faster and more compatible" than alternative advising methods, aligning with the Perceived Usefulness construct. Finally, one participant suggested greater personalization, recommending the system "make it tailored more towards individual users and their specific situation"—feedback consistent with the 75% preference for personalized advice shown in Figure 14. [Image] Figure 16. Qualitative theme distribution. Usability and Satisfaction were the most frequently occurring themes (3 mentions each), followed by Efficiency and Personalization.

---

_End of Section 5_
