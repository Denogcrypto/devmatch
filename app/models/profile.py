from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    display_name = Column(String(128), nullable=False)
    title = Column(String(128), nullable=True)
    bio = Column(Text, nullable=True)
    skills = Column(String(256), nullable=True)
    availability = Column(String(64), default="Available")
    location = Column(String(128), nullable=True)
    languages = Column(String(128), nullable=True)
    created_at = Column(String(64), nullable=True)
    updated_at = Column(String(64), nullable=True)

    user = relationship("User", back_populates="profile")
