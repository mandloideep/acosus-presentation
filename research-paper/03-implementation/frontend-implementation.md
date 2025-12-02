# Frontend Implementation

This document provides a comprehensive overview of the ACOSUS frontend implementation, including the technology stack, user interface components, user journey flows, and design considerations.

---

## 1. Technology Stack

### 1.1 Core Framework

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.3.1 | Component-based UI framework |
| **TypeScript** | 5.4.5 | Static typing and developer experience |
| **Vite** | 5.3.1 | Build tool with SWC compiler (fast HMR) |
| **React Router** | 6.23.1 | Client-side routing and navigation |

### 1.2 State Management & Data Fetching

| Library | Version | Purpose |
|---------|---------|---------|
| **TanStack Query** (React Query) | 5.45.1 | Server state management, caching, optimistic updates |
| **React Hook Form** | 7.52.0 | Form state management with validation |
| **Zod** | 3.23.8 | Schema validation and TypeScript type inference |
| **React Context API** | Built-in | Global application state (UserContext, WorkflowContext) |

**Key Custom Contexts:**
- `UserContext`: Authentication state, login/logout mutations, user profile
- `WorkflowContext`: Survey workflow state, system stage, quiz availability
- `StudentContext`: Advisor-acting-on-behalf-of-student state

### 1.3 UI Component Library

| Library | Version | Purpose |
|---------|---------|---------|
| **Radix UI** | Various | Headless, accessible UI primitives |
| **shadcn/ui** | Custom | Pre-built components on Radix UI |
| **Tailwind CSS** | 3.4.4 | Utility-first CSS framework |
| **Tabler Icons** | 3.6.0 | Icon library (1000+ icons) |
| **Framer Motion** | 11.18.2 | Animations and transitions |

**Radix UI Components Used:**
- Dialog, Alert Dialog (modals and confirmations)
- Dropdown Menu, Tabs, Radio Groups
- Checkboxes, Switches, Progress bars
- Tooltips, Popovers, Alerts

### 1.4 Rich Text & Data Visualization

| Library | Version | Purpose |
|---------|---------|---------|
| **Lexical** | 0.34.0 | Rich text editor (admin survey descriptions) |
| **Recharts** | 2.12.7 | React charts library for dashboards |
| **React Day Picker** | 8.10.1 | Date selection component |

### 1.5 Utilities & Helpers

| Library | Purpose |
|---------|---------|
| **Axios** | HTTP client with custom instances for v1/v2 APIs |
| **Sonner** | Toast notifications |
| **Dayjs** | Date/time manipulation |
| **React Spinners** | Loading indicators |
| **React Error Boundary** | Error boundary wrapper |
| **Nanoid** | Unique ID generation |
| **use-debounce** | Debouncing utility hook |
| **PostHog** | Analytics and user event tracking |

### 1.6 Build and Deployment

#### Docker Multi-Stage Build

```dockerfile
# Stage 1: Build
FROM node:lts-alpine AS builder
WORKDIR /app
COPY package*.json tsconfig.json ./
RUN npm install
COPY . .
ENV MODE=production
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY frontend-nginx.conf /etc/nginx/conf.d/default.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
EXPOSE 80
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
```

**Key Features:**
- Multi-stage build for minimal image size
- Runtime environment variable injection via `env-config.js` template
- No secrets baked into Docker image (security best practice)

#### Nginx Configuration

```nginx
server {
    listen 80;
    server_name _;
    root /usr/share/nginx/html;
    index index.html;

    # SPA routing - try files, fallback to index.html
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API proxy to backend service
    location /api {
        proxy_pass http://backend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Authorization $http_authorization;
    }
}
```

---

## 2. User Interface Components

### 2.1 Application Layout

The application uses a consistent layout structure across all authenticated pages:

```
┌─────────────────────────────────────────────────────────────┐
│  Header (Logo, Navigation, User Menu)                        │
├──────────────┬──────────────────────────────────────────────┤
│              │                                               │
│   Sidebar    │           Main Content Area                  │
│  (Collapsed/ │                                               │
│   Expanded)  │   ┌───────────────────────────────────┐      │
│              │   │  Page Content                     │      │
│  - Dashboard │   │                                   │      │
│  - Surveys   │   │  [Dynamic based on route]        │      │
│  - Profile   │   │                                   │      │
│  - Settings  │   └───────────────────────────────────┘      │
│              │                                               │
└──────────────┴──────────────────────────────────────────────┘
```

