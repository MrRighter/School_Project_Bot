from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


# основная клавиатура
base_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
base_kb.add("Составить задачи").add("Составить контрольную").add("Кнопка по приколу")

# инлайн кнопки для предметов
subject_list = InlineKeyboardMarkup(row_width=2)
subject_list.add(InlineKeyboardButton(text="Физика", callback_data="phys"),
                 InlineKeyboardButton(text="Математика", callback_data="mathem"),
                 InlineKeyboardButton(text="Информатика", callback_data="inf"))


# (физика) инлайн кнопки для выбора темы
phys_list = InlineKeyboardMarkup(row_width=1)
phys_list.add(InlineKeyboardButton(text="Равномерное движение", callback_data="u_motion"),
              InlineKeyboardButton(text="Равноускоренное движение", callback_data="ea_motion"))

# (физика) инлайн кнопки для равномерного движения
u_q_phys_list = InlineKeyboardMarkup(row_width=2)
u_q_phys_list.add(InlineKeyboardButton(text="Время", callback_data="u_time"),
                  InlineKeyboardButton(text="Путь", callback_data="u_distance"),
                  InlineKeyboardButton(text="Скорость", callback_data="u_speed"))

# (физика) инлайн кнопки для равноускоренного движения
ea_q_phys_list = InlineKeyboardMarkup(row_width=3)
ea_q_phys_list.add(InlineKeyboardButton(text="Время", callback_data="ea_time"),
                   InlineKeyboardButton(text="Путь", callback_data="ea_distance"),
                   InlineKeyboardButton(text="Ускорение", callback_data="ea_boost"),
                   InlineKeyboardButton(text="Начальную скорость", callback_data="ea_first_speed"),
                   InlineKeyboardButton(text="Конечную скорость", callback_data="ea_second_speed"),)


# (математика) инлайн кнопки для выбора темы/направления
mathem_list = InlineKeyboardMarkup(row_width=2)
mathem_list.add(InlineKeyboardButton(text="Алгебра", callback_data="algebra"),
                InlineKeyboardButton(text="Геометрия", callback_data="geometry"),
                InlineKeyboardButton(text="Гипотезы", callback_data="hypothesis"))

# (математика) инлайн кнопки для алгебры
algebra_list = InlineKeyboardMarkup(row_width=1)
algebra_list.add(InlineKeyboardButton(text="2+2", callback_data="2+2"),
                 InlineKeyboardButton(text="4+4", callback_data="4+4"))

# (математика) инлайн кнопки для геометрии
geometry_list = InlineKeyboardMarkup(row_width=1)
geometry_list.add(InlineKeyboardButton(text="бла бла бла", callback_data="bla"),
                 InlineKeyboardButton(text="бе бе бе", callback_data="be"))

# (математика) инлайн кнопки для гипотез
hypothesis_list = InlineKeyboardMarkup(row_width=1)
hypothesis_list.add(InlineKeyboardButton(text="Гипотеза Коллатца", callback_data="hyp_coll"))