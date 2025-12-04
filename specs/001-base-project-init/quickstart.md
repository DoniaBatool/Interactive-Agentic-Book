# Quickstart Guide: Base Project Initialization

**Feature**: 001-base-project-init
**Date**: 2025-12-04
**Audience**: Developers setting up local development environment

## Overview

This guide walks you through setting up the AI-Native Physical AI & Robotics Textbook development environment from scratch. After completing these steps, you'll have:

- ✅ Frontend (Docusaurus) running at `http://localhost:3000`
- ✅ Backend (FastAPI) running at `http://localhost:8000`
- ✅ All placeholder folders and configuration files in place
- ✅ Ready to implement future features

**Estimated Time**: 10 minutes (with good internet connection)

## Prerequisites

Before starting, ensure you have:

### Required Software

1. **Node.js 18+**
   ```bash
   node --version  # Should output v18.0.0 or higher
   ```
   Install from: https://nodejs.org/

2. **Python 3.11+**
   ```bash
   python3 --version  # Should output 3.11.0 or higher
   ```
   Install from: https://www.python.org/downloads/

3. **Git**
   ```bash
   git --version  # Any recent version
   ```
   Install from: https://git-scm.com/downloads

### Optional (Recommended)

- **VS Code** or your preferred code editor
- **Docker Desktop** (for containerization features, not required for local development)
- **Postman** or **curl** (for testing backend API)

## Step-by-Step Setup

### Step 1: Clone the Repository

```bash
# Clone the project
git clone https://github.com/your-username/interactive-agentic-book.git
cd interactive-agentic-book

# Checkout the feature branch (if working on this feature)
git checkout 001-base-project-init
```

### Step 2: Setup Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Open .env in your editor and fill in values (all optional for now)
# For initial setup, you can leave everything as placeholders
```

**Example `.env` file** (initial scaffold - all optional):
```bash
# OpenAI API (optional - not used in initial scaffold)
OPENAI_API_KEY=sk-your-key-here-optional

# Qdrant Vector Database (optional - not used in initial scaffold)
QDRANT_URL=https://your-instance.qdrant.io:6333
QDRANT_API_KEY=your-qdrant-api-key-optional

# Neon Serverless Postgres (optional - not used in initial scaffold)
DATABASE_URL=postgresql://user:password@host/database

# BetterAuth (optional - not used in initial scaffold)
BETTERAUTH_SECRET=your-32-character-secret-key-optional

# SMTP Email (optional - not used in initial scaffold)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@example.com
SMTP_PASSWORD=your-app-password-optional

# Application Configuration (optional - defaults work)
NODE_ENV=development
PORT_FRONTEND=3000
PORT_BACKEND=8000
```

**Note**: Since this is the initial scaffold phase with no actual integrations, you can leave all values as placeholders. The applications will start and run without them, logging warnings about missing credentials.

### Step 3: Setup Frontend (Docusaurus)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (this may take 2-3 minutes)
npm install

# Start the development server
npm start
```

**Expected Output**:
```
[INFO] Starting the development server...
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

**Verify**: Open `http://localhost:3000` in your browser. You should see the Docusaurus default homepage.

**Common Issues**:
- **Port 3000 already in use**: Change port with `npm start -- --port 3001`
- **EACCES permission error**: Run with `sudo` (not recommended) or fix npm permissions
- **Module not found**: Delete `node_modules/` and `package-lock.json`, then run `npm install` again

### Step 4: Setup Backend (FastAPI)

Open a **new terminal** (keep frontend running), then:

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -e .

# Start the FastAPI development server
uvicorn app.main:app --reload
```

**Expected Output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Verify**: Open `http://localhost:8000/health` in your browser. You should see:
```json
{
  "status": "healthy",
  "timestamp": "2025-12-04T17:30:00.000Z"
}
```

**API Documentation**: Visit `http://localhost:8000/docs` for interactive Swagger UI.

**Common Issues**:
- **Port 8000 already in use**: Change port with `uvicorn app.main:app --reload --port 8001`
- **Module not found**: Ensure virtual environment is activated and dependencies installed
- **Python version error**: Verify Python 3.11+ is installed and used for venv creation

### Step 5: Verify Project Structure

```bash
# From project root, check folder structure
ls -la

# Should see:
# - frontend/        (Docusaurus application)
# - backend/         (FastAPI application)
# - infrastructure/  (Docker configurations)
# - scripts/         (Setup automation scripts)
# - .env.example     (Environment variable template)
# - .gitignore       (Git ignore rules)
# - README.md        (Project documentation)
```

**Check Placeholders**:
```bash
# Backend placeholders
ls backend/app/agents/subagents/  # Should see .gitkeep
ls backend/app/agents/skills/     # Should see .gitkeep
ls backend/app/services/          # Should see qdrant_client.py, openai_client.py

# Frontend placeholders
ls frontend/src/components/       # Should see .gitkeep
ls frontend/src/theme/            # Should see .gitkeep
```

### Step 6: Run Quick Tests

**Test Frontend**:
```bash
# In frontend directory
npm run build

# Should complete without errors
# Build output in frontend/build/
```

