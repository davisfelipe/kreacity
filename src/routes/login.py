from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.business import LoginUser
from src.models import UserInput

login_routes = APIRouter()


@login_routes.post("/login")
def login_user(user: UserInput):
    use_case = LoginUser()
    response = use_case.handle(user)

    return JSONResponse(content=response.dict(), status_code=response.status_code)
