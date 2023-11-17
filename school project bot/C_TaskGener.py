from random import *


var = [i for i in range(51)] # рандом число для любых данных
acc=[i for i in range(1, 10)] # рандом число для ускорения

class TaskGenerator():
    def GenerateTask(self, key):
        #Subject =  key['Subject']#Предмет: физика, математика
        Type = key['Type']#Тип: КР по теме, подготовка к КР, СР, ДЗ
        #Сomplexity = key['Complexity']#Сложность: сложно (C), нормально (B), легко (A)
        if key["Subject"] == "физика":
            if key["Theme"] == "равномерное движение":
                if key["Subtopic"] == "время":
                    TaskClass = "uniform_time"
                elif key["Subtopic"] == "путь":
                    TaskClass = "uniform_distance"
                elif key["Subtopic"] == "скорость":
                    TaskClass = "uniform_speed"
            elif key["Theme"] == "равноускоренное движение":
                if key["Subtopic"] == "ускорение":
                    TaskClass = choice(["equidistant_acceleration_first", "equidistant_acceleration_second"])
                elif key["Subtopic"] == "конечная скорость":
                    TaskClass = choice(["equidistant_final_speed_first", "equidistant_final_speed_second"])
                elif key["Subtopic"] == "начальная скорость":
                    TaskClass = choice(["equidistant_start_speed_first", "equidistant_start_speed_second", "equidistant_start_speed_third"])
                elif key["Subtopic"] == "путь":
                    TaskClass = choice(["equidistant_distance_first", "equidistant_distance_second"])
                elif key["Subtopic"] == "время":
                    TaskClass = choice(["equidistant_time_first", "equidistant_time_second"])
        elif key["Subject"] == "математика":
            pass

        if Type == 'СР':
            if TaskClass == "uniform_time":
                return self.uniform_time()
            elif TaskClass == 'uniform_speed':
                return self.uniform_speed()
            elif TaskClass == "uniform_distance":
                return self.uniform_distance()
            elif TaskClass == 'equidistant_acceleration_first':
                return self.equidistant_acceleration_first()
            elif TaskClass == 'equidistant_acceleration_second':
                return self.equidistant_acceleration_second()
            elif TaskClass == 'equidistant_final_speed_first':
                return self.equidistant_final_speed_first()
            elif TaskClass == 'equidistant_final_speed_second':
                return self.equidistant_final_speed_second()
            elif TaskClass == 'equidistant_start_speed_first':
                return self.equidistant_start_speed_first()
            elif TaskClass == 'equidistant_start_speed_second':
                return self.equidistant_start_speed_second()
            elif TaskClass == 'equidistant_start_speed_third':
                return self.equidistant_start_speed_third()
            elif TaskClass == 'equidistant_distance_first':
                return self.equidistant_distance_first()
            elif TaskClass == 'equidistant_distance_second':
                return self.equidistant_distance_second()
            elif TaskClass == 'equidistant_time_first':
                return self.equidistant_time_first()
            elif TaskClass == 'equidistant_time_second':
                return self.equidistant_time_second()

    def uniform_time(self): #равномерное движение (найти время)
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ", "Тело катится прямолинейно и равномерно со скоростью "] #список первой части задачи
        first_var = str(choice(var)) #рандомная скорость
        second_task_var = [" м/с. Пройденое расстояние равное ", " м/с. Оно переместилось на ", " м/с. Перемещение равно "] #список второй части задачи
        second_var = str(choice(var)) #рандомное расстояние
        third_task_var = ' м. Найти время движения тела.' #концовка задачи
        return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

    def uniform_speed(self) : #равномерное движение (найти скорость)
        first_task_var = ["Тело прошло путь равный ", "Тело перерместилось на "] #список первой части задачи
        first_var = str(choice(var)) #рандомное расстояние
        second_task_var = [" м. Время движения тела равно ", " м за "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = ' с. Найти скорость движения тела.' #концовка задачи
        return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

    def uniform_distance(self) : ##равномерное движение (найти расстояние)
        first_task_var = ["Тело двигается прямолинейно и равномерно со скоростью ", "Тело катится прямолинейно и равномерно со скоростью "] #список первой части задачи
        first_var = str(choice(var)) #рандомная скорость
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = ' с. Найти расстояние пройденное телом.' #концовка задачи
        return choice(first_task_var)+first_var+choice(second_task_var)+second_var+third_task_var #возвращает текст задачи

    def equidistant_acceleration_first(self): #равноускоренное движение (найти ускорение)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = [' с. Скорость в этот момент равна ', " с. Конечная скорость равна "] #список третьей части задачи
        third_var=str(choice(var))#рандомная конечная скорость
        fourth_task_var=' м/с. Найти ускорение тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_acceleration_second(self): #равноускоренное движение (найти ускорение)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Расстояние пройденое телом равно ", " м/с. Перемещение равно "] #список второй части задачи
        second_var = str(choice(var)) #рандомное расстояние
        third_task_var = [' м. Скорость в этот момент равна ', " м. Конечная скорость равна "] #список третьей части задачи
        third_var=str(choice(var))#рандомная конечная скорость
        fourth_task_var=' м/с. Найти ускорение тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_final_speed_first(self): #равноускоренное движение (найти cкорость)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_final_speed_second(self): #равноускоренное движение (найти cкорость)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Расстояние пройденое телом равно ", " м/с на путь равный "] #список второй части задачи
        second_var = str(choice(var)) #рандомное расстояние
        third_task_var = [' м. Ускорение тела равно ', " м с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти конечную скорость тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_start_speed_first(self): #равноускоренное движение (найти cкорость)
        first_task_var = ["Тело движется со скоростью ", "Тело перемещается со скоростью "] #список первой части задачи
        first_var = str(choice(var)) #рандомная конечная скорость
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_start_speed_second(self): #равноускоренное движение (найти cкорость)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
        first_var = str(choice(var)) #рандомная конечная скорость
        second_task_var = [" м. Время движения тела равно ", " м за "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_start_speed_third(self): #равноускоренное движение (найти cкорость)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
        first_var = str(choice(var)) #рандомное расстояние
        second_task_var = [" м. Конечная скорость равна ", " м. С конечной скоростью "] #список второй части задачи
        second_var = str(choice(var)) #рандомное конечная скорость
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти начальную скорость тела.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_time_first(self): #равноускоренное движение (найти время)
        first_task_var = ["Тело переместилось на ", "Тело прошло расстояние равное "] #список первой части задачи
        first_var = str(choice(var)) #рандомное расстояние
        second_task_var = [" м. Начальная скорость равна ", " м. Оно начинало двигаться со скоростью "] #список второй части задачи
        second_var = str(choice(var)) #рандомное начальная скорость
        third_task_var = [' м/с. Ускорение тела равно ', " м/с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти время.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_time_second(self): #равноускоренное движение (найти время)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с с ускорением ", " м/с. Ускорение равно "] #список второй части задачи
        second_var = str(choice(acc)) #рандомное ускорение
        third_task_var = [' м/с^2. Скорость равна ', " м/с^2. Конечная скорость равна "] #список третьей части задачи
        third_var=str(choice(var))#рандомная конечная скорость
        fourth_task_var=' м/с. Найти время.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_distance_first(self): #равноускоренное движение (найти расстояние)
        first_task_var = ["Тело начинает движение со скоростью ", "Тело начинает перемещатся со скоростью "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Время движения тела равно ", " м/с на протяжении "] #список второй части задачи
        second_var = str(choice(var)) #рандомное время
        third_task_var = [' с. Ускорение тела равно ', " с с укорением равным "] #список третьей части задачи
        third_var=str(choice(acc))#рандомное ускорение
        fourth_task_var=' м/с^2. Найти расстояние пройденое телом.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи

    def equidistant_distance_second(self): #равноускоренное движение (найти расстояние)
        first_task_var = ["Тело начинает движение со скоростью ", "Скорость тела в начале пути равна "] #список первой части задачи
        first_var = str(choice(var)) #рандомная начальная скорость
        second_task_var = [" м/с. Ускорение тела равно ", " м/с с ускорением "] #список второй части задачи
        second_var = str(choice(acc)) #рандомное ускорение
        third_task_var = [' м/с^2. Скорость в этот момент равна ', " м/с^2. Конечная скорость равна "] #список третьей части задачи
        third_var=str(choice(var))#рандомная конечная скорость
        fourth_task_var=' м/с. Найти расстояние пройденое телом.'
        return choice(first_task_var) + first_var + choice(second_task_var) + second_var + choice(third_task_var) + third_var + fourth_task_var# возвращает текст задачи