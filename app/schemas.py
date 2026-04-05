from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# Schema for input validation 
class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    type: str # 'Income' or 'Expense'
    category: str
    date: date
    notes: Optional[str] = None


class RecordResponse(RecordCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  

# Schema for the analytics endpoint
class SummaryResponse(BaseModel):
    total_income: float
    total_expenses: float
    current_balance: float
