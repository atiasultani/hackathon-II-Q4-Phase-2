from sqlalchemy import create_engine
from sqlmodel import SQLModel, create_engine
from typing import Optional
from ..config import settings

DATABASE_URL = settings.database_url