from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import tasks, auth
from app.database.migrations import create_db_and_tables

app = FastAPI(title="Todo App API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)