"""
Pytest configuration and fixtures for the Healthcare Management System tests.
"""
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Set environment variables for testing
os.environ["ENVIRONMENT"] = "testing"
os.environ["SECRET_KEY"] = "test_secret_key_for_testing_minimum_32_characters_long"

# Use SQLite for local testing if DATABASE_URL is not set
if "DATABASE_URL" not in os.environ:
    os.environ["DATABASE_URL"] = "sqlite:///./test.db"
