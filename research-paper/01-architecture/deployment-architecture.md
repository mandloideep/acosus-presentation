# ACOSUS Deployment Architecture

## Overview

The ACOSUS Cybersecurity Training Platform employs a containerized microservices architecture deployed on an on-premise RHEL 9 server at Northeastern Illinois University. The system uses Docker for containerization, Nginx as a reverse proxy with load balancing, and GitHub Actions for CI/CD automation.

**Production Domain:** `https://cybersecurity.neiu.edu`

---

## Infrastructure Components Diagram

```
                                    INTERNET
                                        │
                                        ▼
                            ┌───────────────────────┐
                            │    RHEL 9 Server      │
                            │  cybersecurity.neiu.edu│
                            └───────────────────────┘
                                        │
                    ┌───────────────────┴───────────────────┐
                    │           NGINX (Host)                 │
                    │    Ports: 80 (→443), 443              │
                    │    SSL: /etc/pki/nginx/               │
                    │    Load Balancer: least_conn          │
                    └───────────────────────────────────────┘
                              │                    │
              ┌───────────────┘                    └───────────────┐
              │                                                    │
              ▼                                                    ▼
    ┌─────────────────────┐                          ┌─────────────────────┐
    │   FRONTEND POOL     │                          │   BACKEND POOL      │
    │   (React + Nginx)   │                          │   (Express.js)      │
    └─────────────────────┘                          └─────────────────────┘
              │                                                    │
    ┌─────────┴─────────┐                    ┌─────────────────────┼─────────────────────┐
    │                   │                    │                     │                     │
    ▼                   ▼                    ▼                     ▼                     ▼
┌─────────┐       ┌─────────┐         ┌───────────┐         ┌───────────┐         ┌───────────┐
│frontend │       │frontend │         │ backend-1 │         │ backend-2 │         │ backend-3 │
│   -1    │       │   -2    │         │ :3001     │         │ :3002     │         │ :3003     │
│ :8081   │       │ :8082   │         │ 4 workers │         │ 4 workers │         │ 4 workers │
└─────────┘       └─────────┘         └───────────┘         └───────────┘         └───────────┘
                                             │                     │                     │
                                             └──────────┬──────────┘─────────────────────┘
                                                        │
                                             ┌──────────┴──────────┐
                                             │    MODEL POOL       │
                                             │   (Python/Flask)    │
                                             └─────────────────────┘
                                                        │
                                    ┌───────────────────┼───────────────────┐
                                    │                   │                   │
                                    ▼                   ▼                   ▼
                              ┌───────────┐       ┌───────────┐       ┌───────────┐
                              │  model-1  │       │  model-2  │       │  model-3  │
                              │   :5051   │       │   :5052   │       │   :5053   │
                              └───────────┘       └───────────┘       └───────────┘
                                    │                   │                   │
                                    └───────────────────┴───────────────────┘
                                                        │
                                                        ▼
                                             ┌─────────────────────┐
                                             │   SHARED VOLUME     │
                                             │   model_storage     │
                                             │   (ML Models)       │
                                             └─────────────────────┘

                                    ┌─────────────────────────────────────┐
                                    │         EXTERNAL SERVICES           │
                                    ├─────────────────────────────────────┤
                                    │  MongoDB Atlas (Cloud Database)    │
                                    │  PostHog Cloud (Analytics)         │
                                    │  Resend (Email Service)            │
                                    │  OpenAI API (AI Predictions)       │
                                    └─────────────────────────────────────┘
```

---

## Docker Container Architecture

### Container Overview

| Container | Image | Port(s) | Resources | Purpose |
|-----------|-------|---------|-----------|---------|
| `backend-init` | `aiacosus/backend-init:latest-prod` | None | - | Database migrations (runs once) |
| `frontend-1` | `aiacosus/frontend:latest-prod` | 8081:80 | 2 CPU, 1GB RAM | React SPA serving |
| `frontend-2` | `aiacosus/frontend:latest-prod` | 8082:80 | 2 CPU, 1GB RAM | React SPA serving |
| `backend-1` | `aiacosus/backend:latest-prod` | 3001:3000 | 4 CPU, 10GB RAM | API server (4 workers) |
| `backend-2` | `aiacosus/backend:latest-prod` | 3002:3000 | 4 CPU, 10GB RAM | API server (4 workers) |
| `backend-3` | `aiacosus/backend:latest-prod` | 3003:3000 | 4 CPU, 10GB RAM | API server (4 workers) |
| `model-1` | `aiacosus/model:latest-prod` | 5051:5051 | 4 CPU, 4GB RAM | ML prediction service |
| `model-2` | `aiacosus/model:latest-prod` | 5052:5051 | 4 CPU, 4GB RAM | ML prediction service |
| `model-3` | `aiacosus/model:latest-prod` | 5053:5051 | 4 CPU, 4GB RAM | ML prediction service |

### Dockerfiles

The system uses separate Dockerfiles for development and production environments:

#### Backend Dockerfile (Production)
- **Base Image:** `node:lts-alpine` (Node 22)
- **Build Process:** TypeScript compilation, bcrypt native module rebuild
- **Entry Point:** `cluster.js` (multi-worker process management)
- **Security:** No secrets in image layers; runtime configuration via `.env` file
- **Location:** `backend/Dockerfile.prod`

#### Backend Init Dockerfile (Production)
- **Purpose:** Database migrations with distributed locking
- **Execution:** Runs once before backend containers start
- **Entry Point:** `node dist/init/run-migrations.js`
- **Exit Behavior:** Code 0 (success) or 1 (failure)
- **Location:** `backend/Dockerfile.init.prod`

#### Frontend Dockerfile (Production)
- **Build Stage:** `node:lts-alpine` for React/Vite compilation
- **Runtime Stage:** `nginx:alpine` for static file serving
- **Entry Point:** `docker-entrypoint.sh` (runtime config injection)
- **Security:** Environment variables injected at container startup, not build time
- **Location:** `frontend/Dockerfile.prod`

#### Model Dockerfile (Production)
- **Base Image:** `python:3.12-slim`
- **Dependencies:** HDF5 for TensorFlow/Keras model loading
- **Entry Point:** `python main.py` (Flask server)
- **Location:** `model/Dockerfile`

---

## Service Communication Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           REQUEST FLOW                                       │
└─────────────────────────────────────────────────────────────────────────────┘

1. USER REQUEST (HTTPS)
   │
   └──► https://cybersecurity.neiu.edu/
         │
         ▼
2. NGINX REVERSE PROXY (Host)
   │
   ├──► Route: /           → Frontend Pool (8081, 8082)
   │                         Load Balancer: least_conn
   │
   └──► Route: /api        → Backend Pool (3001, 3002, 3003)
                             Load Balancer: least_conn

