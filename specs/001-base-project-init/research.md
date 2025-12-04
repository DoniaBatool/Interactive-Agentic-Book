# Research: Base Project Initialization

**Feature**: 001-base-project-init
**Date**: 2025-12-04
**Purpose**: Document technology choices, best practices, and implementation approaches for project scaffolding

## Overview

This document captures research findings for establishing the foundational project structure. Since this is an infrastructure setup task with well-established technology stack (mandated by constitution), research focuses on initialization patterns, configuration best practices, and folder structure conventions.

## Technology Decisions

### 1. Frontend Framework: Docusaurus 3.x

**Decision**: Use Docusaurus 3.x as the primary frontend framework

**Rationale**:
- **Constitutional Mandate**: Constitution Principle II explicitly requires Docusaurus-First strategy
- **Documentation-Focused**: Purpose-built for creating documentation sites with excellent DX
- **React Integration**: Built on React 18+, enabling custom components for interactive features
- **Static Generation**: Produces static HTML for optimal performance and GitHub Pages compatibility
- **MDX Support**: Native support for embedding React components in Markdown
- **Plugin Architecture**: Extensible for future RAG chatbot, personalization, and translation features

**Initialization Method**:
```bash
npx create-docusaurus@latest frontend classic --typescript
```

**Alternatives Considered**:
- **Next.js**: More flexible but overkill for documentation-focused site
- **VitePress**: Lighter weight but lacks React ecosystem integration
- **Custom React**: Would require reinventing documentation infrastructure

**Best Practices**:
- Use TypeScript for type safety
- Follow Docusaurus project structure conventions
- Configure `docusaurus.config.js` with site metadata early
- Use classic preset for standard documentation features

### 2. Backend Framework: FastAPI 0.109+

**Decision**: Use FastAPI as the Python backend framework

**Rationale**:
- **Constitutional Mandate**: Constitution Principle III specifies FastAPI for RAG chatbot backend
- **Modern Python**: Native async/await support, type hints with Pydantic
- **OpenAPI Integration**: Automatic API documentation generation
- **Performance**: One of the fastest Python frameworks (comparable to Node.js/Go)
- **Developer Experience**: Excellent documentation, intuitive decorator-based routing

**Initialization Pattern**:
Manual project structure creation following FastAPI best practices (no official CLI exists)

**Alternatives Considered**:
- **Django**: Too heavyweight for API-only backend, brings unnecessary ORM/admin
- **Flask**: Older design, lacks native async support and type validation
- **Starlette**: FastAPI is built on Starlette, using FastAPI gives higher-level abstractions

**Best Practices**:
- Use `uvicorn` as ASGI server for development
- Structure with `app/` directory containing modular components
- Use Pydantic models for request/response validation
- Implement dependency injection for configuration and services
- Use `python-dotenv` for environment variable management

### 3. Python Dependency Management: pyproject.toml

**Decision**: Use `pyproject.toml` with `pip` for Python dependency management

**Rationale**:
- **PEP 518 Standard**: Modern Python packaging standard
- **Single Configuration**: Combines project metadata, dependencies, and build config
- **Tool Compatibility**: Works with pip, setuptools, and modern Python tooling

**Configuration Structure**:
```toml
[project]
name = "ai-robotics-textbook-backend"
version = "0.1.0"
requires-python = ">=3.11"

[project.dependencies]
fastapi = "^0.109.0"
uvicorn = {extras = ["standard"], version = "^0.27.0"}
pydantic = "^2.5.0"
python-dotenv = "^1.0.0"
# Placeholders for future features
qdrant-client = "^1.7.0"
openai = "^1.10.0"
psycopg2-binary = "^2.9.9"
sqlalchemy = "^2.0.25"
```

**Alternatives Considered**:
- **Poetry**: More opinionated, adds extra tooling layer
- **Pipenv**: Falling out of favor, slower resolver
- **requirements.txt**: Legacy approach, lacks metadata structure

### 4. Node.js Package Manager: npm

**Decision**: Use npm (default with Node.js) for JavaScript/TypeScript dependencies

**Rationale**:
- **Ubiquitous**: Comes with Node.js, no additional installation
- **Docusaurus Compatibility**: Official Docusaurus docs use npm examples
- **Simplicity**: Works out-of-box, minimal configuration needed

