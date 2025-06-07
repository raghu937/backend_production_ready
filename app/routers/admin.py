from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import user as user_model, interest as interest_model, payment as payment_model
from app.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    total_users = db.query(user_model.User).count()
    total_interests = db.query(interest_model.Interest).count()
    total_payments = db.query(payment_model.Payment).count()
    return {
        "total_users": total_users,
        "total_interests": total_interests,
        "total_payments": total_payments
    }