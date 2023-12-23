import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

from Kb_and_InlButtons import *
from Class_Creator import *
import callbacks as call
from callbacks import *

if os.path.exists(".env"):
    load_dotenv()
    print("Environment variables loaded successfully!")
else:
    print(".env file not found.")

api_bot = os.getenv("API_BOT")
bot = Bot(api_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start']) # команда старт
async def process_start_command(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\n"
                        "Нажми /let_is_go_study, чтобы приступить к решению задач.")


@dp.message_handler(commands=['help']) # команда для помощи
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ы!")


@dp.callback_query_handler() # callback данные
async def handle_callback_query(callback_query: types.CallbackQuery):
    await call.callback_query_data(callback_query, bot)


@dp.message_handler(commands=['let_is_go_study']) # 'главная' команда для запуска
async def type_list_command(message: types.Message):
    await message.answer("Выберите нужный вам тип решения задач", reply_markup=task_type_list)


@dp.message_handler() # обработка полученных данных и отправка готового сообщения
async def send_result(message: types.Message):
    id = message['from']['id']
    index = users.get_user_index(id)

    try:
        key = {'Type': users.List['task_type'][index],
                'Subject': users.List['subject'][index],
                'Theme': users.List['theme'][index],
                'Theme_section': users.List['theme_section'][index],
                "N": users.List['number'][index]}

        path = f'./{message.from_user.full_name} {message.from_user.id}.pdf'
        if users.List['export'][index] == "send_to_telega":
            await message.answer(text=Creator().function_creator(key))
        elif users.List['export'][index] == "send_pdf":
            Creator().export_task(path, key)
            await message.answer_document(open(path, "rb"))
        elif users.List['export'][index] == "send_to_telega_and_pdf":
            await message.answer(text=Creator().export_task(path, key))
            await message.answer_document(open(path, "rb"))
    except:
        await message.answer(text="Некорректный ввод данных!!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    try:
        print("бот запущен")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")