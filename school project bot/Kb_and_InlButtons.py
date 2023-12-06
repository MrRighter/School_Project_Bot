from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# инлайн кнопки для выбора вида работы
task_type_list = InlineKeyboardMarkup(row_width=1)
task_type_list.add(InlineKeyboardButton(text="Однотипные задачи", callback_data="single_tasks"),
                   InlineKeyboardButton(text="Контрольная работа", callback_data="test_work"))


# инлайн кнопки для предметов
subject_list = InlineKeyboardMarkup(row_width=2)
subject_list.add(InlineKeyboardButton(text="Физика", callback_data="phys"),
                 InlineKeyboardButton(text="Математика", callback_data="mathem"),
                 InlineKeyboardButton(text="Информатика", callback_data="informatics"))
subject_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_subject"))

# инлайн кнопки для предметов (контрольная)
subject_list_kr = InlineKeyboardMarkup(row_width=2)
subject_list_kr.add(InlineKeyboardButton(text="Физика", callback_data="phys_kr"))
                #  InlineKeyboardButton(text="Математика", callback_data="mathem_kr"),
                #  InlineKeyboardButton(text="Информатика", callback_data="informatics_kr"))
subject_list_kr.add(InlineKeyboardButton(text="Назад", callback_data="back_from_subject_kr"))


# (физика) инлайн кнопки для выбора раздела темы (контрольная)
theme_phys_list_kr = InlineKeyboardMarkup(row_width=2)
theme_phys_list_kr.add(InlineKeyboardButton(text="Кинематика", callback_data="Kinematics_kr"))
                #     InlineKeyboardButton(text="Баллистика", callback_data="Ballistics_kr"),
                #     InlineKeyboardButton(text="Статика", callback_data="Statics_kr"),
                #     InlineKeyboardButton(text="Работа и энергия", callback_data="Work_and_energy_kr"))
theme_phys_list_kr.add(InlineKeyboardButton(text="Назад", callback_data="back_from_theme_phys_kr"))


# (физика) инлайн кнопки для выбора раздела темы
theme_phys_list = InlineKeyboardMarkup(row_width=2)
theme_phys_list.add(InlineKeyboardButton(text="Кинематика", callback_data="Kinematics"),
                    InlineKeyboardButton(text="Баллистика", callback_data="Ballistics"),
                    InlineKeyboardButton(text="Статика", callback_data="Statics"),
                    InlineKeyboardButton(text="Работа и энергия", callback_data="Work_and_energy"))
theme_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_theme_phys"))

# (физика) инлайн кнопки для выбора раздела темы
phys_list = InlineKeyboardMarkup(row_width=1)
phys_list.add(InlineKeyboardButton(text="Равномерное движение", callback_data="u_motion"),
              InlineKeyboardButton(text="Равноускоренное движение", callback_data="ea_motion"))
phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_phys"))

# (физика) инлайн кнопки для равномерного движения
u_q_phys_list = InlineKeyboardMarkup(row_width=3)
u_q_phys_list.add(InlineKeyboardButton(text="Время", callback_data="u_time"),
                  InlineKeyboardButton(text="Путь", callback_data="u_distance"),
                  InlineKeyboardButton(text="Скорость", callback_data="u_speed"),
                  InlineKeyboardButton(text="Графики зависимости", callback_data="dependency_graphs"))
u_q_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_u_q_phys"))

# (физика) инлайн кнопки для равноускоренного движения
ea_q_phys_list = InlineKeyboardMarkup(row_width=3)
ea_q_phys_list.add(InlineKeyboardButton(text="Время", callback_data="ea_time"),
                   InlineKeyboardButton(text="Путь", callback_data="ea_distance"),
                   InlineKeyboardButton(text="Ускорение", callback_data="ea_boost"),
                   InlineKeyboardButton(text="Начальную скорость", callback_data="ea_first_speed"),
                   InlineKeyboardButton(text="Конечную скорость", callback_data="ea_second_speed"))
ea_q_phys_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_ea_q_phys"))


# (математика) инлайн кнопки для выбора темы/направления
mathem_list = InlineKeyboardMarkup(row_width=2)
mathem_list.add(InlineKeyboardButton(text="Алгебра", callback_data="algebra"),
                InlineKeyboardButton(text="Геометрия", callback_data="geometry"))
mathem_list.add(InlineKeyboardButton(text="Назад", callback_data="back_from_mathem"))