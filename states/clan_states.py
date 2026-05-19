from aiogram.fsm.state import StatesGroup
from aiogram.fsm.state import State

class ClanRegistration(StatesGroup):

    waiting_uid = State()

    waiting_experience_type = State()

    waiting_experience_text = State()

    waiting_screenshot = State()
