from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.core.config import settings
from app.api.routes import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting SimpleAgent service...")
    # TODO: Initialize database connection
    # TODO: Initialize Redis connection
    # TODO: Start background tasks
    
    yield
    
    # Shutdown
    print("Shutting down SimpleAgent service...")
    # TODO: Close database connections
    # TODO: Close Redis connections
    # TODO: Clean up resources


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Visual browser automation platform",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/screenshots", StaticFiles(directory="screenshots"), name="screenshots")
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")

# Include API routes
app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/")
async def root():
    return {
        "message": "Welcome to SimpleAgent",
        "version": "0.1.0",
        "docs": f"{settings.api_prefix}/docs",
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        workers=1 if settings.debug else settings.workers,
    )