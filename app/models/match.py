from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(32), default="active")
    score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User")
