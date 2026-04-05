import os
from sqlalchemy import create_engine    #type:ignore
from sqlalchemy.orm import sessionmaker #type:ignore
from dotenv import load_dotenv
from .models import Base

load_dotenv()

# Retrieve the database URL from the environment..
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# IMPORTANT: Remove the connect_args={"check_same_thread": False} parameter.

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Creates all tables defined in models.py
    Base.metadata.create_all(bind=engine)