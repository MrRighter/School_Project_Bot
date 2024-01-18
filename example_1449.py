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
        self.InputA = TextField(value='1', width=100, label="Input A")
        self.ViewGraphs = Checkbox(label="Хочу посмотреть графики", value=True, on_change=self.Obrab_ViewGraphs)
        self.Standartaligment = MainAxisAlignment.START
        self.Choose_Predmet = Dropdown(
            label="Предмет",
            data='Type',
            value='Физика',
            on_change=self.set_Themes_List,
            options=[
                dropdown.Option("Физика"),
            ],
        )
        self.Themes_List = []
        self.Choose_Tema = Dropdown(
            label="Тема",
            data='Type',
            value='Физика',
            on_change=self.rebuildSetup,
            options=self.Themes_List,
        )
        self.ON_OFF_Radio = RadioGroup(
            on_change=self.ObrabON_OFF_Radio,
            value='СР',
            content=Row(
                [
                 Radio(value="КР", label="Контрольная работа"),
                 Radio(value="СР", label="Текстовые задачи"),
                 ]
            )
        )
        self.DrowButton = ElevatedButton('Drow', on_click=self.DrowSimplePlot)
        self.DrowIconButton = IconButton(icon=icons.TASK_ALT_OUTLINED, on_click=self.DrowSimplePlot, icon_color='green')
        self.StartPicNumber = 0
        self.DisplayedPic = 260
        self.Name = TextField(visible=False)
        self.AlertIndex = 0
        self.JesusButton = IconButton(icon=icons.ACCESSIBILITY_SHARP,icon_color='red',on_click=self.Alert)


    def set_Themes_List(self, e):
        print(e.control)
        if e.control.value == "Физика":
            self.Themes_List = ["Равноускорегное", "2"]
        print(self.Themes_List)
        self.Choose_Tema.options = self.Themes_List
        self.Choose_Tema.update()


    def Alert(self,e):
        self.AlertIndex += 1
        self.page.dialog = AlertDialog(
            modal=True,
            title=Text(f'{self.AlertIndex}'),
            actions=[self.JesusButton])
        self.page.dialog.open = True
        self.page.update()
    def Obrab_ViewGraphs(self, e):
        if e.control.value:
            self.ChooseFunction.visible = True
            self.InputA.visible = True
            self.DrowButton.visible = True
            self.DrowIconButton.visible = True
            self.Label.visible = True
            self.ON_OFF_Radio.visible = True
        else:
            self.ChooseFunction.visible = False
            self.InputA.visible = False
            self.DrowButton.visible = False
            self.DrowIconButton.visible = False
            self.Label.visible = False
            self.ON_OFF_Radio.visible = False
        self.ChooseFunction.update()
        self.InputA.update()
        self.DrowButton.update()
        self.DrowIconButton.update()
        self.Label.update()
        self.ON_OFF_Radio.update()

    def ObrabON_OFF_Radio(self, e):
        if e.control.value == 'ON':
            self.Label.value = e.control.value
        else:
            self.Label.value = e.control.value
        self.Label.update()

    def DrowSimplePlot(self, e):
        drow = Drow(self)
        drow.DrowSimplePlot()

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

    def get_Home(self):
        row1 = Row([self.ON_OFF_Radio], alignment=self.Standartaligment)
        row2 = Row([self.Choose_Predmet, self.JesusButton], alignment=self.Standartaligment)
        row3 = Row([self.Choose_Tema], alignment=self.Standartaligment)
        row4 = Row([self.ViewGraphs, self.InputA, self.DrowButton, self.DrowIconButton], alignment=self.Standartaligment)
        body = Column([
                       row1,
                       row2,
                       row3,
                       row4,
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
            if e == 'Home':
                return self.get_Home()
            elif e == 'Settings':
                return self.get_Buttons()
        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_Home()
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
        Window.rebuild('Home')
        page.window_center()
        page.window_width = 1400
        page.window_height = 800


    app(target=main)
