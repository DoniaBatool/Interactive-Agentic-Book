#!/bin/bash

# Start all services for the Physical AI Textbook

echo "🚀 Starting Physical AI Textbook Services..."
echo ""

# Check if node_modules exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

if [ ! -d "auth-server/node_modules" ]; then
    echo "📦 Installing auth server dependencies..."
    cd auth-server && npm install && cd ..
fi

# Start services in background
echo "🔐 Starting BetterAuth server on port 8001..."
(cd auth-server && npm run dev) &
AUTH_PID=$!

echo "🤖 Starting FastAPI backend on port 8000..."
(cd backend && source ../venv/bin/activate 2>/dev/null || source ../venv/Scripts/activate 2>/dev/null && uvicorn backend.app.main:app --reload --port 8000) &
BACKEND_PID=$!

sleep 2

echo "📚 Starting Docusaurus frontend on port 3000..."
npm run start &
FRONTEND_PID=$!

echo ""
echo "✅ All services started!"
echo ""
echo "   Frontend:      http://localhost:3000"
echo "   BetterAuth:    http://localhost:8001"
echo "   FastAPI:       http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "kill $AUTH_PID $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait

