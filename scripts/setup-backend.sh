#!/bin/bash
# Backend setup script
# Creates virtual environment and installs Python dependencies

set -e

echo "🐍 Setting up backend (FastAPI)..."
echo ""

# Navigate to backend directory
cd "$(dirname "$0")/../backend"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo "   Please install Python 3.11+ from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]); then
    echo "❌ ERROR: Python version must be 3.11 or higher"
    echo "   Current version: $(python3 --version)"
    echo "   Please upgrade from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python $(python3 --version | cut -d' ' -f2) detected"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -e .

echo ""
echo "✅ Backend setup complete!"
echo ""
echo "🚀 To start development server:"
echo "   cd backend"
echo "   source .venv/bin/activate"
echo "   uvicorn app.main:app --reload"
echo ""
