# Quickstart – Feature 013: Auth & Personalization (BetterAuth)

## Prerequisites

- Node.js 18+ installed
- Python 3.11+ with venv
- Neon PostgreSQL database (from Feature 012)
- OpenAI API key for personalization

## Architecture Overview

```
Frontend (:3000) → BetterAuth Server (:8001) → Neon DB
                → FastAPI Backend (:8000)   → Neon DB + Qdrant
```

## Install Dependencies

### 1. BetterAuth Server Setup

```bash
cd C:\Users\Leo\interactive-agentic-book\auth-server
npm install
```

### 2. Backend Dependencies

```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
pip install asyncpg email-validator
```

## Environment Variables

Add to `.env` in project root:

```env
# Database (shared between BetterAuth and FastAPI)
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-1.aws.neon.tech/textbook_db?sslmode=require

# OpenAI for personalization
OPENAI_API_KEY=sk-proj-...

# Optional: Auth server port
AUTH_PORT=8001

# Optional: Frontend URL for CORS
FRONTEND_URL=http://localhost:3000

# OAuth Providers (Optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret

# Email Service (Optional - for email verification and password reset)
# Currently logs to console. In production, integrate with:
# - SendGrid: SENDGRID_API_KEY=...
# - Resend: RESEND_API_KEY=...
# - SMTP: SMTP_HOST=..., SMTP_PORT=..., SMTP_USER=..., SMTP_PASS=...
```

## Database Setup

### Create BetterAuth Tables

1. Go to Neon Console: https://console.neon.tech
2. Select your database
3. Open SQL Editor
4. Run this SQL:

```sql
-- BetterAuth required tables
CREATE TABLE IF NOT EXISTS "user" (
    "id" TEXT PRIMARY KEY,
    "email" TEXT UNIQUE NOT NULL,
    "emailVerified" BOOLEAN DEFAULT FALSE,
    "name" TEXT,
    "image" TEXT,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Custom fields for personalization
    "softwareLevel" TEXT DEFAULT 'beginner',
    "hardwareLevel" TEXT DEFAULT 'none',
    "technologies" TEXT DEFAULT '{}',
    "learningGoals" TEXT
);

CREATE TABLE IF NOT EXISTS "session" (
    "id" TEXT PRIMARY KEY,
    "userId" TEXT NOT NULL REFERENCES "user"("id") ON DELETE CASCADE,
    "expiresAt" TIMESTAMP NOT NULL,
    "token" TEXT UNIQUE NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "ipAddress" TEXT,
    "userAgent" TEXT
);

CREATE TABLE IF NOT EXISTS "account" (
    "id" TEXT PRIMARY KEY,
    "userId" TEXT NOT NULL REFERENCES "user"("id") ON DELETE CASCADE,
    "accountId" TEXT NOT NULL,
    "providerId" TEXT NOT NULL,
    "accessToken" TEXT,
    "refreshToken" TEXT,
    "idToken" TEXT,
    "accessTokenExpiresAt" TIMESTAMP,
    "refreshTokenExpiresAt" TIMESTAMP,
    "scope" TEXT,
    "password" TEXT,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "verification" (
    "id" TEXT PRIMARY KEY,
    "identifier" TEXT NOT NULL,
    "value" TEXT NOT NULL,
    "expiresAt" TIMESTAMP NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Start All Services

### Terminal 1: Frontend
```bash
cd C:\Users\Leo\interactive-agentic-book
npm run start
```

### Terminal 2: BetterAuth Server
```bash
cd C:\Users\Leo\interactive-agentic-book\auth-server
npm run dev
```

### Terminal 3: FastAPI Backend
```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
uvicorn backend.app.main:app --reload --port 8000
```

## Verify Services

Check all services are running:

| Service | URL | Expected Response |
|---------|-----|------------------|
| Frontend | http://localhost:3000 | Docusaurus homepage |
| BetterAuth | http://localhost:8001/health | `{"status":"ok"}` |
| FastAPI | http://localhost:8000/health | `{"status":"ok"}` |

## Test Authentication Flow

### 1. Sign Up
1. Go to: http://localhost:3000/auth/signup
2. Fill form:
   - Email: `test@example.com`
   - Password: `password123`
   - Name: `Test User`
   - Software Level: `Intermediate`
   - Hardware Level: `Some`
   - Technologies: Check `Python`, `ROS 2`
   - Learning Goals: `Learn humanoid robotics`
3. Click **Create Account**
4. Should redirect to home with user menu visible

### 2. Test Personalization
1. Go to any chapter: http://localhost:3000/docs/intro
2. Should see personalization banner with level badge
3. Click **✨ Personalize Content** button
4. Wait for processing (spinner shows)
5. Content should adapt to "Intermediate" level
6. Should see **✓ Content personalized for your level!**
7. Click **Restore Original** to revert

### 3. Profile Management
1. Click user menu → **Profile**
2. Update software level to "Advanced"
3. Test personalization again (should be more complex)

## Troubleshooting

### BetterAuth Server Issues
```bash
# Check if port 8001 is free
netstat -an | findstr :8001

# Restart auth server
cd auth-server
npm run dev
```

### Database Connection Issues
```bash
# Test database connection
psql "postgresql://user:pass@host/db" -c "SELECT 1;"
```

### Frontend Build Issues
```bash
# Clear cache and reinstall
npm run clear
npm install
npm run start
```

## Development Workflow

### Making Changes
1. **Auth Changes**: Restart BetterAuth server
2. **Backend Changes**: FastAPI auto-reloads
3. **Frontend Changes**: Docusaurus auto-reloads

### Adding New User Fields
1. Update `auth-server/src/auth.ts` additionalFields
2. Add database migration
3. Update frontend forms and types

### Debugging
- **Auth Server Logs**: Check terminal 2
- **Backend Logs**: Check terminal 3  
- **Frontend Errors**: F12 → Console tab
- **Network Requests**: F12 → Network tab

## Production Deployment

### Environment Variables
```env
# Production database
DATABASE_URL=postgresql://prod-user:pass@prod-host/db

# Production OpenAI
OPENAI_API_KEY=sk-proj-production-key

# Production URLs
FRONTEND_URL=https://yourdomain.com
AUTH_PORT=8001
```

### Build Commands
```bash
# Build auth server
cd auth-server && npm run build

# Build frontend
npm run build

# Backend runs directly with uvicorn
```

### Security Checklist
- [ ] Change JWT_SECRET_KEY in production
- [ ] Use HTTPS for all services
- [ ] Set secure CORS origins
- [ ] Enable database SSL
- [ ] Use environment-specific API keys

---

**🎯 Quick Start Complete!**

You now have:
- ✅ BetterAuth authentication system
- ✅ Content personalization based on user level
- ✅ Profile management with preferences
- ✅ Session persistence and security
- ✅ Dark/light mode compatibility

**Next Steps**: Test all features and customize personalization prompts for your content!