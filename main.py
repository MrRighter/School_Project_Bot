from random import *

themes = ["Равноускоренное движение", "Равномерное движение"]  # темы задач
subtopics = {'Равномерное движение': ['Найти время', "Найти путь", "Найти скорость"],
             "Равноускоренное движение": ['Найти путь', "Найти начальную скорость", "Найти время", "Найти ускорение",
                                          "Найти конечную скорость"]}  # подтемы задач
sign = ['+', '-']
var = [i for i in range(101)]  # список возможных переменных


def uniform_time_first():  # равномерное движение (найти время)
    first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ",
                      "Тело катится прямолинейно и равномерно со скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Пройденое расстояние равное ", " м/с. Оно переместилось на ",
                       " м/с. Перемещение равно "]  # список второй части задачи
    third_task_var = ' м. Найти время движения тела.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def uniform_time_second():  # равномерное движение (найти время)
    first_task_var = ["Пройденное телом расстояние равно ", "Тело переместилось на "]  # список первой части задачи
    second_task_var = [" м прямолинейно и равномерно со скоростью ", " м. Скорость тела равна ",
                       " м. Скорость постоянная и равна "]  # список второй части задачи
    third_task_var = ' м/с. Найти время движения тела.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def uniform_speed_first():  # равномерное движение (найти скорость)
    first_task_var = ["Тело прошло путь равный ", "Тело перерместилось на "]  # список первой части задачи
    second_task_var = [" м. Время движения тела равно ", " м за "]  # список второй части задачи
    third_task_var = ' с. Найти скорость движения тела.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def uniform_speed_second():  # равномерное движение (найти скорость)
    first_task_var = ["Время движения тела равно ", "За "]  # список первой части задачи
    second_task_var = [" с тело переместилось на ", " с перемещение тела равно "]  # список второй части задачи
    third_task_var = ' м. Найти скорость движения тела.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def uniform_distance_first():  ##равномерное движение (найти расстояние)
    first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ",
                      "Тело катится прямолинейно и равномерно со скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
    third_task_var = ' с. Найти расстояние пройденное телом.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def uniform_distance_second():  ##равномерное движение (найти расстояние)
    first_task_var = ["Время движения тела равно ",
                      "За "]  # список первой части задачи
    second_task_var = [" с. Двигаясь прямолинейно и равномерно со скоростью ",
                       " с. Скорость тела равна "]  # список второй части задачи
    third_task_var = ' м/с. Найти расстояние пройденное телом.'  # концовка задачи
    return choice(first_task_var) + str(choice(var)) + choice(
        second_task_var) + str(choice(var)) + third_task_var  # возвращает текст задачи


