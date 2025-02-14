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
        self.column = Column(scroll=ScrollMode.AUTO, height=300)
        self.column_text_fast = Column(scroll=ScrollMode.AUTO, height=300, width=300)
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

            for i in range(int(e.control.value)):
                print(
                    f'Задача {i} Раздел {self.column.controls[i].controls[0].value} Тема {self.column.controls[i].controls[1].value}')
                # тут можно посмотреть как обращаться к отдельным задачам их списка

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







"""СТАРЫЙ КОД"""

# import re
# from os import getcwd
# from sys import platform

# from flet import *

# import Final_Executing_func as FEF


# Mac = False
# path = ''
# if Mac == True:
#     splitter = '/'
# else:
#     splitter = '\\'
# for item in getcwd().split(splitter):
#     path += item + '/'
# if platform == 'win32':
#     splitter = '/'
# else:
#     splitter = '/'


# class Interface():
#     "Этот класс для..."

#     def __init__(self, page):
#         self.splitter = splitter
#         self.page = page
#         self.selected_index = 0
#         self.ThemsDict = {'Физика': {'Кинематика': ["Равномерное движение", "Равноускоренное движение"],
#                                      'Баллистика': ["Свободное падение тел", "Баллистическое движение", ]
#                                      }}

#         self.InputAA = TextField(value='1', visible=False, width=200, label="Количество задач")
#         self.InputAAC = TextField(value='1', visible=False, width=200, label="Количество задач")
#         self.Column = Column(scroll=ScrollMode.AUTO, height=300)
#         self.ColumnTextFast = Column(scroll=ScrollMode.AUTO, height=300,width=300)
#         self.NumberOfTasks = TextField(on_change=self.example_func, on_submit=self.example_func,
#                                        label="Количество задач")

#         self.ViewGraphs = Checkbox(label="Выбрать тему?", value=False, on_change=self.Obrab_ViewGraphs,
#                                    visible=False)
#         self.PDFPROVERKA = Checkbox(label="PDF", value=False, visible=False)
#         self.TXTPROVERKA = Checkbox(label="TXT", value=True, visible=False)
#         self.Standartaligment = MainAxisAlignment.START
#         self.ChooseFunction = Dropdown(
#             label="Выберите предмет",
#             data='Type',
#             on_change=self.ChooseTema,
#             options=[
#                 dropdown.Option("Физика")
#             ],
#         )
#         self.ChoosePredmet = Dropdown(
#             label="Выберите предмет",
#             data='Type',
#             options=[
#                 dropdown.Option("Физика")
#             ],
#         )

#         self.ChooseTemaDropdown = Dropdown(
#             label="Выберите раздел",
#             data='Type',
#             visible=False,
#             on_change=self.SetChoosePodTemaDropdown,
#         )

#         self.ChoosePodTemaDropdown = Dropdown(
#             label="Выберите тему",
#             data='Type',
#             visible=False,
#         )

#         self.ON_OFF_Radio = RadioGroup(
#             value='СР',
#             content=Row(
#                 [
#                     Radio(value="СР", label='Самостоятельная работа'),
#                     Radio(value="КР", label='Контрольная работа'),
#                 ]
#             )
#         )
#         self.DrowButton = ElevatedButton('Составить', on_click=self.DrowSimplePlot)
#         self.DrowButtonC = ElevatedButton('Составить', on_click=self.DrowSimplePlotC)
#         self.Label = Text('Выбор работы:  ', visible=True)

#     def CorrectTheme(self, e):
#         self.R = e.control.value
#         if self.ChoosePredmet.value == list(self.ThemsDict.keys())[0]:
#             if e.control.value == list(self.ThemsDict['Физика'].keys())[0]:
#                 self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Кинематика'])
#             elif e.control.value == list(self.ThemsDict['Физика'].keys())[1]:
#                 self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Баллистика'])
#             self.Column.controls[e.control.key].controls[2].update()
#         pass

