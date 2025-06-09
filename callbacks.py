from Kb_and_InlButtons import *
import Final_Executing_func as fef
from Final_Executing_func import *


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
    elif callback_query.data == "back_from_numbers":
        index = users.get_user_index(id)
        if users.List['for_numbers'][index] == "Mechanics_kr" or users.List['for_numbers'][index] == "Kinematics_kr" or users.List['for_numbers'][index] == "Ballistics_kr":
            await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Доступные темы", reply_markup=theme_phys_list_kr)
        elif users.List['for_numbers'][index] == "uniform_motion" or users.List['for_numbers'][index] == "equiaxed_motion":
            await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=k_m_phys_list)
        elif users.List['for_numbers'][index] == "free_fall_of_bodies" or users.List['for_numbers'][index] == "ballistic_motion":
            await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите раздел данной темы", reply_markup=b_m_phys_list)
    elif callback_query.data == "back_from_export":
        await callback_query.answer()
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


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
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "Kinematics_kr": # кинематика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'theme', "кинематика")
        users.set_parametr(id, 'theme_section', "")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "Ballistics_kr": # баллистика (контрольная)
        await callback_query.answer()
        users.set_parametr(id, 'theme', "баллистика")
        users.set_parametr(id, 'theme_section', "")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# (физика) разделы темы для кинематики
    elif callback_query.data == "uniform_motion": # тема - равномерное движение
        await callback_query.answer()
        users.set_parametr(id, 'theme_section', "равномерное движение")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "equiaxed_motion": # тема - равноускоренное движение
        await callback_query.answer()
        users.set_parametr(id, 'theme_section', "равноускоренное движение")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# (физика) разделы темы для баллистики
    elif callback_query.data == "free_fall_of_bodies":
        await callback_query.answer()
        users.set_parametr(id, "theme_section", "свободное падение тел")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)
    elif callback_query.data == "ballistic_motion":
        await callback_query.answer()
        users.set_parametr(id, "theme_section", "баллистическое движение")
        users.set_parametr(id, "for_numbers", callback_query.data)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите нужное количество задач", reply_markup=numbers_list)


# выбрать количество задач
    elif callback_query.data == "1":
        await callback_query.answer()
        users.set_parametr(id, "number", 1)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "2":
        await callback_query.answer()
        users.set_parametr(id, "number", 2)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "3":
        await callback_query.answer()
        users.set_parametr(id, "number", 3)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "4":
        await callback_query.answer()
        users.set_parametr(id, "number", 4)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "5":
        await callback_query.answer()
        users.set_parametr(id, "number", 5)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "6":
        await callback_query.answer()
        users.set_parametr(id, "number", 6)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "7":
        await callback_query.answer()
        users.set_parametr(id, "number", 7)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "8":
        await callback_query.answer()
        users.set_parametr(id, "number", 8)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "9":
        await callback_query.answer()
        users.set_parametr(id, "number", 9)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "10":
        await callback_query.answer()
        users.set_parametr(id, "number", 10)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "11":
        await callback_query.answer()
        users.set_parametr(id, "number", 11)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "12":
        await callback_query.answer()
        users.set_parametr(id, "number", 12)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "13":
        await callback_query.answer()
        users.set_parametr(id, "number", 13)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "14":
        await callback_query.answer()
        users.set_parametr(id, "number", 14)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)
    elif callback_query.data == "15":
        await callback_query.answer()
        users.set_parametr(id, "number", 15)
        await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text="Выберите как отправить задачи", reply_markup=export_list)


# как отправить готовые задачи
    elif callback_query.data == "telega":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_to_telega")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await fef.send_result(message=callback_query.message)
    elif callback_query.data == "pdf":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_pdf")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await fef.send_result(message=callback_query.message)
    elif callback_query.data == "telega_and_pdf":
        await callback_query.answer()
        users.set_parametr(id, "export", "send_to_telega_and_pdf")
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        await fef.send_result(message=callback_query.message)
