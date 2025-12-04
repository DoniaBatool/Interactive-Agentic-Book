#!/bin/bash
# Master setup script
# Sets up both frontend and backend for development

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  AI-Native Physical AI & Robotics Textbook"
echo "  Master Setup Script"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check prerequisites
echo "🔍 Checking prerequisites..."
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ ERROR: Node.js is not installed"
    echo "   Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo "   Please install Python 3.11+ from https://www.python.org/downloads/"
    exit 1
fi

# Check Git
if ! command -v git &> /dev/null; then
    echo "❌ ERROR: Git is not installed"
    echo "   Please install Git from https://git-scm.com/downloads"
    exit 1
fi

echo "✅ All prerequisites satisfied"
echo ""

# Setup environment variables
echo "📋 Setting up environment variables..."
if [ ! -f "$REPO_ROOT/.env" ]; then
    cp "$REPO_ROOT/.env.example" "$REPO_ROOT/.env"
    echo "✅ Created .env file from .env.example"
    echo "⚠️  Please edit .env and fill in your API keys"
else
    echo "✅ .env file already exists"
fi
echo ""

# Setup frontend
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Frontend Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
bash "$REPO_ROOT/scripts/setup-frontend.sh"

# Setup backend
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Backend Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
bash "$REPO_ROOT/scripts/setup-backend.sh"

# Success message
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ Setup Complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🚀 Next steps:"
echo ""
echo "  1. Edit .env file with your API keys:"
echo "     nano .env"
echo ""
echo "  2. Start frontend (in one terminal):"
echo "     cd frontend"
echo "     npm start"
echo ""
echo "  3. Start backend (in another terminal):"
echo "     cd backend"
echo "     source .venv/bin/activate"
echo "     uvicorn app.main:app --reload"
echo ""
echo "  4. Access the application:"
echo "     Frontend: http://localhost:3000"
echo "     Backend:  http://localhost:8000"
echo "     API Docs: http://localhost:8000/docs"
echo ""
echo "📚 For detailed setup guide, see:"
echo "   specs/001-base-project-init/quickstart.md"
echo ""
