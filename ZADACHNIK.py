from os import getcwd
from sys import platform
from Drow import Drow
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


def get_buttons():
    But_list = []
    f = open('./But_list.txt')
    for row in f:
        But_list.append(row.split(' ')[0])
    return But_list


But_list = get_buttons()


class Interface():
    "Этот класс для..."

    def __init__(self, page):
        self.splitter = splitter
        self.page = page
        self.selected_index = 0
        self.InputA = TextField(value='1', width=200, label="Количество задач", visible=False)
        self.ViewGraphs = Checkbox(label="Выбрать подтему?", value=False, on_change=self.Obrab_ViewGraphs,
                                   visible=False)
        self.PDFPROVERKA = Checkbox(label="PDF", value=False, visible=False)
        self.TXTPROVERKA = Checkbox(label="TXT", value=True, visible=False)
        self.Standartaligment = MainAxisAlignment.START
        self.ChooseFunction = Dropdown(
            label="Выберите предмет",
            data='Type',
            # value='Физика',
            on_change=self.ChooseTema,
            options=[
                dropdown.Option("Физика"),
                dropdown.Option("Математика"),
            ],
        )
        self.ChooseTemaDropdown = Dropdown(
            label="Выберите тему",
            data='Type',
            # value='Механика',
            visible=False,
            on_change=self.SetChoosePodTemaDropdown,
        )
        self.ChoosePodTemaDropdown = Dropdown(
            label="Выберите подтему",
            data='Type',
            value='Механика',
            visible=False,
            # on_change=self.ChooseTema,
        )
        self.Choose_KR_SR_Text = Text('Самостоятельная работа')
        self.ON_OFF_Radio = RadioGroup(
            on_change=self.ObrabON_OFF_Radio,
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
        self.StartPicNumber = 0
        self.DisplayedPic = 260
        self.Name = TextField(visible=False)
        self.AlertIndex = 0
        self.JesusButton = IconButton(icon=icons.ACCESSIBILITY_SHARP, icon_color='red', on_click=self.Alert)

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

    def Alert(self, e):
        self.AlertIndex += 1
        self.page.dialog = AlertDialog(
            modal=True,
            title=Text(f'{self.AlertIndex}'),
            actions=[self.JesusButton])
        self.page.dialog.open = True
        self.page.update()

    def Obrab_ViewGraphs(self, e):
        if e.control.value:
            self.ChoosePodTemaDropdown.visible = True
        else:
            self.ChoosePodTemaDropdown.visible = False
        self.ChoosePodTemaDropdown.update()

    def ObrabON_OFF_Radio(self, e):
        if e.control.value == 'СР':
            self.Choose_KR_SR_Text.value = 'Самостоятельная работа'
        else:
            self.Choose_KR_SR_Text.value = 'Контрольная работа'
        self.Choose_KR_SR_Text.update()

    def DrowSimplePlot(self, e):
        print('Создай меня')
        print(self.TXTPROVERKA.value)
        print(self.PDFPROVERKA.value)
        pass

    def rebuildSetup(self, e):
        self.rebuild('Setup')
        return 'Setup'

    def get_menu(self):
        rail = NavigationRail(
            selected_index=self.selected_index,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=icons.CREATE, text="Run", on_click=self.DrowSimplePlot),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon_content=Icon(icons.SETTINGS),
                    selected_icon=icons.SETTINGS,
                    label="Setup"
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.BOOKMARK_BORDER),
                    selected_icon_content=Icon(icons.BOOKMARK),
                    label="Buttons",
                ),
            ],
            on_change=self.rebuild,
        )
        return rail

    def get_Setup(self):
        row2 = Row([self.ChooseFunction, self.DrowButton], alignment=self.Standartaligment)
        row4 = Row([self.Label, self.ON_OFF_Radio], alignment=self.Standartaligment)
        row5 = Row([self.ChooseTemaDropdown, self.ViewGraphs], alignment=self.Standartaligment)
        row6 = Row([self.ChoosePodTemaDropdown], alignment=self.Standartaligment)
        row7 = Row([self.InputA, self.TXTPROVERKA, self.PDFPROVERKA], alignment=self.Standartaligment)
        body = Column([
            row4,
            row2,
            row5,
            row6,
            row7

        ])
        return body

    def Plus(self, e):
        self.StartPicNumber += self.DisplayedPic
        self.rebuild('Buttons')

    def Minus(self, e):
        if self.StartPicNumber >= self.DisplayedPic:
            self.StartPicNumber -= self.DisplayedPic
            self.rebuild('Buttons')

    def Set_StartPicNumber(self, e):
        self.StartPicNumber = (int(e.control.value) // self.DisplayedPic) * self.DisplayedPic
        self.rebuild('Buttons')

    def PrintName(self, e):
        self.Name.value = e.control.icon
        self.Name.visible = True
        self.Name.update()

    def get_Buttons(self):
        row0 = Row([ElevatedButton('Left', on_click=self.Minus),
                    ElevatedButton('Right', on_click=self.Plus),
                    TextField(value=self.StartPicNumber, on_submit=self.Set_StartPicNumber),
                    self.Name])
        row1 = Row([], alignment=self.Standartaligment)
        row2 = Row([], alignment=self.Standartaligment)
        row3 = Row([], alignment=self.Standartaligment)
        row4 = Row([], alignment=self.Standartaligment)
        row5 = Row([], alignment=self.Standartaligment)
        row6 = Row([], alignment=self.Standartaligment)
        row7 = Row([], alignment=self.Standartaligment)
        row8 = Row([], alignment=self.Standartaligment)
        row9 = Row([], alignment=self.Standartaligment)
        row10 = Row([], alignment=self.Standartaligment)
        row11 = Row([], alignment=self.Standartaligment)
        row12 = Row([], alignment=self.Standartaligment)
        for button in But_list[int(self.StartPicNumber):int(self.StartPicNumber) + 20]:
            row1.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[20 + int(self.StartPicNumber):int(self.StartPicNumber) + 40]:
            row2.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[40 + int(self.StartPicNumber):int(self.StartPicNumber) + 60]:
            row3.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[60 + int(self.StartPicNumber):int(self.StartPicNumber) + 80]:
            row4.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[80 + int(self.StartPicNumber):int(self.StartPicNumber) + 100]:
            row5.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[100 + int(self.StartPicNumber):int(self.StartPicNumber) + 120]:
            row6.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[120 + int(self.StartPicNumber):int(self.StartPicNumber) + 140]:
            row7.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[140 + int(self.StartPicNumber):int(self.StartPicNumber) + 160]:
            row8.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[160 + int(self.StartPicNumber):int(self.StartPicNumber) + 180]:
            row9.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[180 + int(self.StartPicNumber):int(self.StartPicNumber) + 200]:
            row10.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[220 + int(self.StartPicNumber):int(self.StartPicNumber) + 240]:
            row11.controls.append(IconButton(icon=button, on_click=self.PrintName))
        for button in But_list[240 + int(self.StartPicNumber):int(self.StartPicNumber) + 260]:
            row12.controls.append(IconButton(icon=button, on_click=self.PrintName))

        body = Column([Row([Text('Setup')]),
                       row0,
                       row1,
                       row2,
                       row3,
                       row4,
                       row5,
                       row6,
                       row7,
                       row8,
                       row9,
                       row10,
                       row11,
                       row12,
                       ])
        return body

    def get_body(self, e):
        if isinstance(e, str):  # Обработка вызова из класса
            if e == 'Setup':
                return self.get_Setup()
            elif e == 'Buttons':
                return self.get_Buttons()
        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_Setup()
            elif e.control.selected_index == 1:
                return self.get_Buttons()

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
        Window.rebuild('Setup')
        page.window_center()


    app(target=main)
