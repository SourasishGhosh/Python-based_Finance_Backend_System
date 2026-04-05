from fastapi import APIRouter, Depends, HTTPException, status
from app import crud, schemas
from sqlalchemy.orm import Session  #type:ignore
from typing import List
from app import dependencies

router = APIRouter(prefix="/records", tags=["Records"])

@router.post("/", response_model=schemas.RecordResponse, status_code=status.HTTP_201_CREATED)
def create_record(record: schemas.RecordCreate, db: Session = Depends(dependencies.get_db), current_user = Depends(dependencies.require_admin)):
    try:
        return crud.create_user_record(db=db, record=record, user_id=current_user.id)
    except Exception as e:
        # Clear handling of invalid operations 
        raise HTTPException(status_code=400, detail="Invalid data provided")

@router.get("/summary", response_model=schemas.SummaryResponse)
def get_summary(db: Session = Depends(dependencies.get_db), current_user = Depends(dependencies.get_current_user)):
    # Both Analyst and Admin can view summaries
    return crud.get_financial_summary(db=db, user_id=current_user.id)
