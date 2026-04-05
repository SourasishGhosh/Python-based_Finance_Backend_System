from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session  #type:ignore
from .database import SessionLocal
from .models import User, RoleEnum

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# In a real app, this would decode a JWT token. Here we are using a mock example.
def get_current_user(db: Session = Depends(get_db)):

    # Mocking an Admin user for demonstration purposes
    user = db.query(User).filter(User.username == "admin_user").first()
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user




# Role-based Dependencies 
def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != RoleEnum.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Admin privileges required to perform this action"
        )
    return current_user




def require_analyst_or_admin(current_user: User = Depends(get_current_user)):
    if current_user.role not in [RoleEnum.ANALYST, RoleEnum.ADMIN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Insufficient permissions. Analyst or Admin required."
        )
    return current_user
