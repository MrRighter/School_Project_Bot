from os import getcwd
from sys import platform
from flet import (
    Page,
    Row,
    Text,
    icons,
    Dropdown,
    MainAxisAlignment,
    dropdown,
    app,
    VerticalDivider,
    Column,
    FloatingActionButton,
    NavigationRail,
    NavigationRailLabelType,
    Icon,
    NavigationRailDestination,
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
        self.Standartaligment = MainAxisAlignment.START
        self.Label1 = Text('Что вас привлекает в спорте')
        self.Vopros1 = Dropdown(
            label="Вопрос1",
            on_change=self.Otvet1,
            width=400,
            options=[
                dropdown.Option("Возможность активно провести время"),
                dropdown.Option("Возможность поработать в команде"),
                dropdown.Option("Возможность потренировать мышцы"),
                dropdown.Option("Возможность проанализировать стратегию противника"),
            ],
        )
        self.Label2 = Text('', visible=False)
        self.Vopros2 = Dropdown(
            label="Вопрос2",
            width=400,
            on_change=self.Otvet2,
            visible=False,
        )

    def get_menu(self):

        rail = NavigationRail(
            selected_index=self.selected_index,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=icons.CREATE, text="Подтвердить", on_click=self.Podtverdit,
                                         visible=False, ),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon_content=Icon(icons.SETTINGS),
                    selected_icon=icons.SETTINGS,
                    label="Опрос"
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.BOOKMARK_BORDER),
                    selected_icon_content=Icon(icons.BOOKMARK),
                    label="Опрос2",
                ),
            ],
            on_change=self.rebuild,
        )
        return rail

    def Podtverdit(self, e):
        pass
    def Otvet1(self,e):
        self.Vopros2.options = []
        if e.control.value == 'Возможность активно провести время':
            self.Label2.value = 'Что в тренировке важно для вас?'
            self.Vopros2.options.append(dropdown.Option("Бег"))
            self.Vopros2.options.append(dropdown.Option("Прыжки"))
            self.Vopros2.options.append(dropdown.Option("Катание на лыжах"))
            self.Vopros2.options.append(dropdown.Option("Зимние виды спорта"))
        elif e.control.value == 'Возможность поработать в команде':
            self.Label2.value = 'Какой спорт вам ближе?'
            self.Vopros2.options.append(dropdown.Option("Футбол"))
            self.Vopros2.options.append(dropdown.Option("Баскетбол"))
            self.Vopros2.options.append(dropdown.Option("Гандбол"))
            self.Vopros2.options.append(dropdown.Option("Волейбол"))
            self.Vopros2.options.append(dropdown.Option("Базовые упражнения"))
        elif e.control.value == 'Возможность потренировать мышцы':
            self.Label2.value = 'Какие группы мышц вы хотите тренировать?'
            self.Vopros2.options.append(dropdown.Option("Мышцы рук"))
            self.Vopros2.options.append(dropdown.Option("Мышцы ног"))
            self.Vopros2.options.append(dropdown.Option("Мышцы спины"))
            self.Vopros2.options.append(dropdown.Option("Мышцы пресса"))
            self.Vopros2.options.append(dropdown.Option("Базовые упражнения"))
        elif e.control.value == 'Возможность проанализировать стратегию противника':
            self.Label2.value = 'Пробовали играть в эти игры?'
            self.Vopros2.options.append(dropdown.Option("Шашки"))
            self.Vopros2.options.append(dropdown.Option("Шахматы"))
            self.Vopros2.options.append(dropdown.Option("Покер"))
            self.Vopros2.options.append(dropdown.Option("Двадцать одно"))
        self.Vopros2.visible = True
        self.Label2.visible = True
        self.Vopros2.update()
        self.Label2.update()
    def Otvet2(self,e):
        pass

    def rebuildSetup(self, e):
        self.rebuild('Setup')
        return 'Setup'

    def get_Opros(self):
        row0 = Row([self.Label1], alignment=self.Standartaligment)
        row1 = Row([self.Vopros1, ], alignment=self.Standartaligment)
        row1_5 = Row([self.Label2], alignment=self.Standartaligment)
        row2 = Row([self.Vopros2], alignment=self.Standartaligment)
        body = Column([Row([Text('Setup')]),
                       row0,
                       row1,
                       row1_5,
                       row2,
                       ])
        return body

    def get_Opros2(self):
        body = Column([Row([Text('Опрос2')])
                       ])
        return body

    def get_body(self, e):
        if isinstance(e, str):  # Обработка вызова из класса
            if e == 'Опрос':
                return self.get_Opros()
            elif e == 'Опрос2':
                return self.get_Opros2()
        elif isinstance(e.control, NavigationRail):  # Обработка вызова из Навигационного меню
            if e.control.selected_index == 0:
                return self.get_Opros()
            elif e.control.selected_index == 1:
                return self.get_Opros2()

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
        Window.rebuild('Опрос')
        page.window_center()
        page.window_width = 1400
        page.window_height = 800


    app(target=main)
