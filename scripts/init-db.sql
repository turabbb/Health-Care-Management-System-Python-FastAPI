-- =============================================================================
-- HEALTHCARE DATABASE INITIALIZATION SCRIPT
-- This script runs when PostgreSQL container starts for the first time
-- =============================================================================

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Grant privileges (if running as specific user)
GRANT ALL PRIVILEGES ON DATABASE healthcare TO postgres;

-- Log initialization
DO $$
BEGIN
    RAISE NOTICE 'Healthcare database initialized successfully at %', NOW();
END $$;
