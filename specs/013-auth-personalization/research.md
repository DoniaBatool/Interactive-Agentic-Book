# Research Notes – Feature 013: Auth & Personalization

## BetterAuth Overview

BetterAuth (https://www.better-auth.com/) is a modern authentication library:

- **TypeScript-first**: Full type safety
- **Framework agnostic**: Works with any framework
- **Self-hosted**: No vendor lock-in
- **Flexible**: Email/password, OAuth, magic links
- **Secure**: Built-in best practices

### BetterAuth vs Alternatives

| Feature | BetterAuth | NextAuth | Clerk |
|---------|------------|----------|-------|
| Self-hosted | ✅ | ✅ | ❌ |
| TypeScript | ✅ | ✅ | ✅ |
| Price | Free | Free | Paid |
| Customization | High | Medium | Low |
| Setup Complexity | Medium | Low | Low |

## Implementation Approach

### Option 1: Use BetterAuth Directly
- Install `better-auth` npm package
- Configure with database adapter
- Use built-in React hooks

### Option 2: Custom Implementation (Chosen)
- Implement auth logic in FastAPI backend
- Use BetterAuth concepts (session tokens, password hashing)
- More control over flow and database schema
- Better integration with existing FastAPI backend

## Password Hashing

### bcrypt (Recommended)
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
hashed = pwd_context.hash("password123")

# Verify password
is_valid = pwd_context.verify("password123", hashed)
```

### Why bcrypt?
- Adaptive: Cost factor can be increased over time
- Salted: Each hash includes unique salt
- Slow: Intentionally slow to prevent brute force
- Battle-tested: Used by millions of applications

## JWT Session Tokens

### Token Structure
```python
from jose import jwt

payload = {
    "sub": str(user_id),
    "email": email,
    "exp": datetime.utcnow() + timedelta(days=7),
    "iat": datetime.utcnow()
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### Token Storage Options

| Method | Security | Persistence | XSS Safe |
|--------|----------|-------------|----------|
| httpOnly Cookie | High | Yes | Yes |
| localStorage | Low | Yes | No |
| sessionStorage | Medium | No | No |
| Memory | High | No | Yes |

**Chosen**: httpOnly Cookie (best balance of security and UX)

## Cookie Settings

```python
response.set_cookie(
    key="session_token",
    value=token,
    httponly=True,      # JavaScript can't access
    secure=True,        # HTTPS only
    samesite="lax",     # CSRF protection
    max_age=604800,     # 7 days
    path="/",           # Available on all paths
)
```

## Profile Questions Design

### Software Experience Levels
- **Beginner**: New to programming or just learning Python
- **Intermediate**: Comfortable with Python, some experience with frameworks
- **Advanced**: Professional developer, familiar with ROS/robotics

### Hardware Experience Levels
- **None**: No experience with embedded systems or robots
- **Some**: Basic Arduino/Raspberry Pi, or used robots in demos
- **Extensive**: Worked with Jetson, RealSense, or professional robots

### Technologies (Checkboxes)
- Python
- ROS 2
- Gazebo/Isaac Sim
- NVIDIA Isaac
- AI/ML (TensorFlow, PyTorch)
- Unity
- Linux/Ubuntu
- Docker

## Personalization Use Cases

1. **Content Level Adjustment**
   - Beginner: More explanations, basic examples
   - Advanced: Skip basics, focus on advanced topics

2. **RAG Context Enhancement**
   - Include user profile in system prompt
   - "This user is a beginner with no ROS experience..."

3. **Chapter Personalization Button**
   - Rewrite chapter content for user's level
   - Cache personalized versions

## Security Best Practices

1. **Password Requirements**
   - Minimum 8 characters
   - Mix of letters and numbers (optional)
   - Check against common passwords

2. **Rate Limiting**
   - Max 5 login attempts per minute
   - Account lockout after 10 failures
   - CAPTCHA for suspicious activity

3. **Session Security**
   - Short token expiry (7 days)
   - Token refresh on activity
   - Single session or multi-device choice

4. **CORS Configuration**
   - Strict origin validation
   - Credentials: include only for trusted origins

