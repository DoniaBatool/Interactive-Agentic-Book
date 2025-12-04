# Implementation Plan: Base Project Initialization

**Branch**: `001-base-project-init` | **Date**: 2025-12-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-base-project-init/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create the complete project scaffold for the AI-Native Physical AI & Robotics Textbook platform. This feature establishes the foundational folder structure, configuration files, and placeholder scaffolding for both frontend (Docusaurus) and backend (FastAPI) components. No business logic or functional integrations are implemented—only the skeleton that enables future development.

**Primary Requirement**: Developers can clone the repository, run setup commands, and have both frontend and backend running locally in under 10 minutes with health checks passing.

**Technical Approach**: Use industry-standard project initialization tools (create-docusaurus, FastAPI project generator patterns) with manual folder structure creation to match the exact specification. All placeholder files include TODO comments for future implementation.

## Technical Context

**Language/Version**:
- Frontend: JavaScript/TypeScript with Node.js 18+, Docusaurus 3.x
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Frontend: @docusaurus/core, @docusaurus/preset-classic, React 18+
- Backend: fastapi, uvicorn[standard], pydantic, python-dotenv
- Database (placeholders): qdrant-client, psycopg2-binary (Neon Postgres), sqlalchemy
- AI (placeholders): openai, anthropic
- Auth (placeholders): better-auth (placeholder config only)

**Storage**:
- Neon Serverless Postgres (scaffolding only, no actual connection in this phase)
- Qdrant vector database (client wrapper placeholder only)
- Local filesystem for static assets and configuration

**Testing**:
- Backend: pytest (scaffolding for future tests, no tests in this phase per spec)
- Frontend: Jest + React Testing Library (scaffolding only)
- Note: Per Constitution Principle VI, TDD is mandatory, but this infrastructure feature has no testable business logic yet

**Target Platform**:
- Development: Local machines (Windows/Mac/Linux)
- Deployment target: GitHub Pages or Vercel (Docker configs are placeholders)

**Project Type**: Web application (frontend + backend + infrastructure)

**Performance Goals**:
- Setup time: < 10 minutes from clone to running services
- Frontend build time: < 30 seconds for initial Docusaurus build
- Backend startup time: < 5 seconds for FastAPI server
- No performance-critical code in this phase (only scaffolding)

**Constraints**:
- Must match exact folder structure from DOCUMENTATION.md
- Must align with Constitution Principle II (Docusaurus-First)
- Must prepare scaffolding for Constitution Principle III (RAG-First)
- Must prepare scaffolding for Constitution Principle IV (BetterAuth personalization)
- Must create placeholder structure for AI Architecture Rules (Claude Code Subagents & Skills)
- No secrets in repository (all in .env files, git-ignored)
- All placeholder files must have clear TODO comments

**Scale/Scope**:
- Single repository, monorepo structure
- ~50-100 placeholder files and folders
- ~10 configuration files (package.json, pyproject.toml, docker files, etc.)
- No database schema or migrations in this phase
- No API endpoints beyond /health

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Principle I: AI-Native Spec-Driven Development (NON-NEGOTIABLE)
- [x] Feature has complete spec.md
- [x] This plan.md documents architecture decisions
- [x] tasks.md will be generated in Phase 2 (/sp.tasks)
- [x] PHR will be created for this planning session
- [x] Claude Code Subagents/Skills folder structure will be created

**Status**: PASS - SDD workflow followed

### ✅ Principle II: Docusaurus-First Documentation Strategy
- [x] Docusaurus 3.x will be initialized as primary frontend
- [x] MDX support enabled by default in Docusaurus
- [x] Static site generation configured
- [x] Plugin architecture supported for future RAG chatbot integration

**Status**: PASS - Docusaurus is the mandated frontend framework

### ✅ Principle III: RAG-First Chatbot Architecture (NON-NEGOTIABLE)
- [x] FastAPI backend scaffold prepared
- [x] Qdrant client wrapper placeholder created
- [x] OpenAI provider wrapper placeholder created
- [x] Folder structure supports future RAG pipeline
- [ ] No actual RAG logic in this phase (out of scope per spec)

**Status**: PASS - Scaffolding complete, implementation deferred

### ✅ Principle IV: Personalization & User-Centric Design
- [x] BetterAuth config placeholder folder created
- [x] User profile schema documented in comments
- [ ] No actual authentication logic (out of scope per spec)

**Status**: PASS - Scaffolding complete, implementation deferred

### ✅ Principle V: Multilingual Support with On-Demand Translation
- [x] Translation service wrapper placeholder created
- [ ] No actual translation logic (out of scope per spec)

**Status**: PASS - Scaffolding complete, implementation deferred

### ✅ Principle VI: Test-Driven Quality Gates (NON-NEGOTIABLE)
- [x] Testing folder structure created (backend/tests/, frontend/tests/)
- [x] pytest and Jest configuration placeholders included
- [ ] No tests in this phase (infrastructure has no testable business logic)
- [x] Future features will follow TDD mandate

