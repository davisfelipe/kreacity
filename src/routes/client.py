from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.business import CreateClient
from src.models import ClientInput

user_routes = APIRouter()


@user_routes.post("/user")
def create_user(client: ClientInput):
    use_case = CreateClient()
    response = use_case.handle(client)
    return JSONResponse(content=response.dict(), status_code=response.status_code)
