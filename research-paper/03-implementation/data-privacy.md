# Data Collection, Storage, and Privacy

## Document Purpose
This document details ACOSUS's approach to data collection, storage, privacy protections, and access controls. It covers compliance considerations for educational research involving student data.

---

## 1. Data Collection

### 1.1 Types of Data Collected

ACOSUS collects three primary categories of student data:

#### Demographic Data
| Field | Type | Purpose | Required |
|-------|------|---------|----------|
| Gender | Enum | Demographic analysis | Optional |
| Age Group | Enum | Cohort analysis | Optional |
| Ethnicity | Enum | Underrepresented population tracking | Optional |
| First Generation Status | Boolean | Support targeting | Optional |

**Source**: [student.model.ts](../../../backend/src/models/student.model.ts) - `gender`, `ageGroup`, `ethnicity`, `isFirstGeneration` fields

#### Academic Records
| Field | Type | Purpose | Source |
|-------|------|---------|--------|
| Degree Type | Enum | Program classification | Profile survey |
| Major | String | Academic pathway | Profile survey |
| Student Status | Enum | Enrollment tracking | Profile survey |
| Previous Institution Type | Enum | Transfer pathway analysis | Profile survey |
| Student University ID | String | Institutional linkage | Manual entry |
| Current Semester | String | Progress tracking | Profile survey |
| Semester Subjects | Array | Course enrollment | Manual/integration |
| Grades | Map | Academic performance | Manual entry |
| Earned Credits | Number | Progress metrics | Calculated |
| Start/End Dates | Date | Program timeline | Profile survey |
| Success Rate | Number | Predicted/actual outcomes | ML model / surveys |

**Source**: [student.model.ts](../../../backend/src/models/student.model.ts) - Academic schema fields

#### Survey Response Data
| Survey Type | Data Collected | Frequency | Purpose |
|-------------|----------------|-----------|---------|
| **Factor Survey** | Success predictors (GPA, SAT, family support, learning preferences) | Once per enrollment + updates | ML model input features |
| **Target Survey** | Self-reported readiness/success rate | Early adoption phase | Ground truth labels for training |
| **Profile Questions** | Demographics, study habits, career goals | Registration + periodic updates | Student profiling |
| **Prediction Feedback** | 1-5 star rating | After each prediction | Model validation |

**Answer Data Structure** ([answer.model.ts](../../../backend/src/models/answer.model.ts)):
```typescript
{
  questionId: ObjectId,
  answer: string | number | boolean | string[] | number[] | boolean[],
  answerWeightage: number,        // Normalized value for ML
  answerScope: "quiz" | "profile",
  selectedOptionId: ObjectId[],
  modifiedBy: {
    userId: ObjectId,
    role: "student" | "advisor" | "admin",
    modifiedAt: Date
  }
}
```

### 1.2 Collection Methods

#### Self-Service Surveys
- **Registration Flow**: Students complete demographic profile and consent during account creation
- **Factor Surveys**: Periodic surveys measuring success predictors (5-10 questions, ~3 minutes)
- **Target Surveys**: Readiness self-assessment (during early adoption phase only)
- **Feedback Collection**: Star rating after viewing ML predictions

#### Manual Entry
- Academic advisors can update student profiles through admin interface
- Grade information entered manually per semester
- University ID linkage configured during onboarding

#### Planned Integrations
- **Note**: Direct integration with institutional SIS (Student Information Systems) is planned but not yet implemented
- Current data relies entirely on self-reported information

### 1.3 Data Quality Assurance

#### Input Validation
All survey responses are validated using Zod schemas before storage:

**Example Validation** ([validation/](../../../backend/src/validation/)):
```typescript
// Answer validation ensures:
// - Required fields present
// - Answer type matches question type
// - Values within expected ranges
// - Option IDs reference valid questions
```

#### Audit Trail
Every data modification tracks:
- **Who**: `createdBy`, `updatedBy`, `modifiedBy.userId`
- **Role**: `modifiedBy.role` (student, advisor, admin)
- **When**: `createdAt`, `updatedAt`, `modifiedBy.modifiedAt`

