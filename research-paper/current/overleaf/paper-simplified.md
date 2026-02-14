# ACOSUS Paper — Simplified Language Reference

> This document mirrors the structure of `main-v2.tex`. For each section it provides:
> 1. **AI patterns spotted** — phrases that sound machine-generated
> 2. **Word swaps** — heavy words → plain alternatives
> 3. **Simplified version** — the section rewritten in plain English
> 4. **Flow notes** — suggestions for more natural ordering or transitions

---

## Abstract

### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "face unique challenges that traditional advising systems fail to address" | Classic AI framing: problem → solution setup that's too tidy |
| "limited visibility into pre-transfer trajectories" | Unnecessarily abstract; no human says "trajectories" for "course histories" |
| "predictive models calibrated on native student populations" | Correct but stiff — could just say "built for non-transfer students" |
| "introduces two architectural innovations" | "Architectural innovations" is a very AI-inflated way to describe what these are |
| "treats data scarcity as a fundamental design constraint rather than a limitation to overcome" | This is a nice idea but the phrasing is overworked — too many abstract nouns |
| "validated the data collection workflow" | Passive + abstract. Who validated it? Students did. |
| "with participants rating both Perceived Ease of Use and Perceived Usefulness highly" | Clunky noun stacking |

### Word swaps

| Original | Simpler |
|---|---|
| "fragmented information across institutions" | "scattered records across schools" |
| "limited visibility into pre-transfer trajectories" | "little access to students' earlier coursework" |
| "architectural innovations" | "design choices" or "key design decisions" |
| "dual-survey architecture" | "two-survey setup" (keep "dual-survey architecture" as a defined term, but introduce it plainly) |
| "progressive learning framework" | "step-by-step learning approach" (again, keep as term but introduce clearly) |
| "treats data scarcity as a fundamental design constraint" | "works around having little data from the start" |
| "validated the data collection workflow" | "tested whether the survey process works" |

### Simplified version

> Transfer students — especially those from underrepresented groups in computing — run into problems that regular advising tools were not built to handle. Their records are scattered across schools, receiving universities know little about their earlier coursework, and most prediction models were built for students who started as freshmen. We built ACOSUS (AI-driven counseling system for transfer students), an advising platform made specifically for this group. The system has two key design decisions: first, a two-survey setup that keeps outcome measurement separate from data collection while giving advisors a single, combined view of each student; and second, a step-by-step learning approach that works around having little data from the start instead of treating it as something to fix later. In a pilot test with transfer students at a public urban university, we confirmed that the survey process works smoothly — participants found the system both easy to use and useful. The system is now live and gathering data so we can evaluate its predictions in the future.
>
> **Keywords:** transfer students, intelligent advising, machine learning, higher education, student success prediction.

### Flow notes

- The abstract tries to do too much in a single breath. Consider splitting into: (1) the problem (2 sentences), (2) what we built (2 sentences), (3) results (1–2 sentences), (4) current status (1 sentence).
- "Introduces two architectural innovations" oversells — just describe what the system does and let the reader decide if it's innovative.

---

## Section 1: Introduction

### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "an alternative pathway to baccalaureate attainment has gained prominence" | Nobody talks like this. "More students are starting at community colleges" is the idea. |
| "a substantial share of students now begin their post-secondary careers" | "Post-secondary careers" is a roundabout way to say "college education" |
| "the proportion even higher in computing and other STEM majors and among first-generation, low-income, and racially minoritized learners" | Overloaded list crammed into one clause |
| "offers an affordable on-ramp to bachelor's-level credentials" | "On-ramp to credentials" is jargon-on-jargon |
| "navigate opaque articulation agreements, uneven credit recognition, and limited visibility" | Triple abstraction pile-up |
| "contend simultaneously with structural barriers, financial constraints, and feelings of isolation" | Another triple pile-up — a hallmark of AI writing |
| "Persistence and timely graduation are therefore central concerns" | Stiff topic sentence; sounds like a textbook |
| "transient decline in GPA and sense of belonging" | "Transient decline" is unnecessarily formal |
| "paint an incomplete picture" | Cliche that AI models love |
| "Effective advising is widely regarded as the linchpin of transfer-student success" | "Linchpin" is one of those words AI overuses |
| "A more holistic, data-rich approach...is urgently needed" | Classic AI closer — "urgently needed" to set up the solution |
| "To address this gap, we designed and evaluated" | Very standard AI transition |
| "Our contributions are as follows" | Every AI paper uses this exact phrase |

### Word swaps

| Original | Simpler |
|---|---|
| "baccalaureate attainment" | "earning a bachelor's degree" |
| "gained prominence" | "become more common" |
| "post-secondary careers" | "college education" |
| "racially minoritized learners" | "students of color" or "underrepresented racial groups" |
| "affordable on-ramp" | "cheaper starting point" or "affordable entry point" |
| "opaque articulation agreements" | "unclear transfer credit rules" |
| "contend simultaneously with" | "deal with" |
| "transient decline" | "temporary dip" or "short-term drop" |
| "central concerns" | "major worries" or "key issues" |
| "paint an incomplete picture" | "don't tell the whole story" or "miss important parts" |
| "widely regarded as the linchpin" | "one of the most important factors" |
| "holistic, data-rich approach" | "broader approach that uses more kinds of data" |
| "urgently needed" | "overdue" or just "needed" |
| "To address this gap" | "To fill this gap" or "With this in mind" |

### Simplified version

