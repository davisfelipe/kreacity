from dataclasses import dataclass
from os import environ

__all__ = [
    'api_information'
]

api_information = dict(
    title = 'Kreacity Employees',
    description = 'Any description about kreacity',
    version = '1.0.0',
)


@dataclass
class MongoDB:
    mongo_uri: str = environ.get('MONGO_URI')


@dataclass
class JWT:
    phrase: str = environ.get('JWT_TOKEN')
