from fastapi import FastAPI

from src.config import api_information

app = FastAPI(**api_information)
