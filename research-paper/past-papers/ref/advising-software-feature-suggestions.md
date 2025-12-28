Here is the requested Markdown file content. The Literature Review has been summarized as requested, while the Methodology, Results, and Discussion sections contain the verbatim text from the paper, cleaned of line breaks, PDF artifacts, and in-text academic citations (e.g., "(Smith, 2020)") to ensure the context is clear for AI processing.

---

# BibTeX Citation

```bibtex
@article{nguyen2024community,
  title={Community College Articulation Agreement Websites: Students' Suggestions for New Academic Advising Software Features},
  author={Nguyen, David Van and Doroudi, Shayan and Epstein, Daniel A.},
  journal={Community College Journal of Research and Practice},
  year={2024},
  publisher={Taylor \& Francis},
  doi={10.1080/10668926.2024.2356330}
}

```

# Paper Summary: Literature Review

**User Experience of Articulation Agreement Reports and Websites**
Students and academic advisors rely heavily on websites for transfer information, yet many 2-year and 4-year college websites contain missing, incomplete, outdated, or confusing information. In contrast, websites recognized for student success place transfer information prominently near the homepage and use various media forms.

Research indicates that most articulation agreements are written at a post-bachelor’s reading level, exceeding the comprehension level of many community college students. These agreements often use undefined administrative jargon and language that instills doubt about credit applicability. Furthermore, inconsistent formatting between universities makes cross-referencing difficult, with users finding Excel formats hard to read and preferring PDFs.

The fragmentation of information is also a barrier. Users find it easier to locate agreements when they are centralized on a single website (like ASSIST for California), whereas scattered agreements across individual institutional websites create difficulties.

**Academic-Advising-Related Prototypes**
Researchers have developed prototypes to assist with academic advising, though few focus specifically on community colleges. Existing prototypes for non-transfer students focus on recommending majors, courses, or optimal academic plans, as well as predicting workload and grades.

Tools for advisors include systems to identify at-risk students, determine course offerings, and offload tasks to chatbots. Specifically related to articulation agreements, some prototypes use semi-automation to reduce the workload of articulation officers by suggesting potential course equivalencies, allowing officers to focus on validating plausible suggestions rather than manual search.

# Methodology

**Overview**
We conducted a qualitative study to gather California community college transfer students' suggestions for new academic-advising-related software features for the ASSIST website. Our qualitative data consisted of open-ended survey data and semi-structured interviews. Before conducting the study, we pilot tested the study's survey and interview with three transfer students. We then revised the study based on the pilot test feedback.

**Participants**
We recruited 24 community college transfer students through the CSU and UC campuses' subreddit, which are online forums. The main participant eligibility requirements were (a) at least 18 years old and (b) current community college transfer student at a UC or CSU campus. The participant incentive was a $15 gift card. Furthermore, when provided with 5-point unipolar response options, students on average rated their prior knowledge of ASSIST as "very knowledgeable" (M=4.0, SD=0.7). During the results section of this paper, participants will be referred to as P1-P24.

**Procedure**
Research sessions were conducted through Zoom videoconference between November 2021 to December 2021. The scheduled length of the research session was 45 minutes. First, study participants completed an experimental task where they created an optimal academic plan, which is outside the scope of this paper. Then, participants completed the survey, which was administered via Qualtrics. Aside from demographic questions, there were three open-ended survey questions that are relevant to this specific paper. Two questions asked for suggestions to improve ASSIST and one question asked for concerns they had with ASSIST.

Finally, if the research session had time remaining, we then conducted semi-structured interviews with study participants to gather their software feature suggestions for ASSIST. 22 out of 24 study participants were interviewed. We told participants not to worry about real-world constraints such as feasibility or cost when making software feature suggestions. For each participant quote in the results section, we will designate whether the researcher or the participant initiated the conversation about the software feature topic.

**Analysis**
We used Otter.ai to obtain automated transcriptions of our interview audio. We then manually reviewed the Otter.ai transcripts to fix automated transcription mistakes. We also took a denaturalized approach to our transcripts. In other words, we removed false starts, repeated words or phrases, and filler words in order to improve clarity without changing the speaker's original meaning. We analyzed our qualitative data using the ATLAS.ti software. We specifically used structural coding to code the open-ended survey data and interview data. We then conducted thematic analysis on the codes. In other words, we coded interview and survey responses based on the software feature they represent. Then we categorized software feature codes into conceptually similar higher-level themes.

