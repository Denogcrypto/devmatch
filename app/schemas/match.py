from pydantic import BaseModel
from typing import Optional

class MatchBase(BaseModel):
    title: str
    description: Optional[str]
    status: Optional[str] = "active"
    score: Optional[float] = 0.0

class MatchCreate(MatchBase):
    user_id: int

class MatchUpdate(MatchBase):
    pass

class MatchRead(MatchBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
