from sqlalchemy import Column, Integer, String, Float, Date, Enum, ForeignKey   #type:ignore 
from sqlalchemy.orm import declarative_base #type:ignore
import enum

Base = declarative_base()

class RoleEnum(str, enum.Enum):
    VIEWER = "Viewer"
    ANALYST = "Analyst"
    ADMIN = "Admin"

class TransactionType(str, enum.Enum):
    INCOME = "Income"
    EXPENSE = "Expense"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.VIEWER) # Role handling 

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False) # Income or expense 
    category = Column(String, index=True)
    date = Column(Date, index=True)
    notes = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))