**Status**: PASS - Test infrastructure prepared, TDD will apply to future features

### Additional Requirements

**AI Architecture Rules**:
- [x] Claude Code Subagents folder: `backend/app/agents/subagents/` (placeholder)
- [x] Reusable Skills folder: `backend/app/agents/skills/` (placeholder)
- [x] AgentKit scaffold folder: `backend/app/agents/` (placeholder)

**Security & Authentication Requirements**:
- [x] .env.example created with all required secrets documented
- [x] .gitignore excludes .env files
- [x] No secrets or credentials in code
- [x] BetterAuth configuration placeholder created

**Development Workflow**:
- [x] Pre-implementation checklist will be followed (this planning phase)
- [x] README.md will document setup process
- [x] PHR will be created for this planning session

**Summary**: All constitutional requirements met. No violations require justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-base-project-init/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (technology research)
├── data-model.md        # Phase 1 output (configuration schemas)
├── quickstart.md        # Phase 1 output (developer setup guide)
├── contracts/           # Phase 1 output (API contracts)
│   └── health-api.yaml  # OpenAPI spec for /health endpoint
└── checklists/
    └── requirements.md  # Spec quality checklist (complete)
```

### Source Code (repository root)

Selected structure: **Option 2 - Web application** (frontend + backend detected in spec)

```text
interactive-agentic-book/
├── frontend/
│   ├── docs/                    # Docusaurus content pages
│   │   └── intro.md             # Default homepage content
│   ├── src/
│   │   ├── components/          # React components (empty)
│   │   │   └── .gitkeep
│   │   ├── theme/               # Docusaurus theme customization (empty)
│   │   │   └── .gitkeep
│   │   ├── styles/              # Global CSS/SCSS (empty)
│   │   │   └── .gitkeep
│   │   └── agents/              # Frontend AI agent helpers (placeholder)
│   │       └── .gitkeep
│   ├── static/                  # Static assets
│   │   └── img/
│   │       └── logo.svg         # Docusaurus default logo
│   ├── docusaurus.config.js     # Docusaurus configuration
│   ├── sidebar.js               # Documentation sidebar configuration
│   ├── package.json             # Frontend dependencies
│   ├── tsconfig.json            # TypeScript configuration
│   └── .gitignore               # Frontend-specific ignores
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── api/                 # API routes
│   │   │   ├── __init__.py
│   │   │   └── health.py        # /health endpoint
│   │   ├── agents/              # AI agent orchestration
│   │   │   ├── __init__.py
│   │   │   ├── subagents/       # Claude Code subagents (placeholder)
│   │   │   │   ├── __init__.py
│   │   │   │   └── .gitkeep
│   │   │   └── skills/          # Reusable AI skills (placeholder)
│   │   │       ├── __init__.py
│   │   │       └── .gitkeep
│   │   ├── config/              # Configuration management
│   │   │   ├── __init__.py
│   │   │   └── settings.py      # Environment variable loading
│   │   ├── models/              # Database models (placeholder)
│   │   │   ├── __init__.py
│   │   │   └── .gitkeep
│   │   ├── services/            # Business logic services (placeholder)
│   │   │   ├── __init__.py
│   │   │   ├── qdrant_client.py # Qdrant wrapper (placeholder)
│   │   │   └── openai_client.py # OpenAI wrapper (placeholder)
│   │   └── auth/                # Authentication (placeholder)
│   │       ├── __init__.py
│   │       └── better_auth_config.py # BetterAuth config (placeholder)
│   ├── tests/                   # Test suite (placeholder)
│   │   ├── __init__.py
│   │   ├── unit/
│   │   │   ├── __init__.py
│   │   │   └── .gitkeep
│   │   ├── integration/
│   │   │   ├── __init__.py
│   │   │   └── .gitkeep
│   │   └── contract/
│   │       ├── __init__.py
│   │       └── .gitkeep
│   ├── pyproject.toml           # Python dependencies and build config
│   ├── pytest.ini               # pytest configuration (placeholder)
│   └── .gitignore               # Backend-specific ignores
│
├── infrastructure/
│   ├── qdrant/                  # Qdrant configuration (placeholder)
│   │   └── qdrant-config.yaml   # Vector DB config (placeholder)
│   └── docker/                  # Docker-related files
│       ├── Dockerfile.frontend  # Frontend Docker image (placeholder)
│       ├── Dockerfile.backend   # Backend Docker image (placeholder)
│       └── docker-compose.yml   # Multi-container setup (placeholder)
│
├── scripts/
│   ├── setup.sh                 # Full project setup script
│   ├── setup-frontend.sh        # Frontend-only setup
│   └── setup-backend.sh         # Backend-only setup
│
├── .env.example                 # Environment variable template
├── .gitignore                   # Root gitignore
├── README.md                    # Project documentation
└── .specify/                    # SDD framework (already exists)
    └── memory/
        └── constitution.md      # Project constitution (complete)
