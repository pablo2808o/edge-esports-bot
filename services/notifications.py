async def send_lobby_data(
    bot,
    user_id,
    room_id,
    password
):

    await bot.send_message(
        chat_id=user_id,
        text=(
            "🏆 Данные лобби\n\n"
            f"🆔 ID: {room_id}\n"
            f"🔑 Пароль: {password}"
        )
    )
