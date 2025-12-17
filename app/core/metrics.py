# =============================================================================
# PROMETHEUS METRICS MODULE
# Healthcare Management System - Application Metrics
# =============================================================================

from prometheus_client import Counter, Histogram, Gauge, Info, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
import psutil

# =============================================================================
# METRICS DEFINITIONS
# =============================================================================

# Request metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint'],
    buckets=[0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0]
)

REQUESTS_IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'Number of HTTP requests currently being processed',
    ['method', 'endpoint']
)

# Application metrics
APP_INFO = Info('healthcare_app', 'Healthcare application information')

# Database metrics
DB_CONNECTIONS_ACTIVE = Gauge(
    'db_connections_active',
    'Number of active database connections'
)

DB_QUERY_DURATION = Histogram(
    'db_query_duration_seconds',
    'Database query duration in seconds',
    ['operation', 'table']
)

# Cache metrics
CACHE_HITS = Counter(
    'cache_hits_total',
    'Total cache hits',
    ['cache_type']
)

CACHE_MISSES = Counter(
    'cache_misses_total',
    'Total cache misses',
    ['cache_type']
)

# Business metrics
APPOINTMENTS_CREATED = Counter(
    'appointments_created_total',
    'Total appointments created',
    ['status']
)

PATIENTS_REGISTERED = Counter(
    'patients_registered_total',
    'Total patients registered'
)

DOCTORS_REGISTERED = Counter(
    'doctors_registered_total',
    'Total doctors registered'
)

# System metrics
SYSTEM_CPU_USAGE = Gauge(
    'system_cpu_usage_percent',
    'System CPU usage percentage'
)

SYSTEM_MEMORY_USAGE = Gauge(
    'system_memory_usage_percent',
    'System memory usage percentage'
)

SYSTEM_DISK_USAGE = Gauge(
    'system_disk_usage_percent',
    'System disk usage percentage'
)

# =============================================================================
# PROMETHEUS MIDDLEWARE
# =============================================================================

class PrometheusMiddleware(BaseHTTPMiddleware):
    """
    Middleware to collect Prometheus metrics for all HTTP requests
    """
    
    async def dispatch(self, request: Request, call_next):
        # Skip metrics endpoint itself to avoid recursion
        if request.url.path == "/metrics":
            return await call_next(request)
        
        method = request.method
        path = self._get_path_template(request)
        
        # Track in-progress requests
        REQUESTS_IN_PROGRESS.labels(method=method, endpoint=path).inc()
        
        # Record start time
        start_time = time.time()
        
        try:
            response = await call_next(request)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
            raise e
        finally:
            # Calculate duration
            duration = time.time() - start_time
            
            # Record metrics
            REQUEST_COUNT.labels(
                method=method,
                endpoint=path,
                status_code=status_code
            ).inc()
            
            REQUEST_LATENCY.labels(
                method=method,
                endpoint=path
            ).observe(duration)
            
            REQUESTS_IN_PROGRESS.labels(
                method=method,
                endpoint=path
            ).dec()
        
        return response
    
    def _get_path_template(self, request: Request) -> str:
        """
        Get the path template for the request (normalizes path parameters)
        """
        path = request.url.path
        
        # Normalize common path patterns
        # Replace numeric IDs with placeholder
        import re
        path = re.sub(r'/\d+', '/{id}', path)
        
        return path


# =============================================================================
# METRICS ENDPOINT
# =============================================================================

async def metrics_endpoint():
    """
    Endpoint to expose Prometheus metrics
    """
    # Update system metrics before returning
    update_system_metrics()
    
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


def update_system_metrics():
    """
    Update system-level metrics
    """
    try:
        SYSTEM_CPU_USAGE.set(psutil.cpu_percent())
        SYSTEM_MEMORY_USAGE.set(psutil.virtual_memory().percent)
        SYSTEM_DISK_USAGE.set(psutil.disk_usage('/').percent)
    except Exception:
        pass  # Ignore errors in metrics collection


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def set_app_info(version: str, environment: str):
    """
    Set application info metric
    """
    APP_INFO.info({
        'version': version,
        'environment': environment,
        'app_name': 'healthcare-api'
    })


def record_db_query(operation: str, table: str, duration: float):
    """
    Record a database query metric
    """
    DB_QUERY_DURATION.labels(operation=operation, table=table).observe(duration)


def record_cache_hit(cache_type: str = 'redis'):
    """
    Record a cache hit
    """
    CACHE_HITS.labels(cache_type=cache_type).inc()


def record_cache_miss(cache_type: str = 'redis'):
    """
    Record a cache miss
    """
    CACHE_MISSES.labels(cache_type=cache_type).inc()


def record_appointment_created(status: str = 'scheduled'):
    """
    Record an appointment creation
    """
    APPOINTMENTS_CREATED.labels(status=status).inc()


def record_patient_registered():
    """
    Record a patient registration
    """
    PATIENTS_REGISTERED.inc()


def record_doctor_registered():
    """
    Record a doctor registration
    """
    DOCTORS_REGISTERED.inc()
