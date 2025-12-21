"""
Authentication service for password hashing and JWT tokens.
Feature 013: Auth & Personalization
"""

import logging
from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from jose import jwt, JWTError

from app.core.config import get_settings

logger = logging.getLogger(__name__)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get settings
settings = get_settings()
JWT_SECRET_KEY = settings.jwt_secret_key
JWT_ALGORITHM = settings.jwt_algorithm
JWT_EXPIRY_DAYS = settings.jwt_expiry_days


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash.
    
    Args:
        plain_password: Plain text password to verify
        hashed_password: Stored hash to compare against
        
    Returns:
        True if password matches, False otherwise
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        logger.error(f"Password verification error: {e}")
        return False


def create_session_token(
    user_id: int,
    email: str,
    remember_me: bool = False
) -> str:
    """
    Create a JWT session token.
    
    Args:
        user_id: User's database ID
        email: User's email
        remember_me: If True, extend expiry to 30 days
        
    Returns:
        JWT token string
    """
    expiry_days = 30 if remember_me else JWT_EXPIRY_DAYS
    expire = datetime.utcnow() + timedelta(days=expiry_days)
    
    payload = {
        "sub": str(user_id),
        "email": email,
        "exp": expire,
        "iat": datetime.utcnow(),
        "type": "session"
    }
    
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    logger.debug(f"Created session token for user {user_id}")
    return token


def verify_session_token(token: str) -> Optional[dict]:
    """
    Verify and decode a JWT session token.
    
    Args:
        token: JWT token string
        
    Returns:
        Decoded payload dict or None if invalid
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        
        # Verify token type
        if payload.get("type") != "session":
            logger.warning("Invalid token type")
            return None
        
        return payload
    
    except JWTError as e:
        logger.debug(f"JWT verification failed: {e}")
        return None
    except Exception as e:
        logger.error(f"Token verification error: {e}")
        return None


def get_user_id_from_token(token: str) -> Optional[int]:
    """
    Extract user ID from a session token.
    
    Args:
        token: JWT token string
        
    Returns:
        User ID or None if invalid
    """
    payload = verify_session_token(token)
    if payload and "sub" in payload:
        try:
            return int(payload["sub"])
        except (ValueError, TypeError):
            return None
    return None


def get_token_expiry_seconds(remember_me: bool = False) -> int:
    """
    Get token expiry in seconds for cookie max_age.
    
    Args:
        remember_me: If True, return 30 days, otherwise JWT_EXPIRY_DAYS
        
    Returns:
        Expiry in seconds
    """
    days = 30 if remember_me else JWT_EXPIRY_DAYS
    return days * 24 * 60 * 60

