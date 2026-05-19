from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.clan_states import ClanRegistration

router = Router()

@router.message()
async def clan_register(
    message: Message,
    state: FSMContext
):

    if message.text == "📛 Вступить в клан":

        await state.set_state(
            ClanRegistration.waiting_uid
        )

        await message.answer(
            "Введите UID PUBG MOBILE:"
        )


@router.message(
    ClanRegistration.waiting_uid
)
async def process_uid(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        uid=message.text
    )

    await state.set_state(
        ClanRegistration.waiting_experience_type
    )

    await message.answer(
        "Есть ли опыт в киберспорте?"
    )


@router.message(
    ClanRegistration.waiting_experience_type
)
async def process_exp(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        exp_type=message.text
    )

    await state.set_state(
        ClanRegistration.waiting_experience_text
    )

    await message.answer(
        "Опишите опыт:"
    )


@router.message(
    ClanRegistration.waiting_experience_text
)
async def process_exp_text(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        exp_text=message.text
    )

    await state.set_state(
        ClanRegistration.waiting_screenshot
    )

    await message.answer(
        "Отправьте скрин статистики:"
    )


@router.message(
    ClanRegistration.waiting_screenshot
)
async def process_photo(
    message: Message,
    state: FSMContext
):

    photo = message.photo[-1]

    data = await state.get_data()

    await message.answer(
        "✅ Спасибо!\n\n"
        "Вы успешно зарегистрированы "
        "в EDGE esports.\n\n"
        "В течение дня вам напишет "
        "@pasha2808"
    )

    await message.bot.send_photo(
        chat_id=5609127466,
        photo=photo.file_id,
        caption=(
            "📛 Новая заявка\n\n"
            f"UID: {data['uid']}\n"
            f"Опыт: {data['exp_type']}\n\n"
            f"{data['exp_text']}"
        )
    )

    await state.clear()
