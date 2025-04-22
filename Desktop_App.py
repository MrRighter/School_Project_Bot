"""НОВЫЙ КОСТЫЛЬНО-РАБОТАЮЩИЙ КОД"""


import re
from os import getcwd
from sys import platform

from flet import *

import Final_Executing_func as FEF

# Константы
MAC = False
path = ''
if MAC:
    splitter = '/'
else:
    splitter = '\\'
for item in getcwd().split(splitter):
    path += item + '/'
if platform == 'win32':
    splitter = '/'
else:
    splitter = '/'


class Interface:
    def __init__(self, page):
        self.splitter = splitter
        self.page = page
        self.selected_index = 0
        self.themes_dict = {
            'Физика': {
                'Кинематика': ["Равномерное движение", "Равноускоренное движение"],
                'Баллистика': ["Свободное падение тел", "Баллистическое движение", ]
            }
        }

        # Элементы интерфейса
        self.input_aa = TextField(value='1', visible=False, width=200, label="Количество задач")
        self.input_aac = TextField(value='1', visible=False, width=200, label="Количество задач")
        self.column = Column(scroll=ScrollMode.AUTO, height=1000)
        self.column_text_fast = Column(
            scroll=ScrollMode.AUTO,
            expand=True,
            height=1000,
            width=1000,
            auto_scroll=True
)
        self.number_of_tasks = TextField(on_change=self.example_func, on_submit=self.example_func, label="Количество задач")

        self.view_graphs = Checkbox(label="Выбрать тему?", value=False, on_change=self.obrab_view_graphs, visible=False)
        self.pdf_proverka = Checkbox(label="PDF", value=False, visible=False)
        self.txt_proverka = Checkbox(label="TXT", value=True, visible=False)
        self.standartaligment = MainAxisAlignment.START
        self.choose_function = Dropdown(
            label="Выберите предмет",
            data='Type',
            on_change=self.choose_tema,
            options=[
                dropdown.Option("Физика")
            ],
        )
        self.choose_predmet = Dropdown(
            label="Выберите предмет",
            data='Type',
            options=[
                dropdown.Option("Физика")
            ],
        )

        self.choose_tema_dropdown = Dropdown(
            label="Выберите раздел",
            data='Type',
            visible=False,
            on_change=self.set_choose_pod_tema_dropdown,
        )

        self.choose_pod_tema_dropdown = Dropdown(
            label="Выберите тему",
            data='Type',
            visible=False,
        )

        self.on_off_radio = RadioGroup(
            value='СР',
            content=Row(
                [
                    Radio(value="СР", label='Самостоятельная работа'),
                    Radio(value="КР", label='Контрольная работа'),
                ]
            )
        )
        self.drow_button = ElevatedButton('Составить', on_click=self.drow_simple_plot)
        self.drow_button_c = ElevatedButton('Составить', on_click=self.drow_simple_plot_c)
        self.label = Text('Выбор работы:  ', visible=True)

    def correct_theme(self, e):
        self.r = e.control.value
        if self.choose_predmet.value == list(self.themes_dict.keys())[0]:
            if e.control.value == list(self.themes_dict['Физика'].keys())[0]:
                self.add_options(self.column.controls[e.control.key].controls[2], self.themes_dict['Физика']['Кинематика'])
            elif e.control.value == list(self.themes_dict['Физика'].keys())[1]:
                self.add_options(self.column.controls[e.control.key].controls[2], self.themes_dict['Физика']['Баллистика'])
            self.column.controls[e.control.key].controls[2].update()
        pass

    def correct_pod_theme(self, e):
        self.t = e.control.value
        if self.choose_predmet.value == 'Физика':
            # Если выбрана тема1
            if e.control.value == 'Кинематика':
                self.add_options(self.column.controls[e.control.key].controls[2], self.themes_dict['Физика']['Кинематика'])
            elif e.control.value == 'Баллистика':
                self.add_options(self.column.controls[e.control.key].controls[2], self.themes_dict['Физика']['Баллистика'])
            self.column.controls[e.control.key].controls[2].update()
        # тут можно посмотреть как обращаться к отдельным задачам их списка

    def example_func(self, e):
        # self.txt_proverka.visible=True
        # self.txt_proverka.update()
        # self.pdf_proverka.visible = True
        # self.pdf_proverka.update()
        e.control.value = re.sub("[a-zA-Za-яА-Я]", "", e.control.value)
        e.control.update()
        if e.control.value != '':
            self.column.controls = []
            for i in range(1, int(e.control.value) + 1):
                if self.choose_predmet.value == 'Физика':
                    self.column.controls.append(Row([Text(f'{i}'),
                                                     Dropdown(label='Раздел', width=200, on_change=self.correct_theme,
                                                              key=i - 1),
                                                     Dropdown(label='Тема', width=200, on_change=self.correct_pod_theme,
                                                              key=i - 1),
                                                     ]))
                    self.add_phisics_thems(self.column.controls[i - 1].controls[1])

            self.row6.clean()
            self.row6.controls.append(self.column)
            self.row6.update()

    def choose_tema(self, e):
        if e.control.value == 'Физика':
            self.add_options(self.choose_tema_dropdown, list(self.themes_dict['Физика'].keys()))
        # self.view_graphs.visible = True
        # self.view_graphs.update()
        self.choose_tema_dropdown.visible = True
        self.choose_tema_dropdown.update()

    def add_phisics_thems(self, object):
        l = ['Кинематика', 'Баллистика']
        object.options = []
        for theme in l:
            object.options.append(dropdown.Option(theme))

    def add_options(self, object, names):
        object.options = []
        for theme in names:
            object.options.append(dropdown.Option(theme))

    def add_phisics_pod_tema(self, object, tema):
        if tema == 'Кинематика':
            self.add_options(object, self.themes_dict['Физика']['Кинематика'])
        elif tema == 'Баллистика':
            self.add_options(object, self.themes_dict['Физика']['Баллистика'])

    def set_choose_pod_tema_dropdown(self, e):
        self.add_phisics_pod_tema(self.choose_pod_tema_dropdown, e.control.value)
        self.choose_pod_tema_dropdown.value = ''
        self.choose_pod_tema_dropdown.visible = True
        self.choose_pod_tema_dropdown.update()
        self.input_aa.visible = True
        # self.txt_proverka.visible = True
        # self.pdf_proverka.visible = True
        self.input_aa.update()
        # self.txt_proverka.update()
        # self.pdf_proverka.update()

    def obrab_view_graphs(self, e):
        pass
        #     if e.control.value:
        #         self.choose_pod_tema_dropdown.visible = True
        #     else:
        #         self.choose_pod_tema_dropdown.visible = False
        #     self.choose_pod_tema_dropdown.update()

    def drow_simple_plot(self, e):
        key = {
            "Subject": self.choose_function.value,
            'Theme': self.choose_tema_dropdown.value,
            'Theme_section': self.choose_pod_tema_dropdown.value,
            'N': int(self.input_aa.value),
            # 'PDF':self.pdf_proverka.value,
            # 'TXT':self.txt_proverka.value
        }

        text = FEF.GetTaskText(key)

        self.column_text_fast.controls = []
        self.column_text_fast.controls.append(Row([Text(value=f'{text}', width=300, height=300)],
                                                width=300, height=300, scroll=ScrollMode.AUTO))
        self.column_text_fast.update()

    def drow_simple_plot_c(self, e):
        key = {
            "Subject": self.choose_predmet.value,
            'Theme': self.r,
            'Theme_section': self.t,
            'N': int(self.input_aac.value),
            # 'PDF':self.pdf_proverka.value,
            # 'TXT':self.txt_proverka.value
        }
        text = FEF.GetTaskText(key)
        self.column_text_fast.controls = []
        self.column_text_fast.controls.append(Row([Text(value=f'{text}', width=300, height=300)],
                                                width=300, height=300, scroll=ScrollMode.AUTO))
        self.column_text_fast.update()

    def get_menu(self):
        rail = NavigationRail(
            selected_index=self.selected_index,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon_content=Icon(icons.HOME),
                    selected_icon=icons.HOME,
                    label="Быстрая генерация"
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.SETTINGS),
                    selected_icon=icons.SETTINGS,
                    label="Конструктор",
                ),
            ],
            on_change=self.rebuild,
        )
        return rail

    def get_setup(self):
        row1 = Row([self.label, self.on_off_radio], alignment=self.standartaligment)
        row2 = Row([self.choose_function, self.drow_button], alignment=self.standartaligment)
        row3 = Row([self.choose_tema_dropdown, self.view_graphs], alignment=self.standartaligment)
        row4 = Row([self.choose_pod_tema_dropdown], alignment=self.standartaligment)
        row5 = Row([self.input_aa, self.txt_proverka, self.pdf_proverka], alignment=self.standartaligment)

        body = Column([Row([Text('Быстрая генерация')]),
                       row1,
                       row2,
                       row3,
                       row4,
                       row5,
                       self.column_text_fast,
                       ])
        return body

    def get_constructor(self):
        row1 = Row([self.label, self.on_off_radio], alignment=self.standartaligment)
        row2 = Row([self.choose_predmet, self.drow_button_c], alignment=self.standartaligment)
        row3 = Row([self.number_of_tasks], alignment=self.standartaligment)
        self.row6 = Row(alignment=self.standartaligment)
        row7 = Row([self.txt_proverka, self.pdf_proverka], alignment=self.standartaligment)

        body = Column([row1,
                       row2,
                       row3,
                       self.row6,
                       row7,
                       self.column_text_fast,
                       ])
        return body

    def get_body(self, e):
        if isinstance(e, str):  # Обработка вызова из класса
            if e == 'Быстрая генерация':
                return self.get_setup()
            elif e == 'Конструктор':
                return self.get_constructor()

        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_setup()
            elif e.control.selected_index == 1:
                return self.get_constructor()

    def rebuild(self, e):
        self.page.clean()
        body = self.get_body(e)
        self.page.add(
            Row(
                [
                    self.get_menu(), VerticalDivider(width=1),
                    Column([body], alignment=MainAxisAlignment.START, expand=True),
                ], expand=True,
            )
        )
        self.page.update()
        pass


