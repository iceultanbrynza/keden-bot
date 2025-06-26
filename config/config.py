from dataclasses import dataclass
from environs import Env
from pathlib import Path

env = Env()
env_path = Path(__file__).resolve().parent / '.env'
if env_path.exists():
    env.read_env(env_path)

URL = env("BITRIX_API")
HOST=env('REDIS_HOST')
PORT=env('REDIS_PORT')
PASSWORD=env('REDIS_PASSWORD')
DJANGO_URL=env('DJANGO_URL')

@dataclass
class Config:
    token:str
    admins:list[str]

def load_config():
    env = Env()
    env.read_env()

    return Config(
        token=env('TOKEN'),
        admins=list(map(int, env.list('ADMINS')))
    )