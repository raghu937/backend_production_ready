from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import partner_preference as partner_model
from app.database import get_db

router = APIRouter(prefix="/preferences", tags=["preferences"])

@router.post("/create")
def create_preference(user_id: int, preferred_religion: str, preferred_caste: str,
                      preferred_income: str, preferred_education: str,
                      db: Session = Depends(get_db)):
    preference = partner_model.PartnerPreference(
        user_id=user_id,
        preferred_religion=preferred_religion,
        preferred_caste=preferred_caste,
        preferred_income=preferred_income,
        preferred_education=preferred_education
    )
    db.add(preference)
    db.commit()
    db.refresh(preference)
    return {"msg": "Preference saved", "preference_id": preference.id}