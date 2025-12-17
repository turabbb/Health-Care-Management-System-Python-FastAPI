# 🏥 Healthcare Management System

A comprehensive healthcare appointment management system built with **FastAPI**, featuring complete DevOps infrastructure including Docker, Kubernetes, Terraform, Ansible, CI/CD pipelines, and monitoring.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue)
![Terraform](https://img.shields.io/badge/Terraform-1.6-purple)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [API Endpoints](#-api-endpoints)
- [DevOps Infrastructure](#-devops-infrastructure)
- [Monitoring](#-monitoring)
- [Testing](#-testing)
- [Project Structure](#-project-structure)

---

## ✨ Features

### Application Features
- **Patient Management** - Register, update, search patients
- **Doctor Management** - Manage doctors and their availability
- **Appointment Scheduling** - Book, reschedule, cancel appointments
- **User Authentication** - JWT-based authentication with role-based access
- **API Documentation** - Auto-generated Swagger/OpenAPI docs

### DevOps Features
- **Containerization** - Full Docker Compose stack
- **Infrastructure as Code** - Terraform with LocalStack
- **Configuration Management** - Ansible playbooks
- **Container Orchestration** - Kubernetes manifests with Kustomize
- **CI/CD Pipeline** - GitHub Actions with 8 stages
- **Monitoring** - Prometheus metrics + Grafana dashboards

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Load Balancer                            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────┐
│                     FastAPI Application                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   Patients  │  │   Doctors   │  │     Appointments        │  │
│  │     API     │  │     API     │  │         API             │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└───────┬─────────────────┬─────────────────┬─────────────────────┘
        │                 │                 │
┌───────▼───────┐ ┌───────▼───────┐ ┌───────▼───────┐
│  PostgreSQL   │ │     Redis     │ │   RabbitMQ    │
│   Database    │ │     Cache     │ │    Queue      │
└───────────────┘ └───────────────┘ └───────────────┘
        │
┌───────▼─────────────────────────────────────────────────────────┐
│                      Monitoring Stack                           │
│  ┌─────────────────────┐      ┌─────────────────────┐          │
│  │     Prometheus      │──────│      Grafana        │          │
│  │    (Metrics)        │      │   (Dashboards)      │          │
│  └─────────────────────┘      └─────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | FastAPI, Python 3.11, SQLAlchemy |
| **Database** | PostgreSQL 15 |
| **Cache** | Redis 7 |
| **Message Queue** | RabbitMQ 3 |
| **Containerization** | Docker, Docker Compose |
| **Orchestration** | Kubernetes, Minikube |
| **IaC** | Terraform, LocalStack |
| **Configuration** | Ansible |
| **CI/CD** | GitHub Actions |
| **Monitoring** | Prometheus, Grafana |
| **Authentication** | JWT (python-jose) |

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/turabbb/Health-Care-Management-System-Python-FastAPI.git
cd Health-Care-Management-System-Python-FastAPI
```

### 2. Start with Docker Compose
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps
```

### 3. Access the Application
| Service | URL | Credentials |
|---------|-----|-------------|
| **FastAPI App** | http://localhost:8000 | - |
| **API Docs** | http://localhost:8000/docs | - |
| **Prometheus** | http://localhost:9090 | - |
| **Grafana** | http://localhost:3000 | admin / admin |
| **RabbitMQ** | http://localhost:15672 | guest / guest |

### 4. Run Locally (Development)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run application
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login and get JWT token |

### Patients
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients/` | List all patients |
| POST | `/api/patients/` | Create new patient |
| GET | `/api/patients/{id}` | Get patient by ID |
| PUT | `/api/patients/{id}` | Update patient |
| DELETE | `/api/patients/{id}` | Delete patient |

### Doctors
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/doctors/` | List all doctors |
| POST | `/api/doctors/` | Create new doctor |
| GET | `/api/doctors/{id}` | Get doctor by ID |
| POST | `/api/doctors/{id}/availability` | Set availability |

### Appointments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/appointments/` | List appointments |
| POST | `/api/appointments/` | Create appointment |
| PUT | `/api/appointments/{id}` | Update appointment |
| DELETE | `/api/appointments/{id}` | Cancel appointment |

### Health & Metrics
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/metrics` | Prometheus metrics |

---

## 🔧 DevOps Infrastructure

### Docker
```bash
# Start full stack
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop all services
docker-compose down
```

### Kubernetes (Minikube)
```bash
# Start Minikube
minikube start

# Deploy application
kubectl apply -k k8s/overlays/dev/

# Check status
kubectl get pods -n healthcare

# Access service
minikube service healthcare-api -n healthcare
```

### Terraform (LocalStack)
```bash
# Start LocalStack
docker-compose -f docker-compose.localstack.yml up -d

# Initialize and apply
cd infra
terraform init
terraform plan
terraform apply
```

### Ansible
```bash
cd ansible
ansible-playbook -i inventory/hosts.ini playbook.yml
```

---

## 📊 Monitoring

### Prometheus Metrics
The application exposes custom metrics at `/metrics`:
- `http_requests_total` - Total HTTP requests
- `http_request_duration_seconds` - Request latency
- `system_cpu_usage_percent` - CPU usage
- `system_memory_usage_percent` - Memory usage
- `patients_registered_total` - Business metrics
- `appointments_created_total` - Business metrics

### Grafana Dashboard
1. Access Grafana at http://localhost:3000
2. Login with admin / admin
3. Navigate to Dashboards → Healthcare System Overview

---

## 🧪 Testing

```bash
# Run all tests
pytest app/tests/ -v

# Run with coverage
pytest app/tests/ -v --cov=app --cov-report=html

# Run specific test file
pytest app/tests/test_api.py -v
```

---

## 📁 Project Structure

```
Health-Care-Management-System-Python-FastAPI/
├── app/                          # FastAPI Application
│   ├── api/                      # API routes
│   │   ├── routes/
│   │   │   ├── appointment.py
│   │   │   ├── auth.py
│   │   │   ├── doctor.py
│   │   │   └── patient.py
│   │   └── deps.py
│   ├── core/                     # Core modules
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── metrics.py
│   │   └── notifications.py
│   ├── crud/                     # Database operations
│   ├── db/                       # Database models
│   ├── schemas/                  # Pydantic schemas
│   ├── tests/                    # Test files
│   └── main.py                   # Application entry
├── k8s/                          # Kubernetes manifests
│   ├── base/
│   └── overlays/
├── infra/                        # Terraform files
├── ansible/                      # Ansible playbooks
├── monitoring/                   # Prometheus & Grafana
│   ├── prometheus/
│   └── grafana/
├── .github/workflows/            # CI/CD pipeline
├── docker-compose.yml            # Docker Compose
├── Dockerfile                    # Application Dockerfile
└── requirements.txt              # Python dependencies
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Turab** - DevOps Final Exam Project

---

⭐ Star this repository if you found it helpful!
