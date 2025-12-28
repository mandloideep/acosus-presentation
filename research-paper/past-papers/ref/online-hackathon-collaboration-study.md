Here is the Markdown file you requested. It includes the BibTeX citation, the summary, and the transcribed content of the paper, including data tables, formatted for optimal use as an AI reference context.

---

# Research Paper Reference: Online Hackathon Collaboration Study

## 1. BibTeX Citation

```bibtex
@article{schulten2022collaboration,
  title={How do participants collaborate during an online hackathon? An empirical, quantitative study of communication traces},
  author={Schulten, Cleo and Nolte, Alexander and Spikol, Daniel and Chounta, Irene-Angelica},
  journal={Frontiers in Computer Science},
  volume={4},
  pages={983164},
  year={2022},
  doi={10.3389/fcomp.2022.983164}
}

```

## 2. Summary

**Paper Overview**
This paper investigates how teams communicate and collaborate in an online setting. The authors analyzed archival data (Slack messages) from a 48-hour online hackathon focused on crisis response technology, which took place in April 2020. The dataset included 253 channels and over 14,000 messages.

**Research Objectives**
The study answers three main questions:

1. How teams use the official communication platform (Slack) provided by organizers.
2. What communication patterns exist within teams (specifically looking at symmetry/balance of contribution).
3. What external tools are mentioned and utilized by participants.

**Key Findings**

- **Scaffolding & Milestones:** Team communication is heavily influenced by "scaffolding" (structure) provided by organizers. There are significant spikes in messaging activity around official "checkpoints" and deadlines.
- **Platform Usage:** The official platform (Slack) was primarily used for organizational purposes—connecting with mentors and officials—rather than deep collaborative work. Intra-team channels had low message volumes, suggesting active work happened elsewhere.
- **Communication Asymmetry:** Communication within team channels was highly unbalanced. Often, a single team member dominated the channel, likely acting as a liaison to mentors or organizers.
- **External Tools:** Participants frequently mentioned external tools, with Zoom being the most common, followed by Facebook and YouTube. However, mentioning a tool did not statistically change the volume of messages immediately before or after the mention.

**Conclusion**
The authors conclude that while official channels are vital for administration and milestone tracking, they do not capture the full extent of team collaboration. Active collaboration often shifts to external synchronous tools (like Zoom), leaving only "traces" or administrative chatter on the official platform.

---

## 3. Paper Content Transcription

### Abstract

"We conducted an archival analysis of communication traces of teams during a 48-h event. Our findings indicate that teams scaffold their communication around the design of an event, influenced by milestones set by the organizers. The officially selected communication platform's main use was to organize the event and the teams and to facilitate contact between participants and hackathon officials."

### 1. Introduction & Motivation

"Most studies on hackathons rely on observations and/or post-event interviews as their source of information. This bears several limitations related to potential interpretation bias, scale, and timing."

"To address this gap, we propose a data-informed approach utilizing communication traces (for example, chat messages) of hackathon teams. Our focus is on understanding how teams communicate during an event."

**Research Questions:**

- **RQ1:** "How do team members use the official communication tool provided by the hackathon organizers?"

- **RQ2:** "What patterns can we identify in the communication activity of team members?"

- **RQ3:** "What communication tools—other than the official communication tool—are mentioned, and to what extent?"

### 2. Background

"While scaffolding during in-person events can be flexible, online events require a more rigid structure. This structure commonly revolves around communication channels that are set up by hackathon organizers and that often include different channels for asynchronous and synchronous communication."

"Recent work in the context of online hackathons has, however, revealed that teams often use different tools than the ones provided by event organizers for their internal communication."

### 3. Empirical Method

#### 3.1 Hackathon Setting

"The hackathon we studied took place online in April 2020... It focused on developing ideas for technology use in crisis response."

- **Tools:** "The organizers used Slack, Facebook live, Zoom, and YouTube for this event."

- **Slack Usage:** "Slack was used as a workspace to facilitate communication with event officials and participants."

#### 3.2 Data Description

"After filtering, the dataset consisted of 253 channels with 1,212 users and 14,324 messages."