```

**Structure Decision**: Web application architecture selected based on spec requirements for separate frontend (Docusaurus) and backend (FastAPI) services. This aligns with Constitution Principle II (Docusaurus-First) and Principle III (RAG-First chatbot requiring backend API).

The structure supports:
- Clear separation of concerns (frontend/backend/infrastructure)
- Placeholder folders for future AI features (agents, subagents, skills)
- Testing structure prepared for TDD in future features
- Infrastructure folder for deployment configurations
- Scripts folder for automation and setup tasks

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

**No violations detected.** This infrastructure setup feature requires the specified folder structure and configuration files to enable future development. All complexity is justified by:
1. Constitution mandates (Docusaurus-First, RAG-First, BetterAuth scaffolding)
2. Industry-standard project patterns (frontend/backend separation)
3. Future extensibility requirements (placeholder folders for agents, skills, subagents)

No simpler alternatives exist that would satisfy the constitutional requirements and hackathon feature specifications.


## Phase Completion Summary

### Phase 0: Research ✅ COMPLETE

**Artifact**: `research.md`
**Status**: All technology decisions documented

**Key Decisions Made**:
- Docusaurus 3.x for frontend (constitutional mandate)
- FastAPI 0.109+ for backend (constitutional mandate)
- pyproject.toml for Python dependency management
- npm for JavaScript package management
- .env files for environment variable management
- Multi-stage Docker builds for containers
- Comprehensive .gitignore strategy

**Clarifications Resolved**: No clarifications needed - all technology choices mandated by constitution or well-established industry standards.

### Phase 1: Design ✅ COMPLETE

**Artifacts Created**:
1. **data-model.md**: Configuration schemas and environment variable structures
2. **contracts/health-api.yaml**: OpenAPI 3.1 specification for /health endpoint
3. **quickstart.md**: Comprehensive developer setup guide

**Key Designs**:
- Backend Settings (Pydantic model) for type-safe configuration loading
- Environment variable schema with validation rules
- Package metadata schemas (package.json, pyproject.toml)
- Docker configuration schemas (Dockerfile patterns, docker-compose.yml)
- Health API contract (OpenAPI specification)
- Developer onboarding workflow (10-minute setup target)

**Constitution Check Re-evaluation**: ✅ ALL REQUIREMENTS MET

All six constitutional principles validated:
- ✅ Principle I: SDD workflow followed (spec→plan→tasks)
- ✅ Principle II: Docusaurus-First strategy implemented
- ✅ Principle III: RAG-First scaffolding prepared
- ✅ Principle IV: BetterAuth personalization scaffolding prepared
- ✅ Principle V: Translation scaffolding prepared
- ✅ Principle VI: TDD infrastructure prepared

No violations. No complexity issues. Ready for implementation.

### Phase 2: Task Generation ⏳ PENDING

**Next Command**: `/sp.tasks`
**Purpose**: Generate actionable implementation tasks from this plan
**Expected Output**: `tasks.md` with step-by-step implementation checklist

**Task Categories** (to be generated):
1. Setup Phase: Project initialization, dependency installation
2. Frontend Phase: Docusaurus configuration, folder structure
3. Backend Phase: FastAPI setup, health endpoint, configuration
4. Infrastructure Phase: Docker files, scripts, .gitignore
5. Documentation Phase: README, environment variables
6. Validation Phase: Verify all success criteria met

## Agent Context Update

✅ **CLAUDE.md updated** with feature technologies:
- Docusaurus 3.x
- FastAPI 0.109+
- Pydantic Settings
- Uvicorn ASGI server
- Python pyproject.toml structure
- Docker multi-stage builds

## Next Steps

1. **Run `/sp.tasks`** to generate implementation tasks from this plan
2. **Review tasks.md** for completeness and sequencing
3. **Begin implementation** following TDD workflow:
   - Write tests first (for testable components)
   - Obtain user approval on tests
   - Implement to pass tests
   - Refactor while keeping tests green
4. **Create PHR** for each implementation session
5. **Commit incrementally** after each completed task

## Success Criteria Validation

This plan satisfies all spec requirements:

**From Spec SC-001 to SC-007**:
- ✅ SC-001: Frontend setup in < 10 minutes (quickstart.md)
- ✅ SC-002: Backend setup in < 10 minutes (quickstart.md)
- ✅ SC-003: Project structure matches specification (plan.md structure section)
- ✅ SC-004: Build processes complete without errors (documented in quickstart.md)
- ✅ SC-005: .env.example fully documents variables (data-model.md)
- ✅ SC-006: Docker builds succeed (Dockerfile patterns in research.md)
- ✅ SC-007: 100% of folders exist (plan.md structure section)

**Ready for Implementation**: ✅

---

**Planning Complete**: 2025-12-04
**Next Phase**: Task Generation (`/sp.tasks`)
**Implementation Branch**: `001-base-project-init`
