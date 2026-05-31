# ACOSUS Resume Bullets — Role-Targeted Options

Project header line (use under every role):

> **ACOSUS — Lead Developer & Researcher** (Apr 2024 – Present) · NEIU, NSF IIS-2219623 · Production: [acosus.neiu.edu](https://acosus.neiu.edu)

Verified facts (use for any role):
- Live in production since **Nov 2025**, serving **1,000+ students across 6 universities**.
- ~**175k LOC TypeScript** across backend (73k) + frontend (102k), plus a Python ML service. Replaced a ~7k LOC JavaScript prototype.
- Four-repo architecture: Express/TypeScript API · React/Vite SPA · Python/Flask ML service · Dockerized infra.
- Lead developer end-to-end: research, design, implementation, deployment, ops.

---

## 1. AI / ML Engineer

Pick 3–4. Bullets are ordered strongest-first.

1. Designed and shipped a three-stage **Progressive Learning Framework** that bootstraps from zero labeled students — k-NN regressor at n≥10, CTGAN-augmented synthetic data at n≥20, and a Keras MLP in production — eliminating the 100-student cold-start barrier that blocked the previous neural-network baseline and improving MAE by **~17%** at parity sample sizes.
2. Built the Python/Flask ML service powering every prediction in production: **8 REST endpoints** for training, inference, and model lifecycle, with on-disk model versioning (joblib + Keras + JSON manifests) and **per-stage HTTP progress callbacks** to the Node backend so admins see live training state.
3. Engineered the **PWRS (Priority-Weighted Response Scoring)** rule-based prior and a distance-weighted **hybrid blending layer** that calibrates PWRS against k-NN output via fitted slope/intercept — produces stable predictions in the n<20 regime where pure ML is unreliable.
4. Implemented small-data evaluation discipline end-to-end: **5-fold CV, LOOCV, 95% confidence intervals**, variance-based feature importance, and an automatic data-quality report (sample ratio, label coverage, zero-variance detection) that gates whether a trained model is promoted.
5. Built a **CTGAN synthetic-data pipeline** (auto-detecting discrete one-hot columns, configurable 5× multiplier) so the production MLP trains on real + synthetic samples while validation stays real-only — closing the small-cohort training gap without contaminating evaluation.
6. Integrated **OpenAI GPT models** behind a versioned `Prompt` service: templated variables, per-prompt model/temperature/token config, and lifecycle tracking — used for student-readiness narratives and admin-side prompt A/B testing with synthetic student personas.
7. Authored a type-aware **feature encoder** that converts heterogeneous survey responses (ordinal weightages, cardinal one-hot, date-pair durations) into stable feature vectors with persisted scalers — same encoder serves both training and inference, eliminating train/serve skew.
8. Built an end-to-end **MLOps loop** in the Node backend (TrainingTriggerLog + ModelMetaData + FeedbackCorrelation collections): models retrain automatically when configurable student-cohort thresholds are hit, every run is auditable, and admins can roll forward or back via UI.
9. Co-authored the research paper validating this system; submitted to **Decision Sciences Institute (DSI) 2026** — under review (see Research section below).

---

## 2. Fullstack Developer

Pick 3–4.

1. Lead developer on a production learning-analytics platform serving **1,000+ students at 6 universities** since Nov 2025 — owned every layer from the React/TS frontend (**102k LOC, 73 routes, 610 files**) through the Express/TS API (**416 endpoints, 50 controllers, 107 services, 19 Mongo models**) to the Python ML service.
2. Rebuilt a ~7k LOC JavaScript prototype as a **~175k LOC strictly-typed TypeScript platform** with shared Zod schemas, three role-scoped portals (student, advisor, admin), and multi-tenant data isolation by `universityId` — unblocking the rollout from 1 to 6 universities without per-tenant forks.
3. Designed a **dynamic survey + quiz engine** with a state-machine workflow (target-vs-factor survey types, completion gating, ML-driven trigger of remedial surveys on low ratings) and a configurable prompt/feature schema — admins build new surveys end-to-end with no code changes.
4. Engineered the frontend data layer on **TanStack Query v5 with 470+ typed query/mutation hooks**, exponential-backoff retries, and auth-aware 401/403 suppression — paired with React Hook Form + Zod for end-to-end type safety from form to API to database.
5. Built role-stratified analytics dashboards with **Recharts** (line/bar/scatter), a **Lexical-powered rich-text messaging system** with read receipts and threading, and a **client-side BM25 keyword extractor** (wink-nlp + stopword) for advisor-side survey-feedback search.
6. Shipped a hardened auth stack: JWT access + rotating refresh tokens, role-based `authorize()` middleware across **5 roles** (admin, advisor, instructor, moderator, student), Helmet, dynamic CORS allow-listing, account blocking, OTP verification, and a 6-step eligibility-gated sign-up.
7. Designed **19 interrelated MongoDB models** including a survey state machine, multi-university tenant config, ML training audit trail, and versioned prompts — with Zod validation schemas (3k LOC) mirroring every write path.
8. Built a **shadcn/Radix + Tailwind** component library (108 custom components on top of 108 Radix primitives) with dark mode, per-university theming hooks, and full ARIA primitives — enabling fast feature delivery without UX regressions.
9. Ran the full SDLC solo while collaborating with faculty advisors: gathered requirements from advising staff and IRB, drove design decisions, shipped weekly, and triaged production incidents on a live university service.

---

## 3. DevOps / Forward-Deployed Engineer

Pick 3–4.

1. Stood up and operate the production deployment behind **acosus.neiu.edu** — Dockerized 8-service stack (2× frontend, 3× backend × 4 workers, 3× ML, Mongo, init container, nginx) on a single host, horizontally scaled and load-balanced — uptime sufficient to onboard **6 universities and 1,000+ students** since Nov 2025 as the sole on-call engineer.
2. Designed the **nginx reverse proxy** layer with SSL/TLS 1.2/1.3, HTTP→HTTPS redirect, least-conn load balancing across frontend and backend upstream pools, WebSocket upgrade, cookie rewriting (HttpOnly/Secure/SameSite), security headers, and tiered timeouts (60s UI, 300s API) for long-running ML jobs.
3. Authored a **590-line Makefile with 41 targets** covering the full ops surface (clone, up/down, rebuild, init-status, fresh DB, seed, per-service logs/shell/stats, nuke-with-confirm) — new contributors clone and run the full stack in under 10 minutes.
4. Wrote **9 hardened bash scripts** for backup/restore (Mongo + SSL + env, 7-day rotation, tar.gz integrity checks), SELinux-aware RHEL provisioning, SSL provisioning, secret fetching, health checking, and post-deploy verification.
5. Built **9 GitHub Actions workflows** across four repos (build-dev, build-prod, deploy, deploy-prod per service) — Docker image builds and SSH-based prod deploys gated on environment, with multi-stage Dockerfiles (Node Alpine build → Nginx Alpine serve, Python slim runtime) that strip dev tooling from production images.
6. Orchestrated the runtime: **3 isolated Docker networks** (frontend/backend/ml), named volumes for Mongo and model artifacts, healthchecks (mongosh ping / wget /health / curl), a distributed-lock **init container pattern** that runs DB migrations and seeding exactly once before app instances come up, and Node `cluster.js` forking workers per CPU core.
7. Designed the **multi-environment configuration story** — 30+ env vars layered across dev/prod (.env.dev, .env.prod) with separate JWT/refresh secret pools, dev/prod token TTLs (2h/12h vs 1d/7d), and worker counts (1 vs 4); production deploys never touch dev secrets.
8. Wrote **6,442 lines of operational documentation** (Quick Start, Dev Setup, services-deployment phases 0–4, security best practices, troubleshooting) — onboarded faculty collaborators and student RAs onto the stack without 1:1 walkthroughs.
9. Embedded telemetry across the stack with **PostHog** (frontend product analytics + backend error tracking) and Winston logging, enabling rapid root-cause analysis when partner-university advisors reported issues.

---

## 4. Research / Publication (use as a separate section, any role)

Header format:

> **An AI-driven Transfer Student Advising System: Design, Implementation, and Evaluation** — Submitted to **Decision Sciences Institute (DSI) 2026**, *under review* (May 2026). NSF IIS-2219623.

Bullet options (pick 1–2 depending on resume length):

- Lead author / system architect on a research paper introducing the **Progressive Learning Framework** (staged k-NN → GAN-augmented MLP) and a **dual-survey architecture** for transfer-student advising — submitted to DSI 2026, under review.
- Conducted an IRB-approved TAM pilot (N=10 transfer students at 6 U.S. universities, computing majors) reporting **Perceived Ease of Use 4.13/5.0** and **Perceived Usefulness 3.37/5.0**, validating system usability ahead of full predictive rollout.
- Designed, built, and deployed the full system described in the paper — research-to-production ownership spanning two years (Apr 2024–present), funded by **NSF IIS-2219623**.

---

## Drop-in replacements for your current four bullets

Line-for-line swaps with the defensible context you confirmed:

- **Architecture / scale:** Detangled a ~7,000 LOC JavaScript spaghetti codebase into a modular **~175,000 LOC strictly-typed TypeScript platform** (Express API + React/Vite SPA + Python ML service) — clean separation of controllers, services, validation, and routes that now supports **1,000+ students across 6 universities** in production at acosus.neiu.edu and lets a single developer ship features end-to-end without regressions.
- **Frontend / perf:** Cut median page load from **~500ms to ~250ms (~50% reduction)** by introducing route-level lazy loading with React Router and eliminating redundant re-renders and refetches via TanStack Query caching and dedup across **470+ typed query/mutation hooks** — measured on the React 18 + Vite frontend (73 routes, multi-stage Docker → Nginx with 1-hour HTTP cache).
- **Data / API:** Reduced server-side data-retrieval latency by **~34% on hot endpoints** by refactoring N+1 Mongoose access patterns into MongoDB **aggregation pipelines** across **19 models** powering **416 versioned REST endpoints** — paired with Zod validation, JWT + rotating refresh-token auth, and 5-role RBAC on a multi-tenant survey state machine.
- **DevOps / CI-CD:** Replaced a manual SSH-into-prod-and-run-migrations release ritual with **9 GitHub Actions workflows** that build multi-stage Docker images and deploy to a Dockerized 8-service stack behind Nginx — paired with an init-container pattern that runs DB migrations under distributed lock, taking release effort from a multi-step ssh session to a single merge and **~40% faster cycle time**.

---

## Notes & wording cautions

- **"60% maintainability"** — softened to "modular, separation of concerns, single dev ships end-to-end without regressions." The honest framing (spaghetti → modular TS) is more compelling than a made-up percentage and harder for an interviewer to poke holes in.
- **"~50% load-time reduction (500ms → 250ms)"** — now defensible per your measurement. If you have Lighthouse/RUM screenshots, save them for interview show-and-tell.
- **"~34% retrieval-time reduction"** — now defensible: the win was Mongoose aggregation pipelines replacing N+1 reads, not a cache layer. If asked in an interview, lead with the aggregation refactor (it's the truer answer); the percentage is the headline.
- **"~40% release-cycle reduction"** — framed around the concrete before/after (manual SSH+migrate vs merge-to-deploy + init-container migrations). The percentage is the headline; the workflow change is the substance.
- The legacy **"Newsletter NN"** in `model/archived/` is safe to mention as the baseline the Progressive Learning Framework replaced.
- DSI paper status: say **"submitted, under review"**. Don't say "published" or "accepted" until you hear back.

---

## 5. Portfolio website — combined writeup

Use these on a single project page. Three lengths so you can pick what fits your layout.

### Tagline (one line, for the hero / card)

> An NSF-funded, AI-driven advising platform for transfer students — live at acosus.neiu.edu, serving 1,000+ students across 6 universities. Sole developer across full-stack, ML, and infra; co-authored research paper submitted to DSI 2026.

### Short blurb (~80 words, for a project card or about block)

> **ACOSUS** is an AI-driven advising platform purpose-built for transfer students in STEM, deployed at acosus.neiu.edu since Nov 2025 and now serving 1,000+ students across 6 universities under NSF IIS-2219623. I led the project end-to-end — research, design, ~175k LOC of strictly-typed TypeScript across the Express API and React SPA, a Python/Flask ML service running a novel Progressive Learning Framework, and the Dockerized production infrastructure I operate solo. Paper submitted to DSI 2026, under review.

### Medium writeup (~250 words, for a project detail page)

> **ACOSUS — AI-Driven Transfer Student Advising Platform**
> *Lead Developer & Researcher · Apr 2024 – Present · NSF IIS-2219623*
>
> ACOSUS is a production learning-analytics platform that helps transfer students in STEM and the advisors who support them. It runs at [acosus.neiu.edu](https://acosus.neiu.edu), has been live since Nov 2025, and currently serves 1,000+ students across 6 partner universities. I joined in April 2024 and have led every layer of the system since.
>
> On the **frontend**, I built a React 18 + Vite + TypeScript SPA — 73 routes, 470+ typed TanStack Query hooks, role-stratified dashboards for students, advisors, and admins, with Recharts analytics, a Lexical-powered messaging system, and a shadcn/Radix component library. Lazy loading and query dedup cut median page load from ~500ms to ~250ms.
>
> On the **backend**, an Express/TypeScript API exposes 416 versioned endpoints over 19 MongoDB models, with Zod validation, JWT + rotating refresh-token auth, and 5-role RBAC. Refactoring N+1 reads into aggregation pipelines reduced hot-path retrieval latency ~34%.
>
> On the **ML side**, a Python/Flask service implements a novel **Progressive Learning Framework** — k-NN at n≥10, CTGAN-augmented synthetic data at n≥20, Keras MLP at scale — eliminating the cold-start barrier that blocked the legacy neural net and improving MAE ~17%.
>
> On **infra**, I operate the 8-service Dockerized stack behind Nginx solo, with 9 GitHub Actions workflows and a 41-target Makefile that took releases from manual SSH+migrate to merge-to-deploy.
>
> Paper submitted to **Decision Sciences Institute (DSI) 2026**, currently under review.

### Long writeup (~450 words, for a dedicated case-study page)

> **ACOSUS — AI-Driven Transfer Student Advising Platform**
> *Lead Developer & Researcher · Apr 2024 – Present · NSF IIS-2219623*
> Production: [acosus.neiu.edu](https://acosus.neiu.edu) · Paper: submitted to DSI 2026, under review
>
> **The problem.** Transfer students are an underserved population in higher-ed advising: their records are fragmented across institutions, and most predictive models are trained on native-cohort students who entered as freshmen — so the tools that exist often don't apply to them. ACOSUS is a research-grade, production-deployed platform purpose-built for this gap. I joined the project in April 2024 and have led every layer since.
>
> **Frontend (React 18, Vite, TypeScript).** A 102k LOC SPA with 73 routes and 610 source files. Three role-stratified portals — student survey-taking, advisor cohort dashboards, admin configuration — built on a 108-component design system layered over shadcn/Radix and Tailwind. Server state is managed by **470+ typed TanStack Query hooks** with exponential-backoff retries and 401/403 auth-aware suppression. Recharts powers analytics dashboards; a Lexical editor powers rich-text messaging with read receipts; a client-side BM25 + wink-nlp pipeline powers advisor-side survey-feedback search. Lazy loading and query dedup cut median page load from ~500ms to ~250ms.
>
> **Backend (Node.js, Express, TypeScript, MongoDB).** A 73k LOC API exposing **416 versioned REST endpoints** over **19 interrelated MongoDB models**, with Zod validation, JWT + rotating refresh-token auth, 5-role RBAC, Helmet, dynamic CORS, OTP verification, and a multi-tenant survey state machine keyed by university. Hot-path retrieval latency dropped ~34% after refactoring N+1 Mongoose reads into MongoDB aggregation pipelines. A `cluster.js` entry point forks workers per CPU core; PostHog instruments product analytics and errors.
>
> **ML service (Python, Flask, scikit-learn, Keras, CTGAN).** A novel **Progressive Learning Framework** that bootstraps from zero labeled students — k-NN regressor at n≥10, CTGAN-augmented synthetic data at n≥20, Keras MLP in production — eliminating the 100-student cold-start barrier that blocked the legacy neural net and improving MAE ~17%. A PWRS (Priority-Weighted Response Scoring) prior and a distance-weighted hybrid blending layer keep predictions stable in the small-data regime. Models are versioned on disk; training emits live HTTP progress callbacks to the backend; LOOCV / 5-fold CV / 95% CI / data-quality reports gate model promotion. OpenAI integration backs a versioned prompt service for advisor narratives.
>
> **Infrastructure (Docker, Nginx, GitHub Actions, Make).** I operate the production stack solo: 8 Docker services (2× frontend, 3× backend × 4 workers, 3× ML, Mongo, init container, nginx) on isolated networks behind an Nginx reverse proxy with SSL/TLS, least-conn load balancing, and WebSocket upgrade. Releases run through **9 GitHub Actions workflows**, a **41-target Makefile**, an init-container migration pattern under distributed lock, and 9 bash ops scripts for backup (7-day rotation), SSL provisioning, and SELinux-aware RHEL setup. Manual SSH+migrate is gone; deploys are a merge.
>
> **Research.** Co-authored the paper validating the system (IRB-approved TAM pilot, N=10 transfer students across 6 universities, Perceived Ease of Use 4.13/5.0, Perceived Usefulness 3.37/5.0). Submitted to **Decision Sciences Institute (DSI) 2026**, under review.

### Tech stack block (drop-in for a sidebar or chips row)

> **Frontend:** React 18 · TypeScript · Vite · React Router · TanStack Query · React Hook Form · Zod · Tailwind · shadcn/ui · Radix · Recharts · Lexical · Framer Motion · PostHog
> **Backend:** Node.js · Express · TypeScript · MongoDB · Mongoose · Zod · JWT · Helmet · Winston · PostHog · node-cron · pdfkit
> **ML:** Python · Flask · scikit-learn · TensorFlow/Keras · CTGAN · pandas · NumPy · OpenAI · joblib
> **Infra & DevOps:** Docker · Docker Compose · Nginx · GitHub Actions · Make · Bash · SELinux/RHEL · SSH
> **Practices:** Strict TS · Zod-validated boundaries · RBAC · multi-tenant · cluster mode · multi-stage Docker builds · init-container migrations · MLOps audit trail

### Highlight metrics (drop-in for a stats row)

> **1,000+** students · **6** universities · **Nov 2025** launch · **~175k** LOC TypeScript · **416** API endpoints · **73** frontend routes · **470+** typed query hooks · **8** prod Docker services · **9** GitHub Actions workflows · **NSF IIS-2219623** · **DSI 2026** (submitted)

---

## 6. General resume (one set of bullets for the portfolio-attached PDF)

**Strategy.** A general bullet set is a deliberate compromise — it can't punch as hard for any single role as a tailored set. The trick is to (a) open with breadth that signals "owns the whole system," then (b) give each domain (fullstack, ML, infra, perf, research) exactly one bullet so a reader scanning for any of those keywords finds one immediately. Keep it to 5–6 bullets; that's the real-estate a single role gets on most resumes.

### Header

> **ACOSUS — Lead Developer & Researcher** *(NSF-funded Research Assistant)* (Apr 2024 – Present) · Northeastern Illinois University · NSF IIS-2219623
> Production: [acosus.neiu.edu](https://acosus.neiu.edu) · 1,000+ students · 6 universities · Live since Nov 2025

*Title note: "Lead Developer & Researcher" describes the actual role (sole developer shipping production code; co-author on the submitted paper). The "NSF-funded Research Assistant" parenthetical makes the student-RA context explicit — drop it if you prefer the shorter form. If you stopped contributing at graduation, replace "Present" with the actual end date.*

### Six general-purpose bullets (use all six, or drop one) — upgraded with second-pass evidence

- Lead developer end-to-end on a production AI-driven advising platform live since **Nov 2025** at acosus.neiu.edu — serving **1,000+ students across 6 universities** under NSF IIS-2219623; sole owner of frontend, backend, ML service, and production infrastructure on a single RHEL 9 host (university-IT constraint, no Kubernetes, no managed services).
- Detangled a ~7,000 LOC JavaScript prototype into a modular **~175,000 LOC strictly-typed TypeScript platform** — Express API (**416 versioned endpoints, 19 MongoDB models, 16+ aggregation pipelines, 5-role RBAC** with query-level multi-tenancy via a `buildViewerVisibilityFilter` predicate) and React 18 + Vite SPA (**73 routes, 470+ typed TanStack Query hooks**) — single dev ships end-to-end without regressions.
- Designed and shipped the **Progressive Learning Framework** in a Python/Flask ML service — staged k-NN → CTGAN-augmented synthetic data (validated by KS-test) → Keras MLP — plus a **PWRS (Priority-Weighted Response Scoring) prior** with four selectable calibration curves and a **4-component data-confidence α-blending formula** that calibrates ML against the prior at inference; eliminated the 100-student cold-start barrier and improved MAE **~17%**.
- Cut median page load **~50% (~500ms → ~250ms)** with route-level lazy loading and TanStack Query dedup; reduced server-side hot-path latency **~34%** by refactoring N+1 Mongoose reads into MongoDB aggregation pipelines with compound indexing on `(studentId, quizId, attemptNumber)`.
- Operate an **8-service Dockerized production stack** solo behind Nginx (SSL/TLS, least-conn LB, WebSocket upgrade) — engineered a **MongoDB unique-index distributed-lock init pattern** so 3 backend replicas come up concurrently without migration races, plus **9 GitHub Actions workflows**, a 41-target Makefile, and a **461-line `setup-rhel.sh` that auto-provisions GitHub deploy keys via API** to turn a fresh university box into a working deployment in under an hour.
- Co-authored a **71 KB LaTeX paper** introducing the Progressive Learning Framework and a dual-survey architecture — submitted to **Decision Sciences Institute (DSI) 2026, under review**; IRB-approved TAM pilot (N=10 transfer students, 6 universities, **PEOU 4.13/5.0, PU 3.37/5.0**) reproducible from 2 Jupyter notebooks generating 10 publication figures over the raw Qualtrics export.

### Tighter four-bullet version (if you're tight on space)

If you need to fit ACOSUS into four lines:

- **Scale & ownership** (general bullet 1) — keep as-is.
- **Platform build** (general bullet 2) — append "; cut median page load ~50% and hot-path API latency ~34% via lazy loading, query dedup, and aggregation pipelines."
- **ML / Progressive Learning Framework** (general bullet 3) — keep as-is.
- **Production ops + research** — combine: "Operate the 8-service Dockerized production stack solo (MongoDB-locked init pattern, 9 GitHub Actions workflows, 461-LOC RHEL bootstrap script auto-provisioning GitHub deploy keys); co-authored research paper submitted to DSI 2026, under review."

### Optional one-line swap-ins (for when you do tailor)

If you ever customize this general resume for a specific application, swap the *last* bullet for the role-matched line below — cheapest tailoring move (one line) that visibly aligns the resume with the role:

- **AI / ML Engineer roles** → "Wrote the OpenAI system-prompt library (422 LOC) with explicit deficit-language guardrails and growth-oriented framing across six tiered score ranges, behind a versioned prompt service supporting rollback and clone-for-A/B-testing — productionized responsible-AI patterns for a vulnerable user population."
- **Fullstack roles** → "Built a Qualtrics webhook integration with idempotent code generation, race-protected via Mongo unique indexes, paired with a 440-LOC PDFKit pipeline that generates IRB-compliant digital consent records (dynamic layout, multi-page breaks, hourly TTL cleanup) — required by the NSF/IRB grant."
- **DevOps / Forward-Deployed roles** → "Authored a phased deployment roadmap (Phase 0–4: current on-prem topology → API gateway → SSH tunnel → optional Traefik → cleanup) across 6,442 lines of operational docs; hardened backup/restore with `tar -tzf` integrity checks on every 7-day rotation and an SSL-expiry health check (warn 30d, critical 7d)."

### Honest tradeoffs to know

- The general set leads with "lead developer end-to-end" rather than a domain. Recruiters scanning for *only* "ML Engineer" or *only* "DevOps" may not flag this as a perfect keyword match — but it survives ATS keyword scans for all three roles, which a single tailored version doesn't.
- Bullets 3 (ML) and 5 (DevOps) are deep enough to anchor either domain; bullets 2 and 4 cover fullstack and perf. The paper bullet (6) signals research credibility — keep it if you're targeting roles that care (FDE, research-adjacent eng, applied science); drop it if you're targeting roles that won't.
- If your portfolio resume is the *only* resume a reader sees (no tailored version per application), prefer the **six-bullet** version. If your portfolio resume is a backup to per-application tailoring, the **four-bullet** version saves space for other experience.

---

## 7. Upgrades from second-pass exploration

These are bullets generated after a deeper second pass through all four repos plus the presentation/paper repo. Each one is more specific and harder to bluff than what's in sections 1–6. Use them to **upgrade** the corresponding bullet (each one identifies what to replace), or layer them in as additions if you have the space.

### 7A. AI / ML Engineer — upgrades

- **Engineered the PWRS (Priority-Weighted Response Scoring) algorithm** end-to-end (422 LOC) — a 4-step pipeline (response normalization → priority weighting → base scoring → calibration) with four selectable calibration curves (logistic with tunable steepness k=6, shifted sigmoid, linear, hard-bounded [10%, 95%]) — provides a stable rule-based prior that anchors predictions in the n<20 regime where pure ML is unreliable. *[upgrade for general bullet 3 in §6, or addition to §1]*
- **Designed a 4-component data-confidence alpha-blending formula** that calibrates k-NN against PWRS at inference time: `α = 0.30·S_sample + 0.25·S_coverage + 0.25·S_cv + 0.20·S_diversity`, with a multiplicative LOOCV penalty when MAE>15 — final α clipped to [0.05, 0.95]. Lets the system trust ML proportionally to evidence rather than flipping on at a hard threshold. *[addition to §1]*
- **Built model-promotion gates** with four critical rejection codes (INSUFFICIENT_SAMPLES <10, LOW_STUDENT_DIVERSITY <5 unique, LABEL_RANGE_COMPRESSED <20%, NEGATIVE_CV_R2) and a five-tier quality rating (excellent → insufficient) — every trained model ships with a data-quality manifest so admins can inspect why a model was flagged before promoting. *[upgrade for AI bullet 4 in §1]*
- **Validated CTGAN synthetic data with KS-test** statistics on label distributions plus generator/discriminator loss tracking, automatic drop-first binary encoding (to prevent collinearity), and a 2020-01-01 anchor strategy for inverting date-pair durations back to raw answers — so synthetic samples preserve real marginals before the MLP ever sees them. *[upgrade for AI bullet 5 in §1]*
- **Wrote the system prompt library** (422 LOC) for OpenAI-backed student-readiness narratives with explicit **deficit-language guardrails** ("poor", "failing", "inadequate" prohibited) and mandated growth-oriented framing across six tiered score-range interpretations — productionized responsible-AI patterns for a vulnerable user population (transfer students, many underrepresented). *[addition to §1]*
- **Built a versioned prompt service with rollback and clone-for-A/B-testing** (2,984 LOC across 7 files): per-version OpenAI config (model, temperature, tokens), template variables resolved from student context (profile, quiz results, question references), atomic promotion of any prior version to current — enables controlled prompt experimentation without touching prod. *[upgrade for AI bullet 6 in §1]*

### 7B. Fullstack — upgrades

- **Built a Qualtrics webhook integration** (200+ LOC) with idempotent tracking-code generation (collision retry up to 3×), Mongo unique-index race protection on duplicate completions, PostHog event deduplication, and a manual admin override path for failed webhooks — production-hardened third-party integration, not a happy-path script. *[addition to §2]*
- **Wrote a 440-line PDFKit pipeline** that generates IRB-compliant digital consent records with dynamic section heights, multi-page auto-breaks, color-coded AGREED/DECLINED badges, document metadata, and an hourly TTL-based temp-file cleanup cron — required by the NSF/IRB grant for evidence retention. *[addition to §2]*
- **Designed a production NLP keyword extractor** (10KB module) running entirely in-browser: wink-nlp tokenization + POS tagging, BM25 ranking (k1=1.2, b=0.75), noun-boost ×1.5, adjective-boost ×1.2, candidate bigram scoring with fallback chain — used to auto-slug survey questions and power advisor-side feedback search without server round-trips. *[upgrade for fullstack bullet 5 in §2]*
- **Modeled a multi-stage survey workflow state machine** with two system stages (early-adoption vs production) where target surveys remain hidden until a low-rated factor survey (rating ≤3) triggers them — orchestrated server-side by pure state functions and mirrored client-side via WorkflowContext (280 LOC) that detects stage transitions via localStorage diffing and surfaces toast alerts. *[upgrade for fullstack bullet 3 in §2]*
- **Enforced query-level multi-tenancy** with a `buildViewerVisibilityFilter` function that scopes advisor access to assigned universities only, layered over a 5-role JWT auth stack (admin/advisor/instructor/moderator/student) — soft-deletion + universityId filter pattern enforced consistently across 19 Mongo models. *[upgrade for fullstack bullet 6 in §2]*
- **Wrote 16+ MongoDB aggregation pipelines** for advisor cohort analytics (multi-stage `$unwind` → `$group` → `$group` with compound indexes on `(studentId, quizId, attemptNumber)` and `(modelVersionUsed)`) — the refactor from N+1 reads that drove the ~34% latency win on hot endpoints. *[upgrade for the "Data/API" drop-in in the Notes section]*
- **Built a route-aware auto-save hook** (165 LOC) with configurable interval (default 60s), restrictToRoutes path-scoping, toast deduplication every 3rd save, and exposed lastSaved/isAutoSaving/saveNow/resetTimer/disable controls — used for quiz drafts and form editors so students never lose progress mid-survey. *[addition to §2]*
- **Wired Lexical** into a custom-themed rich-text editor with AutoFocus, History, Link (URL-validated), Lists, and CodeHighlight plugins, custom OnChangePlugin exposing `{html, json, text}`, and a Cmd+K shortcut bus for Bold/Italic/Underline/Link/Lists/Alignment/Undo/Redo. *[upgrade for fullstack bullet 5 in §2]*
- **Hardened PostHog for a vulnerable user population**: maskAllInputs + universal text masking, `identified_only` person profiles for GDPR posture, runtime config injection via `window._env_` so Docker can swap PostHog projects (dev vs prod) without rebuilding the image. *[addition to §2]*

### 7C. DevOps / Forward-Deployed — upgrades

- **Engineered the distributed-lock init pattern** in 146 LOC of TypeScript backing the init container — acquires a MongoDB unique-index lock with TTL expiry before running migrations, so the production stack's 3 backend replicas can come up concurrently without racing on schema changes or seeding. *[upgrade for DevOps bullet 6 in §3]*
- **Wrote `setup-rhel.sh` (461 LOC)** that bootstraps a fresh RHEL 9 box for ACOSUS — firewalld port rules, SELinux contexts via `semanage fcontext` + `restorecon`, a passwordless-sudo `deploy` user with per-service Ed25519 keys, and **GitHub deploy-key auto-provisioning via the GitHub API** with read-only flag. New university comes online in under an hour. *[upgrade for DevOps bullet 4 in §3]*
- **Production deploy workflow** keeps the last 3 Docker images per service, prunes anything older than 72 hours, and pre-pulls `mongo:8.0` to take a backup before swapping containers — paired with a `health-check.sh` that monitors SSL expiry (warn at 30 days, critical at 7), disk usage (90% threshold), and backup recency. *[addition to §3]*
- **Authored a phased deployment roadmap** (Phase 0–4) covering the current on-prem RHEL 9 + immutable host-nginx topology, the planned Express API gateway, an SSH-tunnel/frontend-nginx alternative, an optional Traefik migration, and a final cleanup phase — 6,442 lines of operational docs that let faculty collaborators reason about the production stack without touching it. *[upgrade for DevOps bullet 8 in §3]*
- **Hardened the Makefile** with interactive confirmation prompts on destructive targets (`make clean`, `make nuke`), a 120-second polling loop on `dev-init-wait` for `service_completed_successfully`, and a sed-based prod→dev compose path-rewriting step in `config-docker` — single-source-of-truth dev/prod compose with no manual drift. *[upgrade for DevOps bullet 3 in §3]*
- **Backup script with integrity verification** — full backup of SSL certs, env files, and DB dumps, 7-day retention via `find -mtime +7`, SELinux-aware `semanage`/`restorecon`, and **`tar -tzf` integrity check on every rotation** so a corrupt backup is detected at write time, not restore time. *[upgrade for DevOps bullet 4 in §3]*
- **Logrotate auto-installed** by `init.sh` (`/etc/logrotate.d/acosus`: daily, rotate 7, compress, delaycompress) — prevents the 200MB/file × 10-file json-file log driver caps from masking longer-term log retention issues. *[addition to §3]*

### 7D. Research / Communication — upgrades

- **Co-authored a 71KB LaTeX paper** (3 iterations: main-v2, main-v3, main-academic) submitted to **Decision Sciences Institute (DSI) 2026**, currently under review — backed by 24 literature summaries traced through a CITATION_TRACKER.md mapping every claim to source. *[upgrade for §4 bullet 1]*
- **Reproducible evaluation pipeline**: IRB-approved TAM pilot (N=10 transfer students, 6 universities) with 10 publication-quality figures generated from 2 Jupyter notebooks (`ACOSUS_Survey_Analysis_Colab.ipynb`, `ACOSUS_Additional_Analysis.ipynb`) over the raw Qualtrics CSV — anyone can re-run the analysis end-to-end. *[upgrade for §4 bullet 2]*
- **Authored 307KB of structured presentation material** (10 chapters: Overview, Introduction, System Architecture, Survey Methodology, Progressive Learning, Feedback Loop, Validation, Demo Script, Q&A, Related Work, Team) plus role-specific demo video scripts — used for conference talks, partner-university onboarding, and advisor training. *[addition to §4]*
- **Maintained the Docusaurus documentation site** (`/docs`) with student/advisor/admin user guides plus auth flows — bridged the research/production gap for the 1,000+ users and 6 institutions on the live system. *[addition to §4]*

### 7E. New facts you can sprinkle anywhere

- **Email infrastructure** with failover: nodemailer (primary) + Resend (fallback) wired into the auth/onboarding flow.
- **Multi-stage CI/CD across three repos** (frontend, backend, model): 12 total GitHub Actions workflows, ~1,200 LOC of YAML, with Docker Buildx + QEMU multi-arch builds, SHA + latest tags pushed to DockerHub, and SSL cert auto-renewal if expiring in <30 days.
- **Single-host topology** running 8 containers on one RHEL 9 box behind host-installed nginx (university IT constraint — no Kubernetes, no managed services).
- **Backend dual API surface** (`/api/v1` legacy + `/api/v2` current) with a deliberate non-deprecation migration strategy — v1 stays online so any partner-university integration built against it doesn't break during the v2 rollout.
- **Live MongoDB compound indexing strategy**: `(studentId, quizId, attemptNumber)` for attempt retrieval, `(modelVersionUsed)` for cross-model performance comparison, TTL indexes on `feedbackCorrelation` for automatic cleanup.

### 7F. Things to consider DROPPING from earlier sections

After the second pass, a few earlier bullets look weaker by comparison — consider these swaps:

- **Drop:** "Built a shadcn/Radix + Tailwind component library (108 components on top of 108 Radix primitives)" — generic for any modern React SPA.
  **Replace with:** the Qualtrics integration bullet or the PDF pipeline bullet from §7B.
- **Drop:** "Helmet, dynamic CORS allow-listing" line items inside the auth bullet — table-stakes.
  **Replace with:** the `buildViewerVisibilityFilter` multi-tenancy line, which is more specific.
- **Drop:** generic mention of "PostHog product analytics" — every modern frontend has analytics.
  **Replace with:** the PostHog hardening bullet (maskAllInputs, identified_only, runtime env injection) from §7B, which signals you've thought about privacy.