**Key Layout Components:**
- `AppShell`: Main application container with sidebar
- `Sidebar`: Collapsible navigation (role-specific menu items)
- `Nav`: Top navigation with breadcrumbs
- `Layout`: Page wrapper with header and body sections

### 2.2 Landing/Onboarding Page

**Route:** `/` (Public website)

**Purpose:** Introduce ACOSUS to prospective users (students, advisors, administrators)

**Sections:**
1. **Hero Section**: System tagline, call-to-action buttons (Login/Register)
2. **Features Section**: Key capabilities (Survey System, ML Predictions, Advisor Tools)
3. **Benefits Section**: Value proposition for different user roles
4. **Team Section**: Research team and institutional collaboration

> **[Figure 2.2-1: Landing Page Screenshot]**
> *Description: Full-page screenshot showing the ACOSUS landing page with hero section, feature highlights, and navigation to login/register.*

### 2.3 Authentication Pages

**Routes:** `/login`, `/register`, `/forgot-password`, `/otp`

**Components:**
- `UserAuthForm`: Email/password login with validation
- `SignUpForm`: Registration with email, name, password
- `ForgotForm`: Password recovery via email
- `OTPForm`: Two-factor authentication code input

**Features:**
- Zod schema validation
- Password visibility toggle
- Error message display
- Loading states during submission
- Automatic redirect after successful authentication

> **[Figure 2.3-1: Login Page Screenshot]**
> *Description: Login form with email and password fields, "Forgot Password" link, and "Create Account" option.*

### 2.4 Student Dashboard

**Route:** `/app/student`

**Component:** `Dashboard` with `AvailableQuizzes`

**Purpose:** Central hub for students to view available surveys and track progress

**Sub-components:**
1. **SystemProgressBanner**: Shows early adoption progress (e.g., "7/10 students enrolled")
2. **TargetQuizSection**: Target surveys available for completion
3. **FactorQuizSection**: Factor surveys (may be blocked until target completion)
4. **QuizCard**: Individual survey card showing:
   - Survey title and description
   - Status badge (Available, In Progress, Completed, Blocked)
   - Progress indicator for in-progress surveys
   - Action button (Start, Continue, View Results)
5. **EmptyState**: Shown when no surveys are available

**Visual Status Indicators:**
| Status | Color | Icon | Description |
|--------|-------|------|-------------|
| Available | Blue | Play icon | Survey ready to start |
| In Progress | Yellow | Clock icon | Survey started, not completed |
| Completed | Green | Checkmark | Survey finished |
| Blocked | Gray | Lock icon | Prerequisites not met |

> **[Figure 2.4-1: Student Dashboard Screenshot]**
> *Description: Student dashboard showing system progress banner at top, available target surveys in cards below, and factor surveys section (showing locked/unlocked state).*

### 2.5 Survey Interface

**Route:** `/app/student/attempt/:quizSlug`

**Component:** `ImprovedStudentQuiz2V2`

**Purpose:** Render survey questions with category-based pagination, auto-save, and progress tracking

**Key Features:**

1. **Category-Based Navigation**
   - Questions grouped by category (Academic, Financial, Personal, etc.)
   - Progress bar showing completion per category
   - Previous/Next navigation between categories

2. **Question Types Supported**
   - Multiple Choice (Single Select): Radio buttons with option weightages
   - Multiple Choice (Multi-Select): Checkboxes
   - Text Input: Short answer fields
   - Slider: Numeric range selection
   - Date Range: Start/end date pickers

3. **Auto-Save Mechanism**
   - 2-second debounce on answer changes
   - Immediate localStorage persistence
   - Background sync to backend (bulk save)
   - Offline detection with warning banner

4. **Progress Tracking**
   - Visual progress bar per category
   - Overall completion percentage
   - Validation of required questions before navigation

**UI Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│  Quiz Progress Header                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Category 1 ████████░░░░  Category 2 ░░░░░░░░░░░░    │   │
│  └──────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Category: Academic Background              Question 1 of 5  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  What is your high school GPA?                       │   │
│  │                                                       │   │
│  │  ○ Below 2.0                                         │   │
│  │  ○ Between 2.0 and 3.0                               │   │
│  │  ● Between 3.0 and 3.5                               │   │
│  │  ○ More than 3.5                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  [← Previous]                              [Next →]         │
│                                                              │
│  Auto-saved: 2 seconds ago                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **[Figure 2.5-1: Survey Interface Screenshot]**
> *Description: Survey taking interface showing progress header, current question with multiple choice options, and navigation buttons.*

