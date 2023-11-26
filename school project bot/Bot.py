import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

from Kb_and_InlButtons import *
# from Class_variables import *
from Class_Creator_Gener import *
# import callbacks as call
# from callbacks import *

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
# async def handle_callback_query(callback_query: types.CallbackQuery):
#     await call.callback_query_data(callback_query, bot)

async def callback_query_data(callback_query: types.CallbackQuery): # callback данные
    global task_type, subject, theme, theme_section, subtopic # вид работы, предмет, тема, раздел темы/направление, что нужно найти
# новые виды работ
    if callback_query.data == "single_tasks":
        await callback_query.answer()
        task_type = "однотипные задания"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list)
    elif callback_query.data == "test_work":
        await callback_query.answer()
        task_type = "контрольная работа"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Контрольная работа пока не доступна")
# кнопки "назад"
    elif callback_query.data == "back_from_subject":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужный вам тип решения задач", reply_markup=task_type_list)
    elif callback_query.data == "back_from_theme_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list)
    elif callback_query.data == "back_from_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list)
    elif callback_query.data == "back_from_u_q_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=phys_list)
    elif callback_query.data == "back_from_ea_q_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=phys_list)
    elif callback_query.data == "back_from_mathem":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list)
# новый
# предмет
    elif callback_query.data == "phys": # предмет физика
        await callback_query.answer()
        subject = "физика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list)
# (физика) новые темы
    elif callback_query.data == "Kinematics":
        await callback_query.answer()
        theme = "кинематика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=phys_list)
    elif callback_query.data == "Ballistics":
        await callback_query.answer()
        theme = "баллистика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")
    elif callback_query.data == "Statics":
        await callback_query.answer()
        theme = "статика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")
    elif callback_query.data == "Work_and_energy":
        await callback_query.answer()
        theme = "работа и энергия"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")
# (физика) новый раздел темы и её искомые
    elif callback_query.data == "u_motion": # тема - равномерное движение
        await callback_query.answer()
        theme_section = "равномерное движение"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Что нужно найти", reply_markup=u_q_phys_list)
    elif callback_query.data == "u_time": # найти время
        await callback_query.answer()
        subtopic = "время"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "u_distance": # найти путь
        await callback_query.answer()
        subtopic = "путь"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "u_speed": # найти скорость
        await callback_query.answer()
        subtopic = "скорость"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "dependency_graphs": # найти скорость
        await callback_query.answer()
        subtopic = "графики зависимости"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
# (физика) новый раздел темы и её искомые
    elif callback_query.data == "ea_motion": # тема - равноускоренное движение
        await callback_query.answer()
        theme_section = "равноускоренное движение"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Что нужно найти", reply_markup=ea_q_phys_list)
    elif callback_query.data == "ea_time": # найти время
        await callback_query.answer()
        subtopic = "время"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_distance": # найти путь
        await callback_query.answer()
        subtopic = "путь"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_boost": # найти ускорение
        await callback_query.answer()
        subtopic = "ускорение"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_first_speed": # найти начальную скорость
        await callback_query.answer()
        subtopic = "начальная скорость"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_second_speed": # найти конечную скорость
        await callback_query.answer()
        subtopic = "конечная скорость"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
# новый
# предмет
    elif callback_query.data == "mathem": # предмет математика
        await callback_query.answer()
        subject = "математика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите направление", reply_markup=mathem_list)
# (математика) новый раздел темы и её искомые
    elif callback_query.data == "algebra": # направление/тема - алгебра
        await callback_query.answer()
        theme_section = "алгебра"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Алгебра пока не доступна")
# (математика) новый раздел темы и её искомые
    elif callback_query.data == "geometry": # направление/тема - геометрия
        await callback_query.answer()
        theme_section = "геометрия"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Геометрия пока не доступна")
# новый
# предмет
    elif callback_query.data == "informatics": # предмет информатика
        await callback_query.answer()
        subject = "информатика"
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Информатика пока не доступна")



@dp.message_handler(commands=['let_is_go_study']) # 'главная' команда для запуска
async def type_list_command(message: types.Message):
    await message.answer("Выберите нужный вам тип решения задач", reply_markup=task_type_list)


@dp.message_handler() # обработка полученных данных и отправка готового сообщения
async def send_result(message: types.Message):
    try:
        number = int(message.text)
        key = {'Type': task_type, 'Subject': subject, 'Theme': theme, 'Theme_section': theme_section, 'Subtopic': subtopic, "N": number}
        await message.answer(text=Creator().function_creator(key))
    except:
        await message.answer(text="Некорректный ввод данных")


if __name__ == '__main__':
    try:
        print("бот запущен")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")