from fastapi import APIRouter
from .shemas import CreateUser
from microshop import crud

users = APIRouter(prefix="/users", tags=["Users"])


@users.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_id=user)
