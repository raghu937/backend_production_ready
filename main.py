from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, profile, partner_preference, interest, chat, payment, admin, boost, report, privacy
from app.database import engine, Base

app = FastAPI(
    title="Matrimony Backend API",
    description="Fully production-grade API similar to Shaadi.com",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Allow CORS for all
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(partner_preference.router)
app.include_router(interest.router)
app.include_router(chat.router)
app.include_router(payment.router)
app.include_router(admin.router)
app.include_router(boost.router)
app.include_router(report.router)
app.include_router(privacy.router)