# 📋 DevOps Implementation Report

## Healthcare Management System - Final Exam Project

**Team Member 1:** Ali Turab, FA22-BSE-003
**Team Member 2:** Abdul Ahad, FA22-BSE-009
**Team Member 3:** Muhammad Umar, FA22-BSE-157
**Date:** December 18, 2025  
**Repository:** https://github.com/turabbb/Health-Care-Management-System-Python-FastAPI

---

## 📑 Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Overview](#2-project-overview)
3. [DevOps Implementation](#3-devops-implementation)
   - [3.1 Docker Containerization](#31-docker-containerization)
   - [3.2 Terraform Infrastructure](#32-terraform-infrastructure)
   - [3.3 Ansible Configuration](#33-ansible-configuration)
   - [3.4 Kubernetes Orchestration](#34-kubernetes-orchestration)
   - [3.5 CI/CD Pipeline](#35-cicd-pipeline)
   - [3.6 Monitoring Stack](#36-monitoring-stack)
4. [Architecture Diagrams](#4-architecture-diagrams)
5. [Testing & Quality Assurance](#5-testing--quality-assurance)
6. [Challenges & Solutions](#6-challenges--solutions)
7. [Conclusion](#7-conclusion)

---

## 1. Executive Summary

This report documents the complete DevOps implementation for a Healthcare Management System built with FastAPI. The project demonstrates proficiency in modern DevOps practices including containerization, infrastructure as code, configuration management, container orchestration, continuous integration/deployment, and monitoring.

### Key Achievements
- ✅ **Docker**: Full-stack containerization with 6 services
- ✅ **Terraform**: Infrastructure as Code with LocalStack (FREE)
- ✅ **Ansible**: Configuration management with roles
- ✅ **Kubernetes**: Complete K8s manifests with Kustomize overlays
- ✅ **CI/CD**: 8-stage GitHub Actions pipeline
- ✅ **Monitoring**: Prometheus + Grafana with custom dashboards
- ✅ **Cost**: $0.00 - All local/free tools used

---

## 2. Project Overview

### 2.1 Application Description
The Healthcare Management System is a RESTful API for managing:
- **Patients** - Registration, medical records, insurance info
- **Doctors** - Profiles, specializations, availability schedules
- **Appointments** - Booking, rescheduling, cancellation
- **Authentication** - JWT-based with role-based access control

### 2.2 Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Backend | FastAPI | 0.104.x |
| Language | Python | 3.11 |
| Database | PostgreSQL | 15 |
| Cache | Redis | 7 |
| Message Queue | RabbitMQ | 3.12 |
| Containerization | Docker | 24.x |
| Orchestration | Kubernetes | 1.28+ |
| IaC | Terraform | 1.6 |
| Config Mgmt | Ansible | 2.15+ |
| CI/CD | GitHub Actions | - |
| Monitoring | Prometheus + Grafana | 2.47 / 10.1 |

---

## 3. DevOps Implementation

### 3.1 Docker Containerization

#### 3.1.1 Docker Compose Architecture

```yaml
Services:
  ├── db (PostgreSQL)         - Port 5432
  ├── redis (Redis)           - Port 6379
  ├── rabbitmq (RabbitMQ)     - Port 5672, 15672
  ├── app (FastAPI)           - Port 8000
  ├── prometheus (Metrics)    - Port 9090
  └── grafana (Dashboards)    - Port 3000
```

#### 3.1.2 Key Features
- **Multi-stage builds** for optimized images
- **Health checks** for all services
- **Named volumes** for data persistence
- **Custom network** for service isolation
- **Environment variables** for configuration

#### 3.1.3 Docker Commands
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Scale application
docker-compose up -d --scale app=3

# Clean up
docker-compose down -v
```

#### 3.1.4 Screenshot Reference
- Docker containers running: `docker ps`
- Service health status: `docker-compose ps`

---

### 3.2 Terraform Infrastructure

#### 3.2.1 Infrastructure Components

Using **LocalStack** for AWS emulation (FREE, no cloud costs):

| Resource | Description | File |
|----------|-------------|------|
| VPC | Virtual Private Cloud | `vpc.tf` |
| Subnets | Public/Private subnets | `vpc.tf` |
| Security Groups | Firewall rules | `security_groups.tf` |
| Variables | Configuration | `variables.tf` |
| Outputs | Resource IDs | `outputs.tf` |

#### 3.2.2 Terraform Configuration

```hcl
# Provider configuration for LocalStack
provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    ec2 = "http://localhost:4566"
    s3  = "http://localhost:4566"
    rds = "http://localhost:4566"
  }
}
```

#### 3.2.3 Terraform Commands
```bash
# Initialize
terraform init

# Plan changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy (cleanup)
terraform destroy
```

#### 3.2.4 Screenshot Reference
- `terraform init` output
- `terraform plan` output
- `terraform apply` output

---

### 3.3 Ansible Configuration

#### 3.3.1 Playbook Structure

```
ansible/
├── ansible.cfg              # Ansible configuration
├── playbook.yml             # Main playbook
├── deploy-k8s.yml           # K8s deployment playbook
├── inventory/
│   ├── hosts.ini            # Static inventory
│   └── aws_ec2.yml          # Dynamic AWS inventory
├── roles/
│   ├── common/              # Common setup tasks
│   ├── docker/              # Docker installation
│   ├── kubernetes/          # K8s setup
│   └── monitoring/          # Monitoring setup
└── vars/
    ├── main.yml             # Main variables
    ├── dev.yml              # Development vars
    └── prod.yml             # Production vars
```

#### 3.3.2 Key Roles

**Common Role:**
- System updates
- Package installation
- User configuration

**Docker Role:**
- Docker CE installation
- Docker Compose setup
- Container runtime configuration

**Kubernetes Role:**
- kubectl installation
- Minikube setup
- Cluster configuration

**Monitoring Role:**
- Prometheus deployment
- Grafana setup
- Alert configuration

#### 3.3.3 Ansible Commands
```bash
# Run playbook
ansible-playbook -i inventory/hosts.ini playbook.yml

# Check syntax
ansible-playbook playbook.yml --syntax-check

# Dry run
ansible-playbook playbook.yml --check
```

---

### 3.4 Kubernetes Orchestration

#### 3.4.1 Kubernetes Resources

| Resource | File | Description |
|----------|------|-------------|
| Namespace | `namespace.yaml` | Isolated environment |
| Deployment | `deployment.yaml` | Application pods |
| Service | `service.yaml` | Load balancing |
| ConfigMap | `configmap.yaml` | Configuration |
| Secret | `secret.yaml` | Sensitive data |
| HPA | `hpa.yaml` | Auto-scaling |
| Ingress | `ingress.yaml` | External access |
| RBAC | `rbac.yaml` | Access control |

#### 3.4.2 Kustomize Overlays

```
k8s/
├── base/                    # Base manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   └── rbac.yaml
└── overlays/
    ├── dev/                 # Development config
    │   └── kustomization.yaml
    └── prod/                # Production config
        └── kustomization.yaml
```

#### 3.4.3 Kubernetes Commands
```bash
# Start Minikube
minikube start

# Deploy to dev environment
kubectl apply -k k8s/overlays/dev/

# Check pods
kubectl get pods -n healthcare

# Check services
kubectl get svc -n healthcare

# View logs
kubectl logs -f deployment/healthcare-api -n healthcare

# Access service
minikube service healthcare-api -n healthcare
```

#### 3.4.4 HPA Configuration
```yaml
spec:
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

### 3.5 CI/CD Pipeline

#### 3.5.1 Pipeline Stages

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   BUILD     │────▶│    LINT     │────▶│    TEST     │
│  (Python)   │     │  (flake8)   │     │  (pytest)   │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
┌─────────────────────────────────────────────▼───────┐
│                                                      │
▼                                                      │
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   DOCKER    │────▶│  TERRAFORM  │────▶│ KUBERNETES  │
│   Build     │     │    Plan     │     │   Deploy    │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
┌─────────────────────────────────────────────▼───────┐
│                                                      │
▼                                                      │
┌─────────────┐     ┌─────────────┐
│   SMOKE     │────▶│ PRODUCTION  │
│   TESTS     │     │   DEPLOY    │
└─────────────┘     └─────────────┘
```

#### 3.5.2 Pipeline Configuration

**File:** `.github/workflows/cicd-pipeline.yml`

| Stage | Trigger | Actions |
|-------|---------|---------|
| Build | Push to main | Install Python, dependencies |
| Lint | After build | Run flake8 |
| Test | After lint | Run pytest with coverage |
| Docker | After test | Build & push image |
| Terraform | After docker | Validate & plan |
| K8s Deploy | After terraform | Apply manifests |
| Smoke Tests | After deploy | Health check |
| Production | Manual approval | Deploy to prod |

#### 3.5.3 Key Pipeline Features
- **Matrix testing** - Multiple Python versions
- **Caching** - pip dependencies cached
- **Artifacts** - Test reports, coverage
- **Secrets** - Secure credential handling
- **Environment protection** - Manual approval for production

---

### 3.6 Monitoring Stack

#### 3.6.1 Prometheus Configuration

**Scrape Targets:**
```yaml
scrape_configs:
  - job_name: 'healthcare-api'
    static_configs:
      - targets: ['app:8000']
    metrics_path: '/metrics'
```

**Custom Metrics Exposed:**

| Metric | Type | Description |
|--------|------|-------------|
| `http_requests_total` | Counter | Total HTTP requests |
| `http_request_duration_seconds` | Histogram | Request latency |
| `http_requests_in_progress` | Gauge | Active requests |
| `system_cpu_usage_percent` | Gauge | CPU usage |
| `system_memory_usage_percent` | Gauge | Memory usage |
| `patients_registered_total` | Counter | Business metric |
| `doctors_registered_total` | Counter | Business metric |
| `appointments_created_total` | Counter | Business metric |

#### 3.6.2 Grafana Dashboard

**Dashboard Panels:**
1. **System Metrics**
   - CPU Usage (Gauge)
   - Memory Usage (Gauge)
   - Disk Usage (Gauge)

2. **Request Metrics**
   - HTTP Request Rate (Time Series)
   - Request Latency P95 (Time Series)
   - Requests by Status Code (Time Series)

3. **Business Metrics**
   - Total Requests (Stat)
   - Patients Registered (Stat)
   - Doctors Registered (Stat)
   - Appointments Created (Stat)

#### 3.6.3 Monitoring URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Prometheus | http://localhost:9090 | Metrics collection |
| Prometheus Targets | http://localhost:9090/targets | Health status |
| Grafana | http://localhost:3000 | Visualization |
| App Metrics | http://localhost:8000/metrics | Raw metrics |

---

## 4. Architecture Diagrams

### 4.1 Overall System Architecture

```
                              ┌──────────────────┐
                              │   GitHub Repo    │
                              │  (Source Code)   │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │  GitHub Actions  │
                              │   (CI/CD)        │
                              └────────┬─────────┘
                                       │
           ┌───────────────────────────┼───────────────────────────┐
           │                           │                           │
           ▼                           ▼                           ▼
    ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
    │   Docker     │          │  Terraform   │          │  Kubernetes  │
    │   Build      │          │   (IaC)      │          │   Deploy     │
    └──────────────┘          └──────────────┘          └──────────────┘
           │                           │                           │
           └───────────────────────────┼───────────────────────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │   Application    │
                              │   (FastAPI)      │
                              └────────┬─────────┘
                                       │
           ┌───────────────────────────┼───────────────────────────┐
           │                           │                           │
           ▼                           ▼                           ▼
    ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
    │  PostgreSQL  │          │    Redis     │          │  RabbitMQ    │
    │  (Database)  │          │   (Cache)    │          │   (Queue)    │
    └──────────────┘          └──────────────┘          └──────────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │   Monitoring     │
                              │ Prometheus/Grafana│
                              └──────────────────┘
```

### 4.2 CI/CD Pipeline Flow

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│  Push   │──▶│  Build  │──▶│  Lint   │──▶│  Test   │──▶│ Docker  │
│  Code   │   │         │   │         │   │         │   │  Build  │
└─────────┘   └─────────┘   └─────────┘   └─────────┘   └────┬────┘
                                                              │
                                                              ▼
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
│  Prod   │◀──│  Smoke  │◀──│   K8s   │◀──│Terraform│◀──│  Push   │
│ Deploy  │   │  Tests  │   │ Deploy  │   │  Plan   │   │  Image  │
└─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘
```

---

## 5. Testing & Quality Assurance

### 5.1 Test Coverage

| Test File | Tests | Coverage |
|-----------|-------|----------|
| `test_api.py` | 6 | API endpoints |
| `test_crud.py` | 5 | Database operations |
| `test_security.py` | 2 | Authentication |
| **Total** | **13** | **~71%** |

### 5.2 Test Commands
```bash
# Run all tests
pytest app/tests/ -v

# With coverage report
pytest app/tests/ -v --cov=app --cov-report=html

# Generate XML report (for CI)
pytest app/tests/ -v --cov=app --cov-report=xml
```

### 5.3 Code Quality
- **Linting:** flake8
- **Type Checking:** Pydantic validation
- **Security:** JWT authentication, password hashing

---

## 6. Challenges & Solutions

### Challenge 1: CI/CD Test Failures
**Problem:** Tests failing with `ModuleNotFoundError: No module named 'app'`

**Solution:** Added `PYTHONPATH` environment variable in GitHub Actions:
```yaml
env:
  PYTHONPATH: ${{ github.workspace }}
```

### Challenge 2: Grafana Dashboard Not Loading
**Problem:** Dashboard provisioning failing with folder configuration error

**Solution:** Removed conflicting `folder` and `foldersFromFilesStructure` options:
```yaml
# Before (error)
folder: 'Healthcare'
foldersFromFilesStructure: true

# After (fixed)
# Removed folder option
```

### Challenge 3: Route Dependency Injection
**Problem:** `'Depends' object has no attribute 'query'`

**Solution:** Fixed FastAPI dependency injection - moved `db: Session = Depends(get_db)` to function parameters instead of function body.

### Challenge 4: Date Serialization
**Problem:** SQLite Date type only accepts Python date objects

**Solution:** Changed CRUD base to use `model_dump()` instead of `jsonable_encoder()` to preserve date types.

### Challenge 5: Large Files in Git
**Problem:** `.terraform` directory (685MB) blocking push to GitHub

**Solution:** Added to `.gitignore` and removed from git tracking:
```bash
git rm -r --cached infra/.terraform
```

---

## 7. Conclusion

This project successfully demonstrates a complete DevOps implementation for a healthcare management system. All required components have been implemented and tested:

### ✅ Completed Deliverables

| Component | Status | Evidence |
|-----------|--------|----------|
| Docker | ✅ Complete | `docker-compose.yml`, `Dockerfile` |
| Terraform | ✅ Complete | `infra/*.tf` files |
| Ansible | ✅ Complete | `ansible/` directory |
| Kubernetes | ✅ Complete | `k8s/` directory |
| CI/CD | ✅ Complete | `.github/workflows/` |
| Monitoring | ✅ Complete | Prometheus + Grafana |
| Documentation | ✅ Complete | README.md, this report |

### 💰 Cost Summary
- **Total Cloud Cost:** $0.00
- **Tools Used:** All free/local (LocalStack, Minikube, Docker)

### 🎯 Key Learnings
1. Infrastructure as Code enables reproducible environments
2. CI/CD pipelines catch issues early in development
3. Monitoring is essential for production systems
4. Containerization simplifies deployment and scaling

---

**Report Generated:** December 18, 2025  
**Project Repository:** https://github.com/turabbb/Health-Care-Management-System-Python-FastAPI
