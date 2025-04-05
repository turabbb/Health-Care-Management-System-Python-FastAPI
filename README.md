# Health Care Management System

![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?logo=fastapi) ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql) ![Redis](https://img.shields.io/badge/Redis-7.0.5-DC382D?logo=redis) ![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.12-FF6600?logo=rabbitmq)

A modern microservices-based healthcare management system built with **FastAPI**, featuring secure patient data management, appointment scheduling, and real-time notifications. Designed for clinics and hospitals to streamline operations while maintaining HIPAA compliance standards.

![System Architecture Diagram](/path/to/architecture.png) <!-- Add actual diagram path -->

## ✨ Key Features

- **Patient Management**
  📝 Secure registration with insurance/ID tracking
  🔍 Advanced search and profile updates
- **Doctor Management**
  ⚕️ Specialization-based profiles with availability schedules
  📅 Dynamic calendar integration
- **Smart Appointment System**
  🚨 Conflict-free scheduling with double-booking prevention
  🔔 Real-time notifications via email/SMS
- **Medical Records**
  🔒 Encrypted storage with role-based access control
  ⛓️ Audit trails for data integrity
- **Performance Optimizations**
  ⚡ Redis caching for high-frequency data
  🐇 RabbitMQ-powered async task processing

## 🛠 Tech Stack

- **Backend Framework**: FastAPI 0.109
- **Database**: PostgreSQL 15 + SQLAlchemy ORM
- **Cache/Queue**: Redis 7 + RabbitMQ 3.12
- **Auth**: JWT + OAuth2
- **Docs**: Swagger/OpenAPI 3.0
- **Testing**: Pytest + HTTPX
- **Deployment**: Docker + Docker Compose

## 🚀 Quick Start

### Prerequisites

- Docker 24.0+ & Docker Compose 2.20+
- Python 3.11+

### Installation

1. Clone repository:
   ```bash
   git clone https://github.com/devalentineomonya/Health-Care-Management-System-Python-FastAPI.git
   cd Health-Care-Management-System-Python-FastAPI
   ```
2. Create `.env` file:
   ```env
   SECRET_KEY=your_ultra_secure_key
   DATABASE_URL=postgresql://user:pass@db:5432/healthcare
   REDIS_URL=redis://redis:6379/0
   RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
   SMTP_ENABLED=true
   ```
3. Start services:
   ```bash
   docker-compose up -d --build
   ```
4. Access API at `http://localhost:8000`

## 📚 API Documentation

- **Interactive Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

![API Docs Screenshot](/path/to/swagger-screenshot.png) <!-- Add screenshot -->

## 🗄 Database Schema

```mermaid
erDiagram
    patients ||--o{ appointments : has
    patients ||--o{ medical_records : "stores"
    doctors ||--o{ appointments : accepts
    doctors ||--o{ availabilities : "has"
    users ||--o{ patients : "represents"
    users ||--o{ doctors : "represents"

    patients {
        uuid id PK
        string insurance_number
        timestamp created_at
    }

    doctors {
        uuid id PK
        string specialization
        jsonb availability_slots
    }

    appointments {
        uuid id PK
        timestamp start_time
        timestamp end_time
        string status
    }
```

## 🔒 Security Features

- **JWT Authentication** with 15-minute token expiration
- **Role-Based Access Control** (Patient, Doctor, Admin)
- 🔑 Argon2 password hashing
- 🛡️ Rate limiting (100 requests/minute)
- 🕵️ Input validation with Pydantic V2
- 🔐 HTTPS-ready configuration

## ⚙️ Project Structure

```
healthcare-system/
├── app/
│   ├── api/           # Route handlers
│   ├── core/          # Config, security, middleware
│   ├── crud/          # Database operations
│   ├── db/            # SQLAlchemy models
│   ├── schemas/       # Pydantic models
│   └── main.py        # FastAPI entrypoint
├── tests/             # Pytest suites
├── docker-compose.yml # Multi-service setup
├── Dockerfile         # Production build
└── requirements.txt   # Python dependencies
```

## 🌐 Production Deployment

1. Configure reverse proxy (Nginx):

   ```nginx
   server {
       listen 443 ssl;
       server_name healthcare.example.com;

       ssl_certificate /path/to/fullchain.pem;
       ssl_certificate_key /path/to/privkey.pem;

       location / {
           proxy_pass http://app:8000;
           proxy_set_header Host $host;
       }
   }
   ```

2. Enable automated backups for PostgreSQL
3. Monitor with:
   - Prometheus/Grafana for metrics
   - ELK Stack for logging
   - Uptime Robot for availability

## 🤝 Contributing

1. Fork the repository
2. Create feature branch:
   ```bash
   git checkout -b feat/amazing-feature
   ```
3. Follow PEP8 guidelines and write tests
4. Submit PR with:
   - Detailed description
   - Screenshots (if UI changes)
   - Updated documentation

## 🚧 Roadmap

- [ ] Telemedicine integration (WebRTC)
- [ ] Patient mobile app (Flutter)
- [ ] AI-powered appointment suggestions
- [ ] Insurance claim processing module
- [ ] Multi-tenant architecture support

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.
