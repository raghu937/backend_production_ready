from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PrivacySetting(Base):
    __tablename__ = "privacy_settings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hide_profile = Column(Boolean, default=False)
    allow_messages_from_all = Column(Boolean, default=True)
    
    user = relationship("User")