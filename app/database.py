from sqlalchemy import create_engine       #type:ignore
from sqlalchemy.orm import sessionmaker #type:ignore
from .models import Base

# Using SQLite as suggested , but this URL can easily be swapped for PostgreSQL (e.g., "postgresql://user:pass@localhost/dbname").
SQLALCHEMY_DATABASE_URL = "sqlite:///./finance_system.db"



# connect_args={"check_same_thread": False} is needed only for SQLite in FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Creates all tables defined in models.py
    Base.metadata.create_all(bind=engine)