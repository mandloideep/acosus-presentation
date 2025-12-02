# Section 3: System Design and Architecture

## 3.1 Overview

This section presents the design and architecture of ACOSUS (AI-Driven Counseling System for Underrepresented Transfer Students), a web-based platform developed to address the academic advising challenges faced by transfer students in computing programs. The system architecture was designed to satisfy four primary objectives: (1) providing advisors with a centralized data platform, (2) solving the cold start problem in machine learning for small cohorts, (3) enabling progressive model evolution as data accumulates, and (4) reducing survey burden through intelligent feedback mechanisms.

The architectural decisions described herein were informed by the unique constraints of transfer student populations, where cohort sizes are typically small (10-50 students initially) and traditional machine learning approaches requiring large training datasets are impractical [CITATION NEEDED].

## 3.2 System Requirements

### 3.2.1 Functional Requirements

The system was designed to address the following functional requirements derived from the needs analysis conducted with academic advisors and transfer student success research [CITATION NEEDED]:

**For Students:**
- Self-service survey completion for demographic and academic data collection
- Visualization of predicted success rates with explanatory context
- Feedback mechanisms for prediction accuracy assessment
- Profile management and progress tracking capabilities

**For Academic Advisors:**
- Centralized access to student profiles and survey responses
- Ability to complete surveys on behalf of students during advising sessions
- Dashboard analytics for cohort-level insights
- Intervention recommendations based on predicted risk levels

**For System Administrators:**
- Survey instrument configuration and management
- Machine learning model training initiation and monitoring
- User role management and access control
- System-wide analytics and reporting

### 3.2.2 Non-Functional Requirements

The system architecture addresses the following non-functional requirements:

| Requirement | Specification |
|-------------|---------------|
| Scalability | Support for 2-3 backend instances with 12 concurrent request handlers |
| Availability | Container-based deployment with automatic restart policies |
| Security | TLS 1.2+ encryption, role-based access control, IRB-compliant data handling |
| Usability | WCAG 2.1 AA compliance, mobile-responsive design |
| Performance | API response times under 300ms for standard operations |

## 3.3 High-Level Architecture

### 3.3.1 Three-Tier Architecture

ACOSUS employs a three-tier architecture consisting of a presentation layer, business logic layer, and data/ML layer. This separation of concerns enables independent scaling and maintenance of each component while facilitating the integration of machine learning capabilities.

[FIGURE 1: High-Level System Architecture Diagram]

The architecture comprises three primary components:

1. **Frontend Application** (Presentation Layer): A React-based single-page application providing role-specific interfaces for students, advisors, and administrators.

2. **Backend API Server** (Business Logic Layer): A Node.js/Express application handling authentication, survey management, success rate calculation, and orchestration of ML predictions.

3. **Model Server** (Data/ML Layer): A Python/Flask service responsible for machine learning model training, synthetic data generation, and prediction inference.

### 3.3.2 Technology Stack

The technology selection was guided by requirements for type safety, developer productivity, and established machine learning ecosystem support.

[TABLE 1: Technology Stack Overview]

| Layer | Technology | Version | Justification |
|-------|------------|---------|---------------|
| Frontend | React, TypeScript | 18.3.1, 5.x | Component-based architecture, type safety |
| Build Tool | Vite | 5.3.1 | Fast development builds, optimized production bundles |
| State Management | TanStack Query | 5.45.1 | Server state caching, optimistic updates |
| UI Components | Radix UI, Tailwind CSS | various, 3.4.4 | Accessible primitives, utility-first styling |
| Backend Runtime | Node.js | 20 LTS | Non-blocking I/O, JavaScript ecosystem |
| Web Framework | Express.js | 4.19.x | Minimal, flexible HTTP server |
| Database | MongoDB | 7.0 | Document flexibility for survey responses |
| ODM | Mongoose | 8.4.x | Schema validation, query building |
| ML Runtime | Python | 3.12 | Scientific computing ecosystem |
| ML Frameworks | TensorFlow, scikit-learn | 2.x, 1.x | Neural networks, classical ML algorithms |
| Containerization | Docker | - | Environment consistency, deployment isolation |
| Reverse Proxy | Nginx | - | Load balancing, SSL termination |

## 3.4 Component Architecture

### 3.4.1 Frontend Architecture

The frontend application implements a role-based routing architecture with distinct interfaces for each user type. The application structure follows the container/presentational component pattern, separating data fetching logic from UI rendering.

**Key Architectural Decisions:**

