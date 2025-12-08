"""
FastAPI application entry point.

Main application instance with CORS middleware and health endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.api.health import router as health_router
from app.api.chapters import router as chapters_router
from app.api import ai_blocks
from app.api import diagram_generation
from app.api import streaming
from app.api import translation
from app.api import rag
from app.auth.routes import router as auth_router
from app.api.progress import router as progress_router
from app.api.search import router as search_router
from app.api.lss import router as lss_router
from app.analytics.telemetry_router import router as telemetry_router
from app.api.lss import router as lss_router

# Create FastAPI application instance
app = FastAPI(
    title="AI Robotics Textbook API",
    version="0.1.0",
    description="Backend API for AI-Native Physical AI & Robotics Textbook",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, tags=["health"])
app.include_router(chapters_router, tags=["chapters"])
app.include_router(ai_blocks.router)
app.include_router(diagram_generation.router)
app.include_router(streaming.router)
app.include_router(translation.router)
app.include_router(rag.router)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(progress_router, tags=["progress"])
app.include_router(search_router, tags=["search"])
app.include_router(lss_router, tags=["lss"])
app.include_router(telemetry_router, tags=["telemetry"])
app.include_router(lss_router, tags=["lss"])


@app.on_event("startup")
async def startup_event():
    """Log application startup."""
    print(f"🚀 Starting AI Robotics Textbook API v0.1.0")
    print(f"📍 Environment: {settings.environment}")
    print(f"🔧 Backend Port: {settings.backend_port}")
    print(f"🌐 CORS Origins: {settings.cors_origins}")
    
    # Log configuration status
    print("\n📋 Configuration Status:")
    print(f"  - OpenAI API Key: {'✅ Configured' if settings.openai_api_key else '⚠️  Not set (optional)'}")
    print(f"  - Qdrant: {'✅ Configured' if settings.qdrant_url else '⚠️  Not set (optional)'}")
    print(f"  - Database: {'✅ Configured' if settings.database_url else '⚠️  Not set (optional)'}")
    print(f"  - BetterAuth: {'✅ Configured' if settings.betterauth_secret else '⚠️  Not set (optional)'}")
    print(f"  - SMTP: {'✅ Configured' if settings.smtp_host else '⚠️  Not set (optional)'}")
    print(f"  - AI Provider: {settings.ai_provider}")
    print(f"  - Qdrant Collection CH1: {'✅ Configured' if settings.qdrant_collection_ch1 else '⚠️  Not set (optional)'}")
    print(f"  - Embedding Model: {'✅ Configured' if settings.embedding_model else '⚠️  Not set (optional)'}")
    print(f"  - LLM Model: {'✅ Configured' if settings.llm_model else '⚠️  Not set (optional)'}")
    print(f"  - Diagram Provider: {settings.diagram_provider}")
    print(f"  - Diagram Model: {'✅ Configured' if settings.diagram_model else '⚠️  Not set (optional)'}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.backend_port)
