import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

import callbacks as call
from callbacks import *


if os.path.exists(".env"):
    load_dotenv()
    print("Environment variables loaded successfully!")
else:
    print(".env file not found.\n")


bot = Bot(os.getenv("API_BOT"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start']) # команда старт
async def process_start_command(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\n"
                        "Нажми на /let_us_go_study, чтобы приступить к решению задач.")


@dp.callback_query_handler() # callback данные
async def handle_callback_query(callback_query: types.CallbackQuery):
    await call.callback_query_data(callback_query, bot)


@dp.message_handler(commands=['let_us_go_study']) # 'главная' команда для запуска
async def type_list_command(message: types.Message):
    await message.answer("Выберите нужный вам тип решения задач", reply_markup=task_type_list)


if __name__ == '__main__':
    try:
        print("бот запущен")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