> **[Figure 2.5-2: Survey Auto-Save Indicator]**
> *Description: Close-up of the auto-save indicator showing "Saving..." animation and "Saved" confirmation.*

### 2.6 Prediction Display

**Context:** Shown after completing Factor Survey (when model is trained, students 11+)

**Component:** `SuccessRateModal` / Prediction Display Section

**Purpose:** Show ML-predicted success rate with similar students for context

**Display Elements:**
1. **Predicted Success Rate**: Large percentage display (e.g., "79%")
2. **Interpretation Text**: "Based on students similar to you..."
3. **Similar Students Section**: Cards showing nearest neighbors
   - Distance/similarity score
   - Success rate of similar student
   - Shared characteristics (same GPA range, same support status)
4. **Feedback Rating**: 5-star rating request

**UI Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│  Your Predicted Success Rate                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│              ╔══════════════════════╗                        │
│              ║        79%           ║                        │
│              ╚══════════════════════╝                        │
│                                                              │
│  Based on students similar to you, we predict your          │
│  success rate is 79%.                                        │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Students Similar to You:                            │   │
│  │                                                       │   │
│  │  • Student A: 82% success rate                       │   │
│  │    Similar GPA range (3.0-3.5)                       │   │
│  │                                                       │   │
│  │  • Student B: 74% success rate                       │   │
│  │    Same family support status                        │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  How accurate is this prediction?                           │
│                                                              │
│  ☆ ☆ ☆ ☆ ☆  (Click to rate 1-5 stars)                       │
│                                                              │
│  [Submit Feedback]                                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

> **[Figure 2.6-1: Prediction Display Screenshot]**
> *Description: Modal showing predicted success rate with percentage, similar students list, and feedback star rating interface.*

### 2.7 Feedback Collection

**Context:** After prediction is shown and student rates accuracy

**Purpose:** Collect student feedback for pseudo-labeling or correction

**Two Paths:**

**Path A: High Rating (≥4 stars)**
- System uses prediction as pseudo-label
- Student sees "Thank you!" confirmation
- No additional survey required

**Path B: Low Rating (<4 stars)**
- System requests Target Survey for correction
- Student provides actual self-assessed success rate
- Correction data used to improve model

> **[Figure 2.7-1: Feedback Submission Screenshot]**
> *Description: Feedback confirmation screen after high rating, showing "Thank you" message and completion status.*

> **[Figure 2.7-2: Correction Request Screenshot]**
> *Description: Screen requesting target survey completion after low rating, with explanation of why correction is needed.*

### 2.8 Student Profile Management

**Routes:** `/app/student/profile/*`

**Sub-pages:**
1. **Account Settings** (`/profile`): Email, password change
2. **Academic Info** (`/profile/academic`): GPA, SAT scores, credits, major
3. **Personal Info** (`/profile/personal`): Demographics, background
4. **Profile Categories** (`/profile/category/:slug`): Custom profile fields defined by admin
5. **Uncategorized** (`/profile/uncategorized`): Questions without category assignment

**Features:**
- Form validation with Zod schemas
- Real-time save with loading indicators
- Profile completion percentage tracking
- Required vs optional field indicators

> **[Figure 2.8-1: Student Profile Page Screenshot]**
> *Description: Student profile editing page showing form fields organized by category with save button and completion indicator.*

### 2.9 Admin Dashboard

**Route:** `/app/admin`

**Component:** `AdminDashboardLiveF`

**Purpose:** Comprehensive analytics and system monitoring for administrators

**Tabs:**

1. **Overview Tab**
   - Total users, students, advisors counts
   - Login trends over time (line chart)
   - System health indicators
   - Recent activity feed

2. **Quizzes Tab**
   - Survey completion rates (bar chart)
   - Quiz-by-quiz completion metrics
   - Workflow summary statistics
   - Average completion time

3. **Students Tab**
   - Demographics breakdown charts:
     - Age distribution (bar chart)
     - Gender distribution (pie chart)
     - Ethnicity breakdown (bar chart)
     - Degree type distribution (pie chart)
   - Student engagement metrics
   - Activity tracking (heatmap)

4. **Models Tab** (Future/Planned)
   - ML model performance metrics
   - Accuracy trends over time
   - MAE, R² tracking
   - Training history

5. **Users Tab**
   - User management overview
   - Role distribution chart
   - Activity logs

**Time Range Filtering:**
- Day, Week, Month, Year options
- All filters apply across all tabs

