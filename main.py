from fastapi import FastAPI

from api import users
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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

app.include_router(users.router)
