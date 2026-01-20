# Physical AI & Humanoid Robotics — Interactive Textbook

Interactive, multilingual (English + Urdu) course site built on **Docusaurus** with:
- **Auth server** (Express + BetterAuth) for sign-in/sign-up + admin panel
- **RAG backend** (FastAPI) for chat + translation + optional persistence

### Live deployments (current defaults in code)
- **Frontend (Docusaurus)**: `https://interactive-agentic-book-frontend.onrender.com`
- **Auth server (BetterAuth)**: `https://interactive-agentic-book.onrender.com`
- **Backend (FastAPI)**: `https://interactive-agentic-book-backend.onrender.com`

## Features (what exists in this repo)
- **Course content**: Docusaurus docs in `docs/`
- **i18n**: English + Urdu (`i18n/`), RTL support
- **Per-page Urdu toggle**: language **defaults back to English on navigation** (does not persist)
- **Auth**: email/password + optional Google/GitHub OAuth, email verification, password reset
- **Admin panel**: user management at `/auth/admin`
- **AI**:
  - **RAG chat** (OpenAI + Qdrant)
  - **Chapter translation** endpoint in backend
- **Testing**: course-structure checks + TypeScript typecheck (`npm test`)

## Tech stack (actual)
### Frontend
- **Docusaurus 3** + **React 19** + **TypeScript**
- Custom theme/components in `src/`
- Docusaurus i18n + custom Urdu toggle logic

### Auth server (`auth-server/`)
- **Node.js** (ESM) + **Express**
- **better-auth**
- **PostgreSQL** (`pg`)
- Email providers supported in code: **SendGrid** or **Gmail SMTP** (plus `resend` dependency)

### Backend (`backend/`)
- **FastAPI** + **Uvicorn**
- **OpenAI** (chat + embeddings)
- **Qdrant** (vector search)
- Optional **PostgreSQL** persistence (async SQLAlchemy/asyncpg)

## Prerequisites
- **Node.js >= 18**
- **Python 3.11+**
- Optional: **PostgreSQL** (needed for auth; backend DB is optional)

## Local development
### 1) Install dependencies
Frontend (repo root):
```bash
npm install
```

Auth server:
```bash
cd auth-server
npm install
cd ..
```

Backend (create venv + install):
```bash
python -m venv venv

# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
.\venv\Scripts\activate.bat
# Linux/WSL:
source venv/bin/activate

pip install -r backend/requirements.txt
```

### 2) Environment variables
Both `auth-server/` and `backend/` load env from a **root `.env`** when you run from the project root.

Create `.env` in the repo root:
```env
# --- URLs (dev) ---
FRONTEND_URL=http://localhost:3000
AUTH_SERVER_URL=http://localhost:8002

# --- Auth server ---
AUTH_PORT=8002
DATABASE_URL=postgresql://USER:PASSWORD@localhost:5432/textbook_db
AUTH_SECRET=change-this-in-production-min-32-chars

# Optional OAuth (enable by setting IDs/secrets)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=

# Optional email (for verification + password reset)
SENDGRID_API_KEY=
SENDGRID_FROM_EMAIL=
GMAIL_USER=
GMAIL_APP_PASSWORD=

# --- Backend (RAG) ---
OPENAI_API_KEY=
QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=textbook-chunks

# Optional (backend persistence)
# DATABASE_URL can be reused (same Postgres)

# Optional: allow additional frontends in dev/prod (comma-separated)
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3) Run services (3 terminals)
Frontend (Docusaurus):
```bash
npm start
```
Runs at `http://localhost:3000`

Auth server (BetterAuth):
```bash
cd auth-server
npm run dev
```
Runs at `http://localhost:8002`

Backend (FastAPI):
```bash
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
API docs at `http://localhost:8000/docs` and health at `http://localhost:8000/health`

## Ingestion (RAG)
To ingest docs into Qdrant (requires OpenAI + Qdrant env vars):
```bash
python backend/scripts/ingest.py --docs-dir docs
```

## Testing
Runs course-structure checks + TS typecheck:
```bash
npm test
```

## Project layout
```
.
├── docs/                 # Course content
├── src/                  # Docusaurus custom pages/components/theme
├── i18n/                 # English + Urdu strings
├── auth-server/          # Express + BetterAuth server (Postgres)
├── backend/              # FastAPI RAG/translation service (OpenAI/Qdrant)
└── tests/                # Course structure validation
```

## Deployment (what this repo is configured for)
- **Frontend**: Render (root `/`) and GitHub Pages (baseUrl `/Interactive-Agentic-Book/`) via `docusaurus.config.ts`
- **Backend/Auth**: Render web services (URLs above are the defaults used in `src/config/env.ts`)

## Admin
- Admin UI: `/<site>/auth/admin`
- Admin privileges are stored in Postgres on the auth server tables; helper SQL lives in `auth-server/*.sql`.
