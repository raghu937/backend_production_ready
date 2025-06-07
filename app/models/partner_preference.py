from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class PartnerPreference(Base):
    __tablename__ = "partner_preferences"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    preferred_religion = Column(String)
    preferred_caste = Column(String)
    preferred_income = Column(String)
    preferred_education = Column(String)
    
    user = relationship("User")