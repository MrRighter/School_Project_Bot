from aiogram import types
from Kb_and_InlButtons import *
import pandas as pd
pd.options.mode.chained_assignment = None


class Users():
    def __init__(self):
        try:
            self.List = pd.read_csv('./users.csv')
        except:
            self.List = pd.DataFrame(columns=['UserID', 'task_type', 'subject', 'theme', 'theme_section', 'subtopic', 'number'])
    def save(self):
        self.List.to_csv('./users.csv')
    def set_parametr(self,id,parametr,value):
        ind = self.List.loc[self.List['UserID']==id].index[0]
        self.List[parametr][ind] = value
    def check_user(self,id):
        if id not in self.List['UserID'].values:
            users.List.loc[len(users.List.index)] = [id, '', '', '', '', '', '']
    def get_user_index(self,id):
        return self.List.loc[self.List['UserID']==id].index[0]

users = Users()


async def callback_query_data(callback_query: types.CallbackQuery, bot): # callback данные
    id = int(callback_query['from']['id'])
    users.check_user(id)

# новые виды работ
    if callback_query.data == "single_tasks":
        await callback_query.answer()
        users.set_parametr(id, 'task_type', "однотипные задания")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list)
    elif callback_query.data == "test_work":
        await callback_query.answer()
        users.set_parametr(id, 'task_type', "контрольная работа")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list_kr)

# кнопки "назад"
    elif callback_query.data == "back_from_subject":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужный вам тип решения задач", reply_markup=task_type_list)
    elif callback_query.data == "back_from_subject_kr":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужный вам тип решения задач", reply_markup=task_type_list)
    elif callback_query.data == "back_from_theme_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list)
    elif callback_query.data == "back_from_theme_phys_kr":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите интересующий предмет", reply_markup=subject_list_kr)
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
        users.set_parametr(callback_query['from']['id'], 'subject', "физика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list)
    elif callback_query.data == "phys_kr": # предмет физика (контрольная)
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subject', "физика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list_kr)

# (физика) новые темы
    elif callback_query.data == "Kinematics": # кинематика
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme', "кинематика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=phys_list)
    elif callback_query.data == "Ballistics": # баллистика
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme', "баллистика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")
    elif callback_query.data == "Statics": # статика
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme', "статика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")
    elif callback_query.data == "Work_and_energy": # работа и энергия
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme', "работа и энергия")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Раздел данной темы пока не доступен")

# (физика) новые темы (контрольная)
    elif callback_query.data == "Kinematics_kr": # кинематика (контрольная)
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme', "кинематика")
        users.set_parametr(callback_query['from']['id'], 'theme_section', "")
        users.set_parametr(callback_query['from']['id'], 'subtopic', "")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")

# (физика) новый раздел темы и её искомые
    elif callback_query.data == "u_motion": # тема - равномерное движение
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme_section', "равномерное движение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Что нужно найти", reply_markup=u_q_phys_list)
    elif callback_query.data == "u_time": # найти время
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "время")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "u_distance": # найти путь
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "путь")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "u_speed": # найти скорость
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "скорость")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "dependency_graphs": # найти скорость
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "графики зависимости")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")

# (физика) новый раздел темы и её искомые
    elif callback_query.data == "ea_motion": # тема - равноускоренное движение
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme_section', "равноускоренное движение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Что нужно найти", reply_markup=ea_q_phys_list)
    elif callback_query.data == "ea_time": # найти время
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "время")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_distance": # найти путь
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "путь")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_boost": # найти ускорение
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "ускорение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_first_speed": # найти начальную скорость
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "начальная скорость")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")
    elif callback_query.data == "ea_second_speed": # найти конечную скорость
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subtopic', "конечная скорость")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Введите количество задач")

# новый
# предмет
    elif callback_query.data == "mathem": # предмет математика
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subject', "математика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите направление", reply_markup=mathem_list)

# (математика) новый раздел темы и её искомые
    elif callback_query.data == "algebra": # направление/тема - алгебра
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme_section', "алгебра")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Алгебра пока не доступна")

# (математика) новый раздел темы и её искомые
    elif callback_query.data == "geometry": # направление/тема - геометрия
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'theme_section', "геометрия")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Геометрия пока не доступна")

# новый
# предмет
    elif callback_query.data == "informatics": # предмет информатика
        await callback_query.answer()
        users.set_parametr(callback_query['from']['id'], 'subject', "информатика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Информатика пока не доступна")