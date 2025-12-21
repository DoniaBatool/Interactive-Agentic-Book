"""
User service for user management operations.
Feature 013: Auth & Personalization
"""

import logging
from typing import Optional, Dict, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.app.models.user import User
from backend.app.models.user_profile import UserProfile
from backend.app.services.auth import hash_password, verify_password

logger = logging.getLogger(__name__)


async def get_user_by_email(
    db: AsyncSession,
    email: str
) -> Optional[User]:
    """
    Get a user by email address.
    
    Args:
        db: Database session
        email: User's email
        
    Returns:
        User object or None
    """
    result = await db.execute(
        select(User)
        .options(selectinload(User.profile))
        .where(User.email == email.lower())
    )
    return result.scalar_one_or_none()


async def get_user_by_id(
    db: AsyncSession,
    user_id: int
) -> Optional[User]:
    """
    Get a user by ID.
    
    Args:
        db: Database session
        user_id: User's ID
        
    Returns:
        User object or None
    """
    result = await db.execute(
        select(User)
        .options(selectinload(User.profile))
        .where(User.id == user_id)
    )
    return result.scalar_one_or_none()


async def create_user(
    db: AsyncSession,
    email: str,
    password: str,
    name: Optional[str] = None,
    profile_data: Optional[Dict[str, Any]] = None
) -> Optional[User]:
    """
    Create a new user with optional profile.
    
    Args:
        db: Database session
        email: User's email
        password: Plain text password (will be hashed)
        name: Optional user name
        profile_data: Optional profile data dict
        
    Returns:
        Created User object or None if error
    """
    try:
        # Check if email already exists
        existing = await get_user_by_email(db, email)
        if existing:
            logger.warning(f"Email already registered: {email}")
            return None
        
        # Create user
        user = User(
            email=email.lower(),
            password_hash=hash_password(password),
            name=name
        )
        db.add(user)
        await db.flush()  # Get user.id
        
        # Create profile
        profile = UserProfile(
            user_id=user.id,
            software_level=profile_data.get("software_level", "beginner") if profile_data else "beginner",
            hardware_level=profile_data.get("hardware_level", "none") if profile_data else "none",
            technologies=profile_data.get("technologies", {}) if profile_data else {},
            learning_goals=profile_data.get("learning_goals") if profile_data else None
        )
        db.add(profile)
        
        await db.commit()
        
        # Reload user with profile relationship
        result = await db.execute(
            select(User)
            .options(selectinload(User.profile))
            .where(User.id == user.id)
        )
        user = result.scalar_one()
        
        logger.info(f"Created user: {user.email}")
        return user
        
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        await db.rollback()
        return None


async def authenticate_user(
    db: AsyncSession,
    email: str,
    password: str
) -> Optional[User]:
    """
    Authenticate a user by email and password.
    
    Args:
        db: Database session
        email: User's email
        password: Plain text password
        
    Returns:
        User object if authenticated, None otherwise
    """
    user = await get_user_by_email(db, email)
    if not user:
        logger.debug(f"User not found: {email}")
        return None
    
    if not user.is_active:
        logger.debug(f"User is inactive: {email}")
        return None
    
    if not verify_password(password, user.password_hash):
        logger.debug(f"Invalid password for: {email}")
        return None
    
    logger.info(f"User authenticated: {email}")
    return user


async def update_profile(
    db: AsyncSession,
    user_id: int,
    profile_data: Dict[str, Any]
) -> Optional[UserProfile]:
    """
    Update a user's profile.
    
    Args:
        db: Database session
        user_id: User's ID
        profile_data: Dict with fields to update
        
    Returns:
        Updated UserProfile or None
    """
    try:
        result = await db.execute(
            select(UserProfile).where(UserProfile.user_id == user_id)
        )
        profile = result.scalar_one_or_none()
        
        if not profile:
            logger.warning(f"Profile not found for user: {user_id}")
            return None
        
        # Update fields if provided
        if "software_level" in profile_data:
            profile.software_level = profile_data["software_level"]
        if "hardware_level" in profile_data:
            profile.hardware_level = profile_data["hardware_level"]
        if "technologies" in profile_data:
            # Merge technologies instead of replacing
            existing = profile.technologies or {}
            existing.update(profile_data["technologies"])
            profile.technologies = existing
        if "learning_goals" in profile_data:
            profile.learning_goals = profile_data["learning_goals"]
        
        await db.commit()
        await db.refresh(profile)
        
        logger.info(f"Updated profile for user: {user_id}")
        return profile
        
    except Exception as e:
        logger.error(f"Error updating profile: {e}")
        await db.rollback()
        return None


async def get_profile(
    db: AsyncSession,
    user_id: int
) -> Optional[UserProfile]:
    """
    Get a user's profile.
    
    Args:
        db: Database session
        user_id: User's ID
        
    Returns:
        UserProfile or None
    """
    result = await db.execute(
        select(UserProfile).where(UserProfile.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def link_session_to_user(
    db: AsyncSession,
    session_id: str,
    user_id: int
) -> bool:
    """
    Link an anonymous session to a user account.
    
    Args:
        db: Database session
        session_id: Browser session ID
        user_id: User's ID
        
    Returns:
        True if linked, False otherwise
    """
    try:
        from backend.app.models.session import Session
        
        result = await db.execute(
            select(Session).where(Session.session_id == session_id)
        )
        session = result.scalar_one_or_none()
        
        if session:
            session.user_id = user_id
            await db.commit()
            logger.info(f"Linked session {session_id} to user {user_id}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error linking session: {e}")
        await db.rollback()
        return False

