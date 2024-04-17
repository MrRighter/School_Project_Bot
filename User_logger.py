import os

from aiogram import types
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()
    print("Environment variables loaded successfully!")
else:
    print(".env file not found.\n")


ig_group = os.getenv("ID_GROUP")


async def get_user_info(message: types.Message, bot):
    text_info = (f"<b>Был произведён запуск бота</b>\n"
                 f"<i>• Имя:</i> {message.from_user.first_name}\n"
                 f"<i>• Фамилия:</i> {message.from_user.last_name}\n"
                 f"<i>• Username:</i> @{message.from_user.username}\n"
                 f"<i>• ID пользователя:</i> {message.from_user.id}\n"
                 f"<i>• Premium:</i> {message.from_user.is_premium}\n"
                 f"<i>• Язык:</i> {message.from_user.language_code}\n"
                 f"<i>• Является ботом:</i> {message.from_user.is_bot}\n")
    await bot.send_message(chat_id=ig_group, text=text_info, parse_mode=types.ParseMode.HTML)
