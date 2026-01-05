from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .api import auth, tasks
from .config import settings

# Create FastAPI app instance
app = FastAPI(
    title="Todo App API",
    description="A full-stack todo application API with user authentication and task management",
    version="1.0.0"
)

# Add security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # In production, specify allowed hosts
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes with /api prefix
app.include_router(auth.router, prefix="/api", tags=["authentication"])
app.include_router(tasks.router, prefix="/api", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Todo App API - Welcome!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}