from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.business import CreateClient, FindClient
from src.models import ClientInput

user_routes = APIRouter()


@user_routes.post("/client")
def create_client(client: ClientInput):
    use_case = CreateClient()
    response = use_case.handle(client)
    return JSONResponse(content=response.dict(), status_code=response.status_code)


@user_routes.get("/client/{client_id}")
def find_client(client_id: int):
    use_case = FindClient()
    response = use_case.handle(client_id)
    return JSONResponse(content=response.dict(), status_code=response.status_code)
