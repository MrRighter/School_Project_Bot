from random import *
from math import *
from fpdf import FPDF

first_task_var_balist = ['Шар бросили со скоростью ', "Шарик бросили вниз со скоростью ",
                         "Катя бросила металический шар со скоростью "]
second_task_var_balist = ['с высоты ', "который находился на высоте ", "с дома высотой "]
first_num_task = ['1 ', '2 ', '3 ', '4 ', '5 ']
second_num_task = ['1 ', '2 ', '3 ', '4 ', '5 ']
quest_task = ['Какое расстояние прошел шар?', "Сколько метров пролетел шар?", "Определите время полета этого шара.",
              "Найти время падения шара.", "На каком расстоянии находится шар от начальной координаты?"]
pdf = FPDF()
pdf.add_font('Arial', '', 'D:\Python\Arial.ttf', uni=True)


class tasks:

    def __init__(self, theme):
        self.theme = theme
        pdf.add_page()
        pdf.set_font('Arial', size=20)
        if self.theme == 'баллистика':
            st = choice(first_task_var_balist)
            f = choice(first_num_task)
            st += f + 'м/с '
            st += choice(second_task_var_balist)
            s = choice(second_num_task)
            st += s + 'м. '
            st += choice(quest_task)
            pdf.multi_cell(200, 10, txt=st)
            t = sqrt((int(s) * 2) / 9.8)
            if 'время' in st:
                pdf.multi_cell(200, 10, txt=f'Ответ: {round(t, 2)} сек', align='L')
            else:
                pdf.multi_cell(200, 10, txt=f'Ответ: {round(int(f) * t, 2)} м.', align='L')
            pdf.output('pdff.pdf')


theme = tasks(input('Введите тему задания '))
