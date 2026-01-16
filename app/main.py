"""
AI Compliance Agent for Aptos dApps

FastAPI application entry point.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.config import get_settings
from app.api.routes import contracts, transactions, compliance, demo
from app.api.websocket import websocket_endpoint
from app.core.transaction_monitor import get_transaction_monitor
from app.models.schemas import HealthResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    settings = get_settings()
    print(f"🚀 Starting Aptos Compliance Agent")
    print(f"📡 Connected to: {settings.aptos_network}")
    print(f"🤖 AI Analysis: {'Enabled (Groq)' if settings.groq_api_key else 'Disabled (no API key)'}")
    print(f"🎯 Demo contracts available at /api/demo/contracts")
    
    # Start transaction monitor
    monitor = get_transaction_monitor()
    await monitor.start()
    print("📊 Transaction monitor started")
    
    yield
    
    # Shutdown
    await monitor.stop()
    print("👋 Shutting down...")


# Create FastAPI app
app = FastAPI(
    title="Aptos Compliance Agent",
    description="AI-powered compliance and security agent for Aptos dApps",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(contracts.router, prefix="/api")
app.include_router(transactions.router, prefix="/api")
app.include_router(compliance.router, prefix="/api")
app.include_router(demo.router, prefix="/api")


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """WebSocket endpoint for real-time alerts."""
    await websocket_endpoint(websocket)


# Health check
@app.get("/api/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint."""
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        version="0.1.0",
        aptos_network=settings.aptos_network,
        ai_enabled=bool(settings.groq_api_key)
    )


# Serve frontend
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")


@app.get("/", tags=["Frontend"])
async def serve_landing():
    """Serve the animated landing page."""
    landing_path = os.path.join(frontend_dir, "landing.html")
    if os.path.exists(landing_path):
        return FileResponse(landing_path)
    # Fallback to dashboard
    return FileResponse(os.path.join(frontend_dir, "index.html"))


@app.get("/index.html", tags=["Frontend"])
async def serve_dashboard():
    """Serve the frontend dashboard."""
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Frontend not found. API is available at /docs"}


@app.get("/styles.css", tags=["Frontend"])
async def serve_css():
    """Serve CSS file."""
    css_path = os.path.join(frontend_dir, "styles.css")
    if os.path.exists(css_path):
        return FileResponse(css_path, media_type="text/css")
    return {"error": "CSS not found"}


@app.get("/app.js", tags=["Frontend"])
async def serve_js():
    """Serve JavaScript file."""
    js_path = os.path.join(frontend_dir, "app.js")
    if os.path.exists(js_path):
        return FileResponse(js_path, media_type="application/javascript")
    return {"error": "JavaScript not found"}


@app.get("/landing.css", tags=["Frontend"])
async def serve_landing_css():
    """Serve landing page CSS."""
    css_path = os.path.join(frontend_dir, "landing.css")
    if os.path.exists(css_path):
        return FileResponse(css_path, media_type="text/css")
    return {"error": "Landing CSS not found"}


@app.get("/landing.js", tags=["Frontend"])
async def serve_landing_js():
    """Serve landing page JS."""
    js_path = os.path.join(frontend_dir, "landing.js")
    if os.path.exists(js_path):
        return FileResponse(js_path, media_type="application/javascript")
    return {"error": "Landing JS not found"}


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
