from fastapi import APIRouter

from microshop.users import crud
from microshop.users.shemas import CreateUser

users_rst = APIRouter(prefix="/users", tags=["Users"])


@users_rst.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_id=user)
