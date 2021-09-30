from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from schemas import User
from db.database import get_db
from db.crud import create_user, get_user, get_users


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User doesn't exist")


@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)


@router.post("/", response_model=User)
async def post_user(user: User, db: Session = Depends(get_db)):
    """Creates a user to the database"""
    db_user = get_user(db=db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db=db, user=user)
