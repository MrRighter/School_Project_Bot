import os

from aiogram import types
from dotenv import load_dotenv


load_dotenv()

ig_group = os.getenv("ID_GROUP")


async def get_user_info(message: types.Message, bot):
    text_info = (f"<b>Был произведён запуск бота</b>\n"
                 f"<i>• Имя:</i> {message.from_user.first_name}\n"
                 f"<i>• Фамилия:</i> {message.from_user.last_name}\n"
                 f"<i>• Username:</i> @{message.from_user.username}\n")
    await bot.send_message(chat_id=ig_group, text=text_info, parse_mode=types.ParseMode.HTML)