#     def CorrectPodTheme(self, e):
#         self.T = e.control.value
#         if self.ChoosePredmet.value == 'Физика':
#             # Если выбрана тема1
#             if e.control.value == 'Кинематика':
#                 self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Кинематика'])
#             elif e.control.value == 'Баллистика':
#                 self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Баллистика'])
#             self.Column.controls[e.control.key].controls[2].update()
#         # тут можно посмотреть как обращаться к отдельным задачам их списка

#     def example_func(self, e):
#         # self.TXTPROVERKA.visible=True
#         # self.TXTPROVERKA.update()
#         # self.PDFPROVERKA.visible = True
#         # self.PDFPROVERKA.update()
#         e.control.value = re.sub("[a-zA-Za-яА-Я]", "", e.control.value)
#         e.control.update()
#         if e.control.value != '':
#             self.Column.controls = []
#             for i in range(1, int(e.control.value) + 1):
#                 if self.ChoosePredmet.value == 'Физика':
#                     self.Column.controls.append(Row([Text(f'{i}'),
#                                                      Dropdown(label='Раздел', width=200, on_change=self.CorrectTheme,
#                                                               key=i - 1),
#                                                      Dropdown(label='Тема', width=200, on_change=self.CorrectPodTheme,
#                                                               key=i - 1),
#                                                      ]))
#                     self.Add_PhisicsThems(self.Column.controls[i - 1].controls[1])

#             self.row6.clean()
#             self.row6.controls.append(self.Column)
#             self.row6.update()

#             for i in range(int(e.control.value)):
#                 print(
#                     f'Задача {i} Раздел {self.Column.controls[i].controls[0].value} Тема {self.Column.controls[i].controls[1].value}')
#                 # тут можно посмотреть как обращаться к отдельным задачам их списка

#     def ChooseTema(self, e):
#         if e.control.value == 'Физика':
#             self.AddOptions(self.ChooseTemaDropdown, list(self.ThemsDict['Физика'].keys()))
#         # self.ViewGraphs.visible = True
#         # self.ViewGraphs.update()
#         self.ChooseTemaDropdown.visible = True
#         self.ChooseTemaDropdown.update()

#     def Add_PhisicsThems(self, object):
#         l = ['Кинематика', 'Баллистика']
#         object.options = []
#         for theme in l:
#             object.options.append(dropdown.Option(theme))

#     def AddOptions(self, object, names):
#         object.options = []
#         for theme in names:
#             object.options.append(dropdown.Option(theme))

#     def AddPhisicsPodTema(self, object, tema):
#         if tema == 'Кинематика':
#             self.AddOptions(object, self.ThemsDict['Физика']['Кинематика'])
#         elif tema == 'Баллистика':
#             self.AddOptions(object, self.ThemsDict['Физика']['Баллистика'])

#     def SetChoosePodTemaDropdown(self, e):
#         self.AddPhisicsPodTema(self.ChoosePodTemaDropdown, e.control.value)
#         self.ChoosePodTemaDropdown.value = ''
#         self.ChoosePodTemaDropdown.visible=True
#         self.ChoosePodTemaDropdown.update()
#         self.InputAA.visible = True
#         # self.TXTPROVERKA.visible = True
#         # self.PDFPROVERKA.visible = True
#         self.InputAA.update()
#         # self.TXTPROVERKA.update()
#         # self.PDFPROVERKA.update()

#     def Obrab_ViewGraphs(self, e):
#         pass
#     #     if e.control.value:
#     #         self.ChoosePodTemaDropdown.visible = True
#     #     else:
#     #         self.ChoosePodTemaDropdown.visible = False
#     #     self.ChoosePodTemaDropdown.update()

#     def DrowSimplePlot(self, e):
#         KEY = {"Subject":self.ChooseFunction.value,
#                'Theme':self.ChooseTemaDropdown.value,
#                'Theme_section':self.ChoosePodTemaDropdown.value,
#                'N':int(self.InputAA.value),
#                # 'PDF':self.PDFPROVERKA.value,
#                # 'TXT':self.TXTPROVERKA.value
#                }

