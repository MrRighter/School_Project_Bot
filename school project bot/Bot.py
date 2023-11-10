import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

from Kb_and_InlButtons import *
from phys_def import *
from callbacks import *
import callbacks as call

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


@dp.message_handler(commands=['type_list']) # 'главная' команда для запуска
async def type_list_command(message: types.Message):
    await message.answer("Выберите нужный вам тип решения задач.", reply_markup=base_kb)


@dp.callback_query_handler() # callback данные
async def handle_callback_query(callback_query: types.CallbackQuery):
    await call.callback_query_keyboard(callback_query, bot)


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
    global item, theme, subtopic, number
    flag = False
    try:
        number = int(message.text)
        a = int(message.text)
        flag = True
    except:
        pass
    if flag:
        if item == "физика":
            if theme == "равномерное движение":
                if subtopic == 'время':
                    for i in range(number):
                        await message.answer(text=uniform_time())
                elif subtopic == "путь":
                    for i in range(number):
                        await message.answer(text=uniform_distance())
                elif subtopic == "скорость":
                    for i in range(number):
                        await message.answer(text=uniform_speed())
            elif theme == 'равноускоренное движение':
                if subtopic == "ускорение":
                    for i in range(number):
                        ans = choice([equidistant_acceleration_first(), equidistant_acceleration_second()])
                        await message.answer(text=ans)
                elif subtopic == "конечная скорость":
                    for i in range(number):
                        ans = choice([equidistant_final_speed_first(), equidistant_final_speed_second()])
                        await message.answer(text=ans)
                elif subtopic == "начальная скорость":
                    for i in range(number):
                        ans = choice([equidistant_start_speed_first(), equidistant_start_speed_second(), equidistant_start_speed_third()])
                        await message.answer(text=ans)
                elif subtopic == "путь":
                    for i in range(number):
                        ans = choice([equidistant_distance_first(), equidistant_distance_second()])
                        await message.answer(text=ans)
                elif subtopic == "время":
                    for i in range(number):
                        ans = choice([equidistant_time_first(), equidistant_time_second()])
                        await message.answer(text=ans)
        elif item == "математика":
            if theme == "алгебра":
                pass
            elif theme == "геометрия":
                pass
            elif theme == "гипотеза":
                if subtopic == "коллатца":
                    try:
                        a = int(message.text)
                        if a <= 0:
                            await message.answer(text="Данное число не подходит и не может быть использовано, введите новое положительное число:")
                        else:
                            calc = []
                            while a != 1:
                                if a % 2 != 0:
                                    a1 = a * 3 + 1
                                    calc.append(f"{a}*3+1={a1}")
                                    a = a1
                                elif a % 2 == 0:
                                    a2 = a // 2
                                    calc.append(f"{a}/2={a2}")
                                    a = a2
                                    if a == 1:
                                        calc.append("Теперь 1 и 4 будут бесконечно преобразовываться друг в друга")
                            response = "\n".join(calc)
                            await message.answer(text=response)
                    except ValueError:
                        await message.answer(text="Некорректный ввод. Введите число.")
        elif item == "информатика":
            pass


if __name__ == '__main__':
    try:
        print("бот запущен")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")