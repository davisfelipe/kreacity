from mongoengine import connect

from src.config import MongoDB


def create_mongo_connection():
    return connect(host = MongoDB.mongo_uri)