> **[Figure 2.9-1: Admin Dashboard Overview Screenshot]**
> *Description: Admin dashboard overview tab showing summary statistics cards and login trend chart.*

> **[Figure 2.9-2: Admin Dashboard Students Tab Screenshot]**
> *Description: Students tab showing demographic charts (age, gender, ethnicity distributions).*

### 2.10 Admin Quiz Management

**Routes:** `/app/admin/quizzes/*`

**Purpose:** Create, edit, and manage surveys (both Target and Factor)

**Features:**

1. **Quiz List** (`/quizzes`)
   - Data table with all quizzes
   - Create new quiz button
   - Filter by type (Target/Factor)
   - Actions: Edit, Delete, View Details

2. **Quiz Detail** (`/quizzes/:quizSlug`)
   - **Categories Tab**: Manage question categories
   - **Questions Tab** (`/c/:categorySlug`): Add/edit questions in category
   - **All Questions Tab** (`/questions`): Table view with bulk operations
   - **Factor Quizzes Tab** (`/factor-quizzes`): Link factor surveys to target surveys
   - **Models Tab** (`/models`): Manage ML models for quiz
   - **Prompt Tab** (`/prompt`): Configure AI prompts (future feature)

3. **Question Editor**
   - Rich text description (Lexical editor)
   - Question type selection
   - Option management with weightages
   - Priority score configuration
   - Required/optional toggle

> **[Figure 2.10-1: Quiz List Page Screenshot]**
> *Description: Admin quiz list showing data table with quiz name, type, status, and action buttons.*

> **[Figure 2.10-2: Quiz Question Editor Screenshot]**
> *Description: Question editing interface showing form fields for question text, options with weightages, and priority score.*

### 2.11 Advisor Dashboard & Student Management

**Routes:** `/app/advisor/*`

**Purpose:** Allow advisors to search students and manage their surveys

**Features:**

1. **Advisor Dashboard** (`/app/advisor`)
   - Overview of assigned students
   - Quick stats and notifications

2. **Student Search** (`SearchStudentV2`)
   - Search by name or email
   - Student result cards with basic info
   - Click to select student for management

3. **Student Profile View** (`/app/advisor/s/:studentId/profile`)
   - Read-only view of student profile
   - Same structure as student self-view
   - Includes: Account, Academic, Personal, Custom categories

4. **Survey Management** (`/app/advisor/s/:studentId/surveys`)
   - List of available surveys for student
   - Take survey on behalf of student
   - View completed survey attempts

5. **Take Survey on Behalf** (`/app/advisor/s/:studentId/surveys/take/:quizSlug`)
   - Same interface as student survey
   - Answers saved with advisor attribution
   - `effectiveUserId = "advisor_:advisorId_student_:studentId"`

> **[Figure 2.11-1: Advisor Student Search Screenshot]**
> *Description: Advisor dashboard showing student search interface with search results displayed as cards.*

> **[Figure 2.11-2: Advisor Student Profile View Screenshot]**
> *Description: Advisor viewing a student's profile in read-only mode with all sections visible.*

---

## 3. User Journey Flows

### 3.1 Flow 1: First-Time Student (Bootstrap Phase, Students 1-10)

