from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio

from config import Config, load_config
from handlers import start_handlers, apply_handlers, my_apps_handlers, bitrix_handlers

config:Config = load_config()

bot = Bot(token=config.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():

    dp.include_router(start_handlers.router)
    dp.include_router(apply_handlers.router)
    dp.include_router(my_apps_handlers.router)
    dp.include_router(bitrix_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
