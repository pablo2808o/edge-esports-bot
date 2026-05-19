import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.clan import router as clan_router
from handlers.admin import router as admin_router
from handlers.bigplay import router as bigplay_router

from services.scheduler import (
    start_scheduler
)

async def main():

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(clan_router)
    dp.include_router(admin_router)
    dp.include_router(bigplay_router)

    start_scheduler()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
