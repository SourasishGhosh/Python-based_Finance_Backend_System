from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session  #type:ignore
from .. import models, dependencies

router = APIRouter(prefix="/users", tags=["User Management"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(
        username: str, 
        role: models.RoleEnum, 
        db: Session = Depends(dependencies.get_db), 
        current_user = Depends(dependencies.require_admin)
    ):          # Allows Admins to create new users and assign roles (Viewer, Analyst, Admin).
    

    existing_user = db.query(models.User).filter(models.User.username == username).first()
    
    if existing_user:           # handling of invalid operations and error responses
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username already registered"
        )
    
    
    new_user = models.User(username=username, hashed_password="fake_hashed_password", role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User {username} created successfully with role {role}"}

@router.get("/me")
def read_users_me(current_user: models.User = Depends(dependencies.get_current_user)): # allows authorized user to view his/her profile
    return {"username": current_user.username, "role": current_user.role}