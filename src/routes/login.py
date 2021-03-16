from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.business import LoginUser
from src.models import UserAuth

login_routes = APIRouter()


@login_routes.post("/login")
def login_user(form_data: UserAuth = Depends()):
    use_case = LoginUser()
    response = use_case.handle(form_data)

    return JSONResponse(content=response.dict(), status_code=response.status_code)
