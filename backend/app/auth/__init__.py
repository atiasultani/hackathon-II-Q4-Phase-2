from better_auth import Auth, Token
from better_auth.fastapi import auth_handler
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Better Auth
auth = Auth(
    secret=os.getenv("BETTER_AUTH_SECRET", "your-super-secret-key-here"),
    api_base_url=os.getenv("BETTER_AUTH_URL", "http://localhost:8000"),
)