**Scenario:** New transfer student registers and completes both Target and Factor surveys during the early adoption phase.

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Registration                                        │
│  Route: /register                                            │
├─────────────────────────────────────────────────────────────┤
│  • Student enters email, name, password                     │
│  • Submits registration form                                │
│  • Receives email verification OTP                          │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Email Verification                                  │
│  Route: /otp                                                 │
├─────────────────────────────────────────────────────────────┤
│  • Student enters OTP from email                            │
│  • Account verified                                         │
│  • Redirected to login                                      │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Login                                               │
│  Route: /login                                               │
├─────────────────────────────────────────────────────────────┤
│  • Student enters credentials                               │
│  • JWT tokens stored                                        │
│  • UserContext populated                                    │
│  • Redirected to /app/student                               │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Complete Profile                                    │
│  Route: /app/student/profile/*                               │
├─────────────────────────────────────────────────────────────┤
│  • ProfileCompletionBanner shows incomplete status          │
│  • Student fills: Account → Academic → Personal             │
│  • Profile completion tracked in WorkflowContext            │
│  • When complete, banner disappears                         │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: View Dashboard                                      │
│  Route: /app/student                                         │
├─────────────────────────────────────────────────────────────┤
│  • SystemProgressBanner: "7/10 students enrolled"           │
│  • TargetQuizSection: Shows Target Survey (Available)       │
│  • FactorQuizSection: Shows Factor Survey (Available*)      │
│  * During bootstrap, both surveys shown                     │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Complete Target Survey                              │
│  Route: /app/student/attempt/:targetQuizSlug                 │
├─────────────────────────────────────────────────────────────┤
│  • Student answers readiness questions (21 questions)       │
│  • PWRS formula calculates success rate                     │
│  • If multi-question: Shows calculated rate for validation  │
│  • Student confirms or provides presumed rate               │
│  • Label stored: { success_rate: 73, source: "target" }    │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 7: Complete Factor Survey                              │
│  Route: /app/student/attempt/:factorQuizSlug                 │
├─────────────────────────────────────────────────────────────┤
│  • Student answers background questions (11 questions)      │
│  • GPA, SAT, Financial support, etc.                       │
│  • Answers normalized and stored as features               │
│  • No prediction shown (< 10 students)                     │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 8: Thank You Screen                                    │
│  Route: /app/student/thank-you                               │
├─────────────────────────────────────────────────────────────┤
│  • Confirmation message displayed                           │
│  • "Thank you for participating in the early adoption"     │
│  • Link to return to dashboard                              │
└─────────────────────────────────────────────────────────────┘
```

**Time Estimate:** 15-20 minutes total
- Registration/Login: 2-3 minutes
- Profile Completion: 3-5 minutes
- Target Survey: 8-10 minutes (21 questions)
- Factor Survey: 3-4 minutes (11 questions)

### 3.2 Flow 2: Returning Student (After 10+ Students Enrolled)

**Scenario:** Student enrolls after bootstrap phase complete; receives ML prediction.

```
┌─────────────────────────────────────────────────────────────┐
│  Steps 1-4: Same as Flow 1                                   │
│  (Registration → Verification → Login → Profile)            │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: View Dashboard (Production Phase)                   │
│  Route: /app/student                                         │
├─────────────────────────────────────────────────────────────┤
│  • SystemProgressBanner: Hidden (production phase)          │
│  • TargetQuizSection: Hidden (not needed initially)        │
│  • FactorQuizSection: Shows Factor Survey (Available)       │
│  • Student only sees Factor Survey to start                │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Complete Factor Survey                              │
│  Route: /app/student/attempt/:factorQuizSlug                 │
├─────────────────────────────────────────────────────────────┤
│  • Student answers background questions (11 questions)      │
│  • ~3 minutes to complete                                   │
│  • Answers sent to backend                                  │
│  • Backend requests prediction from Model Server            │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 7: View Prediction                                     │
│  Component: SuccessRateModal                                 │
├─────────────────────────────────────────────────────────────┤
│  • Modal displays predicted success rate (e.g., 79%)       │
│  • Shows similar students and their rates                  │
│  • Explains prediction basis                               │
│  • Requests feedback: "How accurate is this?" (1-5 ⭐)     │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
           Rating ≥ 4 stars            Rating < 4 stars
                    │                           │
                    ▼                           ▼
┌───────────────────────────┐   ┌───────────────────────────┐
│  Step 8A: Pseudo-Label    │   │  Step 8B: Correction      │
├───────────────────────────┤   ├───────────────────────────┤
│  • System accepts         │   │  • System requests Target │
│    prediction as label    │   │    Survey completion      │
│  • source: "pseudo_label" │   │  • Student provides actual│
│  • Thank you message      │   │    self-assessment (52%)  │
│  • Total time: ~3 min     │   │  • source: "corrected"    │
│                           │   │  • Total time: ~13 min    │
└───────────────────────────┘   └───────────────────────────┘
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 9: Return to Dashboard                                 │
│  Route: /app/student                                         │
├─────────────────────────────────────────────────────────────┤
│  • Factor Survey now shows "Completed" status              │
│  • Student can view attempt history                        │
│  • Feedback contributes to model improvement               │
└─────────────────────────────────────────────────────────────┘
```

**Time Estimate (High Rating Path):** 5-7 minutes total
- Profile Completion: 3-5 minutes
- Factor Survey: 3 minutes
- View Prediction & Rate: 1 minute

**Time Estimate (Low Rating Path):** 13-18 minutes total
- Profile Completion: 3-5 minutes
- Factor Survey: 3 minutes
- View Prediction & Rate: 1 minute
- Target Survey (Correction): 8-10 minutes

### 3.3 Flow 3: Providing Feedback on Prediction

**Scenario:** Detailed flow of the feedback mechanism after prediction display.

```
┌─────────────────────────────────────────────────────────────┐
│  Prediction Displayed                                        │
│  "Your predicted success rate is 79%"                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Student Reviews:                                           │
│  • Predicted percentage                                     │
│  • Similar students list                                    │
│  • Shared characteristics                                   │
│                                                              │
│  Question: "How accurate is this prediction?"               │
│  Rating Input: ☆ ☆ ☆ ☆ ☆                                    │
│                                                              │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                    Student clicks star rating
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
        ⭐⭐⭐⭐ or ⭐⭐⭐⭐⭐                    ⭐, ⭐⭐, or ⭐⭐⭐
            (4-5 stars)                     (1-3 stars)
                    │                           │
                    ▼                           ▼
┌───────────────────────────────┐ ┌───────────────────────────┐
│  HIGH CONFIDENCE PATH         │ │  LOW CONFIDENCE PATH      │
├───────────────────────────────┤ ├───────────────────────────┤
│                               │ │                           │
│  Backend Action:              │ │  UI Action:               │
│  POST /api/v2/feedback/submit │ │  Display correction form  │
│  {                            │ │                           │
│    rating: 5,                 │ │  "We'd like to improve    │
│    predictionShown: 79,       │ │   our prediction."        │
│    usePseudoLabel: true       │ │                           │
│  }                            │ │  "What do YOU think your  │
│                               │ │   actual success rate is?"│
│  Database Entry:              │ │                           │
│  {                            │ │  Slider: 0% ────●──── 100%│
│    label: {                   │ │                 52%       │
│      success_rate: 79,        │ │                           │
│      source: "pseudo_label"   │ │  [Submit Correction]      │
│    }                          │ │                           │
│  }                            │ └─────────────┬─────────────┘
│                               │               │
│  UI Response:                 │               ▼
│  "Thank you! Your feedback    │ ┌───────────────────────────┐
│   helps improve predictions." │ │  Backend Action:          │
│                               │ │  POST /api/v2/target-     │
│  ✓ Survey Complete            │ │       survey/correction   │
│  Total Time: 3 minutes        │ │  {                        │
│                               │ │    rating: 2,             │
└───────────────────────────────┘ │    predictionShown: 79,   │
                                  │    correctedRate: 52      │
                                  │  }                        │
                                  │                           │
                                  │  Database Entry:          │
                                  │  {                        │
                                  │    label: {               │
                                  │      success_rate: 52,    │
                                  │      source: "corrected"  │
                                  │    },                     │
                                  │    feedbackData: {        │
                                  │      error: -27           │
                                  │    }                      │
                                  │  }                        │
                                  │                           │
                                  │  UI Response:             │
                                  │  "Thank you! This helps   │
                                  │   our model learn."       │
                                  │                           │
                                  │  Total Time: 13 minutes   │
                                  └───────────────────────────┘
```

**Feedback Data Captured:**

| Field | Description | Example Value |
|-------|-------------|---------------|
| `predictionShown` | The ML prediction displayed | 79 |
| `rating` | Student's accuracy rating | 2 (1-5 scale) |
| `correctedRate` | Student-provided actual rate (if correction) | 52 |
| `predictionError` | correctedRate - predictionShown | -27 |
| `absoluteError` | \|predictionError\| | 27 |
| `source` | Label source type | "pseudo_label" or "corrected" |

---

## 4. Design Considerations

### 4.1 Accessibility Features

The ACOSUS frontend is designed with WCAG 2.1 AA compliance in mind:

**Semantic HTML:**
- Proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`)
- Semantic elements (`<nav>`, `<main>`, `<article>`, `<section>`)
- Button elements for interactive controls (not styled divs)
- Form labels properly associated with inputs

**ARIA Attributes:**
```tsx
// Example from QuizCard component
<Card role="region" aria-label="Target Surveys Section">
  <div role="list" aria-label="Target survey cards">
    {quizzes.map((quiz) => (
      <QuizCard
        key={quiz.quizId}
        quiz={quiz}
        role="listitem"
        aria-selected={isSelected}
        aria-disabled={isBlocked}
      />
    ))}
  </div>
</Card>
```

**Keyboard Navigation:**
- All interactive elements focusable via Tab key
- Enter/Space to activate buttons
- Arrow keys for radio groups and menus
- Escape to close modals and dropdowns
- Focus trap in modal dialogs

**Color & Contrast:**
- Minimum 4.5:1 contrast ratio for text
- Status indicators use both color and icons
- Dark mode support with appropriate contrast

**Screen Reader Support:**
- Descriptive button labels (not just icons)
- Progress announcements during form submission
- Error messages linked to form fields
- Dynamic content updates announced

### 4.2 Mobile Responsiveness

**Tailwind Breakpoints (Mobile-First):**

| Breakpoint | Width | Usage |
|------------|-------|-------|
| Default | < 640px | Mobile phones |
| `sm` | ≥ 640px | Large phones |
| `md` | ≥ 768px | Tablets |
| `lg` | ≥ 1024px | Laptops |
| `xl` | ≥ 1280px | Desktops |
| `2xl` | ≥ 1536px | Large monitors |

**Responsive Patterns:**

1. **Navigation:**
   - Mobile: Hamburger menu with slide-out drawer
   - Desktop: Full sidebar with collapse toggle

2. **Dashboard Cards:**
   ```tsx
   <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
     {quizzes.map(quiz => <QuizCard key={quiz.id} {...quiz} />)}
   </div>
   ```

3. **Data Tables:**
   - Mobile: Card-based view with stacked fields
   - Desktop: Full table with horizontal scrolling if needed

4. **Forms:**
   - Single column on mobile
   - Multi-column on larger screens
   - Touch-friendly input sizes (minimum 44x44px tap targets)

5. **Survey Interface:**
   - Full-width questions on mobile
   - Side navigation hidden on mobile (use prev/next buttons)
   - Large touch targets for radio/checkbox options

### 4.3 User Experience Optimizations

**1. Auto-Save with Debouncing:**
- 2-second debounce prevents excessive API calls
- Visual indicator shows save status ("Saving...", "Saved ✓")
- localStorage fallback for offline resilience

```typescript
// useAutoSaveV2 hook pattern
const debouncedSave = useDebouncedCallback(
  async (answers) => {
    setIsSaving(true);
    await saveBulkAnswers(answers);
    setIsSaving(false);
    setLastSaved(new Date());
  },
  2000
);
```

**2. Optimistic Updates:**
- UI updates immediately on action
- Background sync with server
- Rollback on error with toast notification

**3. Loading States:**
- Skeleton loaders for content areas
- Spinner overlays for form submissions
- Progress bars for multi-step processes

**4. Error Handling:**
- Toast notifications for non-blocking errors
- Modal dialogs for critical errors
- Retry options for failed operations
- Clear error messages with suggested actions

**5. Offline Support:**
- Network status detection
- Warning banner when offline
- localStorage persistence for unsaved work
- Auto-sync when connection restored

```tsx
// Offline detection example
const isOffline = !navigator.onLine;

{isOffline && (
  <Alert variant="warning">
    <AlertTitle>You're offline</AlertTitle>
    <AlertDescription>
      Your answers are saved locally. They will sync when you reconnect.
    </AlertDescription>
  </Alert>
)}
```

**6. Progress Tracking:**
- Category-by-category completion indicators
- Overall quiz progress percentage
- Profile completion progress banner
- System-wide bootstrap progress (early adoption)

**7. Confirmation Dialogs:**
- Unsaved changes warning on navigation
- Delete confirmation for destructive actions
- Submission confirmation with preview

### 4.4 Performance Optimizations

**1. Code Splitting & Lazy Loading:**
```tsx
// React Router lazy loading
const AdminDashboard = lazy(() => import('./pages/admin/Dashboard'));
const StudentQuiz = lazy(() => import('./pages/student/Quiz'));

<Route
  path="/app/admin"
  element={
    <Suspense fallback={<LoadingSpinner />}>
      <AdminDashboard />
    </Suspense>
  }
/>
```

**2. React Query Caching:**
```typescript
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 2 * 60 * 1000, // 2 minutes
      gcTime: 24 * 60 * 60 * 1000, // 24 hours
      refetchOnWindowFocus: true,
      retry: (failureCount, error) => {
        // Don't retry auth errors
        if (error?.response?.status === 401) return false;
        return failureCount < 3;
      },
    },
  },
});
```

**3. Image Optimization:**
- SVG icons for UI elements
- Lazy loading for images
- Appropriate image compression

**4. Bundle Size Management:**
- Tree shaking for unused code
- Dynamic imports for large components
- Vite build optimization

### 4.5 Security Considerations

**1. Authentication:**
- JWT tokens stored securely
- Automatic token refresh
- Logout clears all session data

**2. Input Validation:**
- Zod schemas for all form inputs
- Server-side validation (defense in depth)
- XSS prevention via React's built-in escaping

**3. Protected Routes:**
```tsx
// Role-based route protection
<Route
  path="/app/admin/*"
  element={
    <ProtectedRoute allowedRoles={['admin']}>
      <AdminLayout />
    </ProtectedRoute>
  }
/>
```

**4. API Security:**
- Authorization header on all requests
- CORS configuration
- Rate limiting (server-side)

---

## 5. Component Architecture Summary

### 5.1 Directory Structure

```
src/
├── components/
│   ├── ui/                    # Base UI components (Radix + shadcn)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── ...
│   ├── custom/                # Custom components
│   │   ├── app-shell.tsx
│   │   ├── sidebar.tsx
│   │   ├── common-data-table.tsx
│   │   └── ...
│   ├── route/                 # Routing components
│   │   ├── protected-route.tsx
│   │   └── roleRouter.tsx
│   └── student/               # Student-specific components
│       └── search/
├── pages/
│   ├── student/               # Student pages
│   │   ├── dashboard/
│   │   ├── quizzes/
│   │   │   └── quiz/
│   │   │       └── components/
│   │   │           ├── studentQuizFormWithHooks2V2.tsx
│   │   │           └── hooks/
│   │   │               ├── useQuizForm.ts
│   │   │               └── useLocalStorageAnswers.ts
│   │   └── profile/
│   ├── admin/                 # Admin pages
│   │   ├── dashboard/
│   │   ├── quizzes/
│   │   └── users/
│   ├── advisor/               # Advisor pages
│   │   ├── dashboard/
│   │   └── students/
│   ├── auth/                  # Authentication pages
│   └── www/                   # Public website pages
├── contexts/
│   ├── UserContext.tsx        # Authentication state
│   ├── WorkflowContext.tsx    # Survey workflow state
│   └── StudentContext.tsx     # Advisor-acting context
├── service/
│   └── v2/                    # API services
│       ├── student/
│       │   ├── workflow/
│       │   ├── quiz/
│       │   └── attempt/
│       ├── admin/
│       └── advisor/
├── hooks/                     # Custom React hooks
│   ├── useQuizForm.ts
│   └── useAutoSaveV2.ts
├── lib/                       # Utilities
│   ├── axiosV2.ts
│   └── logger.ts
├── constants/                 # Route and API constants
├── assets/                    # Static assets
├── main.tsx                   # App entry point
└── mainRouter.tsx             # Router configuration
```

### 5.2 Key Custom Hooks

| Hook | Purpose | Used In |
|------|---------|---------|
| `useQuizForm` | Complete quiz form state and logic | Student quiz pages |
| `useQuizV2` | Fetch quiz content and previous answers | Quiz components |
| `useLocalStorageAnswers` | Persist answers locally | Quiz auto-save |
| `useAutoSaveV2` | Debounced auto-save to backend | Quiz components |
| `useSubmitBulkAnswersV2` | Batch answer submission | Quiz completion |
| `useGetWorkflowStatusV2` | Fetch survey workflow state | WorkflowContext |
| `useUser` | Authentication state and mutations | Auth components |

---

## 6. Figure Placement Summary

| Figure ID | Description | Suggested Location |
|-----------|-------------|-------------------|
| 2.2-1 | Landing Page Screenshot | After Landing/Onboarding section |
| 2.3-1 | Login Page Screenshot | After Authentication Pages section |
| 2.4-1 | Student Dashboard Screenshot | After Student Dashboard section |
| 2.5-1 | Survey Interface Screenshot | After Survey Interface section |
| 2.5-2 | Auto-Save Indicator | After Survey Interface section |
| 2.6-1 | Prediction Display Screenshot | After Prediction Display section |
| 2.7-1 | Feedback Submission Screenshot | After Feedback Collection section |
| 2.7-2 | Correction Request Screenshot | After Feedback Collection section |
| 2.8-1 | Student Profile Page | After Profile Management section |
| 2.9-1 | Admin Dashboard Overview | After Admin Dashboard section |
| 2.9-2 | Admin Dashboard Students Tab | After Admin Dashboard section |
| 2.10-1 | Quiz List Page | After Quiz Management section |
| 2.10-2 | Quiz Question Editor | After Quiz Management section |
| 2.11-1 | Advisor Student Search | After Advisor Dashboard section |
| 2.11-2 | Advisor Student Profile View | After Advisor Dashboard section |

---

## Document Metadata

- **Last Updated:** December 2024
- **Status:** Production (deployed at acosus.neiu.edu)
- **Frontend Version:** 0.0.1
- **React Version:** 18.3.1
- **Build Tool:** Vite 5.3.1