**Test Backend Health Endpoint**:
```bash
# Using curl
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","timestamp":"2025-12-04T17:30:00.000Z"}

# Using httpie (if installed)
http GET localhost:8000/health
```

### Step 7: (Optional) Test Docker Setup

If you have Docker installed:

```bash
# From project root
cd infrastructure/docker

# Build frontend image
docker build -f Dockerfile.frontend -t ai-textbook-frontend:latest ../..

# Build backend image
docker build -f Dockerfile.backend -t ai-textbook-backend:latest ../..

# Run with docker-compose
docker-compose up

# Verify:
# - Frontend at http://localhost:3000
# - Backend at http://localhost:8000/health
```

**Note**: Docker configurations are placeholders and may need refinement for production use.

## Development Workflow

### Running Both Services

**Option 1: Separate Terminals** (Recommended for development)
```bash
# Terminal 1 - Frontend
cd frontend && npm start

# Terminal 2 - Backend
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload
```

**Option 2: Background Processes**
```bash
# Frontend in background
cd frontend && npm start &

# Backend in background
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload &

# View logs
tail -f ~/.npm/_logs/*.log
tail -f backend/logs/app.log  # if logging configured
```

**Option 3: Use tmux or screen** (for advanced users)

### Making Changes

**Frontend Changes**:
- Edit files in `frontend/docs/` for content
- Edit `frontend/src/components/` for React components
- Edit `frontend/docusaurus.config.js` for configuration
- Hot reload is automatic (changes appear immediately)

**Backend Changes**:
- Edit files in `backend/app/`
- Uvicorn's `--reload` flag auto-restarts on file changes
- Check logs for any errors

**Environment Variables**:
- Update `.env` file
- Restart backend to pick up changes (frontend needs rebuild)

### Stopping Services

```bash
# Stop frontend (in its terminal)
Ctrl + C

# Stop backend (in its terminal)
Ctrl + C

# Or if running in background
pkill -f "npm start"
pkill -f "uvicorn"
```

## Verification Checklist

Before proceeding to implement features, verify:

- [ ] Frontend loads at `http://localhost:3000`
- [ ] Backend health endpoint responds at `http://localhost:8000/health`
- [ ] Frontend shows Docusaurus default page
- [ ] Backend API docs accessible at `http://localhost:8000/docs`
- [ ] All placeholder folders exist (use `find . -name ".gitkeep"`)
- [ ] `.env` file created (even if using placeholder values)
- [ ] No errors in terminal logs
- [ ] Both services start in under 10 seconds

## Next Steps

Once setup is complete:

1. **Read the Constitution**: `.specify/memory/constitution.md` for project principles
2. **Review Spec**: `specs/001-base-project-init/spec.md` for feature details
3. **Check Plan**: `specs/001-base-project-init/plan.md` for architecture
4. **Run `/sp.tasks`**: Generate implementation tasks from this plan
5. **Start Implementing**: Follow TDD workflow (tests first, then implementation)

## Troubleshooting

### Frontend Issues

**Problem**: `npm install` fails with EACCES error
**Solution**: Fix npm permissions or use nvm (Node Version Manager)
```bash
# Using nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

**Problem**: Port 3000 already in use
**Solution**: Use a different port
```bash
npm start -- --port 3001
```

**Problem**: Build fails with "Cannot find module"
**Solution**: Clear cache and reinstall
```bash
rm -rf node_modules package-lock.json
npm install
```

### Backend Issues

**Problem**: `ModuleNotFoundError` even after pip install
**Solution**: Ensure virtual environment is activated and re-install
```bash
deactivate  # if already in venv
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Problem**: `uvicorn: command not found`
**Solution**: Install uvicorn explicitly
```bash
pip install "uvicorn[standard]"
```

**Problem**: Port 8000 already in use
**Solution**: Use a different port
```bash
uvicorn app.main:app --reload --port 8001
```

### Environment Variable Issues

**Problem**: Backend warns about missing environment variables
**Solution**: This is expected in initial scaffold. Add values to `.env` when needed:
```bash
# Edit .env and add your actual API keys
nano .env  # or code .env
```

**Problem**: `.env` changes not taking effect
**Solution**: Restart the backend server (frontend requires rebuild)
```bash
# Stop and restart backend
Ctrl + C
uvicorn app.main:app --reload
```

## Resources

- **Docusaurus Docs**: https://docusaurus.io/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Python Virtual Environments**: https://docs.python.org/3/library/venv.html
- **npm Docs**: https://docs.npmjs.com/
- **Project Constitution**: `.specify/memory/constitution.md`
- **GitHub Issues**: Report problems at `https://github.com/your-username/interactive-agentic-book/issues`

## Support

If you encounter issues not covered here:

1. Check the **troubleshooting section** above
2. Search **existing GitHub issues**
3. Ask in the project **Discord/Slack** (if available)
4. Create a **new GitHub issue** with:
   - OS and version
   - Node.js and Python versions
   - Complete error message
   - Steps to reproduce

---

**Success!** 🎉 Your development environment is ready. Start building features by running `/sp.tasks` to generate implementation tasks.
