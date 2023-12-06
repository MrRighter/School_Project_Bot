from random import *

sign = ['+', '-']
var = [i for i in range(101)]  # список возможных переменных


class TaskGenerator():
    def questions_for_kr(self):
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

    def tests_for_kr(self):
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


    def phis_kr_kinematics(self):
        return choice([self.uniform_time_first(), self.uniform_time_second(), self.uniform_speed_first(), self.uniform_speed_second(),
                       self.uniform_distance_first(), self.uniform_distance_second(), self.equidistant_acceleration_first(),
                       self.equidistant_acceleration_second(), self.equidistant_acceleration_third(), self.equidistant_acceleration_fourth(),
                       self.equidistant_final_speed_first(), self.equidistant_final_speed_second(), self.equidistant_final_speed_third(),
                       self.equidistant_final_speed_fourth(), self.equidistant_start_speed_first(), self.equidistant_start_speed_second(),
                       self.equidistant_start_speed_third(), self.equidistant_start_speed_fourth(), self.equidistant_start_speed_fifth(),
                       self.equidistant_start_speed_sixth(), self.equidistant_time_first(), self.equidistant_time_second(),
                       self.equidistant_time_third(), self.equidistant_time_fourth(), self.equidistant_distance_first(), self.equidistant_distance_second(),
                       self.equidistant_distance_third(), self.equidistant_distance_fourth(), self.uniform_equations_first(), self.uniform_equations_second(),
                       self.uniform_equations_third()])


    def uniform_time(self):
        return choice([self.uniform_time_first(), self.uniform_time_second()])

    def uniform_speed(self):
        return choice([self.uniform_speed_first(), self.uniform_speed_second()])

    def uniform_distance(self):
        return choice([self.uniform_distance_first(), self.uniform_distance_second()])

    def equidistant_acceleration(self):
        return choice([self.equidistant_acceleration_first(), self.equidistant_acceleration_second(), self.equidistant_acceleration_third(), self.equidistant_acceleration_fourth()])

    def equidistant_final_speed(self):
        return choice([self.equidistant_final_speed_first(), self.equidistant_final_speed_second(), self.equidistant_final_speed_third(), self.equidistant_final_speed_fourth()])

    def equidistant_start_speed(self):
        return choice([self.equidistant_start_speed_first(), self.equidistant_start_speed_second(), self.equidistant_start_speed_third(), self.equidistant_start_speed_fourth(), self.equidistant_start_speed_fifth(), self.equidistant_start_speed_sixth()])

    def equidistant_time(self):
        return choice([self.equidistant_time_first(), self.equidistant_time_second(), self.equidistant_time_third(), self.equidistant_time_fourth()])

    def equidistant_distance(self):
        return choice([self.equidistant_distance_first(), self.equidistant_distance_second(), self.equidistant_distance_third(), self.equidistant_distance_fourth()])

    def uniform_equations(self):
        return choice([self.uniform_equations_first(), self.uniform_equations_second(), self.uniform_equations_third()])


    def uniform_time_first(self):  # равномерное движение (найти время)
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ",
                        "Тело катится прямолинейно и равномерно со скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Пройденное расстояние равное ", " м/с. Оно переместилось на ",
                        " м/с. Перемещение равно "]  # список второй части задачи
        third_task_var = ' м. Найти время движения тела.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def uniform_time_second(self):  # равномерное движение (найти время)
        first_task_var = ["Пройденное телом расстояние равно ", "Тело переместилось на "]  # список первой части задачи
        second_task_var = [" м прямолинейно и равномерно со скоростью ", " м. Скорость тела равна ",
                        " м. Скорость постоянная и равна "]  # список второй части задачи
        third_task_var = ' м/с. Найти время движения тела.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def uniform_speed_first(self):  # равномерное движение (найти скорость)
        first_task_var = ["Тело прошло путь равный ", "Тело переместилось на "]  # список первой части задачи
        second_task_var = [" м. Время движения тела равно ", " м за "]  # список второй части задачи
        third_task_var = ' с. Найти скорость движения тела.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def uniform_speed_second(self):  # равномерное движение (найти скорость)
        first_task_var = ["Время движения тела равно ", "За "]  # список первой части задачи
        second_task_var = [" с тело переместилось на ", " с перемещение тела равно "]  # список второй части задачи
        third_task_var = ' м. Найти скорость движения тела.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def uniform_distance_first(self):  ##равномерное движение (найти расстояние)
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ",
                        "Тело катится прямолинейно и равномерно со скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
        third_task_var = ' с. Найти расстояние пройденное телом.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def uniform_distance_second(self):  ##равномерное движение (найти расстояние)
        first_task_var = ["Время движения тела равно ",
                        "За "]  # список первой части задачи
        second_task_var = [" с. Двигаясь прямолинейно и равномерно со скоростью ",
                        " с. Скорость тела равна "]  # список второй части задачи
        third_task_var = ' м/с. Найти расстояние пройденное телом.'  # концовка задачи
        return choice(first_task_var) + str(choice(var)) + choice(
            second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи

    def equidistant_acceleration_first(self):  # равноускоренное движение (найти ускорение)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
        third_task_var = [' с. Скорость в этот момент равна ',
                        " с. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти ускорение тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_acceleration_third(self):  # равноускоренное движение (найти ускорение)
        first_task_var = ["Время движения тела равно ", "Время равно"
                        ]  # список первой части задачи
        second_task_var = [" с. Тело начинает движение со скоростью ",
                        " с. Скорость тела в начале пути равна "]  # список второй части задачи
        third_task_var = [' м/с. Скорость в этот момент равна ',
                        " м/с. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти ускорение тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_acceleration_second(self):  # равноускоренное движение (найти ускорение)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с. Расстояние пройденное телом равно ",
                        " м/с. Перемещение равно "]  # список второй части задачи
        third_task_var = [' м. Скорость в этот момент равна ',
                        " м. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти ускорение тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_acceleration_fourth(self):  # равноускоренное движение (найти ускорение)
        first_task_var = ["Расстояние пройденное телом равно  ",
                        "Перемещение равно "]  # список первой части задачи
        second_task_var = [" м. Тело начинает движение со скоростью ",
                        " м. Скорость тела в начале пути равна "]  # список второй части задачи
        third_task_var = [' м/с. Скорость в этот момент равна ',
                        " м/с. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти ускорение тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_final_speed_first(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_final_speed_third(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Время движения тела равно  ",
                        "Время равно "]  # список первой части задачи
        second_task_var = [" с. Тело начинает движение со скоростью ",
                        " с. Скорость тела в начале пути равна "]  # список второй части задачи

        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_final_speed_second(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с. Расстояние пройденное телом равно ", " м/с на путь равный "]  # список второй части задачи
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_final_speed_fourth(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Расстояние пройденное телом равно ",
                        "Путь, который прошло тело, равен "]  # список первой части задачи
        second_task_var = [" м. Тело начинает движение со скоростью ",
                        " м скорость тела в начале пути равна "]  # список второй части задачи
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_first(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Тело движется со скоростью ", "Тело перемещается со скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_fourth(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Время движения тела равно ", "Время равно"]  # список первой части задачи
        second_task_var = [" с. Тело движется со скоростью ",
                        " с. Тело перемещается со скоростью "]  # список второй части задачи
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_second(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
        second_task_var = [" м. Время движения тела равно ", " м за "]  # список второй части задачи
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_fifth(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Время движения тела равно ", "Время равно"]  # список первой части задачи
        second_task_var = [" с. Тело переместилось на ", " с. Тело прошло расстояние равное "]  # список второй части задачи
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_third(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
        second_task_var = [" м. Конечная скорость равна ", " м. С конечной скоростью "]  # список второй части задачи
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_start_speed_sixth(self):  # равноускоренное движение (найти скорость)
        first_task_var = ["Конечная скорость равна ", "С конечной скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Тело переместилось на ",
                        " м/с. Тело прошло расстояние равное "]  # список второй части задачи
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_time_first(self):  # равноускоренное движение (найти время)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
        second_task_var = [" м. Начальная скорость равна ",
                        " м. Оно начинало двигаться со скоростью "]  # список второй части задачи
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти время.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_time_third(self):  # равноускоренное движение (найти время)
        first_task_var = ["Начальная скорость равна ", "Оно начинало двигаться со скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Тело переместилось на ",
                        " м/с. Тело прошло расстояние равное "]  # список второй части задачи
        third_task_var = [' м. Ускорение тела равно ', " м с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти время.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_time_second(self):  # равноускоренное движение (найти время)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с с ускорением ", " м/с. Ускорение равно "]  # список второй части задачи
        third_task_var = [' м/с^2. Скорость равна ', " м/с^2. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти время.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_time_fourth(self):  # равноускоренное движение (найти время)
        first_task_var = ["Ускорение тела равно ",
                        "Ускорение равно "]  # список первой части задачи
        second_task_var = [" м/с^2. Тело начинает движение со скоростью ",
                        " м/с^2. Скорость тела в начале пути равна "]  # список второй части задачи
        third_task_var = [' м/с. Скорость равна ', " м/с. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти время.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_distance_first(self):  # равноускоренное движение (найти расстояние)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Тело начинает перемещаться со скоростью "]  # список первой части задачи
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
        third_task_var = [' с. Ускорение тела равно ', " с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти расстояние пройденное телом.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_distance_third(self):  # равноускоренное движение (найти расстояние)
        first_task_var = ["Время движения тела равно ",
                        "Время равно "]  # список первой части задачи
        second_task_var = [" с. Тело начинает движение со скоростью ",
                        " с. Тело начинает перемещаться со скоростью "]  # список второй части задачи
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с ускорением равным "]  # список третьей части задачи
        fourth_task_var = ' м/с^2. Найти расстояние пройденное телом.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_distance_second(self):  # равноускоренное движение (найти расстояние)
        first_task_var = ["Тело начинает движение со скоростью ",
                        "Скорость тела в начале пути равна "]  # список первой части задачи
        second_task_var = [" м/с. Ускорение тела равно ", " м/с с ускорением "]  # список второй части задачи
        third_task_var = [' м/с^2. Скорость в этот момент равна ',
                        " м/с^2. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти расстояние пройденное телом.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def equidistant_distance_fourth(self):  # равноускоренное движение (найти расстояние)
        first_task_var = ["Ускорение тела равно ",
                        "Ускорение равно"]  # список первой части задачи
        second_task_var = [" м/с^2. Тело начинает движение со скоростью ",
                        " м/с^2. Скорость тела в начале пути равна "]  # список второй части задачи
        third_task_var = [' м/с^2. Скорость в этот момент равна ',
                        " м/с^2. Конечная скорость равна "]  # список третьей части задачи
        fourth_task_var = ' м/с. Найти расстояние пройденное телом.'
        return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
            third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи

    def uniform_equations_first(self):
        first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]  # список первой части задачи
        second_task_var = f"х = {str(choice(var))} {choice(sign)} {str(choice(var))}t "
        final_task_var = 'С какой скоростью перемещается это тело?'  # концовка задачи
        return choice(first_task_var) + second_task_var + final_task_var  # возвращает текст задачи

    def uniform_equations_second(self):
        first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]  # список первой части задачи
        second_task_var = f"х1 = {str(choice(var))} {choice(sign)} {str(choice(var))}t, "
        third_task_var = f'а движение второго тела уравнением х2 = {str(choice(var))} {choice(sign)} {str(choice(var))} '
        final_task_var = 'С какой скоростью перемещаются эти точки и где они встретятся?'  # концовка задачи
        return choice(first_task_var) + second_task_var + third_task_var + final_task_var  # возвращает текст задачи

    def uniform_equations_third(self):
        first_task_var = ["Движение материальной точки описывается уравнениями ", "Движение тела описывается уравнениями "]  # список первой части задачи
        second_task_var = f"y = {str(choice(var))} {choice(sign)} {str(choice(var))}t, "
        third_task_var = f' x = {str(choice(var))} {choice(sign)} {str(choice(var))} '
        final_task_var = 'Найти уравнение зависимости y(x).'  # концовка задачи
        return choice(first_task_var) + second_task_var + third_task_var + final_task_var  # возвращает текст задачи