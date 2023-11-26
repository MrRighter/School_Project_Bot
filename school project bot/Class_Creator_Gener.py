from random import *

sign = ['+', '-']
var = [i for i in range(101)]  # список возможных переменных


class Creator():
    def function_creator(self, key):
        #Тип: КР по теме, подготовка к КР, СР, ДЗ
        #Complexity = key['Complexity']#Сложность: сложно (C), нормально (B), легко (A)
        text_result = ""
        if key["Type"] == "однотипные задания":
            if key["Subject"] == "физика":
                if key["Theme"] == "кинематика":
                    if key["Theme_section"] == "равномерное движение":
                        if key["Subtopic"] == "время":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().uniform_time()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "путь":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().uniform_distance()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "скорость":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().uniform_speed()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "графики зависимости":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().uniform_equations()}\n\n'
                            return text_result
                        else:
                            pass
                    elif key["Theme_section"] == "равноускоренное движение":
                        if key["Subtopic"] == "ускорение":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equidistant_acceleration()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "конечная скорость":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equidistant_final_speed()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "начальная скорость":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equidistant_start_speed()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "время":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equidistant_time()}\n\n'
                            return text_result
                        elif key["Subtopic"] == "путь":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equidistant_distance()}\n\n'
                            return text_result
                        else:
                            pass
                elif key["Theme"] == "баллистика":
                    pass
                elif key["Theme"] == "статика":
                    pass
                elif key["Theme"] == "работа и энергия":
                    pass
            elif key["Subject"] == "математика":
                pass
        elif key["Type"] == "контрольная работа":
            pass


class TaskGenerator():
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