**Positionality**
We limit this brief discussion of positionality to just the lead author as he was the one responsible for collecting and analyzing the qualitative data. The lead author did not have a preexisting relationship with any study participants. The lead author was a California community college alumnus who has personal experience using ASSIST to prepare to transfer to UC and CSU campuses. To be transparent, the lead author had a preconception going into the study that the ASSIST website provides a poor user experience and needs improvement. Among other sources, he drew from his personal experiences when developing the interview guide. Furthermore, his positionality likely influenced how interviews were conducted and analyzed (e.g., an interviewer without personal experience with ASSIST may have asked more follow-up questions to clarify when interviewees use ASSIST-related terminology or talk about common ASSIST use cases).

# Results

We identified four themes around students' software feature suggestions for ASSIST: (a) features that automate laborious academic advising tasks, (b) features to reduce ambiguity with articulation agreements, (c) features to mitigate mistakes in term-by-term course planning, and (d) features to facilitate online advising from advisors and student peers.

## Features that Automate Laborious Academic Advising Tasks

When done manually, certain articulation-agreement-related tasks are too time-consuming that it (a) may not be possible for a community college advisor to complete within a 30-minute advising appointment or (b) may deter students from performing such tasks on their own. This theme has two software feature suggestions: (a) query other community colleges that offer the university course equivalent and (b) query university major programs that the student is close to completing.

**Query other community colleges that offer the university course equivalent**
A common articulation agreement pain point is that "the [student's community college] doesn't have courses that are equivalent" to a specific university major requirement, which the ASSIST report designates as "No Course Articulated". In other words, these students were unable to fulfill "all of the lower division [university major] requirements at [their] specific [community] college". Accordingly, students have the option of fulfilling university major requirements at community colleges other than their primary community college.

Currently, searching for a specific articulated course at other community colleges is a manual process. P21 said: "[I create a list of the community colleges in my area. And [then I] manually [retrieve] the agreements for each [community college in my list]. And then [I see] if any of them have [the specific] articulated course." Once the student finds the specific articulated course at another community college, they then need to check (a) if the course will be offered in the upcoming term and (b) if they are eligible to enroll.

Students suggested an automated feature where users can input a "[university] course that they need [community college course] equivalents for" and then ASSIST would output "all the courses from different [community colleges] that [articulate] to that [university] course". Furthermore, students suggested an option to "filter [equivalent community college courses by] if it's online, in person, hybrid". Furthermore, if the course has an in-person component then there should be an option to "sort [equivalent community college courses] by area" or distance.

**Query university major programs that the student is close to completing**
In order to speed up time-to-transfer, students suggested a feature to query university major programs that the student is close to completing. Assuming that the student is only interested in one specific major (e.g., biology) and not picky with the university they transfer to, then one potential use case is to sort all UC and CSU campuses by the percentage of completed major requirements for that one specific major.

In another use case, a student could query all the UC and CSU campuses for major requirement completion percentages for all possible majors or restrict it to a user-determined set of similar majors. For example, computer science, computer engineering, software engineering, electrical engineering, and data science are relatively similar. P23 said: "If you're [majoring in] CS, you could potentially go to [major in] math [instead], because there's a lot of overlap [in lower-division major requirements]. You could potentially have a feature where [ASSIST outputs] like, 'You've completed 50% of the major requirements for [UC Riverside] major B. But you've also completed 75% of [UC Riverside] major C.'"

## Features to Reduce Ambiguity with Articulation Agreements

This theme has four software feature suggestions: (a) consistently label major requirements as mandatory or recommended, (b) consistently publish annual ASSIST reports, (c) notification system for ASSIST report changes, and (d) track progress toward completing university transfer requirements.

**Consistently label major requirements as mandatory or recommended**
For context, major requirements on ASSIST reports can be mandatory or recommended. "Mandatory courses... has to be taken before transferring". On the other hand, "highly recommended [major requirements] just means... you could finish it up now [at community college], or you could... [finish it later after] you enter the university". While not mandated, students feel motivated to complete recommended major requirements during community college to become "a top applicant to get into the [university]".

ASSIST does not consistently label which major requirements are mandatory or recommended. For example, P16 said "I found it kind of difficult to tell which ones were required versus which ones were recommended." As such, students suggested consistent labeling of major requirements: "There should always be reminders on what is required vs what is recommended".

