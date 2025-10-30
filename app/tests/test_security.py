from jose import jwt
from datetime import datetime, timedelta

from app.core.security import create_access_token, verify_password, get_password_hash
from app.core.config import settings

def test_create_access_token():
    subject = 1
    role = "admin"
    expires_delta = timedelta(minutes=30)

    token = create_access_token(subject, role, expires_delta)

    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    assert payload["sub"] == str(subject)
    assert payload["role"] == role

    exp = datetime.fromtimestamp(payload["exp"])
    now = datetime.utcnow()
    assert exp > now
    assert exp < now + timedelta(minutes=31)

def test_password_hashing():
    password = "testpassword123"

    hashed_password = get_password_hash(password)

    assert verify_password(password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)
