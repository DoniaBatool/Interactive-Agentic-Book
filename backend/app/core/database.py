"""
Database configuration and session management.
Feature 012: Postgres Persistence
"""

import os
import logging
from typing import AsyncGenerator, Optional

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

# Load .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Database URL from environment
_raw_url = os.getenv("DATABASE_URL", "")

def clean_database_url(url: str) -> str:
    """
    Clean and convert database URL for asyncpg compatibility.
    - Convert postgresql:// to postgresql+asyncpg://
    - Remove sslmode and channel_binding params (handled separately)
    """
    if not url:
        return "postgresql+asyncpg://postgres:postgres@localhost:5432/rag_chatbot"
    
    # Convert driver prefix
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+asyncpg://", 1)
    
    # Remove query params that asyncpg doesn't support directly
    # asyncpg handles SSL differently
    if "?" in url:
        base_url, query = url.split("?", 1)
        # Filter out incompatible params
        params = query.split("&")
        filtered_params = [
            p for p in params 
            if not p.startswith("sslmode=") 
            and not p.startswith("channel_binding=")
        ]
        if filtered_params:
            url = base_url + "?" + "&".join(filtered_params)
        else:
            url = base_url
    
    return url

DATABASE_URL = clean_database_url(_raw_url)

# Check if using NeonDB (serverless) - needs NullPool and SSL
IS_SERVERLESS = "neon.tech" in DATABASE_URL or "supabase" in DATABASE_URL

# Check if SSL is needed (based on original URL)
NEEDS_SSL = "sslmode=require" in _raw_url or IS_SERVERLESS

logger.info(f"Database URL configured: {DATABASE_URL[:50]}...")
logger.info(f"Serverless mode: {IS_SERVERLESS}, SSL: {NEEDS_SSL}")

# Flag to check if database is available
_db_available: Optional[bool] = None


class Base(DeclarativeBase):
    """Base class for all database models."""
    pass


def get_engine():
    """Create and return the async database engine."""
    import ssl
    
    # SSL configuration for cloud databases
    connect_args = {}
    if NEEDS_SSL:
        # Create SSL context for secure connection
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE  # NeonDB uses self-signed certs
        connect_args["ssl"] = ssl_context
    
    if IS_SERVERLESS:
        # Use NullPool for serverless databases (NeonDB, Supabase)
        # Serverless DBs manage their own connection pooling
        logger.info("Using NullPool for serverless database")
        return create_async_engine(
            DATABASE_URL,
            echo=False,
            poolclass=NullPool,
            connect_args=connect_args,
        )
    else:
        # Use standard pool for persistent servers (local PostgreSQL, Docker)
        return create_async_engine(
            DATABASE_URL,
            echo=False,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800,
            connect_args=connect_args,
        )


# Create engine and session factory
try:
    engine = get_engine()
    async_session_factory = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
except Exception as e:
    logger.error(f"Failed to create database engine: {e}")
    engine = None
    async_session_factory = None


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides a database session.
    Use with FastAPI's Depends().
    """
    if async_session_factory is None:
        raise RuntimeError("Database not configured")
    
    session = async_session_factory()
    try:
        yield session
    finally:
        # Close session properly, handling any pending operations
        try:
            await session.commit()
        except Exception:
            await session.rollback()
        finally:
            await session.close()


async def init_db() -> bool:
    """
    Initialize database tables.
    Returns True if successful, False otherwise.
    """
    global _db_available
    
    if engine is None:
        logger.warning("Database engine not available")
        _db_available = False
        return False
    
    try:
        async with engine.begin() as conn:
            # Import models to register them with Base
            from app.models import session, message, user, user_profile, translation  # noqa: F401
            
            # Create all tables
            await conn.run_sync(Base.metadata.create_all)
        
        logger.info("Database tables created successfully")
        _db_available = True
        return True
    
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        _db_available = False
        return False


async def check_db_health() -> bool:
    """
    Check if database connection is healthy.
    """
    if engine is None:
        return False
    
    try:
        from sqlalchemy import text
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


def is_db_available() -> bool:
    """
    Check if database is available (cached result from init).
    """
    return _db_available is True
