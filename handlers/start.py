from aiogram import Router
from aiogram.types import Message

from config import ADMIN_ID
from keyboards.main import main_keyboard

router = Router()

@router.message()
async def start(message: Message):

    is_admin = message.from_user.id == ADMIN_ID

    await message.answer(
        "Добро пожаловать в EDGE esports!",
        reply_markup=main_keyboard(is_admin)
    )
