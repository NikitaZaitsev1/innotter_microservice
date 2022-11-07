from pydantic import BaseModel


class Stats(BaseModel):
    user_id: str
    action: str
