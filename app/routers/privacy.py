from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import privacy as privacy_model
from app.database import get_db

router = APIRouter(prefix="/privacy", tags=["privacy"])

@router.post("/set")
def set_privacy(user_id: int, hide_profile: bool, allow_messages_from_all: bool, db: Session = Depends(get_db)):
    privacy = privacy_model.PrivacySetting(user_id=user_id, hide_profile=hide_profile, allow_messages_from_all=allow_messages_from_all)
    db.add(privacy)
    db.commit()
    db.refresh(privacy)
    return {"msg": "Privacy settings updated"}

@router.get("/{user_id}")
def get_privacy(user_id: int, db: Session = Depends(get_db)):
    privacy = db.query(privacy_model.PrivacySetting).filter(privacy_model.PrivacySetting.user_id == user_id).first()
    return privacy