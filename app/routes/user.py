from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse
from app.models.user import read_user
from app.config.database import get_db


user = APIRouter()


@user.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = read_user(user_id, db)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