**Consistently publish annual ASSIST reports**
ASSIST reports are published every academic year. A common ASSIST pain point was that "some universities haven't updated [their ASSIST reports] in several years". When ASSIST reports aren't up to date, ASSIST "default[s]" to the most recently published report available. However, ASSIST does not provide assurances or any indication that the university is still following the default old report. Students described feeling "confus[ed]" and "uneasy" about possibility following "outdated information" that is no longer applicable.

P13 said that universities should still publish ASSIST reports annually even if there are no content changes in the report: "I understand that [major requirements within ASSIST reports] don't [change] every year... [If that is the case] they should just [publish the same report but] change the [2016] year [in the report] to the [current] year."

**Notification system for ASSIST report changes**
A similar but different pain point is that universities may revise already-published ASSIST reports. However, there is "no indication [within the ASSIST report] that this [report] was updated" and "ASSIST has no way of notifying a user" of report revisions. Due to ASSIST's nontransparent revisions, P23 felt compelled to manually check ASSIST reports for revisions: "I seen some of [the ASSIST reports] change. And so, I check[ed] it pretty frequently, like once or twice every few weeks just to make sure... I don't need a new course or... take a course that's no longer needed."

Students suggested a notification system where "if the school decides to change [the ASSIST report you are using, then] for your account to have a notification". P23 suggested that the notification or e-mail should also describe the revision: "a brief [description of] change[s] like '[community college] course A was changed to [community college] course B to articulate for [university] course C.'"

**Track progress towards completing university transfer requirements**
Community colleges typically have their own internal community-college-specific software for academic planning and degree audits. However, a California community college's internal software may not have the ability to track students' progress toward completing university major requirements. For example, P24 said that her community college's internal academic planning software just tracked "general transfer [requirements]" but it did not track the university's major requirements listed on ASSIST.

Similarly, ASSIST also does not track community college students' progress toward completing university major requirements: "there wasn't a way for me to verify on ASSIST like 'oh, I've already filled this requirement'". As such, students need to manually track their transfer progress. However, manual tracking introduces opportunities for human-error. As touched on in the prior quote, participants suggested a software feature that would explicitly designate "which [transfer] requirements you've already fulfilled and which classes you still have to take to transfer" based on the student's planned and completed community college courses.

## Features to Mitigate Mistakes in Term-by-Term Course Planning

Students suggested an academic planning feature for ASSIST where they can map out term-by-term what future courses they plan to take. In addition, students suggested three software features that would augment the academic planning feature: (a) list prerequisites for community college courses, (b) list past academic terms that a community college course was offered, and (c) nudge students to prioritize completing gateway classes earlier.

**List prerequisites for community college courses**
ASSIST currently "doesn't show prerequisites" on their articulation agreement reports. Consequently, some students will try to unsuccessfully register for a course without realizing that there are unmet prerequisites. As such, research participants suggested that the "ASSIST report could be improved by... listing pre reqs of [community college] classes", which would help "student[s] to factor in the prerequisite classes needed to take the course".

**List past academic terms that a community college course was offered**
ASSIST currently "doesn't tell [students] when this class is [typically] offered". This may cause issues because "sometimes a course may only be offered in fall semester but not in spring". Another ASSIST pain point is that articulation agreement reports still list dormant courses that the community college has not offered in years: "I would find it useful if courses that aren't typically offered at a [community] college aren't displayed [on ASSIST] because I don't want to choose [and plan to take] a [dormant] course that [is actually] not offered". Students suggested a feature that would allow them to "see what... semester [a course is typically offered]".

**Nudge students to prioritize completing gateway classes earlier**
Certain courses require many prerequisites that must be completed sequentially. We refer to this type of prerequisite sequence as gateway classes. If this student delays starting their math courses, then they will be delaying their time-to-transfer by at least 4 semesters. P23 states that some students may not know which courses to prioritize: "[Students] knew the courses they needed to take but they just got lost on when to take them. Like, what class is required for another class? Should I prioritize one or the other?"

As such, research participants suggested that ASSIST should help students prioritize gateway classes. For example, P23 said: "[ASSIST should be] prioritizing the ones that are earlier on in the [prerequisite] sequence. Maybe even having a note saying like, 'This course allows you to take course XYZ.... Prioritize taking this as soon as you're eligible."

## Features to Facilitate Online Advising from Advisors and Student Peers

