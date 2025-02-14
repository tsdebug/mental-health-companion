from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import openai  # If using Gemini API, replace with Google AI SDK
import os
from backend.database import models, get_db

router = APIRouter(prefix="/recommendation", tags=["AI Recommendations"])

# Load API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_ai_suggestion(user_mood: str):
    """
    Get AI-generated mental health suggestions based on the user's mood.
    """
    try:
        # Example with OpenAI (replace with Gemini API as needed)
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Change this to the Gemini AI model
            messages=[{"role": "system", "content": f"Provide mental health advice for someone feeling {user_mood}."}],
            api_key=GOOGLE_API_KEY
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"AI recommendation failed: {str(e)}"

@router.get("/{user_id}")
def recommend(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch the latest mood entry for a user and provide AI-generated suggestions.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    last_mood_entry = db.query(models.MoodEntry).filter(models.MoodEntry.user_id == user_id).order_by(models.MoodEntry.created_at.desc()).first()
    
    if not last_mood_entry:
        return {"message": "No mood data found. Please track your mood first."}

    ai_suggestion = get_ai_suggestion(last_mood_entry.mood)
    
    return {
        "user": user.username,
        "mood": last_mood_entry.mood,
        "suggestion": ai_suggestion
    }
