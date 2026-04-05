from sqlalchemy.orm import Session #type:ignore
from sqlalchemy import func #type:ignore
from .models import Record, TransactionType

def get_financial_summary(db: Session, user_id: int):
    income = db.query(func.sum(Record.amount)).filter(
        Record.owner_id == user_id, Record.type == TransactionType.INCOME
    ).scalar() or 0.0
    
    expenses = db.query(func.sum(Record.amount)).filter(
        Record.owner_id == user_id, Record.type == TransactionType.EXPENSE
    ).scalar() or 0.0
    
    return {
        "total_income": income,
        "total_expenses": expenses,
        "current_balance": income - expenses
    }