**Source**: [answer.model.ts:99-103](../../../backend/src/models/answer.model.ts#L99-L103)

#### Soft Delete Pattern
Data is never immediately destroyed:
- `isDeleted` flag marks records as removed
- Deleted records excluded from queries via partial filter expressions
- Allows recovery and audit compliance

---

## 2. Data Storage

### 2.1 Database Structure

ACOSUS uses **MongoDB** as its primary data store with the following collection organization:

```
┌─────────────────────────────────────────────────────────────────┐
│                         MongoDB                                  │
├─────────────────────────────────────────────────────────────────┤
│  Users Collection                                                │
│  ├── Authentication (email, hashed password, tokens)            │
│  ├── Role (admin, advisor, student, moderator)                  │
│  ├── Consent tracking (isAgreed, agreedAt, content snapshot)    │
│  └── Account status (isBlocked, isDeleted, timestamps)          │
├─────────────────────────────────────────────────────────────────┤
│  StudentProfiles Collection                                      │
│  ├── Demographics (gender, age, ethnicity)                      │
│  ├── Academic records (major, credits, grades)                  │
│  └── Linked to User via studentId                               │
├─────────────────────────────────────────────────────────────────┤
│  Answers Collection                                              │
│  ├── Survey responses (linked to attempts)                      │
│  ├── Modification tracking                                       │
│  └── Indexed: (attemptId, studentId, quizId)                    │
├─────────────────────────────────────────────────────────────────┤
│  Attempts Collection                                             │
│  ├── Quiz attempt metadata                                       │
│  ├── Workflow tracking (early_adoption vs production)           │
│  ├── ML predictions and feedback                                 │
│  └── Indexed: (studentId, quizId, attemptNumber)                │
├─────────────────────────────────────────────────────────────────┤
│  PredictionRequests Collection                                   │
│  ├── ML inference requests and results                          │
│  ├── Feature importance scores                                   │
│  └── Performance metrics                                         │
├─────────────────────────────────────────────────────────────────┤
│  ModelMetaData Collection                                        │
│  ├── Model versioning                                            │
│  ├── Training metrics (MAE, R², cross-validation)               │
│  └── Training data summary (anonymized counts)                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Data Encryption

#### At Rest
| Layer | Implementation | Status |
|-------|----------------|--------|
| Database | MongoDB Atlas encryption at rest (AES-256) | Enabled (Atlas default) |
| File Storage | Temporary PDFs in `/temp` directory | Unencrypted (short-lived, 2hr retention) |
| Credentials | GitHub Secrets + MongoDB Atlas | Managed secrets |

#### In Transit
| Layer | Implementation | Status |
|-------|----------------|--------|
| API Communication | HTTPS (TLS 1.2+) | Required in production |
| Database Connection | MongoDB Atlas TLS | Enabled |
| Cookie Transmission | `secure: true` in production | Implemented |

#### Cloud Infrastructure
ACOSUS uses **MongoDB Atlas** as the managed database service:
- **Encryption at Rest**: AES-256 encryption enabled by default on all Atlas clusters
- **Encryption in Transit**: TLS/SSL required for all connections
- **Network Security**: IP whitelisting and VPC peering available
- **Compliance**: Atlas is SOC 2 Type II, ISO 27001, and HIPAA eligible

#### Password Security
Passwords are **never stored in plaintext**:

```typescript
// Password hashing (user.auth.ts)
const hashedPassword = await bcrypt.hash(password, 10);  // 10 salt rounds

// Password verification (user.model.ts)
userSchema.methods.isPasswordCorrect = async function(password: string) {
  return await bcrypt.compare(password, this.password);
};
```

**Source**: [user.model.ts:201-205](../../../backend/src/models/user.model.ts#L201-L205)

### 2.3 Backup Strategies

| Component | Strategy | Status |
|-----------|----------|--------|
| MongoDB | MongoDB Atlas automated backups | Available (not yet configured) |
| ML Models | Versioned in ModelMetaData | Implemented |
| Configuration | GitHub Secrets | Version controlled |

**Note**: Formal backup strategy with defined retention periods is pending implementation. MongoDB Atlas provides continuous backups and point-in-time recovery capabilities that can be enabled.

### 2.4 Temporary File Management

Consent PDFs and other temporary files are automatically cleaned:

```typescript
// Cleanup job runs hourly (cleanupJob.ts)
cron.schedule("0 * * * *", cleanupOldFiles);

// Default retention: 2 hours
const TEMP_FILES_RETENTION_HOURS = config.tempFilesRetentionHours || 2;
```

**Source**: [cleanupJob.ts](../../../backend/src/jobs/cleanupJob.ts)

---

## 3. Privacy and Consent

### 3.1 Informed Consent Process

#### Pre-Registration Disclosure
Before creating an account, students must:
1. Read the full Informed Consent Form
2. Scroll to the bottom of the consent document
3. Explicitly agree by clicking "I Consent"

#### Consent Form Content
The IRB-approved consent form ([consent.json](../../../backend/src/init/data/consent.json)) includes:

**Study Information**:
- Title: "AN AI-DRIVEN COUNSELING SYSTEM FOR UNDERREPRESENTED TRANSFER STUDENTS"
- Principal Investigator: Dr. Xiwei Wang
- Institution: Northeastern Illinois University, Department of Computer Science
- IRB Protocol: #202 (approved 01/25/2023 under 45 CFR 46.110)

**Key Disclosures**:
- Data types collected (demographic, academic, social/behavioral, career goals)
- Periodic update requests
- Research purpose only
- Compensation ($10 Amazon gift card per data update)

**Confidentiality Statement**:
> "The data will only be used for research purposes and will not be shared with anyone beyond the study team. The computers that host these data will be password protected and the login credentials will not be shared with anyone other than the investigator him/herself. All personal identifiers will be stored in a separate file."

#### Consent Tracking
Each user's consent is stored with their account:

```typescript
consent: {
  title: string,           // Version title
  content: {
    html: string,          // Rendered consent form
    json: object,          // Structured content
    text: string           // Plain text version
  },
  isAgreed: boolean,       // Explicit consent flag
  agreedAt: Date           // Timestamp of agreement
}
```

**Source**: [user.model.ts:67-94](../../../backend/src/models/user.model.ts#L67-L94)

### 3.2 Data Usage Policies

#### Research-Only Use
- Data used exclusively for academic research purposes
- No commercial use or sale of student data
- No sharing beyond the study team

#### Data Minimization
- Only data necessary for ML model training and advising is collected
- Profile questions are optional where possible
- Sensitive fields use "prefer-not-to-say" options

### 3.3 Student Data Rights

#### Right to Access
- Students can view their profile data through the dashboard
- Survey responses are visible in attempt history
- Prediction history with feedback is accessible

#### Right to Correction
- Students can update profile information
- Advisors can correct data on students' behalf (tracked)
- All modifications maintain audit trail

#### Right to Deletion
Current implementation uses **soft delete**:
```typescript
// User model
isDeleted: Boolean,
deletedBy: ObjectId,
deletedAt: Date

// Data becomes inaccessible but retained for:
// - Audit compliance
// - Research integrity
// - Potential recovery
```

**Hard Deletion Process**:
- Students can request complete data removal via email to the research team
- Developer performs manual deletion from MongoDB Atlas upon verified request
- **Note**: Automated hard deletion workflow is not yet implemented

#### Right to Withdraw
- Students can request account deactivation via email
- Upon withdrawal request, all associated data can be permanently removed
- Consent withdrawal honored within reasonable timeframe

### 3.4 Compliance Considerations

#### FERPA (Family Educational Rights and Privacy Act)
| Requirement | ACOSUS Implementation |
|-------------|----------------------|
| Consent before disclosure | Required at registration |
| Access to records | Student dashboard access |
| Right to amend | Edit functionality available |
| Legitimate educational interest | Research purpose documented |

**Note**: ACOSUS is a research prototype; formal FERPA compliance for production deployment requires institutional coordination.

#### IRB Approval
- **Protocol**: NEIU Protocol #202
- **Approval Date**: January 25, 2023
- **Review Type**: Expedited (45 CFR 46.110)
- **Contact**: IRB@neiu.edu, (773) 442-4674

#### Data Protection Principles
| Principle | Implementation |
|-----------|----------------|
| Lawfulness | IRB-approved research protocol |
| Purpose Limitation | Research use only |
| Data Minimization | Optional demographic fields |
| Accuracy | Student self-update capability |
| Storage Limitation | **[ASK PROFESSOR]** - Retention period TBD |
| Integrity & Confidentiality | Password protection, role-based access |

---

## 4. Data Access Controls

### 4.1 Role-Based Access Control (RBAC)

ACOSUS implements four user roles with distinct permissions:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Access Control Matrix                         │
├──────────────┬─────────┬─────────┬─────────┬──────────┬────────┤
│ Resource     │ Student │ Advisor │ Admin   │Moderator │Researcher│
├──────────────┼─────────┼─────────┼─────────┼──────────┼────────┤
│ Own Profile  │ R/W     │ -       │ R/W     │ R        │ -      │
│ Other Profiles│ -      │ R/W*    │ R/W     │ R        │ Anon   │
│ Own Surveys  │ R/W     │ -       │ R       │ R        │ -      │
│ Other Surveys│ -       │ R       │ R/W     │ R        │ Anon   │
│ Predictions  │ Own     │ Assigned│ All     │ All      │ Anon   │
│ ML Models    │ -       │ -       │ R/W     │ R        │ R      │
│ System Config│ -       │ -       │ R/W     │ -        │ -      │
│ User Mgmt    │ -       │ -       │ R/W     │ R        │ -      │
│ Audit Logs   │ -       │ -       │ R       │ R        │ -      │
└──────────────┴─────────┴─────────┴─────────┴──────────┴────────┘

R = Read, W = Write, * = Assigned students only, Anon = Anonymized
```

**Role Definitions** ([constants.ts](../../../backend/src/utils/constants.ts)):
```typescript
ROLE_ADMIN = "admin"       // Full system access
ROLE_ADVISOR = "advisor"   // Student management
ROLE_STUDENT = "student"   // Self-service only
ROLE_MODERATOR = "moderator" // Read-only oversight
```

### 4.2 Authentication Mechanism

#### JWT Token Flow
```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Client  │────▶│   API    │────▶│  MongoDB │
└──────────┘     └──────────┘     └──────────┘
     │                │
     │  1. Login      │
     │───────────────▶│
     │                │ 2. Verify credentials
     │                │    (bcrypt compare)
     │◀───────────────│
     │  Access Token  │ 3. Generate JWT
     │  Refresh Token │
     │                │
     │  4. API Call   │
     │  + Access Token│
     │───────────────▶│
     │                │ 5. Verify JWT
     │                │    (check expiry)
     │◀───────────────│
     │  Response      │
```

**Token Configuration**:
| Token Type | Storage | Expiration | Auto-Refresh |
|------------|---------|------------|--------------|
| Access Token | Cookie/Header | Configurable | At 12hr remaining |
| Refresh Token | Cookie + DB | Configurable | On access token refresh |

**Source**: [auth.middleware.ts](../../../backend/src/middlewares/auth.middleware.ts)

#### Session Security
```typescript
// Cookie options (production)
{
  httpOnly: true,      // Prevents XSS access
  secure: true,        // HTTPS only
  sameSite: "strict"   // CSRF protection
}
```

### 4.3 Anonymization for Research

#### Training Data Anonymization
ML model training uses feature vectors without identifiers:

```python
# Feature vector contains only normalized survey responses
# No student IDs, emails, or names in training data
X = [[0.8, 0.6, 1.0, 0.7],  # Student features only
     [0.5, 0.4, 0.8, 0.6],
     ...]

y = [75, 62, ...]  # Success rates only
```

#### Research Data Export
For external research collaboration:
- Student identifiers replaced with anonymous IDs
- Demographic data aggregated (not individual)
- Currently developer-only access for exports
- **Note**: Formal anonymization pipeline and researcher access process can be developed as needed

### 4.4 Audit Logging

#### User Activity Tracking
| Event | Data Captured | Storage |
|-------|---------------|---------|
| Login | userId, timestamp, IP (via PostHog) | User model + Analytics |
| Survey Submission | attemptId, studentId, timestamp | Attempt model |
| Profile Update | modifiedBy, role, timestamp | Answer/StudentProfile |
| Admin Actions | userId, action, timestamp | Model audit fields |

#### PostHog Analytics Integration
```typescript
// Event capture for monitoring
posthog.captureEvent(distinctId, event, properties);
posthog.identifyUser(distinctId, properties);

// Configurable per environment
POSTHOG_ENABLED=true/false
```

**Source**: [posthog.service.ts](../../../backend/src/services/posthog/posthog.service.ts)

#### Model Training Audit
Complete audit trail for ML operations:

```typescript
// TrainingTriggerLog tracks:
{
  triggerType: "initial_knn" | "knn_retrain" | "gan_train" | "neural_train" | "manual",
  status: "pending" | "queued" | "training" | "completed" | "failed",
  triggeredAt: Date,
  queuedAt: Date,
  trainingStartedAt: Date,
  completedAt: Date,
  duration: number,
  error: { message, stack, code, isRetryable }
}
```

**Source**: [trainingTriggerLog.model.ts](../../../backend/src/models/trainingTriggerLog.model.ts)

---

## 5. Outstanding Items

### 5.1 Pending Professor Clarification
| Item | Question | Impact |
|------|----------|--------|
| Data Retention Period | How long should student data be retained after graduation/withdrawal? | Affects storage limitation compliance |
| Backup Retention | What retention period for database backups? | Affects disaster recovery policy |

### 5.2 Planned Improvements
| Feature | Status | Priority |
|---------|--------|----------|
| Automated hard deletion workflow | Not implemented | Medium |
| Formal researcher access request process | Not implemented | Low |
| MongoDB Atlas backup configuration | Available, not configured | High |
| Anonymization pipeline for research exports | Manual process | Medium |

---

## 6. Summary

### Security Posture
| Category | Status |
|----------|--------|
| Encryption at Rest | MongoDB Atlas AES-256 |
| Encryption in Transit | TLS enabled |
| Password Security | bcrypt (10 rounds) |
| Access Control | Role-based (4 roles) |
| Audit Logging | Comprehensive |
| Consent Management | IRB-compliant |

### Current Limitations
1. No automated backup retention policy
2. Hard deletion requires manual developer intervention
3. No formal researcher data access process
4. Data retention period undefined

---

## Document Metadata

- **Source**: ACOSUS Backend Repository Code Review
- **Models Reviewed**: user.model.ts, student.model.ts, answer.model.ts, attempt.model.ts
- **Infrastructure**: MongoDB Atlas (cloud-hosted)
- **Last Updated**: December 2024
- **Status**: Complete (pending professor input on retention policy)