def equidistant_acceleration_first():  # равноускоренное движение (найти ускорение)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
    third_task_var = [' с. Скорость в этот момент равна ',
                      " с. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти ускорение тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_acceleration_third():  # равноускоренное движение (найти ускорение)
    first_task_var = ["Время движения тела равно ", "Время равно"
                      ]  # список первой части задачи
    second_task_var = [" с. Тело начинает движение со скоростью ",
                       " с. Скорость тела в начале пути равна "]  # список второй части задачи
    third_task_var = [' м/с. Скорость в этот момент равна ',
                      " м/с. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти ускорение тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_acceleration_second():  # равноускоренное движение (найти ускорение)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с. Расстояние пройденое телом равно ",
                       " м/с. Перемещение равно "]  # список второй части задачи
    third_task_var = [' м. Скорость в этот момент равна ',
                      " м. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти ускорение тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_acceleration_fourth():  # равноускоренное движение (найти ускорение)
    first_task_var = ["Расстояние пройденое телом равно  ",
                      "Перемещение равно "]  # список первой части задачи
    second_task_var = [" м. Тело начинает движение со скоростью ",
                       " м. Скорость тела в начале пути равна "]  # список второй части задачи
    third_task_var = [' м/с. Скорость в этот момент равна ',
                      " м/с. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти ускорение тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_final_speed_first():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_final_speed_third():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Время движения тела равно  ",
                      "Вермя равно "]  # список первой части задачи
    second_task_var = [" с. Тело начинает движение со скоростью ",
                       " с. Скорость тела в начале пути равна "]  # список второй части задачи

    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_final_speed_second():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с. Расстояние пройденое телом равно ", " м/с на путь равный "]  # список второй части задачи
    third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_final_speed_fourth():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Расстояние пройденое телом равно ",
                      "Путь, который прошло тело, равен "]  # список первой части задачи
    second_task_var = [" м. Тело начинает движение со скоростью ",
                       " м скорость тела в начале пути равна "]  # список второй части задачи
    third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_first():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Тело движется со скоростью ", "Тело перемещается со скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_fourth():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Время движения тела равно ", "Время равно"]  # список первой части задачи
    second_task_var = [" с. Тело движется со скоростью ",
                       " с. Тело перемещается со скоростью "]  # список второй части задачи
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_second():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
    second_task_var = [" м. Время движения тела равно ", " м за "]  # список второй части задачи
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_fifth():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Время движения тела равно ", "Время равно"]  # список первой части задачи
    second_task_var = [" с. Тело переместилось на ", " с. Тело прошло расстояние равное "]  # список второй части задачи
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_third():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
    second_task_var = [" м. Конечная скорость равна ", " м. С конечной скоростью "]  # список второй части задачи
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_start_speed_sixth():  # равноускоренное движение (найти cкорость)
    first_task_var = ["Конечная скорость равна ", "С конечной скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Тело переместилось на ",
                       " м/с. Тело прошло расстояние равное "]  # список второй части задачи
    third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_time_first():  # равноускоренное движение (найти время)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "]  # список первой части задачи
    second_task_var = [" м. Начальная скорость равна ",
                       " м. Оно начинало двигаться со скоростью "]  # список второй части задачи
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти время.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_time_third():  # равноускоренное движение (найти время)
    first_task_var = ["Начальная скорость равна ", "Оно начинало двигаться со скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Тело переместилось на ",
                       " м/с. Тело прошло расстояние равное "]  # список второй части задачи
    third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти время.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_time_second():  # равноускоренное движение (найти время)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с с ускорением ", " м/с. Ускорение равно "]  # список второй части задачи
    third_task_var = [' м/с^2. Скорость равна ', " м/с^2. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти время.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_time_fourth():  # равноускоренное движение (найти время)
    first_task_var = ["Ускорение тела равно ",
                      "Ускорение равно "]  # список первой части задачи
    second_task_var = [" м/с^2. Тело начинает движение со скоростью ",
                       " м/с^2. Скорость тела в начале пути равна "]  # список второй части задачи
    third_task_var = [' м/с. Скорость равна ', " м/с. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти время.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_distance_first():  # равноускоренное движение (найти расстояние)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Тело начинает перемещатся со скоростью "]  # список первой части задачи
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "]  # список второй части задачи
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти расстояние пройденое телом.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_distance_third():  # равноускоренное движение (найти расстояние)
    first_task_var = ["Время движения тела равно ",
                      "Время равно "]  # список первой части задачи
    second_task_var = [" с. Тело начинает движение со скоростью ",
                       " с. Тело начинает перемещатся со скоростью "]  # список второй части задачи
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "]  # список третьей части задачи
    fourth_task_var = ' м/с^2. Найти расстояние пройденое телом.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_distance_second():  # равноускоренное движение (найти расстояние)
    first_task_var = ["Тело начинает движение со скоростью ",
                      "Скорость тела в начале пути равна "]  # список первой части задачи
    second_task_var = [" м/с. Ускорение тела равно ", " м/с с ускорением "]  # список второй части задачи
    third_task_var = [' м/с^2. Скорость в этот момент равна ',
                      " м/с^2. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти расстояние пройденое телом.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def equidistant_distance_fourth():  # равноускоренное движение (найти расстояние)
    first_task_var = ["Ускорение тела равно ",
                      "Ускорение равно"]  # список первой части задачи
    second_task_var = [" м/с^2. Тело начинает движение со скоростью ",
                       " м/с^2. Скорость тела в начале пути равна "]  # список второй части задачи
    third_task_var = [' м/с^2. Скорость в этот момент равна ',
                      " м/с^2. Конечная скорость равна "]  # список третьей части задачи
    fourth_task_var = ' м/с. Найти расстояние пройденое телом.'
    return choice(first_task_var) + str(choice(var)) + choice(second_task_var) + str(choice(var)) + choice(
        third_task_var) + str(choice(var)) + fourth_task_var  # возвращает текст задачи


def uniform_equations_first():
    first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]  # список первой части задачи
    second_task_var = f"х = {str(choice(var))} {choice(sign)} {str(choice(var))}t "
    final_task_var = 'С какой скоростью перемещается это тело?'  # концовка задачи
    return choice(first_task_var) + second_task_var + final_task_var  # возвращает текст задачи


def uniform_equations_second():
    first_task_var = ["Движение материально точки описывается уравнением ", "Движение тела описывается уравнением "]  # список первой части задачи
    second_task_var = f"х1 = {str(choice(var))} {choice(sign)} {str(choice(var))}t, "
    third_task_var = f'а движение второго тела уравнением х2 = {str(choice(var))} {choice(sign)} {str(choice(var))} '
    final_task_var = 'С какой скоростью перемещаются эти точки и где они встретятся?'  # концовка задачи
    return choice(first_task_var) + second_task_var + third_task_var + final_task_var  # возвращает текст задачи

def uniform_equations_third():
    first_task_var = ["Движение материальной точки описывается уравнениями ", "Движение тела описывается уравнениями "]  # список первой части задачи
    second_task_var = f"y = {str(choice(var))} {choice(sign)} {str(choice(var))}t, "
    third_task_var = f' x = {str(choice(var))} {choice(sign)} {str(choice(var))} '
    final_task_var = 'Найти уравнение зависимости y(x).'  # концовка задачи
    return choice(first_task_var) + second_task_var + third_task_var + final_task_var  # возвращает текст задачи



def result(theme, subtopic, number):  # выводит нужное количество задач на выбранную тему
    if theme == "Равномерное движение":
        if subtopic == 'Найти время':
            for i in range(number):
                print(choice([uniform_time_first(), uniform_time_second()]))
        elif subtopic == "Найти путь":
            for i in range(number):
                print(choice([uniform_distance_first(), uniform_distance_second()]))
        elif subtopic == "Найти скорость":
            for i in range(number):
                print(choice([uniform_speed_first(), uniform_speed_second()]))
        elif subtopic == 'Уравнения':
            for i in range(number):
                print(choice([uniform_equations_second(), uniform_equations_first(), uniform_equations_third()]))
        else:
            print("Такой подтемы не существует...")
    elif theme == 'Равноускоренное движение':
        if subtopic == "Найти ускорение":
            for i in range(number):
                print(choice([equidistant_acceleration_first(), equidistant_acceleration_second(),
                              equidistant_acceleration_third(), equidistant_acceleration_fourth()]))
        elif subtopic == "Найти конечную скорость":
            for i in range(number):
                print(choice(
                    [equidistant_final_speed_first(), equidistant_final_speed_second(), equidistant_final_speed_third(),
                     equidistant_final_speed_fourth()]))
        elif subtopic == "Найти начальную скорость":
            for i in range(number):
                print(choice([equidistant_start_speed_first(), equidistant_start_speed_second(),
                              equidistant_start_speed_third(), equidistant_start_speed_fifth(),
                              equidistant_start_speed_fourth(), equidistant_start_speed_sixth()]))
        elif subtopic == "Найти путь":
            for i in range(number):
                print(choice([equidistant_distance_first(), equidistant_distance_third(), equidistant_distance_second(),
                              equidistant_distance_fourth()]))
        elif subtopic == "Найти время":
            for i in range(number):
                print(choice([equidistant_time_first(), equidistant_time_second(), equidistant_time_third(),
                              equidistant_time_fourth()]))
        else:
            print("Такой подтемы не существует...")
    else:
        print("Такой темы не существует...")


theme = input("Введите тему задания ")
subtopic = input("Введите подтему задания ")
number = int(input("Введите количество заданий "))

result(theme, subtopic, number)
