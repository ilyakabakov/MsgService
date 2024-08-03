import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

WEB_API_URL = "http://web:8000/api/v1"

storage_r = RedisStorage.from_url(
    "redis://redis:6379/0"
)
bot_instance = Bot(token=os.getenv('TELEGRAM_TOKEN'))

dp = Dispatcher(storage=storage_r)
