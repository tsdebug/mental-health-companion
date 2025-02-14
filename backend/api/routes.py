from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.auth import router as auth_router
from recommendation.recommendation import router as recommendation_router
from database import get_db, models

router = APIRouter()

# Include authentication and AI recommendation routes
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(recommendation_router, prefix="/recommend", tags=["Recommendations"])

@router.get("/")
def welcome():
    return {"message": "Welcome to the AI-Based Mental Health Companion API"}

@router.post("/mood/")
def track_mood(user_id: int, mood: str, journal_entry: str = None, db: Session = Depends(get_db)):
    """
    Allows users to track their mood with optional journaling.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    mood_entry = models.MoodEntry(user_id=user_id, mood=mood, journal_entry=journal_entry)
    db.add(mood_entry)
    db.commit()
    db.refresh(mood_entry)

    return {
        "message": "Mood tracked successfully",
        "mood": mood,
        "journal": journal_entry
    }
