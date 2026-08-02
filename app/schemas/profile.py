from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    display_name: str
    title: Optional[str]
    bio: Optional[str]
    skills: Optional[str]
    availability: Optional[str]
    location: Optional[str]
    languages: Optional[str]

class ProfileCreate(ProfileBase):
    user_id: int

class ProfileUpdate(ProfileBase):
    pass

class ProfileRead(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
