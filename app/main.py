from fastapi import FastAPI
from .database import init_db
from .routers import records

# Initialize the database tables on startup
init_db()

# Create the FastAPI instance
app = FastAPI(
    title="Finance Tracking System API",
    description="A backend for managing financial records and generating summaries.",
    version="1.0.0"
)

# Include routers to maintain clean file organization
app.include_router(records.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Finance Tracking System API. Visit /docs for the API interface."}
