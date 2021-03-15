from fastapi import FastAPI

from src.config import api_information
from src.database import MongoDatabase
from src.routes import login_routes, user_routes

app = FastAPI(**api_information)
db = MongoDatabase.create_mongo_connection()

app.include_router(login_routes)
app.include_router(user_routes)
