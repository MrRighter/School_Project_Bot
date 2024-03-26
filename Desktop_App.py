import re
from os import getcwd
from sys import platform
from Class_Creator import Creator
import Final_Executing_func as FEF
from flet import (
    ElevatedButton,
    Page,
    Row,
    Text,
    icons,
    TextField,
    Checkbox,
    Dropdown,
    IconButton,
    MainAxisAlignment,
    dropdown,
    RadioGroup,
    Radio,
    app,
    VerticalDivider,
    Column,
    FloatingActionButton,
    NavigationRail,
    NavigationRailLabelType,
    Icon,
    NavigationRailDestination,
    AlertDialog,
    ScrollMode
)

Mac = False
path = ''
if Mac == True:
    splitter = '/'
else:
    splitter = '\\'
for item in getcwd().split(splitter):
    path += item + '/'
if platform == 'win32':
    splitter = '/'
else:
    splitter = '/'


class Interface():
    "Этот класс для..."

    def __init__(self, page):
        self.splitter = splitter
        self.page = page
        self.selected_index = 0
        self.ThemsDict = {'Физика': {'Динамика': ['Законы ньютона', "Сила упругости"],
                                     'Кинематика': ["Равномерное движение", "Равноускоренное движение"],
                                     'Баллистика': ["Свободное падение тел", "Баллистическое движение", ]
                                     },
                          'Математика': {1, 2}, }

        self.InputAA = TextField(value='1', visible=False, width=200, label="Количество задач")
        self.Column = Column(scroll=ScrollMode.AUTO, height=300)
        self.ColumnTextFast = Column(scroll=ScrollMode.AUTO, height=300,width=300)
        self.NumberOfTasks = TextField(on_change=self.example_func, on_submit=self.example_func,
                                       label="Количество задач")

        self.ViewGraphs = Checkbox(label="Выбрать подтему?", value=False, on_change=self.Obrab_ViewGraphs,
                                   visible=False)
        self.PDFPROVERKA = Checkbox(label="PDF", value=False, visible=False)
        self.TXTPROVERKA = Checkbox(label="TXT", value=True, visible=False)
        self.Standartaligment = MainAxisAlignment.START
        self.ChooseFunction = Dropdown(
            label="Выберите предмет",
            data='Type',
            on_change=self.ChooseTema,
            options=[
                dropdown.Option("Физика"),
                dropdown.Option("Математика"),
            ],
        )
        self.ChoosePredmet = Dropdown(
            label="Выберите предмет",
            data='Type',
            # on_change=self.ChooseTema,
            options=[
                dropdown.Option("Физика"),
                dropdown.Option("Математика"),
            ],
        )

        self.ChooseTemaDropdown = Dropdown(
            label="Выберите тему",
            data='Type',
            visible=False,
            on_change=self.SetChoosePodTemaDropdown,
        )

        self.ChoosePodTemaDropdown = Dropdown(
            label="Выберите подтему",
            data='Type',
            visible=False,
        )

        self.ON_OFF_Radio = RadioGroup(
            value='СР',
            content=Row(
                [
                    Radio(value="СР", label='Самостоятельная работа'),
                    Radio(value="КР", label='Контрольная работа'),
                ]
            )
        )
        self.DrowButton = ElevatedButton('Составить', on_click=self.DrowSimplePlot)
        self.Label = Text('Выбор работы:  ', visible=True)

    def CorrectTheme(self, e):
        print(e.control)
        if self.ChoosePredmet.value == list(self.ThemsDict.keys())[0]:
            if e.control.value == list(self.ThemsDict['Физика'].keys())[0]:
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Динамика'])
            elif e.control.value == list(self.ThemsDict['Физика'].keys())[1]:
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Кинематика'])
            elif e.control.value == list(self.ThemsDict['Физика'].keys())[2]:
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Баллистика'])
            self.Column.controls[e.control.key].controls[2].update()
        pass

    def CorrectPodTheme(self, e):
        print(e.control)
        if self.ChoosePredmet.value == 'Физика':
            # Если выбрана тема1
            if e.control.value == 'Динамика':
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Динамика'])
            elif e.control.value == 'Кинематика':
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Кинематика'])
            elif e.control.value == 'Баллистика':
                self.AddOptions(self.Column.controls[e.control.key].controls[2], self.ThemsDict['Физика']['Баллистика'])
            self.Column.controls[e.control.key].controls[2].update()
        # тут можно посмотреть как обращаться к отдельным задачам их списка

    def example_func(self, e):
        self.TXTPROVERKA.visible=True
        self.TXTPROVERKA.update()
        self.PDFPROVERKA.visible = True
        self.PDFPROVERKA.update()
        e.control.value = re.sub("[a-zA-Za-яА-Я]", "", e.control.value)
        e.control.update()
        if e.control.value != '':
            self.Column.controls = []
            for i in range(1, int(e.control.value) + 1):
                if self.ChoosePredmet.value == 'Физика':
                    self.Column.controls.append(Row([Text(f'{i}'),
                                                     Dropdown(label='Раздел', width=200, on_change=self.CorrectTheme,
                                                              key=i - 1),
                                                     Dropdown(label='Раздел', width=200, on_change=self.CorrectPodTheme,
                                                              key=i - 1),
                                                     ]))
                    self.Add_PhisicsThems(self.Column.controls[i - 1].controls[1])

            self.row6.clean()
            self.row6.controls.append(self.Column)
            self.row6.update()

            for i in range(int(e.control.value)):
                print(
                    f'Задача {i} Раздел {self.Column.controls[i].controls[0].value} Тема {self.Column.controls[i].controls[1].value}')
                # тут можно посмотреть как обращаться к отдельным задачам их списка

    def ChooseTema(self, e):
        if e.control.value == 'Физика':
            self.AddOptions(self.ChooseTemaDropdown, list(self.ThemsDict['Физика'].keys()))
        self.ViewGraphs.visible = True
        self.ViewGraphs.update()
        self.ChooseTemaDropdown.visible = True
        self.ChooseTemaDropdown.update()

    def Add_PhisicsThems(self, object):
        l = ['Динамика', 'Кинематика', 'Баллистика']
        object.options = []
        for theme in l:
            object.options.append(dropdown.Option(theme))

    def AddOptions(self, object, names):
        object.options = []
        for theme in names:
            object.options.append(dropdown.Option(theme))

    def AddPhisicsPodTema(self, object, tema):
        if tema == 'Динамика':
            self.AddOptions(object, self.ThemsDict['Физика']['Динамика'])
        elif tema == 'Кинематика':
            self.AddOptions(object, self.ThemsDict['Физика']['Кинематика'])
        elif tema == 'Баллистика':
            self.AddOptions(object, self.ThemsDict['Физика']['Баллистика'])

    def SetChoosePodTemaDropdown(self, e):
        self.AddPhisicsPodTema(self.ChoosePodTemaDropdown, e.control.value)
        self.ChoosePodTemaDropdown.value = ''
        self.ChoosePodTemaDropdown.update()
        self.InputAA.visible = True
        self.TXTPROVERKA.visible = True
        self.PDFPROVERKA.visible = True
        self.InputAA.update()
        self.TXTPROVERKA.update()
        self.PDFPROVERKA.update()

    def Obrab_ViewGraphs(self, e):
        if e.control.value:
            self.ChoosePodTemaDropdown.visible = True
        else:
            self.ChoosePodTemaDropdown.visible = False
        self.ChoosePodTemaDropdown.update()

    def DrowSimplePlot(self, e):
        print('Создай меня')
        print(self.TXTPROVERKA.value)
        print(self.PDFPROVERKA.value)
        print(self.ON_OFF_Radio.value)
        KEY = {"Subject":self.ChooseFunction.value,
               'Theme':self.ChooseTemaDropdown.value,
               'Theme_section':self.ChoosePodTemaDropdown.value,
               'N':int(self.InputAA.value),
               'PDF':self.PDFPROVERKA.value,
               'TXT':self.TXTPROVERKA.value}
        print(KEY)

        text = FEF.GetTaskText(KEY)

        self.ColumnTextFast.controls = []
        self.ColumnTextFast.controls.append(Row([Text(value=f'{text}',width=300,height=300)],
                                                width=300,height=300,scroll=ScrollMode.AUTO))
        self.ColumnTextFast.update()




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

    def get_Setup(self):
        row1 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
        row2 = Row([self.ChooseFunction, self.DrowButton], alignment=self.Standartaligment)
        row3 = Row([self.ChooseTemaDropdown, self.ViewGraphs], alignment=self.Standartaligment)
        row4 = Row([self.ChoosePodTemaDropdown], alignment=self.Standartaligment)
        row5 = Row([self.InputAA, self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)

        body = Column([Row([Text('Быстрая генерация')]),
                       row1,
                       row2,
                       row3,
                       row4,
                       row5,
                       self.ColumnTextFast,
                       ])
        return body

    def get_Constructor(self):
        row1 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
        row2 = Row([self.ChoosePredmet, self.DrowButton], alignment=self.Standartaligment)
        row3 = Row([self.NumberOfTasks], alignment=self.Standartaligment)
        self.row6 = Row(alignment=self.Standartaligment)
        row7 = Row([self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)

        body = Column([row1,
                       row2,
                       row3,
                       self.row6,
                       row7,
                       ])
        return body

    def get_body(self, e):
        if isinstance(e, str):  # Обработка вызова из класса
            if e == 'Быстрая генерация':
                return self.get_Setup()
            elif e == 'Конструктор':
                return self.get_Constructor()

        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_Setup()
            elif e.control.selected_index == 1:
                return self.get_Constructor()

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
        Window = Interface(page)
        page.window_width = 900
        page.window_height = 860
        Window.rebuild('Быстрая генерация')
        page.window_center()


    app(target=main)