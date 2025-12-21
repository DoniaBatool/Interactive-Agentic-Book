# BetterAuth Server

Authentication server using [BetterAuth](https://better-auth.com/) for the Physical AI Textbook.

## Setup

### 1. Install Dependencies

```bash
cd auth-server
npm install
```

### 2. Environment Variables

Create a `.env` file in the project root with:

```env
# Auth Server
AUTH_PORT=8001

# Database (same as FastAPI backend)
DATABASE_URL=postgresql://user:password@localhost:5432/textbook_db

# Frontend URL (for CORS)
FRONTEND_URL=http://localhost:3000
```

### 3. Run the Server

```bash
# Development
npm run dev

# Production
npm run build
npm run start
```

## Architecture

```
Frontend (Docusaurus :3000)
    │
    ├─── BetterAuth Server (:8001)  ← Authentication
    │         │
    │         └─── PostgreSQL ← User data
    │
    └─── FastAPI Backend (:8000)    ← RAG/Chat/Personalize
              │
              ├─── PostgreSQL ← Chat history
              └─── Qdrant     ← Vector search
```

## API Endpoints

BetterAuth automatically provides these endpoints:

- `POST /api/auth/sign-up/email` - Create account
- `POST /api/auth/sign-in/email` - Login
- `POST /api/auth/sign-out` - Logout
- `GET /api/auth/get-session` - Check session
- `POST /api/auth/update-user` - Update profile

## User Fields

Additional user fields for personalization:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | User's display name |
| `softwareLevel` | string | beginner, intermediate, advanced |
| `hardwareLevel` | string | none, some, extensive |
| `technologies` | JSON string | Known technologies |
| `learningGoals` | string | User's learning goals |

## Running All Services

From the project root:

```bash
# Terminal 1: Frontend
npm run start

# Terminal 2: BetterAuth Server
cd auth-server && npm run dev

# Terminal 3: FastAPI Backend
cd backend && uvicorn backend.app.main:app --reload --port 8000
```

Or use the convenience script:

```bash
./scripts/start-all.sh
```