**Alternatives Considered**:
- **pnpm**: Faster, more efficient disk usage, but requires separate installation
- **yarn**: Popular alternative, but npm has caught up in recent versions

**Decision**: Default to npm, can switch to pnpm/yarn later if needed (spec allows flexibility)

### 5. Environment Variable Management

**Decision**: Use `.env` files with `python-dotenv` (backend) and `dotenv-webpack` (frontend if needed)

**Rationale**:
- **Industry Standard**: Widely adopted pattern (12-factor app methodology)
- **Git Safety**: `.env` excluded from version control, `.env.example` tracked
- **Documentation**: Clear variable listing helps onboarding

**Required Environment Variables** (from spec FR-003):
```bash
# OpenAI API
OPENAI_API_KEY=sk-...

# Qdrant Vector Database
QDRANT_URL=https://...
QDRANT_API_KEY=...

# Neon Serverless Postgres
DATABASE_URL=postgresql://...

# BetterAuth
BETTERAUTH_SECRET=...

# SMTP for email verification
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=...
SMTP_PASSWORD=...
```

**Best Practices**:
- Prefix with service name for clarity (OPENAI_, QDRANT_, etc.)
- Use descriptive placeholder values in `.env.example`
- Document required vs optional variables
- Validate presence of critical variables on application startup

### 6. Docker Configuration

**Decision**: Create placeholder Dockerfiles using multi-stage builds

**Rationale**:
- Spec requires Docker files exist (FR-008) but doesn't require functional containers
- Multi-stage builds optimize image size (separate build and runtime stages)
- Docker Compose simplifies local multi-service development

**Dockerfile Pattern** (Frontend):
```dockerfile
# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Dockerfile Pattern** (Backend):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install -e .
COPY ./app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Note**: These are placeholders and will be refined in deployment features

### 7. Version Control: Git Ignore Strategy

**Decision**: Create comprehensive `.gitignore` covering all environments

**Categories to Exclude**:
- **Secrets**: `.env`, `.env.local`, credentials files
- **Dependencies**: `node_modules/`, `.venv/`, `__pycache__/`
- **Build Artifacts**: `build/`, `dist/`, `.docusaurus/`
- **IDE Files**: `.vscode/`, `.idea/`, `*.swp`
- **OS Files**: `.DS_Store`, `Thumbs.db`
- **Python**: `*.pyc`, `*.pyo`, `*.egg-info/`

**Best Practice**: Use separate `.gitignore` files in frontend/ and backend/ for context-specific ignores

## Implementation Patterns

### Frontend Structure (Docusaurus)

**Initialization Steps**:
1. Run `npx create-docusaurus@latest frontend classic --typescript`
2. Configure `docusaurus.config.js` with project metadata
3. Create placeholder folders: `src/components/`, `src/theme/`, `src/styles/`, `src/agents/`
4. Add `.gitkeep` files to preserve empty folders in git

**Configuration Highlights**:
- **Title**: "AI-Native Physical AI & Robotics Textbook"
- **URL**: TBD (will be GitHub Pages URL)
- **Base URL**: "/" (root deployment)
- **Favicon**: Use Docusaurus default initially
- **Navbar**: Default structure with "Docs", "About" links
- **Footer**: Default Docusaurus footer with project info

### Backend Structure (FastAPI)

**Initialization Pattern**:
1. Create `backend/` directory structure manually
2. Write `backend/app/main.py` with FastAPI app instance
3. Implement `/health` endpoint in `backend/app/api/health.py`
4. Create `backend/app/config/settings.py` for environment variables
5. Add placeholder modules with `__init__.py` and `.gitkeep` files

**Health Endpoint Specification**:
```python
# backend/app/api/health.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
```

**Main Application Pattern**:
```python
# backend/app/main.py
from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="AI Robotics Textbook API",
    version="0.1.0",
    description="Backend API for AI-Native Physical AI & Robotics Textbook"
)

