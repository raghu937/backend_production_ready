from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.models import profile as profile_model
from app.models import user as user_model
from app.database import get_db
import shutil
import os

router = APIRouter(prefix="/profiles", tags=["profiles"])

UPLOAD_DIR = "uploaded_photos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/create")
def create_profile(user_id: int, full_name: str, dob: str, gender: str,
                   religion: str, caste: str, education: str,
                   profession: str, income: str, city: str,
                   file: UploadFile = File(...),
                   db: Session = Depends(get_db)):
    filename = f"{UPLOAD_DIR}/{file.filename}"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    profile = profile_model.Profile(user_id=user_id, full_name=full_name, dob=dob,
                                     gender=gender, religion=religion, caste=caste,
                                     education=education, profession=profession,
                                     income=income, city=city, profile_picture=filename)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return {"msg": "Profile created", "profile_id": profile.id}

@router.get("/{user_id}")
def get_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(profile_model.Profile).filter(profile_model.Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile