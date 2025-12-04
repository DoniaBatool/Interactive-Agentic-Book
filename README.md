# AI-Native Physical AI & Robotics Textbook

> An interactive, AI-powered learning platform for Physical AI and Humanoid Robotics built with Docusaurus and FastAPI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

## 🎯 Project Overview

This platform provides an interactive textbook experience with:
- 📚 **Docusaurus-powered documentation** with MDX support
- 🤖 **AI chatbot with RAG** (Retrieval-Augmented Generation)
- 🌍 **On-demand translation** (English ↔ Urdu)
- 👤 **Personalized learning paths** with user profiles
- 🔐 **Secure authentication** via BetterAuth

Built for the **Agentic AI Hackathon** following **Spec-Driven Development (SDD)** methodology.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js 18+** - [Download](https://nodejs.org/)
- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/downloads/)

Verify installations:
```bash
node --version  # Should be v18.0.0+
python3 --version  # Should be 3.11.0+
git --version  # Any recent version
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/interactive-agentic-book.git
cd interactive-agentic-book
```

### 2. Setup Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and fill in your API keys (optional for initial setup)
# nano .env  # or use your preferred editor
```

### 3. Run Setup Script (Recommended)

```bash
# Automated setup for both frontend and backend
./scripts/setup.sh
```

### 4. Manual Setup (Alternative)

#### Frontend Setup

```bash
cd frontend
npm install
npm start
# Frontend will be available at http://localhost:3000
```

#### Backend Setup

Open a new terminal:

```bash
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

# Start backend server
uvicorn app.main:app --reload
# Backend will be available at http://localhost:8000
```

## 📖 Detailed Setup Guide

For step-by-step instructions with troubleshooting, see the **[Quickstart Guide](specs/001-base-project-init/quickstart.md)**.

**Setup Time**: < 10 minutes with good internet connection ⚡

## 🏗️ Project Structure

```
interactive-agentic-book/
├── frontend/              # Docusaurus documentation site
│   ├── docs/              # Documentation pages (MDX)
│   ├── src/               # React components, theme, styles
│   └── static/            # Static assets (images, files)
├── backend/               # FastAPI backend API
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── agents/        # AI agent orchestration
│   │   ├── config/        # Configuration management
│   │   ├── models/        # Database models
│   │   └── services/      # Business logic
│   └── tests/             # Test suite
├── infrastructure/        # Docker and deployment config
│   ├── docker/            # Dockerfiles and compose
│   └── qdrant/            # Vector DB configuration
├── scripts/               # Setup and automation scripts
├── .specify/              # SDD framework (specs, tasks, PHRs)
└── specs/                 # Feature specifications
```

For a detailed structure diagram, see [STRUCTURE.md](STRUCTURE.md) _(coming soon)_.

## 🧪 Verify Installation

### Check Frontend

```bash
cd frontend
npm run build  # Should complete without errors
```

Visit http://localhost:3000 - you should see the Docusaurus homepage.

### Check Backend

```bash
# Test health endpoint
curl http://localhost:8000/health
# Expected: {"status":"healthy","timestamp":"2025-12-04T..."}
```

Visit http://localhost:8000/docs - you should see the interactive API documentation (Swagger UI).

## 🛠️ Development Workflow

### Running Both Services

**Option 1: Separate Terminals** (Recommended)
```bash
# Terminal 1 - Frontend
cd frontend && npm start

# Terminal 2 - Backend
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload
```

**Option 2: Use the Setup Script**
```bash
# Run both services (requires tmux or screen)
./scripts/start-dev.sh  # Coming soon
```

### Making Changes

- **Frontend**: Edit files in `frontend/docs/` or `frontend/src/` - hot reload automatic
- **Backend**: Edit files in `backend/app/` - auto-restart with `--reload` flag
- **Environment Variables**: Update `.env` and restart backend

### Stopping Services

Press `Ctrl+C` in each terminal, or:
```bash
pkill -f "npm start"
pkill -f "uvicorn"
```

## 📚 Documentation

- **[Project Constitution](`.specify/memory/constitution.md`)** - Core principles and governance
- **[Feature Specifications](`specs/`)** - Detailed feature requirements
- **[Quickstart Guide](`specs/001-base-project-init/quickstart.md`)** - Step-by-step setup
- **[API Documentation](http://localhost:8000/docs)** - Interactive Swagger UI (when backend running)

## 🧰 Tech Stack

### Frontend
- **Docusaurus 3.x** - Documentation framework
- **React 18+** - UI library
- **TypeScript** - Type safety
- **MDX** - Markdown + JSX

### Backend
- **FastAPI 0.109+** - Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python 3.11+** - Programming language

### Infrastructure
- **Qdrant** - Vector database (for RAG)
- **Neon Postgres** - Serverless database
- **BetterAuth** - Authentication
- **OpenAI** - LLM and embeddings

### Development Tools
- **Docker** - Containerization
- **pytest** - Python testing
- **Jest** - JavaScript testing
- **Git** - Version control

## 🐳 Docker Support

Build and run with Docker:

```bash
cd infrastructure/docker

# Build images
docker build -f Dockerfile.frontend -t ai-textbook-frontend:latest ../..
docker build -f Dockerfile.backend -t ai-textbook-backend:latest ../..

# Run with docker-compose
docker-compose up
```

## 🤝 Contributing

We follow **Spec-Driven Development (SDD)** methodology:

1. **Specification** - Define requirements (`/sp.specify`)
2. **Planning** - Create implementation plan (`/sp.plan`)
3. **Tasks** - Break down into atomic tasks (`/sp.tasks`)
4. **Implementation** - TDD approach (`/sp.implement`)
5. **Documentation** - Record decisions (PHRs, ADRs)

See the [constitution](`.specify/memory/constitution.md`) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/interactive-agentic-book/issues)
- **Documentation**: [Quickstart Guide](specs/001-base-project-init/quickstart.md)
- **Constitution**: [Project Principles](`.specify/memory/constitution.md`)

## 🎓 Acknowledgments

Built for the **Agentic AI Hackathon** following principles from:
- **Spec-Driven Development**: https://ai-native.panaversity.org/
- **Docusaurus**: https://docusaurus.io/
- **FastAPI**: https://fastapi.tiangolo.com/

---

**Status**: 🚧 Phase 0 - Base Project Initialization (In Progress)

Ready to start building? Check the [Quickstart Guide](specs/001-base-project-init/quickstart.md)! 🚀
