# Data Model – Feature 013: Auth & Personalization

## Database Schema

### Users Table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

### User Profiles Table

```sql
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    software_level VARCHAR(20) NOT NULL DEFAULT 'beginner',
    hardware_level VARCHAR(20) NOT NULL DEFAULT 'none',
    technologies JSONB DEFAULT '{}',
    learning_goals TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
```

### Sessions Table (Updated)

```sql
-- Add user_id column to existing sessions table
ALTER TABLE sessions ADD COLUMN user_id INTEGER REFERENCES users(id);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
```

## SQLAlchemy Models

### User Model

```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    sessions = relationship("Session", back_populates="user")
```

### UserProfile Model

```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    software_level = Column(String(20), nullable=False, default="beginner")
    hardware_level = Column(String(20), nullable=False, default="none")
    technologies = Column(JSONB, default={})
    learning_goals = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="profile")
```

## API Schemas (Pydantic)

### Signup Request

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    profile: Optional["ProfileCreate"] = None

class ProfileCreate(BaseModel):
    software_level: str = "beginner"  # beginner, intermediate, advanced
    hardware_level: str = "none"      # none, some, extensive
    technologies: Dict[str, bool] = {}
    learning_goals: Optional[str] = None
```

### Signin Request/Response

```python
class SigninRequest(BaseModel):
    email: EmailStr
    password: str
    remember_me: bool = False

class AuthResponse(BaseModel):
    user: "UserResponse"
    message: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: Optional[str]
    profile: Optional["ProfileResponse"]

    class Config:
        from_attributes = True
```

### Profile Schemas

```python
class ProfileResponse(BaseModel):
    software_level: str
    hardware_level: str
    technologies: Dict[str, bool]
    learning_goals: Optional[str]

    class Config:
        from_attributes = True

class ProfileUpdate(BaseModel):
    software_level: Optional[str] = None
    hardware_level: Optional[str] = None
    technologies: Optional[Dict[str, bool]] = None
    learning_goals: Optional[str] = None
```

### Session Response

```python
class SessionResponse(BaseModel):
    authenticated: bool
    user: Optional[UserResponse] = None
```

## Frontend Types

```typescript
interface User {
  id: number;
  email: string;
  name?: string;
  profile?: UserProfile;
}

interface UserProfile {
  softwareLevel: 'beginner' | 'intermediate' | 'advanced';
  hardwareLevel: 'none' | 'some' | 'extensive';
  technologies: {
    python?: boolean;
    ros2?: boolean;
    gazebo?: boolean;
    isaac?: boolean;
    aiMl?: boolean;
    unity?: boolean;
    linux?: boolean;
    docker?: boolean;
  };
  learningGoals?: string;
}

interface AuthState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

interface SignupData {
  email: string;
  password: string;
  name?: string;
  profile?: Partial<UserProfile>;
}

interface SigninData {
  email: string;
  password: string;
  rememberMe?: boolean;
}
```

## JWT Token Payload

```python
{
    "sub": "123",           # User ID as string
    "email": "user@example.com",
    "exp": 1735689600,      # Expiration timestamp
    "iat": 1735084800,      # Issued at timestamp
    "type": "session"       # Token type
}
```

