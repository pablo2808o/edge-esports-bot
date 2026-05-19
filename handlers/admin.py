from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def admin_panel(message: Message):

    if message.text == "🔧 Админ панель":

        await message.answer(
            "🔧 Админ панель EDGE esports"
        )