if __name__ == "__main__":
    def main(page: Page):
        window = Interface(page)
        page.window_width = 900
        page.window_height = 860
        window.rebuild('Быстрая генерация')
        page.update()  # Используйте метод update вместо window_center

    app(target=main)




# import re
# from os import getcwd, path as os_path
# from sys import platform

# from flet import *

# # Предполагается, что Final_Executing_func.py находится в той же директории
# import Final_Executing_func as FEF


# class Interface:
#     def __init__(self, page: Page):
#         self.page = page
#         self.page.title = "Генератор учебных заданий"
#         self.page.vertical_alignment = MainAxisAlignment.START

#         self.themes_dict = {
#             'Физика': {
#                 'Кинематика': ["Равномерное движение", "Равноускоренное движение"],
#                 'Баллистика': ["Свободное падение тел", "Баллистическое движение"],
#             }
#         }

#         # Элементы интерфейса
#         self.number_of_tasks_fast = TextField(
#             label="Количество задач",
#             value="1",
#             keyboard_type=KeyboardType.NUMBER,
#             on_change=self.update_task_fields,
#             on_submit=self.generate_fast_task,
#             expand=True,
#         )
#         self.number_of_tasks_constructor = TextField(
#             label="Количество задач",
#             value="1",
#             keyboard_type=KeyboardType.NUMBER,
#             on_change=self.update_constructor_fields,
#             expand=True,
#         )

