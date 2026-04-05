from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  #type:ignore
from typing import Dict, Any
from .. import schemas, crud, dependencies

router = APIRouter(prefix="/summary", tags=["Summary and Analytics"])

@router.get("/", response_model=schemas.SummaryResponse)

def get_basic_summary( db: Session = Depends(dependencies.get_db), current_user = Depends(dependencies.require_analyst_or_admin)):
    return crud.get_financial_summary(db=db, user_id=current_user.id)
"""
    Returns the total income, total expenses, and current balance.
    As per the assignment, Analysts and Admins can access detailed insights.
"""
@router.get("/category-breakdown", response_model=Dict[str, float])
def get_category_breakdown(db: Session = Depends(dependencies.get_db), current_user = Depends(dependencies.require_analyst_or_admin)):
    # This assumes a crud.get_category_breakdown function exists in the crud.py
    return crud.get_category_breakdown(db=db, user_id=current_user.id)
"""
    Returns a breakdown of expenses by category to evaluate processing 
    and returning meaningful data.
"""