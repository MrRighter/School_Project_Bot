from Class_Gener import *
from fpdf import FPDF


class Creator():
    def export_task(self, path, key):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Arial', '', './Arial.ttf', uni=True)
        pdf.set_font('Arial', '', 14)

        res = self.function_creator(key)
        pdf.multi_cell(190, 10, txt=res)
        pdf.output(path)

        return res
    def function_creator(self, key):
        #Тип: КР по теме, подготовка к КР, СР, ДЗ
        #Complexity = key['Complexity']#Сложность: сложно (C), нормально (B), легко (A)
        text_result = ""

        if key["Type"] == "однотипные задания":
            if key["Subject"] == "физика":
                if key["Theme"] == "кинематика":
                    if key["Theme_section"] == "равномерное движение":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().uniform_motion()}\n\n'
                            return text_result
                    elif key["Theme_section"] == "равноускоренное движение":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().equiaxed_motion()}\n\n'
                            return text_result
                elif key["Theme"] == "баллистика":
                    if key["Theme_section"] == "свободное падение тел":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().ballistics_motion()}\n\n'
                            return text_result
                    elif key["Theme_section"] == "баллистическое движение":
                            for i in range(int(key["N"])):
                                text_result += f'{i+1}) {TaskGenerator().ballistics_corner_motion()}\n\n'
                            return text_result
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
                        num_questions = round(0.3 * int(key["N"]))
                        num_tests = round(0.2 * int(key["N"]))
                        num_problems = int(key["N"]) - num_questions - num_tests
                        for i in range(num_questions):
                            text_result += f'{i+1}) {TaskGenerator().questions_for_kr_kinematics()}\n\n'
                        for i in range(num_tests):
                            text_result += f'{num_questions + i+1}) {TaskGenerator().tests_for_kr_kinematics()}\n\n'
                        for i in range(num_problems):
                            text_result += f'{num_questions + num_tests + i+1}) {TaskGenerator().phis_kr_kinematics()}\n\n'
                        return text_result
                elif key["Theme"] == "механика":
                    if key["Theme_section"] == "":
                        for i in range(int(key["N"])):
                            text_result += f'{i+1}) {TaskGenerator().phis_kr_mechanics()}\n\n'
                        return text_result
                elif key["Theme"] == "баллистика":
                    if key["Theme_section"] == "":
                        for i in range(int(key["N"])):
                            text_result += f'{i+1}) {TaskGenerator().phis_kr_ballistics()}\n\n'
                        return text_result