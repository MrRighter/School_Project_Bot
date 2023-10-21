from random import *
from math import *

themes = ["Равноускоренное движение", "Равномерное движение"] #темы задач
subtopics ={'Равномерное движение' : ['Найти время', "Найти путь", "Найти скорость"], "Равноускоренное движение" : ['Найти путь', "Найти начальную скорость", "Найти время", "Найти ускорение", "Найти конечную скорость"]} #подтемы задач
var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #список возможных переменных

def uniform_time () : #равномерное движение (найти время)
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
    second_var = str(choice(var)) #рандомное расстояние
    third_task_var = ' с. Найти расстояние пройденное телом.' #концовка задачи
    return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

def result(theme, subtopic, number): #выводит нужное количество задач на выбранную тему
    if theme == "Равномерное движение":
        if subtopic == 'Найти время':
            for i in range(number):
                print(uniform_time())
        elif subtopic == "Найти путь":
            for i in range(number):
                print(uniform_distance())
        elif subtopic == "Найти скорость":
            for i in range(number):
                print(uniform_speed())
        else:
            print("Такой подтемы не существует...")
    else:
        print("Такой темы не существует...")

theme = input("Введите тему задания ")
subtopic = input("Введите подтему задания ")
number = int(input("Введите количество заданий "))
result(theme, subtopic, number)