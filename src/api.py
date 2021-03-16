from fastapi import Depends, FastAPI

from src.config import api_information
from src.database import MongoDatabase
from src.routes import login_routes, user_routes
from src.security.jwt_token import get_current_user

app = FastAPI(**api_information)
db = MongoDatabase.create_mongo_connection()

app.include_router(login_routes)
app.include_router(user_routes, dependencies = [Depends(get_current_user)])