#         self.subject_dropdown_fast = Dropdown(
#             label="Выберите предмет",
#             options=[dropdown.Option("Физика")],
#             on_change=self.populate_theme_dropdown_fast,
#             expand=True,
#         )
#         self.theme_dropdown_fast = Dropdown(
#             label="Выберите раздел",
#             options=[],
#             visible=False,
#             on_change=self.populate_sub_theme_dropdown_fast,
#             expand=True,
#         )
#         self.sub_theme_dropdown_fast = Dropdown(
#             label="Выберите тему",
#             options=[],
#             visible=False,
#             expand=True,
#         )

#         self.subject_dropdown_constructor = Dropdown(
#             label="Выберите предмет",
#             options=[dropdown.Option("Физика")],
#             on_change=self.update_constructor_task_fields,
#             expand=True,
#         )
#         self.task_fields_constructor = Column(scroll=ScrollMode.AUTO)

#         self.work_type_radio = RadioGroup(
#             content=Row(
#                 [
#                     Radio(value="СР", label="Самостоятельная работа"),
#                     Radio(value="КР", label="Контрольная работа"),
#                 ]
#             ),
#             value="СР",
#         )

#         self.generate_button_fast = ElevatedButton(
#             "Составить", on_click=self.generate_fast_task
#         )
#         self.generate_button_constructor = ElevatedButton(
#             "Составить", on_click=self.generate_constructor_task
#         )