**User Roles:**
"The 'participant' role describes users who participate in the hackathon in a nonofficial capacity... The 'organizer' role is reserved for users who organized the hackathon event as a whole." "Project manager, lead mentor, and support mentor were official roles in supervising and organizing their assigned teams; they were also responsible for running the checkpoints during the hackathon."

**Table 1: User Data Distribution**

(Transcribed from )

| Role            | Number of Users (N) | Total Messages | Mean (SD)         | Median [Min, Max] |
| --------------- | ------------------- | -------------- | ----------------- | ----------------- |
| Lead mentor     | 7                   | 364            | 52.00 (24.93)     | 50.00 [28, 87]    |
| Mentor          | 8                   | 409            | 51.12 (60.24)     | 26.00 [2, 164]    |
| Organizer       | 2                   | 168            | 84.00 (31.11)     | 84.00 [62, 106]   |
| Participant     | 1,188               | 11,332         | 9.53 (24.65)      | 3.00 [1, 450]     |
| Project Manager | 5                   | 1,784          | 356.80 (86.13)    | 383.00 [265, 462] |
| Support Mentor  | 2                   | 267            | 133.50 (122.32)   | 133.50 [47, 220]  |
| **Overall**     | **1,212**           | **14,324**     | **11.81 (34.73)** | **3.00 [1, 462]** |

#### 3.3 Channel Types

"Additionally, we manually classified the Slack channels according to their main purpose. Out of the 253 channels, 228 were team channels, and 25 were general-purpose channels."

- **Team Channels:** Set up for each team to support team communication and mentorship.

- **General-Purpose Channels:** Facilitated communication between hackathon officials and participants (e.g., helpdesks, intros, announcements).

**Table 2: Channel Data**

(Transcribed from )

| Metric                      | General Purpose (N=25) | Team Channel (N=228) | Overall (N=253) |
| --------------------------- | ---------------------- | -------------------- | --------------- |
| **Number of Messages**      | 5,125                  | 9,199                | 14,324          |
| Mean (SD)                   | 205.00 (217.69)        | 40.34 (79.11)        | 56.61 (112.14)  |
| Median [Min, Max]           | 151 [6, 1076]          | 21.000 [5, 709]      | 23 [5, 1076]    |
| **Messages (no chat-join)** | 4,484                  | 7,713                | 12,197          |
| Mean (SD)                   | 179.36 (211.78)        | 33.82 (78.57)        | 48.20 (108.29)  |
| Median [Min, Max]           | 131 [3, 1058]          | 15.000 [3, 700]      | 16 [3, 1058]    |
| **Users per channel**       |                        |                      |                 |
| Mean (SD)                   | 60.20 (48.37)          | 6.47 (2.50)          | 11.78 (22.05)   |
| Median [Min, Max]           | 54 [3, 256]            | 6.000 [2, 14]        | 7 [2, 256]      |

### 4. Findings

#### 4.1 Teams' Communication through Slack (RQ1)

"In general-purpose channels, on average 179 messages were sent (SD = 211.79) and in team channels on average 34 messages were sent (SD = 78.58). This low average number of messages in team channels... indicates a large number of channels with few messages, which could be because of teams dropping out of the hackathon as well as because of alternative tools being used."

"Around the checkpoints, we saw that the number of messages increased, especially in the general-purpose channels."

**Table 3: Channel Data (High Activity Subsets)**

(Transcribed from )

| Metric                 | 3rd Quartile Channels (N=5) | Top 10 Team Channels (N=10) | Top 5 Gen. Purpose (N=5) | Overall (N=20)  |
| ---------------------- | --------------------------- | --------------------------- | ------------------------ | --------------- |
| **Messages**           | 218                         | 3,444                       | 2,662                    | 6,324           |
| Mean (SD)              | 43.60 (1.14)                | 344.40 (201.53)             | 532.40 (305.59)          | 316.20 (266.78) |
| Median                 | 44                          | 271.00                      | 420                      | 271.00          |
| **Messages (no join)** | 184                         | 3,363                       | 2,441                    | 5,988           |
| Mean (SD)              | 36.80 (3.49)                | 336.30 (201.41)             | 488.20 (319.15)          | 299.40 (262.50) |
| Median                 | 39                          | 262.50                      | 357                      | 262.50          |
| **Users per channel**  |                             |                             |                          |                 |
| Mean (SD)              | 6.80 (3.19)                 | 8.00 (2.78)                 | 112.80 (80.92)           | 33.90 (59.74)   |

