from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

def main_keyboard(is_admin=False):

    keyboard = [

        [KeyboardButton(
            text="📛 Вступить в клан"
        )],

        [KeyboardButton(
            text="⚔️ TDM"
        )],

        [KeyboardButton(
            text="🏆 Турнир EDGE esports"
        )],

        [KeyboardButton(
            text="🎮 Турнир Big Play"
        )],

        [KeyboardButton(
            text="📚 Клановые учения"
        )],
    ]

    if is_admin:

        keyboard.append([

            KeyboardButton(
                text="🔧 Админ панель"
            )
        ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
