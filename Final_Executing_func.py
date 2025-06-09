import os

from aiogram import types
import pandas as pd
pd.options.mode.chained_assignment = None

from Class_Creator import *


class Users():
    def __init__(self):
        try:
            self.List = pd.read_csv('./users.csv')
        except:
            self.List = pd.DataFrame(columns=['UserID', 'task_type', 'subject', 'theme', 'theme_section', 'number', 'export', 'for_numbers', 'for_export'])
    def save(self):
        self.List.to_csv('./users.csv')
    def set_parametr(self, id, parametr, value):
        ind = self.List.loc[self.List['UserID']==id].index[0]
        self.List[parametr][ind] = value
    def check_user(self, id):
        if id not in self.List['UserID'].values:
            users.List.loc[len(users.List.index)] = [id, '', '', '', '', '', '', '', '']
    def get_user_index(self, id):
        return self.List.loc[self.List['UserID']==id].index[0]

users = Users()


async def send_result(message: types.Message):
    id = message['chat']['id']
    index = users.get_user_index(id)

    try:
        key = {'Type': users.List['task_type'][index],
                'Subject': users.List['subject'][index],
                'Theme': users.List['theme'][index],
                'Theme_section': users.List['theme_section'][index],
                'N': users.List['number'][index]}

        path = f'./Файл с задачами.pdf'

        if users.List['export'][index] == "send_to_telega":
            print_text_result = Creator().function_creator(key)
            await message.answer(text=print_text_result[0])
            await message.answer(text=print_text_result[1], parse_mode=types.ParseMode.HTML)
        elif users.List['export'][index] == "send_pdf":
            print_text_result = Creator().export_task(path, key)
            await message.answer_document(open(path, "rb"))
            await message.answer(text=print_text_result[1], parse_mode=types.ParseMode.HTML)
            absolute_path = os.path.abspath(f"{path}")
            os.remove(absolute_path)
        elif users.List['export'][index] == "send_to_telega_and_pdf":
            print_text_result = Creator().export_task(path, key)
            await message.answer(text=print_text_result[0])
            await message.answer_document(open(path, "rb"))
            await message.answer(text=print_text_result[1], parse_mode=types.ParseMode.HTML)
            absolute_path = os.path.abspath(f"{path}")
            os.remove(absolute_path)
    except KeyError as e:
        await message.answer("Ошибка в параметрах задачи")
        print(f"KeyError: {e}")
    except ValueError as e:
        await message.answer("Некорректные входные данные")
        print(f"ValueError: {e}")
    except Exception as e:
        await message.answer("Ошибка генерации задач")
        print(f"Exception: {e}")
