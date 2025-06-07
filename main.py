# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, profile, partner_preference, interest, chat, payment, admin, boost, report, privacy
from app.database import engine, Base

app = FastAPI(
    title="Matrimony Backend API",
    description="Fully production-grade API similar to Shaadi.com",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ✅ Create database tables (Auto-create)
Base.metadata.create_all(bind=engine)

# ✅ Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (you can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include all your routers
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

# ✅ Root Route
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"message": "Matrimony Backend is Live!"}

# ✅ Health Check Route for Render
@app.get("/health")
def health_check():
    return {"status": "healthy"}
