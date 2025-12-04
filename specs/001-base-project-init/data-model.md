# Data Model: Base Project Initialization

**Feature**: 001-base-project-init
**Date**: 2025-12-04
**Purpose**: Define configuration schemas, environment variables, and project metadata structures

## Overview

This feature is purely infrastructure setup with no business entities or database schemas. The "data model" for this phase consists entirely of **configuration structures** that define how the application loads settings, manages environment variables, and validates startup requirements.

**Note**: No user data, business entities, or database tables exist in this phase. Future features will add actual data models for users, content, chat history, etc.

## Configuration Schemas

### 1. Environment Variables Schema

**Purpose**: Define all environment variables required for the application

**Storage**: `.env` file (git-ignored), `.env.example` file (tracked in git)

**Schema Definition**:

```typescript
// Conceptual TypeScript interface (not implemented in this phase)
interface EnvironmentVariables {
  // === OpenAI Configuration ===
  OPENAI_API_KEY: string;          // Required for AI features (placeholder in init phase)

  // === Qdrant Vector Database ===
  QDRANT_URL: string;               // e.g., "https://xyz.qdrant.io:6333"
  QDRANT_API_KEY: string;           // API key for Qdrant cloud

  // === Neon Serverless Postgres ===
  DATABASE_URL: string;             // Connection string: "postgresql://user:pass@host/db"

  // === BetterAuth ===
  BETTERAUTH_SECRET: string;        // Secret key for session encryption (min 32 chars)

  // === SMTP Email Service ===
  SMTP_HOST: string;                // e.g., "smtp.gmail.com"
  SMTP_PORT: number;                // Default: 587 (TLS)
  SMTP_USER: string;                // Email address for sending
  SMTP_PASSWORD: string;            // App password or SMTP password

  // === Application Configuration ===
  NODE_ENV?: 'development' | 'production' | 'test';  // Default: 'development'
  PORT_FRONTEND?: number;           // Default: 3000
  PORT_BACKEND?: number;            // Default: 8000
}
```

**Validation Rules**:
- `OPENAI_API_KEY`: Must start with "sk-", optional in this phase
- `QDRANT_URL`: Must be valid URL format, optional in this phase
- `QDRANT_API_KEY`: Non-empty string, optional in this phase
- `DATABASE_URL`: Must match PostgreSQL connection string format, optional in this phase
- `BETTERAUTH_SECRET`: Minimum 32 characters, optional in this phase
- `SMTP_*`: All optional in this phase (no actual email sending)

**Default Values** (when not provided):
- `NODE_ENV`: "development"
- `PORT_FRONTEND`: 3000
- `PORT_BACKEND`: 8000
- `SMTP_PORT`: 587

### 2. Backend Settings Model (Pydantic)

**Purpose**: Type-safe configuration loading and validation in Python backend

