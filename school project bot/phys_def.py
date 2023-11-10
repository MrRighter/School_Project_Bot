from random import *


var = [i for i in range(51)] # рандом число для любых данных
acc=[i for i in range(1, 10)] # рандом число для ускорения

def uniform_time(): #равномерное движение (найти время)
    first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ", "Тело катится прямолинейно и равномерно со скоростью "] #список первой части задачи
    first_var = str(choice(var)) #рандомная скорость
    second_task_var = [" м/с. Пройденое расстояние равное ", " м/с. Оно переместилось на ", " м/с. Перемещение равно "] #список второй части задачи
    second_var = str(choice(var)) #рандомное расстояние
    third_task_var = ' м. Найти время движения тела.' #концовка задачи
    return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

def uniform_speed() : #равномерное движение (найти скорость)
    first_task_var = ["Тело прошло путь равный ", "Тело перерместилось на "] #список первой части задачи
    first_var = str(choice(var)) #рандомное расстояние
    second_task_var = [" м. Время движения тела равно ", " м за "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = ' с. Найти скорость движения тела.' #концовка задачи
    return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

def uniform_distance() : ##равномерное движение (найти расстояние)
    first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ", "Тело катится прямолинейно и равномерно со скоростью "] #список первой части задачи
    first_var = str(choice(var)) #рандомная скорость
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = ' с. Найти расстояние пройденное телом.' #концовка задачи
    return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

def equidistant_acceleration_first(): #равноускоренное движение (найти ускорение)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = [' с. Скорость в этот момент равна ', " с. Конечная скорость равна "] #список третьей части задачи
    third_var=str(choice(var))#рандомная конечная скорость
    fourth_task_var=' м/с. Найти ускорение тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_acceleration_second(): #равноускоренное движение (найти ускорение)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Расстояние пройденое телом равно ", " м/с. Перемещение равно "] #список второй части задачи
    second_var = str(choice(var)) #рандомное расстояние
    third_task_var = [' м. Скорость в этот момент равна ', " м. Конечная скорость равна "] #список третьей части задачи
    third_var=str(choice(var))#рандомная конечная скорость
    fourth_task_var=' м/с. Найти ускорение тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_final_speed_first(): #равноускоренное движение (найти cкорость)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_final_speed_second(): #равноускоренное движение (найти cкорость)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Расстояние пройденое телом равно ", " м/с на путь равный "] #список второй части задачи
    second_var = str(choice(var)) #рандомное расстояние
    third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти конечную скорость тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_start_speed_first(): #равноускоренное движение (найти cкорость)
    first_task_var = ["Тело движется со скоростью ", "Тело перемещается со скоростью "] #список первой части задачи
    first_var = str(choice(var)) #рандомная конечная скорость
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_start_speed_second(): #равноускоренное движение (найти cкорость)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
    first_var = str(choice(var)) #рандомная конечная скорость
    second_task_var = [" м. Время движения тела равно ", " м за "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_start_speed_third(): #равноускоренное движение (найти cкорость)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
    first_var = str(choice(var)) #рандомное расстояние
    second_task_var = [" м. Конечная скорость равна ", " м. С конечной скоростью "] #список второй части задачи
    second_var = str(choice(var)) #рандомное конечная скорость
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти начальную скорость тела.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_time_first(): #равноускоренное движение (найти время)
    first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
    first_var = str(choice(var)) #рандомное расстояние
    second_task_var = [" м. Начальная скорость равна ", " м. Оно начинало двигаться со скоростью "] #список второй части задачи
    second_var = str(choice(var)) #рандомное начальная скорость
    third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти время.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_time_second(): #равноускоренное движение (найти время)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с с ускорением ", " м/с. Ускорение равно "] #список второй части задачи
    second_var = str(choice(acc)) #рандомное ускорение
    third_task_var = [' м/с^2. Скорость равна ', " м/с^2. Конечная скорость равна "] #список третьей части задачи
    third_var=str(choice(var))#рандомная конечная скорость
    fourth_task_var=' м/с. Найти время.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_distance_first(): #равноускоренное движение (найти расстояние)
    first_task_var = ["Тело начинает движение со скоростью ", "Тело начинает перемещатся со скоростью "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
    second_var = str(choice(var)) #рандомное время
    third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
    third_var=str(choice(acc))#рандомное ускорение
    fourth_task_var=' м/с^2. Найти расстояние пройденое телом.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

def equidistant_distance_second(): #равноускоренное движение (найти расстояние)
    first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
    first_var = str(choice(var)) #рандомная начальная скорость
    second_task_var = [" м/с. Ускорение тела равно ", " м/с с ускорением "] #список второй части задачи
    second_var = str(choice(acc)) #рандомное ускорение
    third_task_var = [' м/с^2. Скорость в этот момент равна ', " м/с^2. Конечная скорость равна "] #список третьей части задачи
    third_var=str(choice(var))#рандомная конечная скорость
    fourth_task_var=' м/с. Найти расстояние пройденое телом.'
    return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи