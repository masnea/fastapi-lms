from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing students and courses",
    version="0.1.0",
    contact={
        "name": "nim",
        "emmail": "nim@nim.com"
    },
    license_info={
        "name": "MIT"
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"user": user}


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrieve."),
                   q: str = Query(None, max_length=5)
                   ):
    return {"user": users[id], "query": q}


@app.get("")
async def get_users():
    return None
