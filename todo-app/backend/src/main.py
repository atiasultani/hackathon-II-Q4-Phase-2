from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.auth import router as auth_router
from .api.tasks import router as tasks_router

app = FastAPI(title="Todo API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",
    "https://hackathon-ii-q4-phase-2-v8x7-mr43bfwyo-atiasultanis-projects.vercel.app/login"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(tasks_router, prefix="/api", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}