from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.business import CreateClient
from src.models import UserInput

user_routes = APIRouter()


@user_routes.post("/user")
def create_user(user: UserInput):
    use_case = CreateClient()
    response = use_case.handle(user)
    return JSONResponse(content=response.dict(), status_code=response.status_code)
