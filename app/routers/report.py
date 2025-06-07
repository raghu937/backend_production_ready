from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import report as report_model
from app.database import get_db

router = APIRouter(prefix="/report", tags=["report"])

@router.post("/user")
def report_user(reporter_id: int, reported_id: int, reason: str, db: Session = Depends(get_db)):
    report = report_model.Report(reporter_id=reporter_id, reported_id=reported_id, reason=reason)
    db.add(report)
    db.commit()
    db.refresh(report)
    return {"msg": "User reported successfully"}