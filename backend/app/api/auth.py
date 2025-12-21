"""
Authentication API endpoints.
Feature 013: Auth & Personalization
"""

import logging
from typing import Optional, Dict, Any

from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_db, is_db_available
from backend.app.services import user as user_service
from backend.app.services import auth as auth_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


# Request/Response Schemas
class ProfileCreate(BaseModel):
    software_level: str = "beginner"
    hardware_level: str = "none"
    technologies: Dict[str, bool] = {}
    learning_goals: Optional[str] = None


class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    profile: Optional[ProfileCreate] = None


class SigninRequest(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool = False


class ProfileResponse(BaseModel):
    software_level: str
    hardware_level: str
    technologies: Dict[str, Any]
    learning_goals: Optional[str]

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    email: str
    name: Optional[str]
    profile: Optional[ProfileResponse] = None

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    user: UserResponse
    message: str


class SessionResponse(BaseModel):
    authenticated: bool
    user: Optional[UserResponse] = None


class MessageResponse(BaseModel):
    message: str


# Endpoints
@router.post("/signup", response_model=AuthResponse, status_code=201)
async def signup(
    request: SignupRequest,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new user account with profile.
    """
    if not is_db_available():
        raise HTTPException(status_code=503, detail="Database not available")
    
    # Validate password
    if len(request.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")
    
    # Create user
    profile_data = request.profile.model_dump() if request.profile else None
    user = await user_service.create_user(
        db=db,
        email=request.email,
        password=request.password,
        name=request.name,
        profile_data=profile_data
    )
    
    if not user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create session token
    token = auth_service.create_session_token(user.id, user.email)
    expiry = auth_service.get_token_expiry_seconds()
    
    # Set cookie
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=expiry,
        path="/"
    )
    
    # Build response
    profile_response = None
    if user.profile:
        profile_response = ProfileResponse(
            software_level=user.profile.software_level,
            hardware_level=user.profile.hardware_level,
            technologies=user.profile.technologies or {},
            learning_goals=user.profile.learning_goals
        )
    
    return AuthResponse(
        user=UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            profile=profile_response
        ),
        message="Account created successfully"
    )


@router.post("/signin", response_model=AuthResponse)
async def signin(
    request: SigninRequest,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    """
    Sign in with email and password.
    """
    if not is_db_available():
        raise HTTPException(status_code=503, detail="Database not available")
    
    # Authenticate
    user = await user_service.authenticate_user(
        db=db,
        email=request.email,
        password=request.password
    )
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Create session token
    token = auth_service.create_session_token(
        user.id,
        user.email,
        remember_me=request.remember_me
    )
    expiry = auth_service.get_token_expiry_seconds(request.remember_me)
    
    # Set cookie
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=expiry,
        path="/"
    )
    
    # Build response
    profile_response = None
    if user.profile:
        profile_response = ProfileResponse(
            software_level=user.profile.software_level,
            hardware_level=user.profile.hardware_level,
            technologies=user.profile.technologies or {},
            learning_goals=user.profile.learning_goals
        )
    
    return AuthResponse(
        user=UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            profile=profile_response
        ),
        message="Signed in successfully"
    )


@router.post("/signout", response_model=MessageResponse)
async def signout(response: Response):
    """
    Sign out and clear session cookie.
    """
    response.delete_cookie(
        key="session_token",
        path="/"
    )
    return MessageResponse(message="Signed out successfully")


@router.get("/session", response_model=SessionResponse)
async def get_session(
    session_token: Optional[str] = Cookie(None),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current session/user info.
    """
    if not session_token:
        return SessionResponse(authenticated=False)
    
    # Verify token
    user_id = auth_service.get_user_id_from_token(session_token)
    if not user_id:
        return SessionResponse(authenticated=False)
    
    # Get user
    user = await user_service.get_user_by_id(db, user_id)
    if not user or not user.is_active:
        return SessionResponse(authenticated=False)
    
    # Build response
    profile_response = None
    if user.profile:
        profile_response = ProfileResponse(
            software_level=user.profile.software_level,
            hardware_level=user.profile.hardware_level,
            technologies=user.profile.technologies or {},
            learning_goals=user.profile.learning_goals
        )
    
    return SessionResponse(
        authenticated=True,
        user=UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            profile=profile_response
        )
    )


@router.get("/profile", response_model=ProfileResponse)
async def get_profile(
    session_token: Optional[str] = Cookie(None),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's profile.
    """
    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = auth_service.get_user_id_from_token(session_token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid session")
    
    profile = await user_service.get_profile(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return ProfileResponse(
        software_level=profile.software_level,
        hardware_level=profile.hardware_level,
        technologies=profile.technologies or {},
        learning_goals=profile.learning_goals
    )


class ProfileUpdate(BaseModel):
    software_level: Optional[str] = None
    hardware_level: Optional[str] = None
    technologies: Optional[Dict[str, bool]] = None
    learning_goals: Optional[str] = None


@router.put("/profile", response_model=ProfileResponse)
async def update_profile(
    request: ProfileUpdate,
    session_token: Optional[str] = Cookie(None),
    db: AsyncSession = Depends(get_db)
):
    """
    Update current user's profile.
    """
    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = auth_service.get_user_id_from_token(session_token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid session")
    
    # Filter out None values
    update_data = {k: v for k, v in request.model_dump().items() if v is not None}
    
    profile = await user_service.update_profile(db, user_id, update_data)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return ProfileResponse(
        software_level=profile.software_level,
        hardware_level=profile.hardware_level,
        technologies=profile.technologies or {},
        learning_goals=profile.learning_goals
    )

