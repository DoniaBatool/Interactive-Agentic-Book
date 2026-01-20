import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.api import chat as chat_api
from app.api import history as history_api
from app.api import auth as auth_api
from app.api import personalize as personalize_api
from app.api import translation as translation_api
from app.core.database import init_db, is_db_available
from app.services.qdrant_client import get_effective_qdrant_url, get_qdrant_client

logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    logger.info("Starting application...")
    
    # Initialize database (optional - will work without it)
    db_initialized = await init_db()
    if db_initialized:
        logger.info("Database initialized successfully")
    else:
        logger.warning("Database not available - chat history will not be persisted")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")


app = FastAPI(title=settings.app_name, lifespan=lifespan)

# CORS middleware - must be added before routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,  # Already a list of strings
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/health")
def health_check():
    qdrant_reachable = False
    qdrant_error = None
    qdrant_collections = None
    qdrant_collection_exists = None

    effective_qdrant_url = get_effective_qdrant_url()

    if settings.qdrant_url:
        try:
            qclient = get_qdrant_client()
            cols = qclient.get_collections().collections
            qdrant_reachable = True
            qdrant_collections = [c.name for c in cols][:25]
            qdrant_collection_exists = any(c.name == settings.qdrant_collection for c in cols)
        except Exception as exc:
            qdrant_error = str(exc)

    return {
        "status": "ok",
        "service": settings.app_name,
        "database": "connected" if is_db_available() else "not configured",
        "openai_configured": bool(settings.openai_api_key),
        "qdrant_configured": bool(settings.qdrant_url),
        "qdrant_url_effective": effective_qdrant_url,
        "qdrant_reachable": qdrant_reachable,
        "qdrant_error": qdrant_error,
        "qdrant_collections": qdrant_collections,
        "qdrant_collection": settings.qdrant_collection,
        "qdrant_collection_exists": qdrant_collection_exists,
    }


# Explicit OPTIONS handler for /chat (in case middleware doesn't catch it)
@app.options("/chat")
async def chat_options(request: Request):
    """Explicit OPTIONS handler for CORS preflight."""
    origin = request.headers.get("origin")
    # Check if origin is in allowed origins
    allowed_origin = origin if origin in settings.allowed_origins else None
    
    headers = {
        "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "content-type, x-session-id",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Max-Age": "600",
    }
    
    if allowed_origin:
        headers["Access-Control-Allow-Origin"] = allowed_origin
    
    return JSONResponse(content={}, headers=headers)


app.include_router(chat_api.router)
app.include_router(history_api.router)
app.include_router(auth_api.router)
app.include_router(personalize_api.router)
app.include_router(translation_api.router)
