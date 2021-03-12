from fastapi import APIRouter

from src.models import UserInput

user_routes = APIRouter()


@user_routes.post("/user")
def create_user(user: UserInput):
    return user
