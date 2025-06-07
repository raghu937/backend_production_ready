from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan = Column(String, nullable=False)  # Gold or Platinum
    stripe_payment_intent = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending/success/failed
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")