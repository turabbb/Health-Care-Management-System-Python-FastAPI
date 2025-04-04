# Healthcare Appointment Scheduling System

A robust, secure backend service that efficiently manages patient data and enables seamless appointment scheduling with healthcare providers.

## Features

- **Patient Management**: Register and manage patient profiles, store basic patient information and contact details, track patient identification and insurance information.
- **Doctor Management**: Maintain doctor profiles with specializations and manage doctor availability schedules.
- **Appointment Scheduling**: Create appointments between patients and doctors, check doctor availability when scheduling, prevent scheduling conflicts and double-bookings, and manage appointment status changes.
- **Medical Records**: Store medical records for patients, link records to specific appointments, and implement appropriate access controls for sensitive information.

## Technical Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Documentation**: Swagger/OpenAPI
- **Message Queue**: RabbitMQ
- **Caching & Rate Limiting**: Redis

## Architecture

The system follows a microservices architecture with the following components:

1. **API Gateway**: Main FastAPI application that handles HTTP requests
2. **Authentication Service**: Handles user authentication and authorization
3. **Patient Service**: Manages patient data
4. **Doctor Service**: Manages doctor data and availability
5. **Appointment Service**: Handles appointment scheduling and conflict prevention
6. **Notification Service**: Sends notifications about appointments

## Project Structure

\`\`\`
healthcare-appointment-system/
├── app/                        # Main application package
│   ├── api/                    # API endpoints
│   │   ├── deps.py             # Dependency injection
│   │   └── routes/             # API route handlers
│   ├── core/                   # Core functionality
│   │   ├── config.py           # Configuration settings
│   │   ├── security.py         # Security utilities
│   │   ├── notifications.py    # Notification handling
│   │   ├── rate_limiter.py     # Rate limiting middleware
│   │   └── cache.py            # Caching middleware
│   ├── crud/                   # Database CRUD operations
│   ├── db/                     # Database models and session
│   │   ├── models.py           # SQLAlchemy models
│   │   └── session.py          # Database session
│   ├── schemas/                # Pydantic schemas
│   ├── tests/                  # Unit and integration tests
│   └── main.py                 # Application entry point
├── Dockerfile                  # Main service Dockerfile
├── Dockerfile.notification     # Notification service Dockerfile
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # Main service dependencies
├── requirements.notification.txt # Notification service dependencies
├── notification_service.py     # Standalone notification service
└── README.md                   # Project documentation
\`\`\`

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+

### Installation

1. Clone the repository:
   \`\`\`
   git clone https://github.com/yourusername/healthcare-appointment-system.git
   cd healthcare-appointment-system
   \`\`\`

2. Create a `.env` file with the following variables:
   \`\`\`
   SECRET_KEY=your-secret-key
   SMTP_SERVER=your-smtp-server
   SMTP_PORT=587
   SMTP_USERNAME=your-smtp-username
   SMTP_PASSWORD=your-smtp-password
   EMAIL_FROM=noreply@yourdomain.com
   \`\`\`

3. Start the services using Docker Compose:
   \`\`\`
   docker-compose up -d
   \`\`\`

4. The API will be available at http://localhost:8000

### Running Tests

\`\`\`
pytest
\`\`\`

## API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/auth/login` - Obtain JWT token
- `POST /api/auth/register` - Register a new user
- `GET /api/auth/me` - Get current user information

### Patients
- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create a new patient
- `GET /api/patients/{id}` - Get patient details
- `PUT /api/patients/{id}` - Update patient information
- `DELETE /api/patients/{id}` - Delete a patient
- `GET /api/patients/search/` - Search for patients

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create a new doctor
- `GET /api/doctors/{id}` - Get doctor details with availability
- `PUT /api/doctors/{id}` - Update doctor information
- `DELETE /api/doctors/{id}` - Delete a doctor
- `POST /api/doctors/{id}/availability` - Add availability for a doctor
- `GET /api/doctors/specialization/{specialization}` - Get doctors by specialization

### Appointments
- `GET /api/appointments/` - List appointments (filtered by user role)
- `POST /api/appointments/` - Create a new appointment
- `GET /api/appointments/{id}` - Get appointment details
- `PUT /api/appointments/{id}` - Update an appointment
- `DELETE /api/appointments/{id}` - Delete an appointment
- `PUT /api/appointments/{id}/status` - Update appointment status
- `GET /api/appointments/doctor/{doctor_id}/available-slots` - Get available slots for a doctor

## Database Schema

The system uses the following database schema:

- **patients**: Stores patient information
- **doctors**: Stores doctor information
- **availabilities**: Stores doctor availability schedules
- **appointments**: Stores appointment information
- **medical_records**: Stores patient medical records
- **users**: Stores user authentication information

## Security

The system implements the following security measures:

- JWT-based authentication
- Role-based access control
- Password hashing
- HTTPS support
- Rate limiting
- Input validation

## Performance Optimizations

- Redis caching for frequently accessed data
- Asynchronous processing with RabbitMQ
- Database query optimization
- Connection pooling

## Deployment

### Local Development
Follow the installation instructions above to deploy the system locally using Docker Compose.

### Production Deployment

For production deployment, consider the following additional steps:

1. Use a production-grade PostgreSQL setup with proper backups
2. Configure HTTPS with a valid SSL certificate
3. Set up monitoring and logging (e.g., Prometheus, Grafana, ELK stack)
4. Use a reverse proxy like Nginx in front of the application
5. Implement proper secrets management

Example production docker-compose.yml adjustments:

\`\`\`yaml
version: '3.8'

services:
  app:
    build: .
    restart: always
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/healthcare
      - REDIS_URL=redis://redis:6379/0
      - RABBITMQ_URL=amqp://user:password@rabbitmq:5672/
      - SECRET_KEY=${SECRET_KEY}
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=healthcare
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G

  # Other services with similar production configurations
\`\`\`

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Check if PostgreSQL is running: `docker-compose ps`
   - Verify database credentials in environment variables
   - Check network connectivity between services

2. **Authentication Issues**
   - Ensure SECRET_KEY is properly set
   - Check token expiration time
   - Verify user credentials

3. **Performance Issues**
   - Check Redis connection for caching
   - Monitor database query performance
   - Check RabbitMQ queue sizes

### Logs

To view logs for troubleshooting:

\`\`\`bash
# View logs for all services
docker-compose logs

# View logs for a specific service
docker-compose logs app

# Follow logs in real-time
docker-compose logs -f app
\`\`\`

## Contributing

We welcome contributions to improve the Healthcare Appointment Scheduling System!

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run tests: `pytest`
5. Commit your changes: `git commit -m "Add some feature"`
6. Push to the branch: `git push origin feature/your-feature-name`
7. Submit a pull request

### Coding Standards

- Follow PEP 8 style guide for Python code
- Write docstrings for all functions, classes, and modules
- Include unit tests for new features
- Update documentation as needed

## Future Enhancements

- **Mobile Application**: Develop a mobile app for patients to schedule appointments
- **Telemedicine Integration**: Add support for virtual appointments
- **Analytics Dashboard**: Implement reporting and analytics features
- **Multi-language Support**: Add internationalization for multiple languages
- **Payment Processing**: Integrate payment gateway for online payments
- **AI-based Scheduling**: Implement intelligent scheduling recommendations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

