from pydantic import BaseModel


class TaskToggleComplete(BaseModel):
    completed: bool