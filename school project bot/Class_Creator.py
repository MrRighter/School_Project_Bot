from Class_Gener import *


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
            if key["Subject"] == "физика":
                if key["Theme"] == "кинематика":
                    if key["Theme_section"] == "":
                        if key["Subtopic"] == "":
                            num_questions = round(0.3 * int(key["N"]))
                            num_tests = round(0.2 * int(key["N"]))
                            num_problems = int(key["N"]) - num_questions - num_tests

                            for i in range(num_questions):
                                text_result += f'{i+1}) {TaskGenerator().questions_for_kr()}\n\n'
                            for i in range(num_tests):
                                text_result += f'{num_questions + i+1}) {TaskGenerator().tests_for_kr()}\n\n'
                            for i in range(num_problems):
                                text_result += f'{num_questions + num_tests + i+1}) {TaskGenerator().phis_kr_kinematics()}\n\n'

                            return text_result
                else:
                    pass
            else:
                pass
        else:
            pass