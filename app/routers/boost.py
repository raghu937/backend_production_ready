from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import boost as boost_model
from app.database import get_db
from datetime import datetime, timedelta

router = APIRouter(prefix="/boost", tags=["boost"])

@router.post("/create")
def create_boost(user_id: int, days: int = 7, db: Session = Depends(get_db)):
    boost_until = datetime.utcnow() + timedelta(days=days)
    boost = boost_model.Boost(user_id=user_id, boost_until=boost_until)
    db.add(boost)
    db.commit()
    db.refresh(boost)
    return {"msg": "Boost activated", "boost_until": boost_until}