#         self.output_text = Text(selectable=True)
#         self.output_column = Container(
#             content=Column([self.output_text], horizontal_alignment=CrossAxisAlignment.START),
#             border=border.all(1, colors.OUTLINE),
#             padding=10,
#             expand=True,
#             height=300,
#         )

#         self.fast_generation_view = Column(
#             [
#                 Text("Быстрая генерация", style=TextStyle(size=20, weight=FontWeight.BOLD)),
#                 Row([Text("Тип работы:", width=150), self.work_type_radio]),
#                 self.subject_dropdown_fast,
#                 self.theme_dropdown_fast,
#                 self.sub_theme_dropdown_fast,
#                 self.number_of_tasks_fast,
#                 self.generate_button_fast,
#                 Text("Результат:", style=TextStyle(weight=FontWeight.BOLD)),
#                 self.output_column,
#             ],
#             horizontal_alignment=CrossAxisAlignment.START,
#             expand=True,
#             scroll=ScrollMode.AUTO,
#         )

#         self.constructor_view = Column(
#             [
#                 Text("Конструктор", style=TextStyle(size=20, weight=FontWeight.BOLD)),

# self.subject_dropdown_constructor,
#                 self.number_of_tasks_constructor,
#                 self.task_fields_constructor,
#                 self.generate_button_constructor,
#                 Text("Результат:", style=TextStyle(weight=FontWeight.BOLD)),
#                 self.output_column,
#             ],
#             horizontal_alignment=CrossAxisAlignment.START,
#             expand=True,
#             scroll=ScrollMode.AUTO,
#         )

#         self.tabs = Tabs(
#             expand=True,
#             tabs=[
#                 Tab(text="Быстрая генерация", content=self.fast_generation_view),
#                 Tab(text="Конструктор", content=self.constructor_view),
#             ],
#             on_change=self.tab_changed,
#         )

#         self.page.add(
#             Tabs(
#             expand=True,
#             tabs=[
#                 Tab(text="Быстрая генерация", content=self.fast_generation_view),
#                 Tab(text="Конструктор", content=self.constructor_view),
#             ],
#             on_change=self.tab_changed,
#         )
#         )

#     def tab_changed(self, e):
#         self.page.update()

#     def populate_theme_dropdown_fast(self, e):
#         self.theme_dropdown_fast.options = [
#             dropdown.Option(key) for key in self.themes_dict.get(e.control.value, {})
#         ]
#         self.theme_dropdown_fast.value = None
#         self.theme_dropdown_fast.visible = True
#         self.theme_dropdown_fast.update()
#         self.sub_theme_dropdown_fast.options = []
#         self.sub_theme_dropdown_fast.value = None
#         self.sub_theme_dropdown_fast.visible = False
#         self.sub_theme_dropdown_fast.update()

#     def populate_sub_theme_dropdown_fast(self, e):
#         self.sub_theme_dropdown_fast.options = [
#             dropdown.Option(item)
#             for item in self.themes_dict.get(
#                 self.subject_dropdown_fast.value, {}
#             ).get(e.control.value, [])
#         ]
#         self.sub_theme_dropdown_fast.value = None
#         self.sub_theme_dropdown_fast.visible = True
#         self.sub_theme_dropdown_fast.update()

