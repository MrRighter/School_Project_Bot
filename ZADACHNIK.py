from os import getcwd
from sys import platform
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
        self.InputA = Dropdown(
            label="Количество задач",
            data='Type',
            visible = False,
            # on_change=self.Vita,
        )
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
        self.ChooseFunctionGener = Dropdown(
            label="Выберите предмет",
            data='Type',
            on_change=self.ChooseTemaGener,
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
        self.ChooseTemaDropdownGener = Dropdown(
            label="Выберите тему",
            data='Type',
            visible=False,
            on_change=self.SetChoosePodTemaDropdownGener,
        )
        self.ChoosePodTemaDropdown = Dropdown(
            label="Выберите подтему",
            data='Type',
            visible=False,
        )
        self.ChoosePodTemaDropdownGener = Dropdown(
            label="Выберите подтему",
            data='Type',
            visible=False,
        )
        # self.ChoosePodTemaDropdownGener2 = Dropdown(
        #     label="Выберите подтему",
        #     data='Type',
        #     visible=False,
        # )
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
        self.Label = Text('Выбор работы:    ', visible=True)


    def SetInputA (self, e):
        for num in range(1, 6):
            self.InputA.options.append(dropdown.Option(num))

    def ChooseTema(self, e):
        if e.control.value == 'Физика':
            l = ['Механика', 'Кинематика', 'Баллистика']
            self.ChooseTemaDropdown.options = []
            for theme in l:
                self.ChooseTemaDropdown.options.append(dropdown.Option(theme))
        self.ViewGraphs.visible = True
        self.ViewGraphs.update()
        self.ChooseTemaDropdown.visible = True
        self.ChooseTemaDropdown.update()

    def ChooseTemaGener(self, e):
        self.SetInputA(e)
        if e.control.value == 'Физика':
            l = ['Механика', 'Кинематика', 'Баллистика']
            self.ChooseTemaDropdownGener.options = []
            for theme in l:
                self.ChooseTemaDropdownGener.options.append(dropdown.Option(theme))
        self.ChooseTemaDropdownGener.visible = True
        self.ChooseTemaDropdownGener.update()

    def SetChoosePodTemaDropdown(self, e):
        if e.control.value == 'Механика':
            l = ['Механика', 'Кинематика', 'Баллистика']
            self.ChoosePodTemaDropdown.options = []
            for theme in l:
                self.ChoosePodTemaDropdown.options.append(dropdown.Option(theme))
        elif e.control.value == 'Кинематика':
            l = ['Кинематика', 'Механика', 'Баллистика']
            self.ChoosePodTemaDropdown.options = []
            for theme in l:
                self.ChoosePodTemaDropdown.options.append(dropdown.Option(theme))
        elif e.control.value == 'Баллистика':
            l = ['Баллистика', 'Механика', 'Кинематика']
            self.ChoosePodTemaDropdown.options = []
            for theme in l:
                self.ChoosePodTemaDropdown.options.append(dropdown.Option(theme))
        self.ChoosePodTemaDropdown.value = ''
        self.ChoosePodTemaDropdown.update()
        self.InputA.visible = True
        self.TXTPROVERKA.visible = True
        self.PDFPROVERKA.visible = True
        self.InputA.update()
        self.TXTPROVERKA.update()
        self.PDFPROVERKA.update()

    def SetChoosePodTemaDropdownGener(self, e):
        if e.control.value == 'Механика':
            l = ['Механика', 'Кинематика', 'Баллистика']
            self.ChoosePodTemaDropdownGener.options = []
            for theme in l:
                self.ChoosePodTemaDropdownGener.options.append(dropdown.Option(theme))
        elif e.control.value == 'Кинематика':
            l = ['Кинематика', 'Механика', 'Баллистика']
            self.ChoosePodTemaDropdownGener.options = []
            for theme in l:
                self.ChoosePodTemaDropdownGener.options.append(dropdown.Option(theme))
        elif e.control.value == 'Баллистика':
            l = ['Баллистика', 'Механика', 'Кинематика']
            self.ChoosePodTemaDropdownGener.options = []
            for theme in l:
                self.ChoosePodTemaDropdownGener.options.append(dropdown.Option(theme))
        self.ChoosePodTemaDropdownGener.value = ''
        self.ChoosePodTemaDropdownGener.update()
        self.InputA.visible = True
        self.TXTPROVERKA.visible = True
        self.PDFPROVERKA.visible = True
        self.ChoosePodTemaDropdownGener.visible = True
        self.ChoosePodTemaDropdownGener.update()
        self.InputA.update()
        self.TXTPROVERKA.update()
        self.PDFPROVERKA.update()

    # def SetChoosePodTemaDropdownGener2(self, e):
    #     if e.control.value == 'Механика':
    #         l = ['Механика', 'Кинематика', 'Баллистика']
    #         self.ChoosePodTemaDropdownGener2.options = []
    #         for theme in l:
    #             self.ChoosePodTemaDropdownGener2.options.append(dropdown.Option(theme))
    #     elif e.control.value == 'Кинематика':
    #         l = ['Кинематика', 'Механика', 'Баллистика']
    #         self.ChoosePodTemaDropdownGener2.options = []
    #         for theme in l:
    #             self.ChoosePodTemaDropdownGener2.options.append(dropdown.Option(theme))
    #     elif e.control.value == 'Баллистика':
    #         l = ['Баллистика', 'Механика', 'Кинематика']
    #         self.ChoosePodTemaDropdownGener2.options = []
    #         for theme in l:
    #             self.ChoosePodTemaDropdownGener2.options.append(dropdown.Option(theme))
    #     self.ChoosePodTemaDropdownGener2.value = ''
    #     self.ChoosePodTemaDropdownGener2.update()
    #     self.InputA.visible = True
    #     self.TXTPROVERKA.visible = True
    #     self.PDFPROVERKA.visible = True
    #     self.ChoosePodTemaDropdownGener2.visible = True
    #     self.ChoosePodTemaDropdownGener2.update()
    #     self.InputA.update()
    #     self.TXTPROVERKA.update()
    #     self.PDFPROVERKA.update()

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
        pass


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
                    label="Расширенная генерация",
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
        row5 = Row([self.InputA, self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)
        body = Column([Row([Text('Быстрая генерация')]),
            row1,
            row2,
            row3,
            row4,
            row5,
        ])
        return body

    def get_Setup2(self):
        row1 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
        row2 = Row([self.ChooseFunctionGener, self.DrowButton], alignment=self.Standartaligment)
        row3 = Row([self.ChooseTemaDropdownGener], alignment=self.Standartaligment)
        row4 = Row([self.InputA], alignment=self.Standartaligment)
        row5 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
        row6 = Row([self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)
        # row7 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
        # row8 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
        # row9 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
        # row10 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
        # row11 = Row([self.ChoosePodTemaDropdownGener], alignment=self.Standartaligment)
-
        body = Column([Row([Text('Расширенная генерация')]),
            row1,
            row2,
            row3,
            row4,
            row5,
            row6,
            # row7,
            # row8,
            # row9,
            # row10,
            # row11,
        ])
        return body


    def get_body(self, e):
        if isinstance(e, str):  # Обработка вызова из класса
            if e == 'Быстрая генерация':
                return self.get_Setup()
            elif e == 'Расширенная генерация':
                return self.get_Setup2()
        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_Setup()
            elif e.control.selected_index == 1:
                return self.get_Setup2()


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
        page.window_width = 730
        page.window_height = 860
        Window.rebuild('Быстрая генерация')
        page.window_center()


    app(target=main)