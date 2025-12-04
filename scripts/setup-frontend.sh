#!/bin/bash
# Frontend setup script
# Installs dependencies and prepares Docusaurus development environment

set -e

echo "🎨 Setting up frontend (Docusaurus)..."
echo ""

# Navigate to frontend directory
cd "$(dirname "$0")/../frontend"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ ERROR: Node.js is not installed"
    echo "   Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ ERROR: Node.js version must be 18 or higher"
    echo "   Current version: $(node --version)"
    echo "   Please upgrade from https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js $(node --version) detected"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
npm install

echo ""
echo "✅ Frontend setup complete!"
echo ""
echo "🚀 To start development server:"
echo "   cd frontend"
echo "   npm start"
echo ""
