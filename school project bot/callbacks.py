# from aiogram import types
# from Kb_and_InlButtons import *


# async def callback_query_keyboard(callback_query: types.CallbackQuery, bot): # callback данные
#     global item, theme, subtopic # предмет, тема/направление, подтема/что нужно найти
# # новый
# # предмет
#     if callback_query.data == "phys": # предмет физика
#         await callback_query.answer()
#         item = "физика"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Доступные темы", reply_markup=phys_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # (физика) новая тема и её подтемы
#     elif callback_query.data == "u_motion": # тема - равномерное движение
#         await callback_query.answer()
#         theme = "равномерное движение"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Что нужно найти", reply_markup=u_q_phys_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "u_time": # найти время
#         await callback_query.answer()
#         subtopic = "время"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "u_distance": # найти путь
#         await callback_query.answer()
#         subtopic = "путь"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "u_speed": # найти скорость
#         await callback_query.answer()
#         subtopic = "скорость"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # (физика) новая тема и её подтемы
#     elif callback_query.data == "ea_motion": # тема - равноускоренное движение
#         await callback_query.answer()
#         theme = "равноускоренное движение"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Что нужно найти", reply_markup=ea_q_phys_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "ea_time": # найти время
#         await callback_query.answer()
#         subtopic = "время"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "ea_distance": # найти путь
#         await callback_query.answer()
#         subtopic = "путь"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "ea_boost": # найти ускорение
#         await callback_query.answer()
#         subtopic = "ускорение"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "ea_first_speed": # найти начальную скорость
#         await callback_query.answer()
#         subtopic = "начальная скорость"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "ea_second_speed": # найти конечную скорость
#         await callback_query.answer()
#         subtopic = "конечная скорость"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите количество задач")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # новый
# # предмет
#     elif callback_query.data == "mathem": # предмет математика
#         await callback_query.answer()
#         item = "математика"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите направление", reply_markup=mathem_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # (математика) новая тема и её подтемы
#     elif callback_query.data == "algebra": # направление/тема - алгебра
#         await callback_query.answer()
#         theme = "алгебра"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите интересующую тему", reply_markup=algebra_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "2+2": # 2+2
#         await callback_query.answer()
#         subtopic = "2+2"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="4")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "4+4": # 4+4
#         await callback_query.answer()
#         subtopic = "4+4"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="8")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # (математика) новая тема и её подтемы
#     elif callback_query.data == "geometry": # направление/тема - геометрия
#         await callback_query.answer()
#         theme = "геометрия"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите интересующую тему", reply_markup=geometry_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "bla": # бла бла бла
#         await callback_query.answer()
#         subtopic = "бла бла бла"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="не придумал что выводить )")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "be": # бе бе бе
#         await callback_query.answer()
#         subtopic = "бе бе бе"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="тоже не придумал что выводить ))")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # (математика) новая тема и её подтемы
#     elif callback_query.data == "hypothesis": # направление/тема - гипотезы
#         await callback_query.answer()
#         theme = "гипотеза"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Выберите гипотезу", reply_markup=hypothesis_list)
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
#     elif callback_query.data == "hyp_coll": # гипотеза Коллатца
#         await callback_query.answer()
#         subtopic = "коллатца"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Введите натуральное число")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
# # новый
# # предмет
#     elif callback_query.data == "inf": # предмет информатика
#         await callback_query.answer()
#         item = "информатика"
#         await bot.send_message(chat_id=callback_query.from_user.id, text="Информатика пока не доступна")
#         await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)