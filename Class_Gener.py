from random import *
from math import *

from sympy import symbols, Eq, solve


sign_args = ['+', '-']

speed_var = [i for i in range(5, 36)]
distance_var = [i for i in range(50, 251)]
time_var = [i for i in range(5, 46)]
deg_var = ['30', '45', '60', '90']

e_time_var = [i for i in range(1, 11)]
acceleration_var = [i for i in range(2, 11)]
first_speed_var = [i for i in range(2, 11)]
second_speed_var = [i for i in range(15, 36)]

ball_speed_var = [i for i in range(1, 6)]
ball_universal_var = [i for i in range(1, 11)]

material_point_args = [i for i in range(1, 21)]


class TaskGenerator():
    def questions_for_kr_kinematics(self):
        return choice(["Что изучает механика?", "Дайте определение механического движения. Приведите примеры.", "Какое движение называется поступательным?",
            "В чем заключается основная задача механики?", "Что такое тело отсчета?", "Что такое система отсчета? Зачем в ней нужны часы?",
            "Зависит ли траектория движения тела от выбора системы отсчёта? Примеры.", "Дайте определение материальной точки.",
            "Что такое путь? Какова его единица в СИ?", "Почему, зная путь не всегда можно определить положение тела?",
            "Дайте определение перемещения. Каким символом его обозначают?", "При каких условиях модуль перемещения равен пройденному пути?",
            "Запишите формулу определения положения тела в пространстве через проекции.", "Какое движение называется прямолинейным равномерным?",
            "Дайте характеристику скорости равномерного прямолинейного движения.", "Какой вид имеет график зависимости скорости от времени при равномерном прямолинейном движении?",
            "Как вычислить перемещение тела, если известны скорость и время движения тела?", "Каков геометрический смысл перемещения?",
            "Запишите уравнение координаты при равномерном прямолинейном движении.", "Что понимают под относительностью механического движения?",
            "Как угол наклона графика координаты равномерного прямолинейного движения зависит от скорости движения тела?",
            "Какие характеристики механического движения изменяются при переходе от одной системы отсчета к другой?",
            "Какие характеристики механического движения остаются неизменными при переходе от одной системы отсчёта к другой?",
            "Всегда ли в качестве неподвижной системы отсчёта нужно выбирать ту, которая связана с Землей? Приведите примеры, подтверждающие ваше утверждение.",
            "Как направлен вектор мгновенной скорости движения тела?", "Какое движение называют равноускоренным прямолинейным?",
            "Дайте определение ускорения движения тела.", "Как движется тело, если направление его ускорения совпадает с направлением скорости движения? Противоположно скорости движения тела?",
            "С помощью каких формул можно вычислить проекцию перемещения при равноускоренном прямолинейном движении?"
            "Что представляет собой график зависимости проекции перемещения от времени?", "Какое движение называют свободным падением тел?",
            "Опишите опыты, с помощью которых можно установить, что ускорение свободного падения не зависит от массы тела.",
            "Как направлено ускорение свободного падения и чему оно равно?", "Какое движение называется криволинейным?",
            "Как и кем было доказано, что при отсутствии сопротивления воздуха все тела тела падают на поверхность Земли с одинаковой скоростью?",
            "Запишите формулу для расчета проекции скорости при свободном падении тел.", "Запишите формулу для расчета проекции перемещения при свободном падении тел",
            "Может ли тело двигаться по криволинейной траектории без ускорения? Доказать.", "Какое движение называют равномерным движением по окружности?",
            "Как направлен вектор мгновенной скорости при криволинейном движении?", "Как определить линейную скорость равномерного движения тела по окружности?",
            "Какие физические величины характеризуют скорость движения тела по окружности?", "Каким соотношением связаны угловая и линейная скорости?",
            "Дать определение линейной скорости. Каким символом ее обозначают? Какова ее единица в СИ?", "По какой формуле определяют центростремительное ускорение тела?",
            "Дайте определение частоты обращения тела по окружности. Какова ее единица в СИ?", "Дайте определение периода обращения тела. Какова его единица в СИ?",
            "Дайте определение угловой скорости движения тела по окружности. Какова ее единица в СИ?"])


    def tests_for_kr_kinematics(self):
        return choice(["Расстояние между начальной и конечной точками - это:\nА) путь\nБ) перемещение\nВ) смещение\nГ) траектория",
            "В каком из следующих случаев движение тела нельзя рассматривать как движение материальной точки?\nА) Движение Земли вокруг Солнца\n"
            "Б) Движение спутника вокруг Земли\nВ) Полет самолета из Владивостока в Москву\nГ) Вращение детали, обрабатываемой на станке",
            "Какие из перечисленных величин являются скалярными?\nА) перемещение\nБ) путь\nВ) скорость",
            "Два автомобиля движутся по прямому шоссе в одном направлении. Если направить ось ОХ вдоль направления движения тел по шоссе, тогда какими будут проекции скоростей автомобилей на ось ОХ?\n"
            "А) обе положительные\nБ) обе отрицательные\nВ) первого - положительная, второго - отрицательная\nГ) первого - отрицательная, второго – положительная",
            "Ускорение характеризует изменение вектора скорости\nА) по величине и направлению\nБ) по направлению\nВ) по величине",
            "Велосипедист движется из точки А велотрека в точку В по кривой АВ. Назовите физическую величину, которую изображает вектор АВ.\n"
            "А) путь\nБ) перемещение\nВ) скорость", "Какие из перечисленных ниже величин являются векторными:\n1) путь\n2) перемещение\n3) скорость",
            "Почему при расчетах можно считать Луну материальной точкой (относительно Земли)?\nА) Луна - шар\nБ) Луна - спутник Земли\nВ) Масса Луны меньше массы Земли\nГ) Расстояние от Земли до Луны во много раз больше радиуса Луны.",
            "Физические величины бывают векторными и скалярными. Какая физическая величина из перечисленных является скалярной?\nА) ускорение\nБ) время\nВ) скорость\nГ) перемещение",
            "Два автомобиля движутся по прямому шоссе в противоположных направлении. Если направить ось ОХ вдоль направления движения первого автомобиля по шоссе, тогда какими будут проекции скоростей автомобилей на ось ОХ?\n"
            "А) обе положительные\nБ) обе отрицательные\nВ) первого - положительная, второго - отрицательная\nГ) первого - отрицательная, второго – положительная",
            "Автомобиль трогается с места и движется с возрастающей скоростью прямолинейно. Какое направление имеет вектор ускорения?\nА) ускорение равно 0\nБ) направлен против движения автомобиля\nВ) направлен в сторону движения автомобиля",
            "Материальная точка-это тело, размерами которого . . .\nА) в данных условиях можно пренебречь\nБ) нельзя пренебречь\nВ) нет правильного ответа",
            "Длина траектории – это  . . .\nА) путь\nБ) перемещение\nВ) траектория", "Линия, вдоль которой движется тело, называется . . .\nА) перемещением\nБ) путем\nВ) траекторией",
            "Вид механического движения, когда все точки тела движутся одинаково:\nА) колебательное\nБ) вращательное\nВ) поступательное",
            "Вертолет равномерно поднимается вертикально вверх. Какова траектория движения точки на конце лопасти винта вертолета в системе отсчета, связанной с корпусом вертолета?\nА) окружность\nБ) винтовая линия\nВ) прямая",
            "Искусственный спутник обращается вокруг Земли по круговой орбите радиусом R с периодом обращения 1 сут. Каковы путь и перемещение спутника за 1 сут?\nА) путь и перемещение одинаковы и равны 0\nБ) путь и перемещение одинаковы и равны 2пR\nВ) путь 2пR, перемещение 0",
            "При криволинейном движении мгновенная скорость материальной точки в каждой точке траектории направлена:\nА) по траектории\nБ) по касательной к траектории в этой точке\nВ) по радиусу кривизны траектории."])


    def phis_kr_mechanics(self):
        self.func = choice([self.uniform_motion_first, self.uniform_motion_second, self.uniform_motion_third, self.uniform_motion_fourth,
                            self.uniform_motion_fifth, self.uniform_motion_sixth, self.uniform_motion_seventh,self.uniform_motion_eighth,
                            self.uniform_motion_ninth,
                            self.equiaxed_motion_first, self.equiaxed_motion_second, self.equiaxed_motion_third, self.equiaxed_motion_fourth,
                            self.equiaxed_motion_fifth, self.equiaxed_motion_sixth, self.equiaxed_motion_seventh, self.equiaxed_motion_eighth,
                            self.equiaxed_motion_ninth, self.equiaxed_motion_tenth, self.equiaxed_motion_eleventh, self.equiaxed_motion_twelfth,
                            self.equiaxed_motion_thirteenth, self.equiaxed_motion_fourteenth, self.equiaxed_motion_fifteenth,
                            self.equiaxed_motion_sixteenth, self.equiaxed_motion_seventeenth, self.equiaxed_motion_eighteenth,
                            self.equiaxed_motion_nineteenth, self.equiaxed_motion_twentieth, self.equiaxed_motion_twenty_one,
                            self.equiaxed_motion_twenty_two,
                            self.ballistics_first, self.ballistics_corner_first, self.ballistics_corner_second,
                            self.ballistics_corner_third])
        return self.func()


    def phis_kr_kinematics(self):
        self.func = choice([self.uniform_motion_first, self.uniform_motion_second, self.uniform_motion_third, self.uniform_motion_fourth,
                            self.uniform_motion_fifth, self.uniform_motion_sixth, self.uniform_motion_seventh,self.uniform_motion_eighth,
                            self.uniform_motion_ninth,
                            self.equiaxed_motion_first, self.equiaxed_motion_second, self.equiaxed_motion_third, self.equiaxed_motion_fourth,
                            self.equiaxed_motion_fifth, self.equiaxed_motion_sixth, self.equiaxed_motion_seventh, self.equiaxed_motion_eighth,
                            self.equiaxed_motion_ninth, self.equiaxed_motion_tenth, self.equiaxed_motion_eleventh, self.equiaxed_motion_twelfth,
                            self.equiaxed_motion_thirteenth, self.equiaxed_motion_fourteenth, self.equiaxed_motion_fifteenth,
                            self.equiaxed_motion_sixteenth, self.equiaxed_motion_seventeenth, self.equiaxed_motion_eighteenth,
                            self.equiaxed_motion_nineteenth, self.equiaxed_motion_twentieth, self.equiaxed_motion_twenty_one,
                            self.equiaxed_motion_twenty_two])
        return self.func()


    def phis_kr_ballistics(self):
        self.func = choice([self.ballistics_first, self.ballistics_corner_first, self.ballistics_corner_second,
                            self.ballistics_corner_third])
        return self.func()


    def uniform_motion(self):
        self.func = choice([self.uniform_motion_first, self.uniform_motion_second, self.uniform_motion_third, self.uniform_motion_fourth,
                            self.uniform_motion_fifth, self.uniform_motion_sixth, self.uniform_motion_seventh,self.uniform_motion_eighth,
                            self.uniform_motion_ninth])
        return self.func()


    def equiaxed_motion(self):
        self.func = choice([self.equiaxed_motion_first, self.equiaxed_motion_second, self.equiaxed_motion_third, self.equiaxed_motion_fourth,
                            self.equiaxed_motion_fifth, self.equiaxed_motion_sixth, self.equiaxed_motion_seventh, self.equiaxed_motion_eighth,
                            self.equiaxed_motion_ninth, self.equiaxed_motion_tenth, self.equiaxed_motion_eleventh, self.equiaxed_motion_twelfth,
                            self.equiaxed_motion_thirteenth, self.equiaxed_motion_fourteenth, self.equiaxed_motion_fifteenth,
                            self.equiaxed_motion_sixteenth, self.equiaxed_motion_seventeenth, self.equiaxed_motion_eighteenth,
                            self.equiaxed_motion_nineteenth, self.equiaxed_motion_twentieth, self.equiaxed_motion_twenty_one,
                            self.equiaxed_motion_twenty_two])
        return self.func()


    def ballistics_motion(self):
        self.func = choice([self.ballistics_first])
        return self.func()


    def ballistics_corner_motion(self):
        self.func = choice([self.ballistics_corner_first, self.ballistics_corner_second, self.ballistics_corner_third])
        return self.func()


    def ballistics_first(self):
        first_task_var = ["Тело свободно падает с высоты ", "Высота падения одного тела равна "]
        second_task_var = ["м, одновременно с ним другое тело начинает падать с высоты ", "м. Высота падения другого тела равна "]
        third_task_var = 'м. Какой должна быть начальная скорость второго тела, чтобы оба тела упали одновременно? '
        fourth_task_var = 'Ускорение свободного падения взять 10 м/с². '
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        hight1 = str(choice(ball_universal_var))
        hight2 = str(choice(ball_universal_var))
        g = 10  # Ускорение свободного падения
        h1 = int(hight1)
        h2 = int(hight2)
        t = sqrt(2*h1/g)
        self.text_ans = [round(abs(h2 - h1)/t, 3)]
        self.text_que = choice(first_task_var) + hight1 + choice(second_task_var) + hight2 + third_task_var + fourth_task_var + choice(fifth_task_var)
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    # def ballistics_second(self):
    #     first_task_var = ["Сколько секунд будет падает тело, если за последние "]
    #     second_task_var = ["с, если с начала падения, оно пролетело "]
    #     third_task_var =  "м?"
    #     time = str(choice(ball_universal_var))
    #     hight = str(choice(ball_universal_var))
    #     self.text_que = choice(first_task_var) + time + choice(second_task_var) + hight + third_task_var
    #     self.text_ans = [round(sqrt(2 * int(hight) / 10), 3)]
    #     self.unit = ["с"]
    #     return [self.text_que, self.text_ans, self.unit]


    def ballistics_corner_first(self):
        first_task_var = ["Начальная скорость тела равна ", "Тело брошено с начальной скоростью ", "Тело начинает движение со скоростью "]
        second_task_var = ["м/с на некоторой высоте. Через какое время вектор скорости будет направлен по углом ",
                        "м/с. Считая, что оно находилось на некоторой высоте, определите время, когда вектор скорости будет направлен под углом "]
        third_task_var = "° к горизонту?"
        speed = str(choice(speed_var))
        deg = choice(deg_var)
        self.text_que = choice(first_task_var) + speed + choice(second_task_var) + deg + third_task_var
        self.text_ans = [round((2 * int(speed) * sin(int(deg))) / 10, 3)]
        self.unit = ['c']
        return [self.text_que, self.text_ans, self.unit]


    def ballistics_corner_second(self):
        first_task_var = ['Тело брошено горизонтально с высоты ', "Тело бросили с высоты "]
        second_task_var = ['м. Определите время полета тела, если оно упало на расстоянии ', "м. Сколько времени летело это тело, если дальность полета равна "]
        third_task_var = "м от места броска."
        hight = str(choice(ball_universal_var))
        distance = str(choice(distance_var))
        self.text_que = choice(first_task_var) + hight + choice(second_task_var) + distance + third_task_var
        self.text_ans = [round(sqrt((2 * int(hight)) / 10), 3)]
        self.unit = ['c']
        return [self.text_que, self.text_ans, self.unit]


    def ballistics_corner_third(self):
        first_task_var = ['Тело бросили под углом ', "Угол броска равен "]
        second_task_var = ['°. Оно падало ', "°. Оно упало за "]
        third_task_var = ['с. Начальная скорость равна ', 'с с начальной скоростью ']
        fourth_task_var = 'м/с. Найти дальность полета тела.'
        deg = choice(deg_var)
        time = str(choice(ball_universal_var))
        speed = str(choice(speed_var))
        self.text_que = choice(first_task_var) + deg + choice(second_task_var) + time + choice(third_task_var) + speed + fourth_task_var
        self.text_ans = [round(int(speed) * cos(int(deg)) * int(time), 3)]
        self.unit = ['м']
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_first(self):
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ", "Тело катится прямолинейно и равномерно со скоростью "]
        second_task_var = [" м/с. Пройденное расстояние равное ", " м/с. Оно переместилось на ", " м/с. Перемещение равно "]
        third_task_var = ' м. Найти время движения тела. '
        fourth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed = str(choice(speed_var))
        distance = str(choice(distance_var))
        self.text_que = choice(first_task_var) + speed + choice(second_task_var) + distance + third_task_var + choice(fourth_task_var)
        self.text_ans = [round(int(distance) / int(speed), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_second(self):
        first_task_var = ["Пройденное телом расстояние равно ", "Тело переместилось на "]
        second_task_var = [" м прямолинейно и равномерно со скоростью ", " м. Скорость тела равна ", " м. Скорость постоянная и равна "]
        third_task_var = ' м/с. Найти время движения тела. '
        fourth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        speed = str(choice(speed_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + speed + third_task_var + choice(fourth_task_var)
        self.text_ans = [round(int(distance) / int(speed), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_third(self):
        first_task_var = ["Тело прошло путь равный ", "Тело переместилось на "]
        second_task_var = [" м. Время движения тела равно ", " м за "]
        third_task_var = ' с. Найти скорость движения тела. '
        fourth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        time = str(choice(time_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + time + third_task_var + choice(fourth_task_var)
        self.text_ans = [round(int(distance) / int(time), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_fourth(self):
        first_task_var = ["Время движения тела равно ", "За "]
        second_task_var = [" с тело переместилось на ", " с перемещение тела равно "]
        third_task_var = ' м. Найти скорость движения тела. '
        fourth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        time = str(choice(time_var))
        self.text_que = choice(first_task_var) + time + choice(second_task_var) + distance + third_task_var + choice(fourth_task_var)
        self.text_ans = [round(int(distance) / int(time), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_fifth(self):
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ","Тело катится прямолинейно и равномерно со скоростью "]
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]
        third_task_var = ' с. Найти расстояние пройденное телом. '
        time = str(choice(time_var))
        speed = str(choice(speed_var))
        self.text_que = choice(first_task_var) + speed + choice(second_task_var) + time + third_task_var
        self.text_ans = [int(speed) * int(time)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_sixth(self):
        first_task_var = ["Время движения тела равно ", "За "]
        second_task_var = [" с. Двигаясь прямолинейно и равномерно со скоростью ", " с. Скорость тела равна "]
        third_task_var = ' м/с. Найти расстояние пройденное телом. '
        time = str(choice(time_var))
        speed = str(choice(speed_var))
        self.text_que = choice(first_task_var) + time + choice(second_task_var) + speed + third_task_var
        self.text_ans = [int(speed) * int(time)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_seventh(self):
        material_point_arg1 = choice(material_point_args)
        material_point_arg2 = choice(material_point_args)
        sign = choice(sign_args)
        first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]
        second_task_var = f"х = {str(material_point_arg1)} {sign} {str(material_point_arg2)}t. "
        final_task_var = 'С какой скоростью перемещается это тело?'
        self.text_que = choice(first_task_var) + second_task_var + final_task_var
        self.text_ans = [material_point_arg2 if sign == "+" else -material_point_arg2]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_eighth(self):
        material_point_arg1 = choice(material_point_args)
        material_point_arg2 = choice(material_point_args)
        material_point_arg3 = choice(material_point_args)
        material_point_arg4 = choice(material_point_args)
        sign1 = choice(sign_args)
        sign2 = choice(sign_args)
        self.text_ans1 = material_point_arg2
        self.text_ans2 = material_point_arg4
        self.text_ans11 = self.text_ans1 if sign1 == "+" else -material_point_arg2
        self.text_ans21 = self.text_ans2 if sign2 == "+" else -material_point_arg4
        self.unit1 = "м/с"
        self.unit2 = "м"
        if self.text_ans21 == self.text_ans11:
            self.text_ans21 += 1
            if sign2 == '+':
                self.text_ans2 += 1
            else:
                self.text_ans2 -= 1
        first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]
        second_task_var = f"х1 = {str(material_point_arg1)} {sign1} {str(self.text_ans1)}t, "
        third_task_var = f'а движение второго тела уравнением х2 = {str(material_point_arg3)} {sign2} {str(self.text_ans2)}t. '
        final_task_var = 'С какой скоростью перемещаются эти точки и где они встретятся?'
        self.text_que = choice(first_task_var) + second_task_var + third_task_var + final_task_var
        intermediate_result = self.text_ans11 - self.text_ans21
        intermediate_result1 = material_point_arg3 - material_point_arg1
        intermediate_result2 = intermediate_result1 / intermediate_result
        text_ans3 = round(material_point_arg1 + (self.text_ans11 * intermediate_result2), 3)
        self.text_ans = [self.text_ans11, self.text_ans21, text_ans3]
        self.unit = [self.unit1, self.unit1, self.unit2]
        return [self.text_que, self.text_ans, self.unit]


    def uniform_motion_ninth(self):
        x, t = symbols('x t')
        material_point_arg1 = choice(material_point_args)
        material_point_arg2 = choice(material_point_args)
        material_point_arg3 = choice(material_point_args)
        material_point_arg4 = choice(material_point_args)
        sign1 = choice(sign_args)
        sign2 = choice(sign_args)
        first_task_var = ["Движение материальной точки описывается уравнениями ", "Движение тела описывается уравнениями "]
        second_task_var = f"y = {str(material_point_arg1)} {sign1} {str(material_point_arg2)}t, "
        third_task_var = f'x = {str(material_point_arg3)} {sign2} {str(material_point_arg4)}t. '
        final_task_var = 'Найти уравнение зависимости y(x).'
        self.text_que = choice(first_task_var) + second_task_var + third_task_var + final_task_var
        eq1 = Eq(material_point_arg1 + (material_point_arg2 if sign1 == "+" else -material_point_arg2) * t, x)
        eq2 = Eq(material_point_arg3 + (material_point_arg4 if sign2 == "+" else -material_point_arg4) * t, x)
        solution = solve((eq1, eq2), (x, t))
        self.text_ans = [solution[x]]
        self.unit = [""]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_first(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]
        third_task_var = [' с. Скорость в этот момент равна ', " с. Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти ускорение тела. '
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        e_time = str(choice(e_time_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + e_time + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((int(speed2) - int(speed1)) / int(e_time), 3)]
        self.unit = ["м/с²"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_third(self):
        first_task_var = ["Время движения тела равно ", "Время равно "]
        second_task_var = [" с. Тело начинает движение со скоростью ", " с. Скорость тела в начале пути равна "]
        third_task_var = [' м/с. Скорость в данный момент равна ', " м/с. Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти ускорение тела. '
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        e_time = str(choice(e_time_var))
        speed1 = str(choice(first_speed_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + e_time + choice(second_task_var) + speed1 + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((int(speed2) - int(speed1)) / int(e_time), 3)]
        self.unit = ["м/с²"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_second(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с. Расстояние пройденное телом равно ", " м/с. Перемещение равно "]
        third_task_var = [' м. Скорость в данный момент равна ', " м. Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти ускорение тела. '
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        distance = str(choice(distance_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + distance + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(((int(speed2)**2) - (int(speed1)**2)) / (int(distance) * 2), 3)]
        self.unit = ["м/с²"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_fourth(self):
        first_task_var = ["Расстояние пройденное телом равно  ", "Перемещение равно "]
        second_task_var = [" м. Тело начинает движение со скоростью ", " м. Скорость тела в начале пути равна "]
        third_task_var = [' м/с. Скорость в данный момент равна ', " м/с. Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти ускорение тела. '
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        speed1 = str(choice(first_speed_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + speed1 + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(((int(speed2)**2) - (int(speed1)**2)) / (int(distance) * 2), 3)]
        self.unit = ["м/с²"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_fifth(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти конечную скорость тела.'
        speed1 = str(choice(first_speed_var))
        e_time = str(choice(e_time_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + e_time + choice(third_task_var) + acceleration + fourth_task_var
        self.text_ans = [round(int(acceleration) * int(e_time) + int(speed1), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_sixth(self):
        first_task_var = ["Время движения тела равно ", "Время равно "]
        second_task_var = [" с. Тело начинает движение со скоростью ", " с. Скорость тела в начале пути равна "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти конечную скорость тела.'
        e_time = str(choice(e_time_var))
        speed1 = str(choice(first_speed_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + e_time + choice(second_task_var) + speed1 + choice(third_task_var) + acceleration + fourth_task_var
        self.text_ans = [round(int(acceleration) * int(e_time) + int(speed1), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_seventh(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с. Расстояние пройденное телом равно ", " м/с на путь равный "]
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]
        fourth_task_var = ' м/с². Найти конечную скорость тела.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        distance = str(choice(distance_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + distance + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(sqrt(int(distance) * int(acceleration) * 2 + (int(speed1)**2)), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_eighth(self):
        first_task_var = ["Расстояние пройденное телом равно ", "Путь, который прошло тело, равен "]
        second_task_var = [" м. Тело начинает движение со скоростью ", " м скорость тела в начале пути равна "]
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]
        fourth_task_var = ' м/с². Найти конечную скорость тела.'
        speed1 = str(choice(first_speed_var))
        distance = str(choice(distance_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + speed1 + choice(third_task_var) + acceleration + fourth_task_var
        self.text_ans = [round(sqrt(int(distance) * int(acceleration) * 2 + (int(speed1)**2)), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_ninth(self):
        first_task_var = ["Тело движется со скоростью ", "Тело перемещается со скоростью "]
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        speed2 = str(choice(second_speed_var))
        e_time = str(choice(e_time_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed2 + choice(second_task_var) + e_time + choice(third_task_var) + acceleration + fourth_task_var
        self.text_ans = [int(speed2) - int(acceleration) * int(e_time)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_tenth(self):
        first_task_var = ["Время движения тела равно ", "Время равно "]
        second_task_var = [" с. Тело движется со скоростью ", " с. Тело перемещается со скоростью "]
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        e_time = str(choice(e_time_var))
        speed2 = str(choice(second_speed_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + e_time + choice(second_task_var) + speed2 + choice(third_task_var) + acceleration + fourth_task_var
        self.text_ans = [int(speed2) - int(acceleration) * int(e_time)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_eleventh(self):
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]
        second_task_var = [" м. Время движения тела равно ", " м за "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        e_time = str(choice(e_time_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + e_time + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((2 * int(distance) - int(acceleration) * (int(e_time)**2)) / (2 * int(e_time)), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_twelfth(self):
        first_task_var = ["Время движения тела равно ", "Время равно "]
        second_task_var = [" с. Тело переместилось на ", " с. Тело прошло расстояние равное "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        e_time = str(choice(e_time_var))
        distance = str(choice(distance_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + e_time + choice(second_task_var) + distance + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((2 * int(distance) - int(acceleration) * (int(e_time)**2)) / (2 * int(e_time)), 3)]
        self.unit =["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_thirteenth(self):
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]
        second_task_var = [" м. Конечная скорость равна ", " м. С конечной скоростью "]
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        speed2 = str(choice(second_speed_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + speed2 + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(sqrt((int(speed2)**2) - (int(distance) * int(acceleration) * 2)), 3)]
        self.unit = ["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_fourteenth(self):
        first_task_var = ["Конечная скорость равна ", "С конечной скоростью "]
        second_task_var = [" м/с. Тело переместилось на ", " м/с. Тело прошло расстояние равное "]
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]
        fourth_task_var = ' м/с². Найти начальную скорость тела.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed2 = str(choice(second_speed_var))
        distance = str(choice(distance_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed2 + choice(second_task_var) + distance + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(sqrt((int(speed2)**2) - (int(distance) * int(acceleration) * 2)), 3)]
        self.unit =["м/с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_fifteenth(self):
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]
        second_task_var = [" м. Начальная скорость равна ", " м. Оно начинало двигаться со скоростью "]
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]
        fourth_task_var = ' м/с². Найти время.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        distance = str(choice(distance_var))
        speed1 = str(choice(first_speed_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + distance + choice(second_task_var) + speed1 + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((sqrt(int(speed1)**2 + 2 * int(acceleration) * int(distance)) - int(speed1)) / int(acceleration), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_sixteenth(self):
        first_task_var = ["Начальная скорость равна ", "Тело начинало двигаться со скоростью "]
        second_task_var = [" м/с. Тело переместилось на ", " м/с. Тело прошло расстояние равное "]
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]
        fourth_task_var = ' м/с². Найти время.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        distance = str(choice(distance_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + distance + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((sqrt(int(speed1)**2 + 2 * int(acceleration) * int(distance)) - int(speed1)) / int(acceleration), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_seventeenth(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с с ускорением ", " м/с. Ускорение равно "]
        third_task_var = [' м/с². Скорость равна ', " м/с². Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти время.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        acceleration = str(choice(acceleration_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + acceleration + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round((int(speed2) - int(speed1)) / int(acceleration), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_eighteenth(self):
        first_task_var = ["Ускорение тела равно ", "Ускорение равно "]
        second_task_var = [" м/с². Тело начинает движение со скоростью ", " м/с². Скорость тела в начале пути равна "]
        third_task_var = [' м/с. Скорость равна ', " м/с. Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти время.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        acceleration = str(choice(acceleration_var))
        speed1 = str(choice(first_speed_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + acceleration + choice(second_task_var) + speed1 + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans =[round((int(speed2) - int(speed1)) / int(acceleration), 3)]
        self.unit = ["с"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_nineteenth(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Тело начинает перемещаться со скоростью "]
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]
        fourth_task_var = ' м/с². Найти расстояние пройденное телом.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        e_time = str(choice(e_time_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + e_time + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(int(speed1) * int(e_time) + (int(acceleration) * (int(e_time)**2) / 2), 3)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_twentieth(self):
        first_task_var = ["Время движения тела равно ", "Время равно "]
        second_task_var = [" с. Тело начинает движение со скоростью ", " с. Тело начинает перемещаться со скоростью "]
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]
        fourth_task_var = ' м/с². Найти расстояние пройденное телом.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        e_time = str(choice(e_time_var))
        speed1 = str(choice(first_speed_var))
        acceleration = str(choice(acceleration_var))
        self.text_que = choice(first_task_var) + e_time + choice(second_task_var) + speed1 + choice(third_task_var) + acceleration + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(int(speed1) * int(e_time) + (int(acceleration) * (int(e_time)**2) / 2), 3)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_twenty_one(self):
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "]
        second_task_var = [" м/с. Ускорение тела равно ", " м/с с ускорением "]
        third_task_var = [' м/с². Скорость в этот момент равна ', " м/с². Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти расстояние пройденное телом.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        speed1 = str(choice(first_speed_var))
        acceleration = str(choice(acceleration_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + speed1 + choice(second_task_var) + acceleration + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(((int(speed2)**2) - (int(speed1)**2)) / (2 * int(acceleration)), 3)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]


    def equiaxed_motion_twenty_two(self):
        first_task_var = ["Ускорение тела равно ", "Ускорение равно "]
        second_task_var = [" м/с². Тело начинает движение со скоростью ", " м/с². Скорость тела в начале пути равна "]
        third_task_var = [' м/с². Скорость в этот момент равна ', " м/с². Конечная скорость равна "]
        fourth_task_var = ' м/с. Найти расстояние пройденное телом.'
        fifth_task_var = ["Ответ округлите до тысячных. ", "Ответ округлите до 3 знаков после запятой. "]
        acceleration = str(choice(acceleration_var))
        speed1 = str(choice(first_speed_var))
        speed2 = str(choice(second_speed_var))
        self.text_que = choice(first_task_var) + acceleration + choice(second_task_var) + speed1 + choice(third_task_var) + speed2 + fourth_task_var + choice(fifth_task_var)
        self.text_ans = [round(((int(speed2)**2) - (int(speed1)**2)) / (2 * int(acceleration)), 3)]
        self.unit = ["м"]
        return [self.text_que, self.text_ans, self.unit]