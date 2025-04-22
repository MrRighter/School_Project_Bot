import re
import os
import sys
import flet as ft
from flet import *

import Final_Executing_func as task_generator


class TaskGeneratorApp:
    """
    Unified Task Generator App with Fast and Constructor modes.
    """

    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Генератор учебных заданий"
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_resizable = False

        # Subjects, themes, and subthemes
        self.subjects = {
            "Физика": {
                "Кинематика": ["Равномерное движение", "Равноускоренное движение"],
                "Баллистика": ["Свободное падение", "Баллистическое движение"],
            }
        }

        # Current view: 0=Fast, 1=Constructor
        self.selected_index = 0

        # Build UI
        self._init_components()
        self._layout()
        self.page.update()

    def _init_components(self):
        # Navigation
        self.nav = NavigationRail(
            selected_index=self.selected_index,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            on_change=self._on_nav_change,
            destinations=[
                NavigationRailDestination(icon=icons.BOLT_OUTLINED, selected_icon=icons.BOLT, label="Быстрая"),
                NavigationRailDestination(icon=icons.BUILD_OUTLINED, selected_icon=icons.BUILD, label="Конструктор"),
            ],
        )

        # Common controls
        self.work_type_radio = RadioGroup(
            content=Row([
                Radio(value="СР", label="Самостоятельная"),
                Radio(value="КР", label="Контрольная"),
            ]),
            value="СР",
        )

        # Fast mode controls with fixed widths
        self.fast_subject = Dropdown(label="Предмет", options=[dropdown.Option(s) for s in self.subjects], width=150)
        self.fast_theme = Dropdown(label="Раздел", options=[], width=150, visible=False)
        self.fast_subtheme = Dropdown(label="Тема", options=[], width=260, visible=False)
        self.fast_count = TextField(label="Количество задач", value="1", keyboard_type=KeyboardType.NUMBER, width=100)
        self.fast_button = ElevatedButton("Сгенерировать", on_click=self._generate_fast, width=180)

        # Constructor mode controls with fixed widths
        self.const_count = TextField(label="Количество заданий", value="1", keyboard_type=KeyboardType.NUMBER, width=100)
        self.const_tasks_container = Column(scroll=ScrollMode.AUTO, spacing=10)
        self.const_button = ElevatedButton("Сгенерировать", on_click=self._generate_constructor, width=180)

        # Output
        self.output = Container(
            content=Column([Text("", selectable=True)], scroll=ScrollMode.AUTO),
            border=border.all(1, colors.GREY_400), padding=10, height=700, width=500
        )

        # Event bindings
        self.fast_subject.on_change = self._on_fast_subject_change
        self.fast_theme.on_change = self._on_fast_theme_change
        self.fast_count.on_change = self._sanitize_numeric
        self.const_count.on_change = self._on_const_count_change

    def _layout(self):
        # Main layout based on selected_index
        content = self._build_fast_view() if self.selected_index == 0 else self._build_constructor_view()
        # Footer label
        footer = Container(
            Text("Made in GoidaLABS", style=TextStyle(size=12, weight=FontWeight.BOLD, italic=True)),
            alignment=alignment.bottom_right,
            padding=5
        )
        self.page.clean()
        self.page.add(
            Row([
                self.nav,
                VerticalDivider(width=1),
                Column([content], expand=True),
                VerticalDivider(width=1),
                self.output,
            ], expand=True, vertical_alignment=CrossAxisAlignment.START),
            footer
        )

    def _build_fast_view(self):
        return Column([
            Text("Быстрая генерация", style=TextStyle(size=20, weight=FontWeight.BOLD)),
            Row([Text("Тип работы:", width=100), self.work_type_radio]),
            Row([self.fast_subject, self.fast_theme, self.fast_subtheme]),
            self.fast_count,
            self.fast_button,
        ], spacing=15, expand=True)

    def _build_constructor_view(self):
        return Column([
            Text("Конструктор заданий", style=TextStyle(size=20, weight=FontWeight.BOLD)),
            self.const_count,
            self.const_tasks_container,
            self.const_button,
        ], spacing=15, expand=True)

    def _on_nav_change(self, e):
        self.selected_index = e.control.selected_index
        self._layout()

    def _sanitize_numeric(self, e):
        e.control.value = re.sub(r"\D", "", e.control.value)
        e.control.update()

    # Fast mode handlers
    def _on_fast_subject_change(self, e):
        sub = e.control.value
        if sub:
            themes = list(self.subjects[sub].keys())
            self.fast_theme.options = [dropdown.Option(t) for t in themes]
            self.fast_theme.value = None
            self.fast_theme.visible = True
            self.fast_subtheme.visible = False

            # Обновляем оба списка и страницу
            self.fast_theme.update()
            self.fast_subtheme.update()
            self.page.update()

    def _on_fast_theme_change(self, e):
        tema = e.control.value
        if tema:
            subs = self.subjects[self.fast_subject.value][tema]
            self.fast_subtheme.options = [dropdown.Option(st) for st in subs]
            self.fast_subtheme.value = None
            self.fast_subtheme.visible = True

            # Обновляем списки и страницу
            self.fast_theme.update()
            self.fast_subtheme.update()
            self.page.update()

    def _generate_fast(self, e):
        if not all([self.fast_subject.value, self.fast_theme.value, self.fast_subtheme.value, self.fast_count.value]):
            return self._show_error("Заполните все обязательные поля!")
        try:
            cfg = {
                "Subject": self.fast_subject.value,
                "Theme": self.fast_theme.value,
                "Theme_section": self.fast_subtheme.value,
                "N": int(self.fast_count.value),
                "Type": self.work_type_radio.value,
            }
            result = task_generator.GetTaskText(cfg)
            self._set_output(result)
        except Exception as ex:
            self._show_error(f"Ошибка: {ex}")

    # Constructor mode handlers
    def _on_const_count_change(self, e):
        self._sanitize_numeric(e)
        val = int(e.control.value) if e.control.value else 0
        self.const_tasks_container.controls.clear()
        if val < 1:
            return
        for i in range(val):
            subj = Dropdown(label=f"Предмет {i+1}", options=[dropdown.Option(s) for s in self.subjects], value="Физика", width=150)
            them = Dropdown(label=f"Раздел {i+1}", options=[dropdown.Option(t) for t in self.subjects["Физика"]], width=150)
            subth = Dropdown(label=f"Тема {i+1}", width=260)
            them.on_change = lambda e, subth=subth: self._populate_subthemes(e, subth)
            self.const_tasks_container.controls.append(Row([subj, them, subth], spacing=10))
        self.const_tasks_container.update()

    def _populate_subthemes(self, e, subth_dropdown):
        tema = e.control.value
        subs = self.subjects["Физика"].get(tema, [])
        subth_dropdown.options = [dropdown.Option(st) for st in subs]
        subth_dropdown.update()

    def _generate_constructor(self, e):
        results = []
        try:
            for row in self.const_tasks_container.controls:
                subj, them, subth = row.controls
                if not all([subj.value, them.value, subth.value]):
                    raise ValueError("Заполните все поля задания")
                cfg = {"Subject": subj.value, "Theme": them.value, "Theme_section": subth.value, "N": 1, "Type": self.work_type_radio.value}
                results.append(task_generator.GetTaskText(cfg))
            self._set_output("\n\n".join(results))
        except Exception as ex:
            self._show_error(str(ex))

    def _set_output(self, text: str):
        self.output.content.controls[0].value = text
        self.output.update()

    def _show_error(self, msg: str):
        self.page.snack_bar = SnackBar(content=Text(msg), open=True)
        self.page.update()


if __name__ == "__main__":
    ft.app(target=TaskGeneratorApp)
