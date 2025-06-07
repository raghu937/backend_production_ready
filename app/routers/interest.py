from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import interest as interest_model
from app.database import get_db

router = APIRouter(prefix="/interest", tags=["interest"])

@router.post("/send")
def send_interest(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    interest = interest_model.Interest(sender_id=sender_id, receiver_id=receiver_id)
    db.add(interest)
    db.commit()
    db.refresh(interest)
    return {"msg": "Interest sent", "interest_id": interest.id}

@router.post("/respond")
def respond_interest(interest_id: int, status: str, db: Session = Depends(get_db)):
    interest = db.query(interest_model.Interest).filter(interest_model.Interest.id == interest_id).first()
    if not interest:
        raise HTTPException(status_code=404, detail="Interest not found")
    interest.status = status
    db.commit()
    return {"msg": "Interest updated", "status": interest.status}