#         text = FEF.GetTaskText(KEY)

#         self.ColumnTextFast.controls = []
#         self.ColumnTextFast.controls.append(Row([Text(value=f'{text}',width=300,height=300)],
#                                                 width=300,height=300,scroll=ScrollMode.AUTO))
#         self.ColumnTextFast.update()

#     def DrowSimplePlotC(self, e):
#         KEY = {"Subject":self.ChoosePredmet.value,
#                'Theme':self.R,
#                'Theme_section':self.T,
#                'N':int(self.InputAAC.value),
#                # 'PDF':self.PDFPROVERKA.value,
#                # 'TXT':self.TXTPROVERKA.value
#                }
#         text = FEF.GetTaskText(KEY)
#         self.ColumnTextFast.controls = []
#         self.ColumnTextFast.controls.append(Row([Text(value=f'{text}',width=300,height=300)],
#                                                 width=300,height=300,scroll=ScrollMode.AUTO))
#         self.ColumnTextFast.update()



#     def get_menu(self):
#         rail = NavigationRail(
#             selected_index=self.selected_index,
#             label_type=NavigationRailLabelType.ALL,
#             min_width=100,
#             min_extended_width=400,
#             group_alignment=-0.9,
#             destinations=[
#                 NavigationRailDestination(
#                     icon_content=Icon(icons.HOME),
#                     selected_icon=icons.HOME,
#                     label="Быстрая генерация"
#                 ),
#                 NavigationRailDestination(
#                     icon_content=Icon(icons.SETTINGS),
#                     selected_icon=icons.SETTINGS,
#                     label="Конструктор",
#                 ),
#             ],
#             on_change=self.rebuild,
#         )
#         return rail

#     def get_Setup(self):
#         row1 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
#         row2 = Row([self.ChooseFunction, self.DrowButton], alignment=self.Standartaligment)
#         row3 = Row([self.ChooseTemaDropdown, self.ViewGraphs], alignment=self.Standartaligment)
#         row4 = Row([self.ChoosePodTemaDropdown], alignment=self.Standartaligment)
#         row5 = Row([self.InputAA, self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)

#         body = Column([Row([Text('Быстрая генерация')]),
#                        row1,
#                        row2,
#                        row3,
#                        row4,
#                        row5,
#                        self.ColumnTextFast,
#                        ])
#         return body

#     def get_Constructor(self):
#         row1 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
#         row2 = Row([self.ChoosePredmet, self.DrowButtonC], alignment=self.Standartaligment)
#         row3 = Row([self.NumberOfTasks], alignment=self.Standartaligment)
#         self.row6 = Row(alignment=self.Standartaligment)
#         row7 = Row([self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)

#         body = Column([row1,
#                        row2,
#                        row3,
#                        self.row6,
#                        row7,
#                        self.ColumnTextFast,
#                        ])
#         return body

#     def get_body(self, e):
#         if isinstance(e, str):  # Обработка вызова из класса
#             if e == 'Быстрая генерация':
#                 return self.get_Setup()
#             elif e == 'Конструктор':
#                 return self.get_Constructor()

#         elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
#             if e.control.selected_index == 0:
#                 return self.get_Setup()
#             elif e.control.selected_index == 1:
#                 return self.get_Constructor()

#     def rebuild(self, e):
#         self.page.clean()
#         body = self.get_body(e)
#         self.page.add(
#             Row(
#                 [
#                     self.get_menu(), VerticalDivider(width=1),
#                     Column([body], alignment=MainAxisAlignment.START, expand=True),
#                 ], expand=True,
#             )
#         )
#         self.page.update()
#         pass


# if __name__ == "__main__":
#     def main(page: Page):
#         Window = Interface(page)
#         page.window_width = 900
#         page.window_height = 860
#         Window.rebuild('Быстрая генерация')
#         page.window_center()

#     app(target=main)
