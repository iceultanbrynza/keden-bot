from dataclasses import dataclass
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / '.env'

URL=os.getenv("BITRIX_API")
HOST=os.getenv('REDIS_HOST')
PORT=os.getenv('REDIS_PORT')
PASSWORD=os.getenv('REDIS_PASSWORD')
DJANGO_URL=os.getenv('DJANGO_URL')

@dataclass
class Config:
    token:str
    admins:list[str]

def load_config():
    admins = os.getenv('ADMINS')
    if admins:
        return Config(
            token=os.getenv('TOKEN'),
            admins=list(map(int, os.getenv('ADMINS').split(',')))
        )
    else:
        return Config(
                token=os.getenv('TOKEN'),
                admins=list(map(int, os.getenv('ADMINS')))
            )