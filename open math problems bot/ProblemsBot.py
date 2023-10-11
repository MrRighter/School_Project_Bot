from aiogram import Bot, types, Dispatcher, executor
import os
from dotenv import load_dotenv


if os.path.exists(".env"):
    load_dotenv()
    print("Environment variables loaded successfully!")
else:
    print(".env file not found.")

api_bot = os.getenv("API_BOT")
bot = Bot(api_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ы!")


@dp.message_handler()
async def process_number(message: types.Message):
    try:
        a = int(message.text)
        if a <= 0:
            await message.reply("Данное число не подходит и не может быть использовано, введите новое положительное число:")
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
            await message.reply(response)
    except ValueError:
        await message.reply("Некорректный ввод. Введите число.")


print("бот запущен")
if __name__ == '__main__':
    executor.start_polling(dp)
