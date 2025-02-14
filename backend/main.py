from fastapi import FastAPI
from backend.api.routes import router as api_router
from backend.database.config import init_db

app = FastAPI(
    title="AI-Based Mental Health Companion",
    description="A platform providing AI-driven mental health support.",
    version="1.0.0"
)

# Initialize database
init_db()

# Include API routes
app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI-Based Mental Health Companion API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)