import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

from Kb_and_InlButtons import *
from C_TaskGener import *
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
                        "Нажми /type_list, чтобы приступить к решению задач.")


@dp.message_handler(commands=['help']) # команда для помощи
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ы!")



@dp.callback_query_handler() # callback данные
# async def handle_callback_query(callback_query: types.CallbackQuery):
#     await call.callback_query_keyboard(callback_query, bot)
async def callback_query_keyboard(callback_query: types.CallbackQuery): # callback данные
    global item, theme, subtopic # предмет, тема/направление, подтема/что нужно найти
# новый
# предмет
    if callback_query.data == "phys": # предмет физика
        await callback_query.answer()
        item = "физика"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Доступные темы", reply_markup=phys_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# (физика) новая тема и её подтемы
    elif callback_query.data == "u_motion": # тема - равномерное движение
        await callback_query.answer()
        theme = "равномерное движение"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Что нужно найти", reply_markup=u_q_phys_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "u_time": # найти время
        await callback_query.answer()
        subtopic = "время"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "u_distance": # найти путь
        await callback_query.answer()
        subtopic = "путь"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "u_speed": # найти скорость
        await callback_query.answer()
        subtopic = "скорость"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# (физика) новая тема и её подтемы
    elif callback_query.data == "ea_motion": # тема - равноускоренное движение
        await callback_query.answer()
        theme = "равноускоренное движение"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Что нужно найти", reply_markup=ea_q_phys_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "ea_time": # найти время
        await callback_query.answer()
        subtopic = "время"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "ea_distance": # найти путь
        await callback_query.answer()
        subtopic = "путь"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "ea_boost": # найти ускорение
        await callback_query.answer()
        subtopic = "ускорение"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "ea_first_speed": # найти начальную скорость
        await callback_query.answer()
        subtopic = "начальная скорость"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "ea_second_speed": # найти конечную скорость
        await callback_query.answer()
        subtopic = "конечная скорость"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# новый
# предмет
    elif callback_query.data == "mathem": # предмет математика
        await callback_query.answer()
        item = "математика"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите направление", reply_markup=mathem_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# (математика) новая тема и её подтемы
    elif callback_query.data == "algebra": # направление/тема - алгебра
        await callback_query.answer()
        theme = "алгебра"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите интересующую тему", reply_markup=algebra_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "2+2": # 2+2
        await callback_query.answer()
        subtopic = "2+2"
        await bot.send_message(chat_id=callback_query.from_user.id, text="4")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "4+4": # 4+4
        await callback_query.answer()
        subtopic = "4+4"
        await bot.send_message(chat_id=callback_query.from_user.id, text="8")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# (математика) новая тема и её подтемы
    elif callback_query.data == "geometry": # направление/тема - геометрия
        await callback_query.answer()
        theme = "геометрия"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите интересующую тему", reply_markup=geometry_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "bla": # бла бла бла
        await callback_query.answer()
        subtopic = "бла бла бла"
        await bot.send_message(chat_id=callback_query.from_user.id, text="не придумал что выводить )")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "be": # бе бе бе
        await callback_query.answer()
        subtopic = "бе бе бе"
        await bot.send_message(chat_id=callback_query.from_user.id, text="тоже не придумал что выводить ))")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# (математика) новая тема и её подтемы
    elif callback_query.data == "hypothesis": # направление/тема - гипотезы
        await callback_query.answer()
        theme = "гипотеза"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите гипотезу", reply_markup=hypothesis_list)
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "hyp_coll": # гипотеза Коллатца
        await callback_query.answer()
        subtopic = "коллатца"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Введите натуральное число")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# новый
# предмет
    elif callback_query.data == "inf": # предмет информатика
        await callback_query.answer()
        item = "информатика"
        await bot.send_message(chat_id=callback_query.from_user.id, text="Информатика пока не доступна")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)



@dp.message_handler(commands=['type_list']) # 'главная' команда для запуска
async def type_list_command(message: types.Message):
    await message.answer("Выберите нужный вам тип решения задач.", reply_markup=base_kb)


@dp.message_handler(text="Составить задачи") # первая кнопка на клавиатуре base_kb
async def subject_choice(message: types.Message):
    await message.answer("Доступные предметы", reply_markup=subject_list)


@dp.message_handler(text="Составить контрольную") # вторая кнопка на клавиатуре base_kb
async def subject_choice2(message: types.Message):
    await message.answer("Контрольной не будет )")


@dp.message_handler(text="Кнопка по приколу") # третья кнопка на клавиатуре base_kb
async def joke_command(message: types.Message):
    await message.answer("Ы")


@dp.message_handler() # обработка полученных данных и отправка готового сообщения
async def send_result(message: types.Message):
    flag = False
    try:
        number = int(message.text)
        a = int(message.text)
        flag = True
    except:
        pass
    if flag:
        A = TaskGenerator()
        result = ""
        for i in range(1, number+1):
            result += f"{i}) {A.GenerateTask({'Type': 'СР', 'Subject': item, 'Theme': theme, 'Subtopic': subtopic})}\n\n"
        await message.answer(text=result)



        # elif item == "математика":
        #     if theme == "алгебра":
        #         pass
        #     elif theme == "геометрия":
        #         pass
        #     elif theme == "гипотеза":
        #         if subtopic == "коллатца":
        #             try:
        #                 a = int(message.text)
        #                 if a <= 0:
        #                     await message.answer(text="Данное число не подходит и не может быть использовано, введите новое положительное число:")
        #                 else:
        #                     calc = []
        #                     while a != 1:
        #                         if a % 2 != 0:
        #                             a1 = a * 3 + 1
        #                             calc.append(f"{a}*3+1={a1}")
        #                             a = a1
        #                         elif a % 2 == 0:
        #                             a2 = a // 2
        #                             calc.append(f"{a}/2={a2}")
        #                             a = a2
        #                             if a == 1:
        #                                 calc.append("Теперь 1 и 4 будут бесконечно преобразовываться друг в друга")
        #                     response = "\n".join(calc)
        #                     await message.answer(text=response)
        #             except ValueError:
        #                 await message.answer(text="Некорректный ввод. Введите число.")
        # elif item == "информатика":
        #     pass


if __name__ == '__main__':
    try:
        print("бот запущен")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")