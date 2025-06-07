from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    full_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    religion = Column(String)
    caste = Column(String)
    education = Column(String)
    profession = Column(String)
    income = Column(String)
    city = Column(String)
    profile_picture = Column(String)  # URL for uploaded photo

    user = relationship("User")