app.include_router(health_router, tags=["health"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Configuration Management Pattern

**Backend Settings (Pydantic)**:
```python
# backend/app/config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str | None = None

    # Qdrant
    qdrant_url: str | None = None
    qdrant_api_key: str | None = None

    # Database
    database_url: str | None = None

    # Auth
    betterauth_secret: str | None = None

    # SMTP
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_user: str | None = None
    smtp_password: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

### Setup Scripts Pattern

**Master Setup Script**:
```bash
#!/bin/bash
# scripts/setup.sh

echo "Setting up AI-Native Physical AI & Robotics Textbook..."

# Check prerequisites
command -v node >/dev/null 2>&1 || { echo "Node.js 18+ required"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Python 3.11+ required"; exit 1; }

# Setup frontend
echo "Setting up frontend..."
cd frontend && npm install && cd ..

# Setup backend
echo "Setting up backend..."
cd backend && python3 -m venv .venv && source .venv/bin/activate && pip install -e . && cd ..

# Create .env from example
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env file created. Please fill in your API keys and credentials."
fi

echo "Setup complete! Run 'npm start' in frontend/ and 'uvicorn app.main:app --reload' in backend/app/"
```

## Placeholder File Strategy

**Purpose**: Preserve empty folders in git while documenting future implementation

**Approach**:
1. Add `.gitkeep` file to empty folders (git convention)
2. Add `__init__.py` to Python packages (makes them importable)
3. Add TODO comments in placeholder Python files

**Example Placeholder**:
```python
# backend/app/services/qdrant_client.py
"""
Qdrant vector database client wrapper.

TODO: Implement Qdrant client initialization and vector operations
This will be used for:
- Storing textbook content embeddings
- Semantic search for RAG chatbot
- User query vectorization
"""

# Placeholder for future implementation
pass
```

## Validation & Success Criteria

### Development Environment Validation

**Checklist**:
1. ✅ Node.js 18+ installed (`node --version`)
2. ✅ Python 3.11+ installed (`python3 --version`)
3. ✅ Git installed (`git --version`)
4. ✅ Frontend runs: `cd frontend && npm start` → localhost:3000
5. ✅ Backend runs: `cd backend && uvicorn app.main:app` → localhost:8000/health returns 200
6. ✅ All folders exist per spec
7. ✅ `.env.example` has all required variables
8. ✅ Docker builds succeed (even if minimal)

### Performance Targets

From spec SC-001 and SC-002:
- **Frontend setup time**: < 10 minutes (npm install + start)
- **Backend setup time**: < 10 minutes (pip install + start)
- **Total setup time**: < 10 minutes (parallel setup possible)

**Measured on**: macOS/Linux with good internet connection

## Risks & Mitigations

### Risk 1: Dependency Installation Failures

**Probability**: Medium (network issues, version conflicts)
**Impact**: High (blocks development)

**Mitigation**:
- Lock dependency versions in `package-lock.json` and `pyproject.toml`
- Provide troubleshooting section in README
- Test on clean VM/container before release

### Risk 2: Port Conflicts

**Probability**: Medium (common dev ports 3000, 8000 often in use)
**Impact**: Low (easy to change ports)

**Mitigation**:
- Document how to change ports in README
- Check port availability in setup scripts
- Suggest alternatives (3001, 8001, etc.)

### Risk 3: Environment Variable Confusion

**Probability**: High (new developers often forget to configure .env)
**Impact**: Medium (services won't connect, but app should still start)

**Mitigation**:
- Clear `.env.example` with descriptive comments
- Backend validates required variables on startup
- Helpful error messages indicating missing variables

### Risk 4: Cross-Platform Compatibility

**Probability**: Medium (Windows vs Unix path differences)
**Impact**: Medium (setup scripts may fail on Windows)

**Mitigation**:
- Use platform-agnostic commands where possible
- Provide Windows-specific setup instructions
- Use forward slashes in paths (works on all platforms)

## Next Steps (Phase 1)

After this research phase is complete, Phase 1 will create:

1. **data-model.md**: Configuration schemas (Environment variables, Settings objects)
2. **contracts/**: API specification for /health endpoint (OpenAPI YAML)
3. **quickstart.md**: Step-by-step developer setup guide

These artifacts will provide the detailed specifications needed for implementation in the `/sp.tasks` phase.

## References

- Docusaurus Documentation: https://docusaurus.io/docs
- FastAPI Documentation: https://fastapi.tiangolo.com/
- 12-Factor App Methodology: https://12factor.net/
- Python Packaging (PEP 518): https://peps.python.org/pep-0518/
- Pydantic Settings: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
