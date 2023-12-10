from aiogram import types
from Kb_and_InlButtons import *
import pandas as pd
pd.options.mode.chained_assignment = None


class Users():
    def __init__(self):
        try:
            self.List = pd.read_csv('./users.csv')
        except:
            self.List = pd.DataFrame(columns=['UserID', 'task_type', 'subject', 'theme', 'theme_section', 'number', "export"])
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
    elif callback_query.data == "back_from_k_m_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list)
    elif callback_query.data == "back_from_b_m_phys":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=theme_phys_list)


# новый предмет
    elif callback_query.data == "phys": # предмет физика
        await callback_query.answer()
        users.set_parametr(id, 'subject', "физика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list)
    elif callback_query.data == "phys_kr": # предмет физика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'subject', "физика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list_kr)


# (физика) новые темы
    elif callback_query.data == "Kinematics": # кинематика
        await callback_query.answer()
        users.set_parametr(id, 'theme', "кинематика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=k_m_phys_list)
    elif callback_query.data == "Ballistics": # баллистика
        await callback_query.answer()
        users.set_parametr(id, 'theme', "баллистика")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=b_m_phys_list)


# (физика) новые темы (контрольная)
    elif callback_query.data == "Mechanics_kr": # механика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'theme', "механика")
        users.set_parametr(id, 'theme_section', "")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "Kinematics_kr": # кинематика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'theme', "кинематика")
        users.set_parametr(id, 'theme_section', "")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "Ballistics_kr": # баллистика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'theme', "баллистика")
        users.set_parametr(id, 'theme_section', "")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# (физика) разделы темы для кинематики
    elif callback_query.data == "uniform_motion": # тема - равномерное движение
        await callback_query.answer()
        users.set_parametr(id, 'theme_section', "равномерное движение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "equiaxed_motion": # тема - равноускоренное движение
        await callback_query.answer()
        users.set_parametr(id, 'theme_section', "равноускоренное движение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# (физика) разделы темы для баллистики
    elif callback_query.data == "free_fall_of_bodies":
        await callback_query.answer()
        users.set_parametr(id, "theme_section", "свободное падение тел")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "ballistic_motion":
        await callback_query.answer()
        users.set_parametr(id, "theme_section", "баллистическое движение")
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# выбрать количество задач
    elif callback_query.data == "1":
        await callback_query.answer()
        users.set_parametr(id, "number", 1)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "2":
        await callback_query.answer()
        users.set_parametr(id, "number", 2)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "3":
        await callback_query.answer()
        users.set_parametr(id, "number", 3)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "4":
        await callback_query.answer()
        users.set_parametr(id, "number", 4)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "5":
        await callback_query.answer()
        users.set_parametr(id, "number", 5)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "6":
        await callback_query.answer()
        users.set_parametr(id, "number", 6)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "7":
        await callback_query.answer()
        users.set_parametr(id, "number", 7)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "8":
        await callback_query.answer()
        users.set_parametr(id, "number", 8)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "9":
        await callback_query.answer()
        users.set_parametr(id, "number", 9)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "10":
        await callback_query.answer()
        users.set_parametr(id, "number", 10)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "11":
        await callback_query.answer()
        users.set_parametr(id, "number", 11)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "12":
        await callback_query.answer()
        users.set_parametr(id, "number", 12)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "13":
        await callback_query.answer()
        users.set_parametr(id, "number", 13)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "14":
        await callback_query.answer()
        users.set_parametr(id, "number", 14)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)
    elif callback_query.data == "15":
        await callback_query.answer()
        users.set_parametr(id, "number", 15)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправит задачи", reply_markup=export_list)


# как отправить готовые задачи
    elif callback_query.data == "telega":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_to_telega")
        # await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "pdf":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_pdf")
        # await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    elif callback_query.data == "telega_and_pdf":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_to_telega_and_pdf")
        # await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)