*Context-Based State Management*: Global application state is managed through React Context providers for authentication (`UserContext`), survey workflow (`WorkflowContext`), and advisor-on-behalf-of-student operations (`StudentContext`). This approach was selected over centralized state management libraries to reduce complexity while maintaining predictable state flows.

*Service Layer Abstraction*: API communication is abstracted through a service layer that provides React Query hooks for each API domain. This pattern enables automatic caching, background refetching, and optimistic updates while decoupling UI components from HTTP concerns.

*Survey Auto-Save Mechanism*: The survey interface implements a debounced auto-save pattern with 2-second delay, dual persistence to localStorage and backend API, and visual save status indicators. This design prevents data loss during network interruptions while minimizing server requests.

[FIGURE 2: Frontend Component Architecture]

### 3.4.2 Backend Architecture

The backend follows a layered architecture pattern with clear separation between routing, controllers, services, and data access:

```
Routes → Controllers → Services → Models
   ↓          ↓            ↓          ↓
 HTTP    Validation   Business    Database
Routing  & Response    Logic      Operations
```

**Routing Layer**: Routes are organized by API version (v1 legacy, v2 primary) and user role (public, student, advisor, admin). This organization enables independent evolution of API contracts while maintaining backward compatibility.

**Controller Layer**: Controllers handle request validation using Zod schemas, extract request parameters, and format responses. Controllers contain no business logic, delegating all operations to the service layer.

**Service Layer**: Services encapsulate business logic including survey workflow management, success rate calculation, model training orchestration, and prediction request handling. Services are designed as stateless functions to facilitate testing and horizontal scaling.

**Model Layer**: MongoDB document schemas are defined using Mongoose with comprehensive validation rules, virtual properties, and pre/post hooks for audit trail maintenance.

### 3.4.3 Model Server Architecture

The Model Server is implemented as a Flask application providing REST endpoints for machine learning operations. The architecture supports asynchronous training job execution through a queue-based system with progress callbacks to the backend.

**Key Components:**

*Training Queue Manager*: Long-running training jobs are queued and executed in background threads, preventing HTTP timeout issues. Progress updates are communicated to the backend through callback endpoints.

*Model Storage*: Trained models are persisted as HDF5 files (neural networks) and pickle files (scalers) in a shared Docker volume accessible to all model server instances.

*Prediction Pipeline*: Inference requests load cached model artifacts, apply feature preprocessing using stored scalers, and return predictions with timing metrics.

[FIGURE 3: Model Server Component Architecture]

## 3.5 Novel Architectural Contributions

### 3.5.1 Dual-Survey Architecture

A key architectural innovation in ACOSUS is the separation of ground truth collection (Target Survey) from feature collection (Factor Survey). This separation enables the progressive learning framework by allowing the system to:

1. Train models to predict success from features alone
2. Reduce survey burden for students after initial model training
3. Enable pseudo-labeling through the feedback loop mechanism

[FIGURE 4: Dual-Survey System Architecture]

The dual-survey architecture addresses a fundamental limitation of traditional approaches where features and outcomes are collected simultaneously, preventing the system from using features to predict outcomes for new students.

### 3.5.2 Progressive Learning Framework

The system implements a progressive learning framework that automatically transitions between model types based on available data:

[TABLE 2: Progressive Learning Phases]

| Phase | Student Count | Model | Training Trigger |
|-------|---------------|-------|-----------------|
| Bootstrap | 0-9 | None | Data collection only |
| Initial Prediction | 10-99 | K-Nearest Neighbors | First 10 students with completed surveys |
| Enhanced Prediction | 100+ | GAN + Neural Network | GAN generates synthetic data for NN training |

**Phase 1 (Bootstrap)**: During initial data collection, all students complete both Target and Factor surveys. No predictions are generated, and data accumulates for model training.

**Phase 2 (KNN Deployment)**: At 10 students, K-Nearest Neighbors is trained. KNN was selected for this phase because it is instance-based (no parameter fitting required), effective with small datasets, and provides interpretable results ("students similar to you achieved...") [CITATION NEEDED].

**Phase 3 (Neural Network with GAN Augmentation)**: At 100 students, a Conditional GAN generates synthetic training data (4x multiplier), enabling neural network training that would otherwise require 1000+ samples. Critically, validation is performed exclusively on real student data to ensure generalization [CITATION NEEDED].

### 3.5.3 Pseudo-Labeling Feedback Loop

