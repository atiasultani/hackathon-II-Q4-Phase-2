from backend.src.main import app

# This file is used by Hugging Face Spaces to run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)