"Our results showed that the 10 team channels with the most messages demonstrated a similar pattern to the general-purpose channels: messaging activity decreased after the first and third checkpoints... while it increased toward the second checkpoint and the submission deadline."

#### 4.2 Communication Patterns (RQ2)

"The Gini coefficient is a measure of symmetry of a distribution... In our case, we used it to measure how symmetrical or balanced the communication was in terms of message count." "The Gini coefficients suggest that conversations in team channels are imbalanced regardless of who participates in these conversations (that is, team members only or team members and other users, such as mentors)." "We found that there were 52 team channels where only one participant wrote messages conversing with non-participants like mentors, project managers, etc."

#### 4.3 Other Communication Tools (RQ3)

"In total, Zoom was mentioned (n = 647) almost as many times as all other tools combined. YouTube and Facebook were next with 209 and 208 mentions, respectively, followed by Slack (n = 123) and Google (n = 81)."

"We found no significant difference (p = 0.382) between the average amount of messages before (M = 2.05, SD = 4.68) and after tool mentions (M = 2.03, SD = 3.92)."

**Table 4: Tool Mentions**

(Transcribed from )

| Tool          | Gen. Purpose Channels (5,125 msgs) | Team Channels (9,199 msgs) | Overall (14,324 msgs) |
| ------------- | ---------------------------------- | -------------------------- | --------------------- |
| **Zoom**      | 281 (5.5%)                         | 366 (4.0%)                 | 647 (4.5%)            |
| **YouTube**   | 123 (2.4%)                         | 86 (0.9%)                  | 209 (1.5%)            |
| **Facebook**  | 112 (2.2%)                         | 96 (1.0%)                  | 208 (1.5%)            |
| **Slack**     | 0 (0%)                             | 123 (0.9%)                 | 123 (0.9%)            |
| **Google**    | 37 (0.7%)                          | 44 (0.5%)                  | 81 (0.6%)             |
| **Hangout**   | 0 (0%)                             | 1 (0.0%)                   | 1 (0.0%)              |
| **Instagram** | 14 (0.3%)                          | 0 (0%)                     | 14 (0.1%)             |
| **Skype**     | 37 (0.7%)                          | 13 (0.3%)                  | 50 (0.3%)             |
| **Telegram**  | 0 (0%)                             | 2 (0.0%)                   | 2 (0.0%)              |
| **Trello**    | 1 (0.0%)                           | 7 (0.0%)                   | 8 (0.1%)              |
| **Twitter**   | 0 (0%)                             | 18 (0.1%)                  | 18 (0.1%)             |
| **WhatsApp**  | 0 (0%)                             | 12 (0.1%)                  | 12 (0.1%)             |
| **All Tools** | 618                                | 707                        | 1325                  |

### 5. Discussion

"When we look at the analysis of the official team channels (RQ1), we see that they are often not utilized as the primary form of communication between the teams. These Slack channels contain limited amounts of chats between participants related to collaborative work."

"However, the official communication tool, Slack, served as the primary platform for the event and the activity in the general-purpose channels suggests that team members use the official communication tool for organizational purposes."

"To understand what patterns can be identified in the team members' communication activities (RQ2) we see an increase in messages around hackathon checkpoints. This increase in activity around milestones is a pattern that has previously been reported in research."

"Hackathon participants mention other communication tools during their Slack discussions, and one could argue that this could indicate that they are switching communication channels (RQ3)... However, these tool mentions do not appear to impact the number of messages significantly."

### 6. Conclusion

"Our findings indicate that active teams use the communication tool provided by the organizers. Analyzing the communication during an event might thus allow organizers to spot inactive teams and provide support."

"Our findings indicate—in line with related work (Powell et al., 2021; Mendes et al., 2022)—that even with a complete dataset from the communication tool provided by the organizers of a hackathon, the investigation of intra-team communication and interaction is complicated because teams use different communication tools."