**Implementation**: `backend/app/config/settings.py`

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    All API keys and credentials are optional in this initial phase.
    Future features will require these values and add validation.
    """

    # === OpenAI Configuration ===
    openai_api_key: Optional[str] = None

    # === Qdrant Vector Database ===
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None

    # === Database Configuration ===
    database_url: Optional[str] = None

    # === Authentication ===
    betterauth_secret: Optional[str] = None

    # === Email Configuration ===
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None

    # === Application Configuration ===
    environment: str = "development"
    backend_port: int = 8000
    cors_origins: list[str] = ["http://localhost:3000"]  # Frontend URL

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Allow both OPENAI_API_KEY and openai_api_key

# Singleton instance
settings = Settings()
```

**Usage Pattern**:
```python
from app.config.settings import settings

# Access configuration
api_key = settings.openai_api_key
if api_key:
    # Initialize OpenAI client
    pass
else:
    # Log warning, skip OpenAI features
    print("Warning: OPENAI_API_KEY not set, AI features disabled")
```

**Validation Strategy**:
- **Optional in init phase**: No errors if variables missing
- **Warnings logged**: Missing variables generate startup warnings
- **Graceful degradation**: App starts even without credentials (no external service calls)

### 3. Frontend Environment Configuration

**Purpose**: Client-side environment variables (minimal in this phase)

**Docusaurus Configuration**: `frontend/docusaurus.config.js`

```javascript
// @ts-check
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI-Native Physical AI & Robotics Textbook',
  tagline: 'Interactive Learning Platform for Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  // Deployment configuration
  url: process.env.SITE_URL || 'https://your-username.github.io',
  baseUrl: process.env.BASE_URL || '/',
  organizationName: process.env.GITHUB_ORG || 'your-username',
  projectName: process.env.PROJECT_NAME || 'interactive-agentic-book',

  // Build configuration
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Internationalization (prepared for Urdu translation feature)
  i18n: {
    defaultLocale: 'en',
    locales: ['en'], // 'ur' will be added in translation feature
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/', // Docs at root
        },
        blog: false, // No blog in this project
        theme: {
          customCss: require.resolve('./src/styles/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Physical AI Textbook',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Learn',
          },
          {
            href: 'https://github.com/your-username/interactive-agentic-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} AI-Native Physical AI Textbook. Built with Docusaurus.`,
      },
    }),
};

module.exports = config;
```

**Environment Variables (Frontend)**:
- `SITE_URL`: Deployment URL (default: placeholder)
- `BASE_URL`: Base path (default: "/")
- `GITHUB_ORG`: GitHub organization name
- `PROJECT_NAME`: Repository name

**Note**: Frontend environment variables are build-time only (embedded in static site)

### 4. Package Metadata Schemas

#### Frontend Package Metadata

**File**: `frontend/package.json`

```json
{
  "name": "ai-robotics-textbook-frontend",
  "version": "0.1.0",
  "private": true,
  "description": "Frontend for AI-Native Physical AI & Robotics Textbook",
  "scripts": {
    "docusaurus": "docusaurus",
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "serve": "docusaurus serve",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids"
  },
  "dependencies": {
    "@docusaurus/core": "^3.0.0",
    "@docusaurus/preset-classic": "^3.0.0",
    "@mdx-js/react": "^3.0.0",
    "clsx": "^2.0.0",
    "prism-react-renderer": "^2.3.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@docusaurus/module-type-aliases": "^3.0.0",
    "@docusaurus/types": "^3.0.0",
    "typescript": "~5.3.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

**Key Fields**:
- `name`: Package identifier
- `version`: Semantic versioning (starts at 0.1.0)
- `scripts`: npm commands for development
- `dependencies`: Production dependencies
- `devDependencies`: Development-only dependencies
- `engines`: Node.js version requirement

#### Backend Package Metadata

**File**: `backend/pyproject.toml`

```toml
[project]
name = "ai-robotics-textbook-backend"
version = "0.1.0"
description = "Backend API for AI-Native Physical AI & Robotics Textbook"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]

dependencies = [
    "fastapi>=0.109.0,<1.0.0",
    "uvicorn[standard]>=0.27.0,<1.0.0",
    "pydantic>=2.5.0,<3.0.0",
    "pydantic-settings>=2.1.0,<3.0.0",
    "python-dotenv>=1.0.0,<2.0.0",
    # Placeholders for future features (optional imports)
    "qdrant-client>=1.7.0,<2.0.0",
    "openai>=1.10.0,<2.0.0",
    "psycopg2-binary>=2.9.9,<3.0.0",
    "sqlalchemy>=2.0.25,<3.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "httpx>=0.25.0",  # For testing FastAPI
    "black>=23.12.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.black]
line-length = 100
target-version = ['py311']

[tool.ruff]
line-length = 100
target-version = "py311"
```

**Key Sections**:
- `[project]`: Package metadata and dependencies
- `[project.optional-dependencies]`: Dev tools (pytest, linters)
- `[build-system]`: Build tool configuration
- `[tool.*]`: Tool-specific configurations (pytest, black, ruff)

### 5. Docker Configuration Schema

#### Frontend Dockerfile

**File**: `infrastructure/docker/Dockerfile.frontend`

```dockerfile
# Multi-stage build for Docusaurus frontend

# Stage 1: Build
FROM node:18-alpine AS builder

WORKDIR /app

# Install dependencies
COPY frontend/package*.json ./
RUN npm ci

# Copy source code
COPY frontend/ ./

# Build static site
RUN npm run build

# Stage 2: Serve with nginx
FROM nginx:alpine

# Copy built site to nginx html directory
COPY --from=builder /app/build /usr/share/nginx/html

# Copy nginx configuration (if custom needed)
# COPY infrastructure/docker/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### Backend Dockerfile

**File**: `infrastructure/docker/Dockerfile.backend`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY backend/pyproject.toml ./

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Copy application code
COPY backend/app ./app

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Docker Compose

**File**: `infrastructure/docker/docker-compose.yml`

```yaml
version: '3.9'

services:
  frontend:
    build:
      context: ../..
      dockerfile: infrastructure/docker/Dockerfile.frontend
    ports:
      - "3000:80"
    environment:
      - NODE_ENV=production

  backend:
    build:
      context: ../..
      dockerfile: infrastructure/docker/Dockerfile.backend
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
    env_file:
      - ../../.env
    depends_on:
      - frontend

# Note: External services (Qdrant, Postgres) configured separately
# They will be added as services in future features when actually used
```

## Relationships & Dependencies

### Configuration Loading Flow

```
┌─────────────────────────────────────────┐
│ System Environment Variables            │
│ (OS environment + .env file)            │
└──────────────┬──────────────────────────┘
               │
               ├──────────────────┐
               │                  │
┌──────────────▼──────┐  ┌────────▼───────────┐
│ Frontend Build      │  │ Backend Runtime     │
│ (docusaurus.config) │  │ (Pydantic Settings) │
└──────────────┬──────┘  └────────┬───────────┘
               │                  │
               │                  │
┌──────────────▼──────┐  ┌────────▼───────────┐
│ Static Site         │  │ FastAPI Application │
│ (embedded config)   │  │ (dynamic config)    │
└─────────────────────┘  └─────────────────────┘
```

**Key Points**:
1. Frontend: Config loaded at build time, embedded in static files
2. Backend: Config loaded at runtime from environment
3. No runtime dependency between frontend/backend configs
4. Both read from same `.env` file during development

### Validation Dependencies

```
.env.example (documentation)
     │
     ▼
.env (user creates, fills in values)
     │
     ├─────────────────────┐
     │                     │
     ▼                     ▼
Frontend Build       Backend Settings
(minimal validation) (Pydantic validation)
     │                     │
     │                     ▼
     │              Optional validations:
     │              - URL format checks
     │              - API key prefix checks
     │              - Required field warnings
     │
     ▼
Static Site (no runtime validation)
```

## State Transitions

**Configuration Lifecycle**:

1. **Development Setup**:
   - Developer copies `.env.example` to `.env`
   - Fills in (optional) credentials
   - App starts with warnings for missing values

2. **Build Time** (Frontend):
   - Docusaurus reads environment variables
   - Embeds configuration in static files
   - No runtime configuration changes possible

3. **Runtime** (Backend):
   - FastAPI loads settings on startup
   - Validates with Pydantic
   - Logs warnings for optional missing values
   - App continues running even with missing credentials

4. **Production Deployment**:
   - Environment variables from hosting platform (Vercel, GitHub Actions)
   - Same configuration schema used
   - Required variables enforced by deployment gates

## Constraints & Invariants

### Invariants

1. **No Secrets in Code**: All sensitive values MUST come from environment variables
2. **Optional in Init Phase**: All API keys optional during initial scaffold phase
3. **Graceful Degradation**: App starts and shows UI even without external service credentials
4. **Consistent Naming**: Environment variable names consistent between `.env.example` and Settings model

### Constraints

1. **Node.js Version**: >= 18.0.0 (enforced in package.json)
2. **Python Version**: >= 3.11 (enforced in pyproject.toml)
3. **Port Availability**: Ports 3000 (frontend) and 8000 (backend) must be available
4. **File System**: Write access required for `.env` creation

## Future Evolution

**Phase 2 (Not in this feature)**:
- User data models (UserProfile, authentication tables)
- Content models (Chapter, Section, Content)
- Chat history models (Conversation, Message)
- Vector storage models (Embedding, Document)

**Phase 3 (Not in this feature)**:
- Database migrations (Alembic for SQLAlchemy)
- Schema versioning
- Data validation rules
- Relationships between entities

**Note**: This infrastructure phase establishes the foundation. Future features will build actual data models on top of this configuration infrastructure.