3. FRONTEND CONTAINERS
   │
   └──► Serve React SPA (static files)
         │
         └──► API calls to /api/* (proxied by Nginx to backends)

4. BACKEND CONTAINERS
   │
   ├──► MongoDB Atlas (external cloud database)
   │     Connection: mongodb+srv://...
   │
   ├──► Model Service (internal network)
   │     URL: http://model-{1,2,3}:5051
   │
   └──► External Services
         ├──► PostHog Cloud (analytics)
         ├──► Resend (email)
         └──► OpenAI API (predictions)

5. MODEL CONTAINERS
   │
   ├──► Load ML models from shared volume
   │     Volume: model_storage:/app/models
   │
   └──► Callback to Backend (optional)
         URL: http://backend-{1,2,3}:3000
```

### Docker Networks

| Network | Purpose | Connected Services |
|---------|---------|-------------------|
| `frontend` | Frontend-to-backend communication | frontend-1, frontend-2, backend-* |
| `backend` | Backend services and database proxies | backend-*, model-* |
| `ml` | Backend-to-model service communication | backend-*, model-* |

---

## Deployment Strategy

### CI/CD Pipeline (GitHub Actions)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CI/CD WORKFLOW                                        │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │   DEVELOPER     │
                    │   Push to Git   │
                    └────────┬────────┘
                             │
                             ▼
        ┌────────────────────────────────────────┐
        │         GitHub Actions Trigger          │
        │   (Manual workflow_dispatch or merge)   │
        └────────────────────┬───────────────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │  BUILD WORKFLOW │           │ DEPLOY WORKFLOW │
    │ build-prod.yml  │           │ deploy-prod.yml │
    └────────┬────────┘           └────────┬────────┘
             │                             │
             ▼                             │
    ┌─────────────────┐                    │
    │  Docker Build   │                    │
    │  & Push to Hub  │                    │
    │  Tag: latest-   │                    │
    │       prod      │                    │
    └────────┬────────┘                    │
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   SSH to RHEL 9     │
                 │   Production Server │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Clone acosus/env    │
                 │ (private secrets)   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Copy .env files to  │
                 │ service directories │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Download latest     │
                 │ docker-compose.yml  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Run deploy-service  │
                 │ .sh script          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ docker compose up   │
                 │ -d (rolling update) │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Cleanup old images  │
                 │ (prune > 72h)       │
                 └─────────────────────┘
```

### Deployment Process

1. **Build Phase** (GitHub Actions → Docker Hub)
   - Triggered manually via `workflow_dispatch` or on merge
   - Builds Docker image from specified branch
   - Pushes to Docker Hub with tags: `latest-prod`, `<git-sha>-prod`, optional custom tag

2. **Deploy Phase** (GitHub Actions → Production Server)
   - SSH connection to production server
   - Clone private `acosus/env` repository (contains secrets)
   - Copy environment files to service directories
   - Download latest `docker-compose.yml` from infra repository
   - Execute `deploy-service.sh` script
   - Rolling container restart with zero downtime

3. **Initialization** (Backend Init Container)
   - Runs database migrations before backend starts
   - Uses distributed locking to prevent race conditions
   - Backend containers wait for successful completion (`service_completed_successfully`)

---

## Production Configuration

### Nginx Configuration

**Location on Server:** `/etc/nginx/conf.d/acosus.conf`

| Configuration | Value |
|--------------|-------|
| HTTP Port | 80 (redirects to 443) |
| HTTPS Port | 443 |
| SSL Certificate | `/etc/pki/nginx/server.crt` |
| SSL Key | `/etc/pki/nginx/private/server.key` |
| SSL Protocols | TLSv1.2, TLSv1.3 |
| Load Balancing | `least_conn` (both pools) |
| Frontend Timeout | 60s |
| API Timeout | 300s (long-running requests) |

### Security Headers
- `X-Frame-Options: SAMEORIGIN`
- `X-XSS-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`

### Cookie Configuration
- HTTPOnly, Secure flags enabled
- SameSite=None for cross-origin authentication
- Domain rewrite: localhost → cybersecurity.neiu.edu

---

## Environment Variables

### Backend Environment

| Variable | Purpose |
|----------|---------|
| `MONGODB_URI` | MongoDB Atlas connection string |
| `ACCESS_TOKEN_SECRET` | JWT access token signing |
| `REFRESH_TOKEN_SECRET` | JWT refresh token signing |
| `AUTH_SECRET` | General authentication secret |
| `RESEND_API_KEY` | Email service API key |
| `POSTHOG_PROD_API_KEY` | Analytics tracking key |
| `ML_ROOT_URL` | Model service URL (internal) |
| `CORS_ORIGIN` | Allowed CORS origins |
| `WORKERS` | Node.js cluster workers (4 in prod) |

### Frontend Environment

| Variable | Purpose |
|----------|---------|
| `VITE_API_URL` | API base URL (`/api` in production) |
| `VITE_POSTHOG_ENABLED` | Enable analytics |
| `VITE_POSTHOG_PROD_API_KEY` | PostHog project key |
| `VITE_POSTHOG_API_HOST` | PostHog API endpoint |

### Model Environment

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | OpenAI API for predictions |
| `EXPRESS_URL` | Backend callback URL |
| `FLASK_DEBUG` | Debug mode (False in prod) |

---

## Scaling and Resource Allocation

### Current Production Configuration

| Service | Instances | CPU (per instance) | Memory (per instance) |
|---------|-----------|-------------------|----------------------|
| Frontend | 2 | 2 cores | 1 GB |
| Backend | 3 | 4 cores | 10 GB |
| Model | 3 | 4 cores | 4 GB |
| **Total** | **8** | **30 cores** | **46 GB** |

### Backend Worker Configuration
Each backend instance runs 4 Node.js workers via cluster mode:
- **Total backend workers:** 3 instances × 4 workers = 12 concurrent request handlers

### Model Storage
- Shared Docker volume: `model_storage`
- SELinux compatibility: `:Z` flag for volume mounts
- All model instances share the same trained models

---

## Monitoring and Logging

### Log Configuration
- **Driver:** `json-file`
- **Max Size:** 200 MB per log file
- **Max Files:** 10 rotated files per container
- **Log Path:** Docker default (`/var/lib/docker/containers/`)

### Health Checks

| Service | Health Check Method | Interval |
|---------|-------------------|----------|
| Frontend | Nginx serves static files | Container restart policy |
| Backend | Node process exit check | 30s (Docker healthcheck) |
| Model | Flask `/health` endpoint | Container restart policy |
| Nginx | `/health` returns 200 OK | External monitoring |

### Analytics (PostHog Cloud)
- Frontend: Page views, user interactions, error tracking
- Backend: HTTP request tracking, error capture, user identification
- Dashboard: `https://app.posthog.com` (ACOSUS Production project)

---

## Rollback Procedures

### Quick Rollback (via GitHub Actions)
1. Navigate to Deploy workflow
2. Enter previous working tag (e.g., `v1`, previous git SHA)
3. Execute workflow

### Manual Rollback (via SSH)
```bash
ssh <user>@cybersecurity.neiu.edu
cd ~/app/infra/docker
export DOCKER_USERNAME=aiacosus
export TAG=<previous-working-tag>
docker pull ${DOCKER_USERNAME}/backend:${TAG}
docker pull ${DOCKER_USERNAME}/frontend:${TAG}
docker compose up -d
```

### Emergency: Disable Features
```bash
# Disable PostHog without rollback
sed -i 's/POSTHOG_ENABLED=true/POSTHOG_ENABLED=false/' ~/app/infra/backend/.env
docker compose restart backend-1 backend-2 backend-3
```

---

## Server Setup (On-Premise RHEL 9)

### Initial Setup Script
**Location:** `infra/scripts/setup-rhel.sh`

1. Install system packages (Docker, git, curl, jq)
2. Create `deploy` user with SSH access
3. Configure SELinux contexts for project directories
4. Clone infrastructure repository
5. Generate per-service SSH keys for GitHub access
6. Configure firewall (ports 80, 443)

### Directory Structure
```
/var/www/acosus/              # Alternative project root
~/app/infra/                  # Deploy user's working directory
    ├── docker/               # Docker compose files
    │   └── docker-compose.yml
    ├── frontend/             # Frontend .env
    │   └── .env
    ├── backend/              # Backend .env
    │   └── .env
    ├── model/                # Model .env
    │   └── .env
    └── ssl/                  # SSL certificates (if local)
```

---

## Development vs Production Comparison

| Aspect | Development | Production |
|--------|-------------|------------|
| **Compose File** | `docker-compose.dev.yml` | `docker-compose.yml` |
| **Database** | Local MongoDB (container) | MongoDB Atlas (cloud) |
| **Backend Instances** | 1 (single worker) | 3 (4 workers each) |
| **Frontend Instances** | 1 | 2 |
| **Model Instances** | 1 | 3 |
| **Hot Reload** | Enabled (nodemon, Vite HMR) | Disabled |
| **SSL** | None (HTTP) | TLS 1.2/1.3 |
| **Reverse Proxy** | Direct port access | Nginx load balancer |
| **Log Rotation** | None | 200MB × 10 files |
| **Resource Limits** | None | CPU/Memory per container |
| **PostHog** | Development project | Production project |

---

## References

- [DEV-SETUP.md](../../infra/docs/DEV-SETUP.md) - Development environment setup
- [V2-DEPLOYMENT-GUIDE.md](../../infra/docs/V2-DEPLOYMENT-GUIDE.md) - Complete deployment guide
- [V2-QUICK-DEPLOY.md](../../infra/docs/V2-QUICK-DEPLOY.md) - Quick deployment checklist
- Docker Compose: `infra/docker/docker-compose.yml`
- Nginx Config: `infra/nginx/nginx.prod.conf`
