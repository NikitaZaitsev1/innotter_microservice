from pydantic import BaseModel

from app.core.enum_classes import Action


class Stats(BaseModel):
    user_id: str
    action: str
