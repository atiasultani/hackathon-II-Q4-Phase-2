from sqlmodel import SQLModel
from typing import Any, Dict, Optional
import uuid
from datetime import datetime
from pydantic import BaseModel, Field

class BaseSQLModel(SQLModel):
    """
    Base class for all SQLModel models in the application.
    """
    pass

class TimestampMixin:
    """
    Mixin class to add created_at and updated_at timestamps to models.
    """
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class UUIDMixin:
    """
    Mixin class to add UUID primary key to models.
    """
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)