> More and more students are starting at community colleges and later transferring to four-year universities to finish their degrees. National studies estimate that over a third of all undergraduates take this route [cite], and the share is even higher among STEM majors, first-generation students, low-income students, and students of color [cite]. While the community college path offers a cheaper way into a bachelor's degree [cite], it creates real coordination problems for both the sending and receiving schools [cite]. Advisors at the four-year school have to work with unclear transfer credit rules, inconsistent credit acceptance, and little knowledge of what the student did before arriving [cite]. For students from groups that are already underrepresented in STEM, these challenges pile on top of financial stress and the feeling of not belonging in their new environment [cite].
>
> Keeping transfer students enrolled and graduating on time is a major concern. These students are more likely than students who started as freshmen to experience "transfer shock" — a temporary dip in GPA and sense of belonging during their first two semesters [cite]. They also drop out at higher rates. Researchers have found that certain measurable factors — cumulative GPA, number of credits accepted, test scores, distance between schools, and financial aid — correlate with whether students stay and graduate [cite]. But these numbers alone miss a lot [cite]. Interview-based studies keep showing that social support, faculty mentorship, and campus involvement (like research opportunities or hackathons) also matter a great deal, and these are hard to capture in standard university databases [cite].
>
> Good advising is one of the most important factors in whether transfer students succeed [cite]. Students want clear, timely, personalized guidance — but advisors at many schools carry such heavy caseloads that they can't dig into each student's background and goals [cite]. The dashboards advisors currently use mostly just show registrar data and early-warning flags designed for freshmen-entry students. They rarely include a student's pre-transfer history, credit transfer details, or the kinds of information students share in conversations about their decision-making [cite]. As a result, prediction models can get things wrong and widen existing inequities [cite]. There is a clear need for a broader approach — one that combines numbers with what transfer students actually experience [cite].
>
> To fill this gap, we designed and tested an intelligent advising system that combines academic records with social, financial, and experiential data collected before and after transfer. Our contributions:
>
> 1. We built an advising platform specifically for transfer students that combines standard academic records with information students provide about their own backgrounds, creating a single longitudinal profile for each student.
> 2. We designed a two-survey setup that keeps outcome measurement (what we're trying to predict) separate from data collection (what we use to predict it). This gives advisors structured, consistent student profiles through a single dashboard.
> 3. We built a modular prediction system with extensive configuration options. The design is algorithm-agnostic — any compatible method can be plugged into each stage — so researchers can test different approaches on their own student populations. Configuration options for survey linkage, phase transitions, and hyperparameters allow customization without changing code.
> 4. We tested the platform with transfer students, who gave feedback on their experience. Results show the system streamlines self-advising and is seen as trustworthy, actionable, and supportive of equity.
>
> The rest of the paper is organized as follows. Section 2 reviews related work on transfer student success and intelligent advising. Section 3 describes our system design, methodology, and implementation. Section 4 reports results from our pilot study. Section 5 concludes and outlines future directions.

### Flow notes

- The first paragraph crams too many citations and population subgroups into one run. Consider: sentence 1 = the trend, sentence 2 = how common it is (with citation), sentence 3 = why it matters for STEM specifically, sentence 4 = the coordination problem. Right now sentences 1–3 are fused.
- "Persistence and timely graduation are therefore central concerns" is a stiff transition. Just say "Keeping these students enrolled and on track to graduate is a major concern."
- The contributions list reads better as shorter bullets. The original contribution #3 is a 3-sentence paragraph pretending to be a bullet point — break it up or shorten it.
- "The remainder of the paper is organized as follows" is fine for a journal paper but could be shortened to "The rest of the paper covers..." without loss.

---

## Section 2: Literature Review

### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "can be grouped into two complementary strands" | AI loves categorizing literature into "strands" |
| "frame upward transfer as a function of 'person inputs'...and 'transfer receptivity,' a campus-level construct encompassing" | Dense academic jargon stacked inside a single sentence |
| "Empirical validation across STEM programs shows that" | Stiff transition — just say "Studies across STEM programs show..." |
| "adds texture to this portrait" | Metaphor mixing (texture + portrait) — very AI |
| "converges on the notion of" | "Converges on the notion" is unnecessarily ornate |
| "a related but distinct challenge compounds the technology gap" | Double abstraction before the reader knows what you're talking about |
| "Paradoxically, this scarcity stems not from a shortage of transfer students but from systemic information fragmentation across institutional boundaries" | This is a good insight buried under heavy language |
| "the rich contextual understanding that community college advisors accumulate over semesters of interaction rarely transfers" | Nice wordplay but the sentence is too long |
| "Drawing on prior quantitative and qualitative insights, we engineer an integrated advising platform" | "Engineer" as a verb for building software is AI-inflated |

### Word swaps

| Original | Simpler |
|---|---|
| "complementary strands" | "two related areas" |
| "frame upward transfer as a function of" | "describe transfer success in terms of" |
| "campus-level construct encompassing" | "campus-wide idea that includes" |
| "Empirical validation" | "Studies" or "Research" |
| "adds texture to this portrait" | "fills in more detail" |
| "converges on the notion of" | "points to" or "centers on" |
| "compounds the technology gap" | "makes the technology problem worse" |
| "systemic information fragmentation across institutional boundaries" | "records being split across different schools" |
| "Drawing on prior quantitative and qualitative insights" | "Building on earlier findings" |
| "we engineer an integrated advising platform" | "we built an advising platform" |
| "mitigates transfer shock" | "reduces transfer shock" or "eases transfer shock" |
| "ever-shifting articulation rules" | "constantly changing transfer credit rules" |

### Simplified version

> Research on transfer student outcomes falls into two related areas [cite]. The first looks at the personal and academic traits that shape a student's transfer experience. The second examines what schools do — especially through advising — to support (or fail to support) these students.
>
> Early models, like Ty et al.'s use of Social-Cognitive Career Theory, describe transfer success in terms of "person inputs" (things like socioeconomic status and self-confidence) and "transfer receptivity" — how welcoming and well-organized the receiving school is [cite]. Studies across STEM programs show that students' self-confidence and goal-setting tend to improve after they move to a four-year school, even as they face unfamiliar academic expectations [cite]. Factor analysis studies confirm that finances, school reputation, distance from home, and family expectations all play into the initial decision to transfer [cite]. Regression analyses link post-transfer GPA to race/ethnicity and first-generation status [cite]. Topic modeling of open-ended survey and social media responses fills in more detail — students express frustration with how credits are evaluated, long commutes, and limited chances to get involved on campus [cite].
>
> Advising research centers on "transfer student capital" — the knowledge and connections students build as they move between schools [cite]. When official advising falls short, many students turn to Reddit, Discord, or peer forums for help with financial aid, housing, and course selection [cite]. Interviews show that relationship-based advising eases transfer shock and helps students feel like they belong [cite]. But advisors themselves say they struggle to keep up with constantly changing transfer credit rules, especially with large caseloads [cite].
>
> Some technology tools have started to appear, but most were designed for students who entered as freshmen [cite]. Typical prediction tools pull from registrar data and LMS clickstreams. They rarely account for transfer-specific factors like how quickly credits were completed or whether students feel they belong at their new school [cite]. Researchers warn that models trained on one type of student population can produce biased results that hurt underrepresented students [cite]. Only a few prototype systems explicitly focus on transfer students, and these are still small-scale [cite].
>
> Given this, researchers have called for mixed-methods approaches that combine quantitative data with richer qualitative information [cite]. Topic modeling is one promising approach: it can pull out recurring themes from written survey responses to surface challenges that don't show up in numbers. Deng et al. used Revealed Causal Mapping on narrative responses to trace how social media use shapes academic experiences for first-generation students [cite]. Thiry et al. used mixed-methods case studies to develop support strategies for STEM transfer students [cite]. But few studies have fed these kinds of unstructured findings back into automated advising tools.
>
> A separate problem makes the technology gap even worse: data scarcity. Ironically, this isn't because there are too few transfer students — it's because their records are split across different schools [cite]. When students transfer, only a thin slice of their academic record moves with them: credits earned, GPA, and course equivalencies. The deeper understanding that community college advisors build up over time — knowledge about family obligations, financial stress, career goals, and early warning signs — rarely makes it to the new school [cite]. University advisors have to reconstruct this picture through time-consuming intake conversations. And machine learning systems face a cold-start problem: each university has to build its training data from scratch, one student at a time [cite]. The very factors that best predict success are exactly the ones that get lost in the transfer process [cite].
>
> Our work addresses these gaps from a systems-design perspective. Building on earlier findings from both quantitative and qualitative research, we built an advising platform that combines standard academic records (transfer credits, GPA, enrollment status) with data students provide about their own experiences. A lightweight, interpretable classifier uses this combined data to generate personalized success predictions. A dashboard delivers these predictions directly to students. Early feedback from the pilot suggests the system fills a real gap in transfer student support and could serve as a scalable model for other schools.

### Flow notes

- The lit review reads like a list of studies rather than a story. Consider grouping more tightly: (1) what predicts transfer success, (2) what role advising plays, (3) what technology exists, (4) what's missing. The current version roughly does this but the transitions between groups are weak.
- The "data scarcity" paragraph starting with "A related but distinct challenge" is one of the best paragraphs in the paper — the insight about information fragmentation is genuinely useful. But it's buried at the end of the lit review. Consider moving it earlier or making it more prominent, since it directly motivates the system design.
- The closing paragraph ("The present work answers these gaps from a systems perspective") is doing double duty as both a lit review conclusion and a system preview. Consider cutting it shorter — the Introduction already set up the contributions.

---

## Section 3: Methodology and Implementation

### AI patterns spotted (section intro)

| Original phrase | Why it sounds AI-generated |
|---|---|
| "This section presents the ACOSUS platform's design and implementation" | Fine but could be shorter |

### Simplified version (section intro)

> This section covers how we designed and built the ACOSUS platform. We start with the overall architecture (3.1), then describe how we collect data through two types of surveys (3.2), explain how survey responses are processed (3.3), walk through the progressive learning framework for small-data settings (3.4), and finish with the configuration options that let other institutions adapt the system (3.5).

---

### 3.1 System Architecture

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "implements a four-layer architecture that separates concerns across presentation, business logic, data persistence, and predictive modeling" | Dense noun pile; "separates concerns across" is developer jargon in an academic paper |
| "This separation enables independent scaling of each layer and supports the system's dual purpose" | Classic AI justification pattern — state the design, immediately explain why it's good |
| "role-specific interfaces through a web-based application" | Roundabout way to say "different web pages for different users" |
| "enforcing the progressive learning framework's phase transitions" | Heavy nominalization |
| "schema-flexible design accommodates researcher-defined survey instruments without requiring database migrations" | Accurate but dense |
| "Asynchronous job queues prevent long-running training tasks from blocking prediction requests" | Fine technically, but could be plainer |

#### Word swaps

| Original | Simpler |
|---|---|
| "separates concerns across" | "splits responsibilities between" |
| "enables independent scaling" | "lets each part grow on its own" |
| "role-specific interfaces" | "different views for different users" |
| "orchestrates application workflows" | "manages how the app works" |
| "schema-flexible design" | "flexible database structure" |
| "accommodates researcher-defined survey instruments" | "handles custom surveys that researchers create" |

#### Simplified version

> ACOSUS uses a four-layer design that splits responsibilities between the user interface, application logic, data storage, and prediction models (Figure 1). This separation lets each part be updated or scaled independently.
>
> The **Presentation Layer** provides different web views for different users. Students can fill out surveys, see predictions, and leave feedback. Advisors see a dashboard that pulls together each student's profile — organized by the same categories as the surveys — so they don't have to hunt through multiple sources. Administrators can set up surveys, start model training, and check system stats.
>
> The **Business Logic Layer** manages the application's workflows and controls when the system moves between phases of the progressive learning framework. It makes sure students see the right interface based on where the system currently is — data collection only during the early phase, predictions plus feedback in later phases.
>
> The **Data Layer** stores users, surveys, responses, and model information in a flexible document database. Because the structure is flexible, researchers can change survey questions without needing to update the database schema.
>
> The **Model Layer** runs as a separate service that handles the heavy lifting: normalizing data, making predictions across all three pipeline stages, and training models. Long training jobs run in background queues so they don't slow down prediction requests. Model versioning ensures that new models only go live after they prove they perform better on real student data.

#### Flow notes

- This section is clean. The four-layer breakdown is straightforward.
- Consider dropping "This separation enables independent scaling of each layer and supports the system's dual purpose" — it's a justification that reads like filler. The separation speaks for itself.

---

### 3.2 Dual-Survey Architecture

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "Before proceeding, we clarify terminology used throughout this paper" | Stiff transition |
| "ACOSUS frames transfer student success prediction as a supervised learning problem where the goal is to predict an outcome from a set of input variables" | Overexplains what supervised learning is |
| "The variables most predictive of transfer success...are seldom captured in standard institutional systems" | Good point, AI-style packaging |
| "Furthermore, academic advisors lack unified access to the information they need; prior research documents that advisors spend significant time gathering student data from disparate sources" | Run-on with semicolon — a very AI pattern |
| "ACOSUS addresses both challenges through a Dual-Survey Architecture that simultaneously feeds AI models and consolidates advisor-facing information" | "Simultaneously feeds...and consolidates" — too many verbs doing too much |
| "operationalizes 'success' as representing the student's likelihood" | "Operationalizes" is jargon |
| "enabling systematic capture of transfer-specific variables" | Nominalized verb chain |

#### Word swaps

| Original | Simpler |
|---|---|
| "Before proceeding" | "First" or "Before we go further" |
| "we clarify terminology" | "we define some key terms" |
| "frames...as a supervised learning problem" | "sets up...as a prediction problem" |
| "seldom captured" | "rarely collected" or "usually missing" |
| "disparate sources" | "different places" or "scattered sources" |
| "operationalizes" | "defines" or "puts into practice" |
| "enabling systematic capture" | "allowing consistent collection" |
| "consolidates advisor-facing information" | "brings together the information advisors need" |
| "explicit associations" | "direct links" |

#### Simplified version

> First, we define some key terms used throughout this paper. ACOSUS sets up transfer student success prediction as a standard prediction problem: given a set of input variables, predict an outcome. We use these terms:
>
> - **Target Survey / Outcome (Y):** The survey that measures what we want to predict — how likely a student is to succeed academically. In ML terms, this is the label.
> - **Factor Survey / Predictors (X):** The surveys that collect the information we use to make predictions — academic background, finances, logistics. In ML terms, these are the features.
> - **Constructs:** The underlying concepts (like self-efficacy or institutional commitment) that we measure through survey questions. A single Factor Survey may cover several constructs.
>
> The factors that best predict transfer success — how credits transfer, how severe "transfer shock" is, whether students feel they belong, and whether they're financially stable — are usually missing from standard university systems [cite]. On top of that, advisors don't have easy access to the information they need. Research shows that advisors spend a lot of time gathering data from different places before they can give useful advice [cite]. ACOSUS tackles both problems with a two-survey design that feeds the AI model and brings together the information advisors need in one place.
>
> Previous research has found that transfer student success depends on multiple factors: academic confidence, commitment to the school, social connections, and clear career goals [cite]. Our own earlier factor analysis identified clusters of variables — academic confidence, time management, financial stability, and support networks — that separate successful transfer students from those who struggle [cite]. Building on this, ACOSUS defines "success" as the student's overall likelihood of doing well across these areas, and "factors" as the things that affect that likelihood.
>
> The system uses two types of surveys to collect this data separately. **Target Surveys** (measuring Y) capture success in one of two ways: (1) a single question where students rate their success on a 0–100 scale, or (2) a multi-question instrument covering constructs like academic confidence, commitment, time management, and career motivation, which get combined into one score. **Factor Surveys** (measuring X) collect the predictor variables, organized into groups: academic background (pre-transfer GPA, transferred credits, test scores), financial situation (scholarships, family support, employment), logistics (commute distance, work hours), and interests/experience (career goals, prior subject experience).
>
> Beyond feeding the AI model, Factor Surveys solve a practical problem for advisors: they make sure every transfer student answers the same questions. This means advisors can compare across students, and no important risk factor gets missed. Responses show up immediately in the advisor dashboard — no need to search through emails, notes, or schedule follow-up meetings.
>
> The system also supports flexible study designs through **survey linkage** — direct links between Target and Factor Surveys. This lets researchers compare different predictor sets, adapt to new factors, and customize for different student groups without changing the underlying system. Section 3.5 explains how this works in practice.

#### Flow notes

- The terminology box ("Before proceeding, we clarify terminology") is necessary but feels like an interruption. Consider moving it to the very start of Section 3 before the architecture subsection, or even making it a brief footnote/sidebar.
- The paragraph that starts "Prior research on transfer student success has identified multiple dimensions..." largely repeats points already made in the Introduction and Literature Review. Consider cutting it down to one sentence that references the earlier discussion.
- The "Beyond their role as predictor vectors for the AI model" paragraph is the most valuable one — it explains why advisors care. Lead with it or give it more weight.

---

### 3.3 Survey Data Processing

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "synthesize information collected from students into feature vectors suitable for predictive modeling" | Dense nominalization — "turn student answers into numbers the model can use" |
| "Each survey question serves as a proxy for an underlying success factor identified in prior research" | Fine content, stiff delivery |
| "operationalizes this differential importance through priority scores" | "Operationalizes this differential importance" is peak AI |
| "These priorities derive from empirical evidence (effect sizes and factor loadings from prior research) and can be dynamically adjusted" | Packing too much into one sentence |
| "A logistic calibration curve is then applied to prevent overconfident predictions at the extremes" | Passive voice + jargon |
| "This type-aware processing ensures that the semantic meaning of responses is preserved during feature engineering" | "Semantic meaning is preserved during feature engineering" — AI loves this phrasing |

#### Word swaps

| Original | Simpler |
|---|---|
| "synthesize information...into feature vectors suitable for" | "turn survey answers into numbers that the model can use" |
| "serves as a proxy for" | "stands in for" or "represents" |
| "operationalizes this differential importance" | "handles the fact that some factors matter more" |
| "derive from empirical evidence" | "come from research findings" |
| "dynamically adjusted" | "updated over time" |
| "logistic calibration curve is then applied" | "we then apply a logistic curve" |
| "prevent overconfident predictions at the extremes" | "keep predictions from being too extreme" |
| "semantic meaning of responses is preserved" | "the meaning behind each answer is kept intact" |

#### Simplified version

> The surveys described in Section 3.2 turn student answers into numbers that the prediction model can use. Each question stands in for a success factor identified in earlier research — for example, our factor analysis mapped observable things (like scholarship status or commute distance) to underlying concepts (like financial stability or school commitment) that predict outcomes [cite].
>
> **Priority Weighting**
>
> Not all factors matter equally. Research consistently shows that some variables — academic self-confidence, financial stability, institutional fit — predict success more strongly than others [cite]. ACOSUS handles this through **priority scores**: each question gets a weight based on how important that factor is, drawing on effect sizes and factor loadings from prior studies. These weights can be updated as advisors learn which factors matter most at their school.
>
> The weighted score calculation is straightforward. For a survey with n questions, where question i has priority p_i and the student picks an option worth w_i^selected out of a maximum w_i^max:
>
> S = sum( (w_i^selected / w_i^max) * p_i ) / sum( p_i )     [Equation 1]
>
> This gives a score between 0 and 1 that accounts for both how good the student's answers are and how important each question is. We then apply a logistic curve to keep predictions from being too extreme at the high and low ends.
>
> These priority weights have another benefit: they can serve as starting points (priors) when we move to more advanced probabilistic models. Features with higher priority get more initial influence, which the model can then adjust based on real data. This connects expert knowledge to learned parameters in a principled way.
>
> **Data Type Handling**
>
> Survey answers come in different types, and each type needs to be converted to numbers differently. The key distinction is between **ordinal** data (answers with a natural order, like "Not confident" < "Somewhat confident" < "Very confident") and **cardinal** data (categories without ranking, like career field choices).
>
> | Data Type | Example | How it's normalized |
> |---|---|---|
> | Ordinal | GPA range: "3.0–3.5" | Direct option weight (e.g., 8/10) |
> | Cardinal | Career: "Industry/Corporate" | Equal weight or domain-specific mapping |
> | Continuous | SAT score: 1250 | Min-max scaling: (x - min) / (max - min) |
>
> This type-aware approach makes sure ordinal answers stay ordered, categorical answers aren't falsely ranked, and continuous values are properly scaled.

#### Flow notes

- This section is relatively clean and technical. The main issue is the opener ("synthesize information collected from students into feature vectors suitable for predictive modeling") which is a mouthful. Just say what it does plainly.
- The "additional advantage" paragraph about Bayesian priors feels tacked on. It's a forward-looking point that could go in 3.4 or 3.5 where you discuss the progressive pipeline and configuration.

---

### 3.4 Progressive Learning Framework

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "addresses data scarcity constraints through a framework that treats them not as limitations to overcome but as fundamental design constraints to embrace" | This sentence is doing philosophical work that sounds very AI — "not X but Y" framing |
| "This immediate utility transforms the cold-start period from a limitation into a productive data-gathering phase" | Same pattern again — "transforms X from Y into Z" |
| "the system's predictive intelligence matures through a three-stage progressive pipeline" | "Predictive intelligence matures" personifies the system |
| "lightweight predictive methods generate initial predictions—this stage emphasizes data quality over prediction sophistication" | "Emphasizes X over Y" — very formulaic |
| "generative techniques that synthesize additional training observations" | Jargon-heavy |
| "This algorithm-agnostic design serves two purposes in the small-data context" | Purpose-listing pattern |
| "positioning ACOSUS not as a fixed implementation but as a generalizable architecture" | Another "not X but Y" — this pattern repeats throughout the paper |

#### Word swaps

| Original | Simpler |
|---|---|
| "treats them not as limitations to overcome but as fundamental design constraints to embrace" | "is built to work with limited data from the start" |
| "delivers value from the very first student enrollment" | "is useful from day one" |
| "predictive intelligence matures" | "prediction ability improves" |
| "lightweight predictive methods" | "simple prediction methods" |
| "emphasizes data quality over prediction sophistication" | "focuses on getting good data rather than fancy predictions" |
| "generative techniques that synthesize additional training observations" | "methods that create realistic fake data to train on" |
| "algorithm-agnostic design" | "flexible design (works with any algorithm)" |
| "positioning ACOSUS not as a fixed implementation but as a generalizable architecture" | "making ACOSUS a flexible framework, not a one-off tool" |

#### Simplified version

> ACOSUS is built to work with limited data from the start. Rather than waiting until enough data exists to make predictions, the system is useful from day one — even before any model is trained, advisors get structured student profiles through the standardized surveys. This means the early period when data is still being collected isn't wasted time; it's a productive phase where advisors already benefit.
>
> **Three-Stage Pipeline**
>
> As more student data comes in, the system's prediction ability improves through three stages:
>
> **Stage 1: Foundation.** The system focuses on collecting high-quality labeled data through the survey instruments. Once enough observations exist, simple prediction methods generate initial results. At this stage, the priority is getting good data, not making sophisticated predictions.
>
> **Stage 2: Augmentation.** As the dataset grows, the system uses generative methods to create realistic synthetic data that expands the training set. These methods learn the patterns in the real data and produce additional samples that preserve the same statistical properties. This gives the system enough data to support more advanced algorithms.
>
> **Stage 3: Refinement.** With a larger training set (real + synthetic), the system switches to advanced nonlinear models that can capture complex relationships between features and outcomes.
>
> The framework is modular: each stage is a swappable component. Any prediction method can serve Stage 1, any data generation technique can serve Stage 2, and any deep learning model can serve Stage 3. This flexibility serves two purposes. First, researchers can compare different algorithms to find what works best for their specific students, rather than being locked into one approach. Second, as new methods emerge in few-shot learning, data augmentation, or neural network design, they can be plugged in without redesigning the system. This makes ACOSUS a flexible framework, not a one-off tool.

#### Flow notes

- The opening paragraph is the strongest one in this subsection — the point about advisors benefiting even before predictions exist is compelling and practical. Good.
- The three stages could use concrete examples. "Lightweight predictive methods" — like what? Even a parenthetical "(e.g., k-nearest neighbors)" would help. Same for augmentation: "(e.g., SMOTE or variational autoencoders)."
- The modularity paragraph at the end repeats the same "not X but Y" pattern that appears throughout the paper. Vary the sentence structure.

---

### 3.5 Configuration Flexibility

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "The algorithm-agnostic design described in Section 3.4 manifests in a configuration system" | "Manifests in" is heavy |
| "Four categories of configuration support this flexibility" | Enumeration setup — very AI |
| "operationalized through explicit linkage configurations" | "Operationalized" again |
| "This linkage mechanism provides several research advantages" | Classic list intro |
| "without disrupting existing data collection or invalidating historical comparisons" | Double negative clause |
| "Default thresholds reflect statistical considerations for each algorithm family" | Dense |
| "This modularity enables empirical comparison" | Repeats the same point from 3.4 |

#### Word swaps

| Original | Simpler |
|---|---|
| "manifests in" | "is built into" or "shows up as" |
| "operationalized through" | "set up through" or "implemented through" |
| "explicit linkage configurations" | "direct link settings" |
| "without disrupting existing data collection" | "without breaking ongoing data collection" |
| "reflect statistical considerations" | "are based on statistical rules of thumb" |
| "conform to the expected interface" | "follow the expected format" or "fit the required pattern" |

#### Simplified version

> The flexible design from Section 3.4 is built into a configuration system that lets researchers adapt the framework without touching the core code. There are four areas of configuration:
>
> **Survey Linkage.** The two-survey setup from Section 3.2 works through link settings: a single Target Survey (outcome Y) can be connected to multiple Factor Surveys (predictor sets X1, X2, X3). This lets researchers test which combination of predictors best predicts success. Specific benefits:
>
> 1. **Comparing predictor sets** — deploy different Factor Surveys to the same group of students and compare which one predicts better.
> 2. **Adding new factors over time** — as research identifies new predictors (e.g., post-pandemic stressors, new measures of transfer shock), new Factor Surveys can be added without breaking ongoing data collection or invalidating past comparisons.
> 3. **Customizing by program** — different departments can use program-specific Factor Surveys (e.g., technical preparation for CS majors) while sharing a common outcome measure.
>
> The other three areas cover the progressive learning pipeline:
>
> **Phase Transition Thresholds.** Administrators set how many observations trigger the jump from one pipeline stage to the next. Defaults are based on statistical rules of thumb for each type of algorithm, but schools can adjust based on their enrollment patterns and how they want to balance prediction availability vs. model reliability.
>
> **Algorithm Selection.** Each pipeline stage accepts any algorithm that fits the required pattern. Stage 1 needs a method that works with very little data (any similarity-based or instance-based method). Stage 2 needs a generative model that can create realistic synthetic data. Stage 3 accepts any supervised learning model capable of handling nonlinear relationships. This lets researchers compare alternatives on their own data rather than being stuck with defaults.
>
> **Hyperparameter Tuning.** Within each algorithm, settings like distance metrics, neighbor counts, generation multipliers, network architectures, and training schedules are all exposed as configuration options. The system logs every configuration choice alongside performance metrics, so researchers can systematically compare settings.
>
> This configuration approach supports the system's goal of being a general-purpose framework. As new methods appear — better few-shot techniques, smarter augmentation, novel architectures — schools can adopt them by updating settings rather than rewriting the system.

#### Flow notes

- This section is mostly fine. The main issue is repetition: the "as methodological advances emerge" closing has appeared in nearly identical form in 3.4 and now here. Pick one place for this point.
- The numbered list under Survey Linkage is clear and useful — this is one of the better-structured parts of the paper.

---

## Section 4: Evaluation

### AI patterns spotted (section intro)

| Original phrase | Why it sounds AI-generated |
|---|---|
| "To assess the usability and perceived value of the ACOSUS platform, we conducted a pilot study" | Standard but stiff |

### Simplified version (section intro)

> To test whether the ACOSUS platform is usable and useful, we ran a pilot study with transfer students at a public urban university. This section covers the study design (4.1), what we measured (4.2), quantitative results (4.3), and qualitative findings (4.4).

---

### 4.1 Study Design

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "Four transfer students (N=4) from Northeastern Illinois University participated in the study" | Fine, standard |
| "This evaluation was conducted during the foundation phase of the progressive learning pipeline" | Overly formal reference back |
| "the system's primary function was structured data collection rather than prediction generation" | "Prediction generation" is jargon |
| "The study protocol received the University's Institutional Review Board (IRB) approval prior to data collection" | Standard but could be shorter |

#### Word swaps

| Original | Simpler |
|---|---|
| "voluntarily enrolled after providing informed consent" | "agreed to participate after giving informed consent" |
| "the system's primary function was structured data collection rather than prediction generation" | "the system was mainly collecting data, not yet making predictions" |
| "administered through Qualtrics" | "given through Qualtrics" |

#### Simplified version

> Four transfer students (N=4) from Northeastern Illinois University took part in the study. They were recruited by email and agreed to participate after giving informed consent. All were active transfer students in computing-related majors. This test happened during the early (foundation) phase of the progressive learning pipeline, when the system was still collecting its first labeled data points and had not yet trained a prediction model — so the system was mainly collecting data, not making predictions. Participants filled out both the Factor and Target Surveys described in Sections 3.2 and 3.3, then completed a feedback survey through Qualtrics. The study was approved by the university's IRB before data collection began.

#### Flow notes

- Consider noting more prominently that N=4 is small and this is a pilot. The current version mentions it but doesn't frame expectations.

---

### 4.2 Evaluation Instruments

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "The feedback survey was designed based on the Technology Acceptance Model (TAM) framework to assess participants' perceptions of the data collection experience" | Long but acceptable for methods section |
| "The instruments are mainly comprised of Likert-scale items (5-point scale) measuring" | "Mainly comprised of" is wordy |

#### Simplified version

> The feedback survey followed the Technology Acceptance Model (TAM) framework [cite]. It included 5-point Likert-scale questions measuring three things: Perceived Usefulness, Perceived Ease of Use, and Behavioral Intention. It also included open-ended questions about interface difficulties, helpful features, missing capabilities, and suggestions for improvement. Table 5 shows the constructs and sample items.

---

### 4.3 Quantitative Results

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "Analysis of the TAM-based constructs revealed strong positive perceptions across all dimensions" | "Revealed strong positive perceptions across all dimensions" — very AI summary language |
| "indicating that all participants found the system straightforward to learn and operate" | "Straightforward to learn and operate" is stiff |
| "reflecting individual differences in how participants valued the system's utility for their specific situations" | Long-winded explanation |
| "This discrepancy may reflect individual differences in social recommendation behavior rather than system satisfaction" | Speculative hedging that feels AI-generated |

#### Word swaps

| Original | Simpler |
|---|---|
| "revealed strong positive perceptions across all dimensions" | "showed positive results across the board" |
| "straightforward to learn and operate" | "easy to learn and use" |
| "reflecting individual differences in how participants valued" | "since participants had different views on" |
| "social recommendation behavior" | "willingness to recommend things to others" |

#### Simplified version

> **TAM Construct Scores**
>
> Results across all TAM constructs were positive.
>
> | Metric | Mean | SD | Min | Max |
> |---|---|---|---|---|
> | Perceived Usefulness (PU) | 4.46 | 0.85 | 3 | 5 |
> | Perceived Ease of Use (PEOU) | 5.00 | 0.00 | 5 | 5 |
> | Likelihood to Continue | 4.75 | 0.50 | 4 | 5 |
> | Likelihood to Recommend | 4.25 | 1.50 | 2 | 5 |
>
> Perceived Ease of Use got a perfect score (M=5.00, SD=0.00) — every participant found the system easy to learn and use. Perceived Usefulness was also high (M=4.46, SD=0.85), though with more variation since participants had different views on how useful the system was for their particular situation.
>
> **Behavioral Intention**
>
> Likelihood to Continue using the system was high (M=4.75, SD=0.50), showing strong personal interest in continued use. Likelihood to Recommend had more spread (M=4.25, SD=1.50), with one participant giving a 2/5. This difference likely reflects that person's general reluctance to recommend things rather than dissatisfaction with the system.

#### Flow notes

- The quantitative results section is short and clear. The main AI tell is the opening sentence. Just report the numbers and let them speak.

---

### 4.4 Qualitative Findings

#### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "Thematic analysis of open-ended responses revealed four primary themes" | Classic AI intro to qualitative results |
| "emerged most frequently" | Standard but stiff |
| "corroborating the quantitative PEOU results" | "Corroborating" is heavy for what's a simple confirmation |

#### Word swaps

| Original | Simpler |
|---|---|
| "Thematic analysis of open-ended responses revealed" | "Open-ended responses fell into" or "We found four themes in the open-ended responses" |
| "emerged most frequently" | "came up most often" |
| "corroborating" | "matching" or "consistent with" |
| "aligning with the Perceived Usefulness construct" | "consistent with the high usefulness scores" |

#### Simplified version

> We found four themes in the open-ended responses.
>
> | Theme | Count | Representative Quote |
> |---|---|---|
> | Usability | 3 | "UI navigation is very user friendly"; "User interface was easy to understand and navigate" |
> | Satisfaction | 3 | "No feature was missing, experience was great"; "None, everything was clear" |
> | Efficiency | 1 | "Faster and more compatible" |
> | Personalization | 1 | "Make it tailored more towards individual users" |
>
> **Usability** came up most often. Participants consistently praised the interface — one said "UI navigation is very user friendly" and another called the system "easy to understand and navigate," matching the perfect ease-of-use scores. **Satisfaction** was equally common; when asked about missing features or difficulties, participants said "No feature was missing, experience was great" and "None, everything was clear." One participant noted **efficiency**, saying the system was "faster and more compatible" than other advising methods, consistent with the high usefulness scores. One participant asked for more **personalization**, suggesting the system "make it tailored more towards individual users and their specific situation."

---

## Section 5: Conclusion and Future Work

### AI patterns spotted

| Original phrase | Why it sounds AI-generated |
|---|---|
| "addressing fragmented information landscapes and data scarcity in departmental-level advising" | "Information landscapes" is abstract |
| "demonstrating strong usability—Perceived Ease of Use achieved a perfect score, indicating the survey workflow balances comprehensiveness with accessibility" | The em-dash sentence tries to pack too much in |
| "The modular architecture, with its emphasis on immediate advisor utility during data collection and configuration-based adaptation, offers a generalizable template" | "Generalizable template" is AI-speak |
| "deploying intelligent systems in small-data educational contexts" | Jargon pile-up at the very end |

#### Word swaps

| Original | Simpler |
|---|---|
| "fragmented information landscapes" | "scattered information" |
| "balances comprehensiveness with accessibility" | "is thorough but still easy to use" |
| "generalizable template" | "reusable model" or "starting point" |
| "deploying intelligent systems in small-data educational contexts" | "building smart tools for schools that don't have much data" |

### Simplified version

> This paper presented ACOSUS, an AI-driven advising system built for transfer students in computing majors. It addresses two core problems: scattered information across schools and limited data for prediction at the department level.
>
> Our main contributions: (1) a two-survey design that keeps outcome measurement separate from data collection while giving advisors consistent, structured student profiles through a single dashboard; (2) a modular prediction system with an algorithm-agnostic design that lets researchers test different approaches for their own student populations, with configuration options for survey linkage, phase transitions, and hyperparameters so schools can adapt the system without changing code; and (3) pilot validation with transfer students (N=4) showing strong usability — Perceived Ease of Use got a perfect score, meaning the surveys are thorough but still easy to complete.
>
> The system is currently live and collecting data during the foundation phase, but the prediction components still need to be evaluated as the dataset grows. The pilot's small sample (N=4), single institution, voluntary participation, and snapshot-in-time design limit what we can generalize from it. Tracking long-term outcomes was beyond this study's scope.
>
> Looking ahead, several directions are open: (1) evaluating the full progressive pipeline once enough data is collected, including accuracy, calibration, and fairness checks; (2) deploying at multiple institutions — community colleges and regional universities — to test whether the approach generalizes; (3) adding advisor feedback loops to improve predictions and evaluating how useful the dashboard is in practice; and (4) exploring LLM integration for personalized explanations and actionable recommendations.
>
> The modular design, with its focus on being useful to advisors from day one and its configuration-based customization, offers a reusable starting point for building smart advising tools at schools that don't have much data yet.

### Flow notes

- The conclusion is compact and covers the right ground.
- Consider being more direct about limitations. "The pilot's small sample size (N=4)" is a real constraint — own it more plainly rather than listing it in a parenthetical cascade.
- The final sentence tries to be a memorable closer but is weighed down by the parenthetical clause. Shorter version: "The system's modular design and focus on immediate advisor utility make it a reusable starting point for other schools facing similar data challenges."

---

## Global Observations

### Recurring AI patterns across the whole paper

1. **"Not X but Y" framing** — appears at least 5 times ("not as limitations to overcome but as fundamental design constraints to embrace," "not as a fixed implementation but as a generalizable architecture," etc.). This is a signature AI rhetorical move. Use it once at most.

2. **Triple noun/adjective pile-ups** — "structural barriers, financial constraints, and feelings of isolation"; "academic background, financial circumstances, and logistical constraints"; "clear, timely, and individualized guidance." These three-item lists appear in almost every paragraph. Vary the pattern — sometimes use two items, sometimes use a different sentence structure.

3. **"Operationalizes"** — appears 3 times. Replace with "defines," "implements," or "puts into practice."

4. **Passive constructions hiding the actor** — "was designed," "was conducted," "is then applied." Academic writing allows some passive voice, but too much makes it sound AI-generated. Use "we" more.

5. **Semicolon-joined independent clauses** — the paper uses semicolons to glue together sentences that should either be two sentences or be rewritten to flow naturally. AI models overuse this pattern.

6. **"This [noun] enables/ensures/supports" sentence pattern** — nearly every paragraph has a sentence structured as "This [design/architecture/separation/approach] [enables/ensures/supports] [some benefit]." Vary the sentence openers.

7. **Hedging phrases** — "it is worth noting," "it should be emphasized," "may reflect individual differences" — these are padding. Cut them or rewrite.

8. **Repeating the same point in different words** — the paper says "algorithm-agnostic" and explains what it means at least 3 separate times (3.4, 3.5, and the conclusion). Say it once clearly and reference it after that.

### Most commonly overused words to search-and-replace

| Overused word | Count (approx.) | Alternatives |
|---|---|---|
| "operationalize(s)" | 3 | define, implement, put into practice |
| "encompassing" | 2 | including, covering |
| "leverage(d)" | 2 | use(d), draw on |
| "facilitate" | 1 | help, enable, allow |
| "utilize" | 0 (good!) | — |
| "holistic" | 1 | broad, comprehensive, well-rounded |
| "paradigm" | 0 (good!) | — |
| "robust" | 0 (good!) | — |
| "novel" | 0 (good!) | — |
| "underscore" | 0 (good!) | — |

### Sentence length issue

Many sentences run 40–60 words. Academic writing is more readable at 20–30 words per sentence. The simplified versions above target this range.