This theme has two software feature suggestions: (a) one-on-one communication with advisors and (b) social features with student peers and advisors.

**One-on-one communication with advisors**
Several students suggested adding features on ASSIST for "communicating [privately] with your school counselors". Possible communication modes included a live "chat box", "asynchronous" messages, or a "Zoom [videoconference] call". In addition to answering questions about "major" requirements or "how to use this ASSIST stuff", some research participants suggested that advisors could also check the validity of students' academic plans online instead of during in-person meetings.

**Social features with student peers and advisors**
Several students suggested that ASSIST add social features such as discussion "forum[s]", "form[ing] groups of other students that also have the same goals", or "[ASSIST could have] like their own Rate My Professor where people who've taken the course can make comments about it". P20 speculated that students would be interested in social features: "community college students are always interested in how other students transferred, especially to big name schools."

P9 said having social features within ASSIST may resolve the limitations of current online websites: "There's websites like College Confidential and then Discord for your specific class. But there's not really a big [centralized] hub for those kind of [articulation-agreement-related social] interactions." Beyond student-to-student interactions, P9 suggested ASSIST could also have "social media type interactions between students and counselors." When asked directly, students said that they would find it helpful if community college advisors and transfer admissions officers had verified accounts to respond to forum posts.

# Discussion

We identified four themes around students' software feature suggestions for ASSIST: (a) features that automate laborious academic advising tasks, (b) features to reduce ambiguity with articulation agreements, (c) features to mitigate mistakes in term-by-term course planning, and (d) features to facilitate online advising from advisors and student peers.

Some of our study participants' software feature suggestions for articulation agreement websites are novel (e.g., notification system for articulation agreement report revisions and query university major programs that the student is close to completing) but many are not novel. Similar to our study, students and academic advisors in other studies have also suggested features to reduce ambiguity/confusion with articulation agreements. Moreover, students in Katsinas et al.'s (2016) evaluation similarly suggested implementing online discussion boards to Alabama's articulation agreement website. Moreover, researchers have already begun prototyping our study participants' software feature suggestions such as academic planning prototypes and prototypes that incorporate social features into academic advising.

More broadly, our study participants' software feature suggestions align with prior research that found articulation agreements can be difficult to interpret and are often out-of-date. Moreover, similar to our study participants, other research has found that students commonly enroll in multiple community colleges; among other reasons, students do this to access transferable/articulated courses not available at their primary community college. Lastly, our results align with prior research that suggest community college academic planning can be complex.

Yadamsuren et al.'s (2008) research suggests that different stakeholder groups may use community college websites in different ways and may have distinct needs. Our study participants were limited to transfer students. Accordingly, additional research is needed to gather user needs and ASSIST software feature suggestions from different stakeholder groups such as academic advisors, articulation officers, transfer admissions officers, and current community college students. Regarding students, user studies should consider purposefully sampling for marginalized student subgroups who have website accessibility needs (e.g., students with disabilities) or who experience transfer-related disparities (e.g., underrepresented racial/ethnic minorities).

In consultation with stakeholders, researchers should also determine the feasibility and prioritization of which new ASSIST software features to implement, if any. Researchers will also need to be mindful of feature creep, which refers to having too many software features that consequently make the software less usable. Furthermore, researchers and administrators should consider and design guardrails against unintended consequences of suggested ASSIST software features. For example, querying university major programs that the student is close to completing may incentivize students to pursue majors or universities that they are less interested in. Another example is students may unknowingly follow erroneous peer advice from discussion forums.

Even if ASSIST did not implement any new software features, there are still non-technology-related improvements that community colleges and universities can make. For example, our study participants discussed common mistakes in academic planning, which can delay students' time-to-transfer. Accordingly, community colleges can offer workshops or online tutorials explaining how academic plans need to account for course prerequisites, gateway courses, and the course offering schedule. On the university side, our study participants complained of the ambiguity with following outdated articulation agreements. As such, universities should include explicit language on their transfer admissions websites on how community college students should proceed when the university's articulation agreements are outdated. As a last example, some study participants were paranoid that universities would change the articulation agreements' university major requirements or community college course articulations. These changes could invalidate the community college courses that students already completed. When updating degree requirements, many universities include grandfather clauses that allow enrolled university students to follow the old degree requirements instead of the new requirements. Similarly, when updating courses in articulation agreements, universities should consider adding grandfather clauses for current community college students who already completed courses under the old articulation agreement.