#     def update_task_fields(self, e):
#         e.control.value = re.sub(r"[^0-9]", "", e.control.value)
#         e.control.update()

#     def generate_fast_task(self, e):
#         subject = self.subject_dropdown_fast.value
#         theme = self.theme_dropdown_fast.value
#         sub_theme = self.sub_theme_dropdown_fast.value
#         n_tasks = int(self.number_of_tasks_fast.value) if self.number_of_tasks_fast.value else 1

#         if subject and theme and sub_theme and n_tasks > 0:
#             key = {
#                 "Subject": subject,
#                 "Theme": theme,
#                 "Theme_section": sub_theme,
#                 "N": n_tasks,
#             }
#             task_text = FEF.GetTaskText(key)
#             self.output_text.value = task_text
#             self.output_column.update()
#         else:
#             self.page.show_snack_bar(
#                 SnackBar(Text("Пожалуйста, заполните все поля."))
#             )

#     def update_constructor_fields(self, e):
#         e.control.value = re.sub(r"[^0-9]", "", e.control.value)
#         e.control.update()
#         self.update_constructor_task_fields(None)

#     def update_constructor_task_fields(self, e):
#         self.task_fields_constructor.controls.clear()
#         num_tasks = (
#             int(self.number_of_tasks_constructor.value)
#             if self.number_of_tasks_constructor.value
#             else 1
#         )
#         for i in range(num_tasks):
#             theme_dropdown = Dropdown(
#                 label=f"Раздел {i+1}",
#                 options=[
#                     dropdown.Option(key)
#                     for key in self.themes_dict.get(
#                         self.subject_dropdown_constructor.value, {}
#                     )
#                 ],
#                 expand=True,
#             )
#             sub_theme_dropdown = Dropdown(
#                 label=f"Тема {i+1}", options=[], expand=True
#             )
#             theme_dropdown.on_change = lambda event: self.populate_constructor_sub_theme(
#                 event, sub_theme_dropdown
#             )
#             self.task_fields_constructor.controls.append(
#                 Column([theme_dropdown, sub_theme_dropdown])
#             )
#         self.task_fields_constructor.update()

#     def populate_constructor_sub_theme(self, e, sub_theme_dropdown):
#             sub_theme_dropdown.options = [
#                 dropdown.Option(item)
#                 for item in self.themes_dict.get(
#                     self.subject_dropdown_constructor.value, {}
#                 ).get(e.control.value, [])
#             ]
#             sub_theme_dropdown.value = None
#             sub_theme_dropdown.update()

#     def generate_constructor_task(self, e):
#         subject = self.subject_dropdown_constructor.value
#         n_tasks = (
#             int(self.number_of_tasks_constructor.value)
#             if self.number_of_tasks_constructor.value
#             else 1
#         )
#         tasks_data = []
#         for i in range(n_tasks):
#             theme_dropdown = self.task_fields_constructor.controls[i].controls[0]
#             sub_theme_dropdown = self.task_fields_constructor.controls[i].controls[1]
#             theme = theme_dropdown.value
#             sub_theme = sub_theme_dropdown.value
#             if theme and sub_theme:
#                 tasks_data.append({"Theme": theme, "Theme_section": sub_theme})
#             else:
#                 self.page.show_snack_bar(
#                     SnackBar(Text("Пожалуйста, выберите раздел и тему для каждой задачи."))
#                 )
#                 return

#         if tasks_data:
#             full_text = ""
#             for task in tasks_data:
#                 key = {"Subject": subject, **task}
#                 full_text += FEF.GetTaskText(key) + "\n\n"
#             self.output_text.value = full_text
#             self.output_column.update()


# if __name__ == "__main__":
#     def main(page: Page):
#         window = Interface(page)
#         page.window_width = 900
#         page.window_height = 860
#         window.rebuild('Быстрая генерация')
#         page.update()  # Используйте метод update вместо window_center

#     main(Page)
