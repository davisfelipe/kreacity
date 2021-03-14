from fastapi import FastAPI

from src.config import api_information
from src.database.database import create_mongo_connection
from src.routes import user_routes

app = FastAPI(**api_information)
db = create_mongo_connection()

app.include_router(user_routes)