The feedback loop mechanism reduces survey burden by using high-confidence predictions as ground truth labels:

[FIGURE 5: Feedback Loop Architecture]

1. Student completes Factor Survey (~3 minutes)
2. System generates prediction using trained model
3. Student rates prediction accuracy (1-5 stars)
4. **High rating (≥4 stars)**: Prediction accepted as pseudo-label; Target Survey skipped
5. **Low rating (<4 stars)**: Student redirected to Target Survey for correction

This approach reduces average survey time from 18 minutes to approximately 5 minutes for students enrolled after model training, while simultaneously generating training data for model improvement.

### 3.5.4 Priority-Weighted Response Scoring (PWRS)

For multi-question Target Surveys, the system calculates success rates using the Priority-Weighted Response Scoring formula, inspired by Item Response Theory [CITATION NEEDED]:

$$S_{final} = \frac{100}{1 + e^{-k\left(\frac{\sum_{i=1}^{n} \left(\frac{w_i^{selected}}{w_i^{max}} \times p_i\right)}{\sum_{i=1}^{n} p_i} - 0.5\right)}}$$

Where:
- $w_i^{selected}$ = weightage of selected answer option
- $w_i^{max}$ = maximum possible weightage for question $i$
- $p_i$ = priority score (1-10) indicating question importance
- $k$ = steepness parameter (default: 6)

The logistic calibration function prevents unrealistic extreme scores (rarely 0% or 100%) and produces an S-shaped distribution reflecting empirical success rate patterns [CITATION NEEDED].

## 3.6 Data Flow Architecture

### 3.6.1 Survey Submission Flow

Survey responses flow through multiple processing stages:

1. **Client Validation**: Zod schemas validate input before submission
2. **Debounced Persistence**: Answers auto-save with 2-second debounce
3. **Dual Write**: Answers stored in both `answers` collection and embedded in `attempts` document
4. **Normalization**: Responses converted to 0-10 scale for ML consumption
5. **Workflow Update**: Survey completion status updated for workflow tracking

### 3.6.2 Prediction Generation Flow

Prediction requests traverse the following path:

1. Backend receives completion notification for Factor Survey
2. Active model metadata retrieved from database
3. Student answers normalized to feature vector
4. Request forwarded to Model Server via internal HTTP
5. Model loaded from shared volume (cached after first load)
6. Inference executed, prediction returned
7. Prediction stored in `predictionRequests` collection
8. Student presented with prediction and feedback interface

### 3.6.3 Model Training Flow

Training follows an asynchronous pattern:

1. Administrator initiates training via admin interface
2. Backend aggregates training data from completed attempts
3. Training job queued on Model Server
4. Synthetic data generation (if GAN phase)
5. Model training with progress callbacks
6. Validation on real student data only
7. Model artifacts saved to shared volume
8. Backend notified of completion with metrics
9. Administrator sets trained model as active

[FIGURE 6: Data Flow Architecture Diagram]

## 3.7 Deployment Architecture

### 3.7.1 Containerized Microservices

The production deployment utilizes Docker containerization with the following service topology:

[TABLE 3: Container Configuration]

| Service | Instances | CPU | Memory | Purpose |
|---------|-----------|-----|--------|---------|
| Frontend | 2 | 2 cores | 1 GB | React SPA serving via Nginx |
| Backend | 3 | 4 cores | 10 GB | API server (4 workers each) |
| Model | 3 | 4 cores | 4 GB | ML training and inference |

Total resource allocation: 30 CPU cores, 46 GB RAM across 8 container instances.

### 3.7.2 Load Balancing and Networking

Nginx serves as the reverse proxy with least-connections load balancing across backend and frontend pools. Three isolated Docker networks segment traffic:

- **Frontend Network**: Frontend-to-backend communication
- **Backend Network**: Backend services and database connections
- **ML Network**: Backend-to-model server communication

### 3.7.3 CI/CD Pipeline

Deployment automation is implemented through GitHub Actions:

1. Developer pushes to repository
2. Docker images built and pushed to Docker Hub
3. SSH deployment to production server
4. Environment configuration applied from secure repository
5. Rolling container restart with zero downtime
6. Database migrations executed via init container

[FIGURE 7: Deployment Architecture Diagram]

## 3.8 Security Architecture

### 3.8.1 Authentication and Authorization

The system implements JWT-based authentication with automatic token refresh:

- **Access Token**: Short-lived, stored in HTTP-only cookies
- **Refresh Token**: Long-lived, stored in database for revocation capability
- **Auto-Refresh**: Tokens refreshed when within 12 hours of expiration

