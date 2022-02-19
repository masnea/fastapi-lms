from fastapi import FastAPI, Path, Query
import fastapi
from pydantic import BaseModel
from typing import Optional, List

from api.utils.users import get_user, get_user_by_email, get_users, create_user
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from pydantic_schemas.user import UserCreate, User

from db.db_setup import get_db
router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def getUsers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users")
async def createUser(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
async def getUser(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
