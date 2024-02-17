from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# инлайн кнопки для выбора вида работы
task_type_list = InlineKeyboardMarkup(row_width=1)
task_type_list.add(InlineKeyboardButton(text="Однотипные задачи", callback_data="single_tasks"),
                   InlineKeyboardButton(text="Контрольная работа", callback_data="test_work"))


# инлайн кнопки для предметов
subject_list = InlineKeyboardMarkup(row_width=2)
subject_list.add(InlineKeyboardButton(text="Физика", callback_data="phys"))
subject_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_subject"))


# инлайн кнопки для предметов (контрольная)
subject_list_kr = InlineKeyboardMarkup(row_width=2)
subject_list_kr.add(InlineKeyboardButton(text="Физика", callback_data="phys_kr"))
subject_list_kr.add(InlineKeyboardButton(text="Назад", callback_data="back_from_subject_kr"))


# (физика) инлайн кнопки для выбора раздела темы (контрольная)
theme_phys_list_kr = InlineKeyboardMarkup(row_width=2)
theme_phys_list_kr.add(InlineKeyboardButton(text="Механика", callback_data="Mechanics_kr"),
                       InlineKeyboardButton(text="Кинематика", callback_data="Kinematics_kr"),
                       InlineKeyboardButton(text="Баллистика", callback_data="Ballistics_kr"))
theme_phys_list_kr.add(InlineKeyboardButton(text="Назад", callback_data="back_from_theme_phys_kr"))


# (физика) инлайн кнопки для выбора раздела темы
theme_phys_list = InlineKeyboardMarkup(row_width=2)
theme_phys_list.add(InlineKeyboardButton(text="Кинематика", callback_data="Kinematics"),
                    InlineKeyboardButton(text="Баллистика", callback_data="Ballistics"))
theme_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_theme_phys"))


# (физика) инлайн кнопки для выбора раздела темы
k_m_phys_list = InlineKeyboardMarkup(row_width=1)
k_m_phys_list.add(InlineKeyboardButton(text="Равномерное движение", callback_data="uniform_motion"),
              InlineKeyboardButton(text="Равноускоренное движение", callback_data="equiaxed_motion"))
k_m_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_k_m_phys"))


# (физика) инлайн кнопки для выбора раздела темы
b_m_phys_list = InlineKeyboardMarkup(row_width=1)
b_m_phys_list.add(InlineKeyboardButton(text="Свободное падение тел", callback_data="free_fall_of_bodies"),
              InlineKeyboardButton(text="Баллистическое движение", callback_data="ballistic_motion"))
b_m_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_b_m_phys"))


# инлайн кнопки для выбора количества задач
numbers_list = InlineKeyboardMarkup(row_width=3)
numbers_list.add(InlineKeyboardButton(text="1", callback_data="1"),
                 InlineKeyboardButton(text="2", callback_data="2"),
                 InlineKeyboardButton(text="3", callback_data="3"),
                 InlineKeyboardButton(text="4", callback_data="4"),
                 InlineKeyboardButton(text="5", callback_data="5"),
                 InlineKeyboardButton(text="6", callback_data="6"),
                 InlineKeyboardButton(text="7", callback_data="7"),
                 InlineKeyboardButton(text="8", callback_data="8"),
                 InlineKeyboardButton(text="9", callback_data="9"),
                 InlineKeyboardButton(text="10", callback_data="10"),
                 InlineKeyboardButton(text="11", callback_data="11"),
                 InlineKeyboardButton(text="12", callback_data="12"),
                 InlineKeyboardButton(text="13", callback_data="13"),
                 InlineKeyboardButton(text="14", callback_data="14"),
                 InlineKeyboardButton(text="15", callback_data="15"))
numbers_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_numbers"))


# инлайн кнопки для выбора отправки готового задания
export_list = InlineKeyboardMarkup(row_width=1)
export_list.add(InlineKeyboardButton(text="Телеграмм", callback_data="telega"),
                InlineKeyboardButton(text="PDF", callback_data="pdf"),
                InlineKeyboardButton(text="Телеграмм и PDF", callback_data="telega_and_pdf"))
export_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_export"))