Role-based access control restricts API endpoints based on user role (student, advisor, admin, moderator).

### 3.8.2 Data Protection

Data protection measures include:

- **Encryption at Rest**: MongoDB Atlas AES-256 encryption
- **Encryption in Transit**: TLS 1.2+ for all communications
- **Password Security**: bcrypt hashing with 10 salt rounds
- **Audit Trail**: All data modifications tracked with user ID, role, and timestamp
- **Soft Delete**: Deleted records retained for audit compliance

### 3.8.3 Privacy Compliance

The system design incorporates privacy requirements from the IRB-approved research protocol (NEIU Protocol #202):

- Informed consent with explicit agreement tracking
- Data usage limited to research purposes
- Personal identifiers stored separately from analytical data
- Student right to access, correction, and withdrawal honored

## 3.9 Design Decisions and Trade-offs

### 3.9.1 MongoDB vs. Relational Database

MongoDB was selected over relational databases for the following reasons:

**Advantages:**
- Schema flexibility for heterogeneous survey responses
- Document model aligns with survey/attempt aggregation patterns
- Native JSON representation simplifies API serialization

**Trade-offs:**
- Lack of referential integrity requires application-level validation
- Complex aggregations require careful index planning
- Transaction support limited (though improved in MongoDB 4.0+)

### 3.9.2 Monolithic Backend vs. Microservices

The backend was implemented as a modular monolith rather than fully decomposed microservices:

**Rationale:**
- Research prototype prioritizing development velocity
- Team size does not warrant operational complexity of microservices
- ML Server separated due to distinct technology stack (Python vs. Node.js)

### 3.9.3 KNN for Cold Start

K-Nearest Neighbors was selected for initial predictions over other algorithms:

**Advantages:**
- No training phase (instance-based)
- Works with 10 samples (minimum for 5-fold CV with k=3)
- Interpretable ("students like you...")
- Non-parametric (no distribution assumptions)

**Limitations:**
- Linear prediction time growth with dataset size
- Memory scales with dataset size
- Sensitive to feature scaling (mitigated by normalization)

## 3.10 Limitations and Future Work

The current architecture has the following limitations that inform future development:

1. **Single-Institution Deployment**: Architecture designed for single-institution use; multi-institution federation would require identity federation and data sharing agreements.

2. **Synchronous Prediction**: Current prediction flow is synchronous; high-latency models would benefit from asynchronous prediction with notification.

3. **Model Interpretability**: Neural network predictions lack built-in explanations; integration of SHAP or LIME would enhance transparency.

4. **Horizontal Scaling**: While the architecture supports multiple instances, database scaling relies on MongoDB Atlas managed services rather than custom sharding.

## 3.11 Summary

This section presented the design and architecture of ACOSUS, highlighting the novel dual-survey architecture, progressive learning framework, and pseudo-labeling feedback loop that collectively address the cold start problem in transfer student success prediction. The three-tier architecture with containerized deployment provides scalability and maintainability, while the security architecture ensures compliance with research ethics requirements.

The architectural innovations enable the system to generate predictions with as few as 10 students—a significant improvement over traditional approaches requiring 1000+ samples—while progressively improving accuracy as the cohort grows.

---

## Figures and Tables Summary

| ID | Description | Status |
|----|-------------|--------|
| [FIGURE 1] | High-Level System Architecture Diagram | Placeholder |
| [FIGURE 2] | Frontend Component Architecture | Placeholder |
| [FIGURE 3] | Model Server Component Architecture | Placeholder |
| [FIGURE 4] | Dual-Survey System Architecture | Placeholder |
| [FIGURE 5] | Feedback Loop Architecture | Placeholder |
| [FIGURE 6] | Data Flow Architecture Diagram | Placeholder |
| [FIGURE 7] | Deployment Architecture Diagram | Placeholder |
| [TABLE 1] | Technology Stack Overview | Complete |
| [TABLE 2] | Progressive Learning Phases | Complete |
| [TABLE 3] | Container Configuration | Complete |

---

## Citations Needed

- Transfer student success research (Section 3.2.1)
- Cold start problem in ML literature (Section 3.3.1)
- KNN effectiveness with small datasets (Section 3.5.2)
- GAN data augmentation for small datasets (Section 3.5.2)
- Item Response Theory foundation for PWRS (Section 3.5.4)
- Success rate distribution patterns (Section 3.5.4)
