from Class_Gener import *
from fpdf import FPDF


class Creator:
    def export_task(self, path, key):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Arial', '', './Arial.ttf', uni=True)
        pdf.set_font('Arial', '', 14)
        res = self.function_creator(key)
        pdf.multi_cell(190, 10, txt=res[0])
        pdf.output(path)
        return res

    def export_PDF(self, path, text):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Arial', '', './Arial.ttf', uni=True)
        pdf.set_font('Arial', '', 14)
        pdf.multi_cell(190, 10, txt=text)
        pdf.output(path)

    def function_creator(self, key):
        que_text_result = ""
        ans_text_result = ""

        if key["Type"] == "СР":  # Самостоятельная работа
            if key["Subject"] == "Физика":
                if key["Theme"] == "Кинематика":
                    if key["Theme_section"] == "Равномерное движение":
                        for i in range(int(key["N"])):
                            que_ans_text = TaskGenerator().uniform_motion()
                            ans_text_result += f'{i + 1}) Ответ: '
                            for j, answer in enumerate(que_ans_text[1]):
                                ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                            que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                            ans_text_result += '\n'
                        return que_text_result, ans_text_result
                    elif key["Theme_section"] == "Равноускоренное движение":
                        for i in range(int(key["N"])):
                            que_ans_text = TaskGenerator().equiaxed_motion()
                            ans_text_result += f'{i + 1}) Ответ: '
                            for j, answer in enumerate(que_ans_text[1]):
                                ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                            que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                            ans_text_result += '\n'
                        return que_text_result, ans_text_result
                elif key["Theme"] == "Баллистика":
                    if key["Theme_section"] == "Свободное падение":
                        for i in range(int(key["N"])):
                            que_ans_text = TaskGenerator().ballistics_motion()
                            ans_text_result += f'{i + 1}) Ответ: '
                            for j, answer in enumerate(que_ans_text[1]):
                                ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                            que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                            ans_text_result += '\n'
                        return que_text_result, ans_text_result
                    elif key["Theme_section"] == "Баллистическое движение":
                        for i in range(int(key["N"])):
                            que_ans_text = TaskGenerator().ballistics_corner_motion()
                            ans_text_result += f'{i + 1}) Ответ: '
                            for j, answer in enumerate(que_ans_text[1]):
                                ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                            que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                            ans_text_result += '\n'
                        return que_text_result, ans_text_result

        elif key["Type"] == "КР":  # Контрольная работа
            if key["Subject"] == "Физика":
                if key["Theme"] == "Кинематика":
                    return self._generate_test(key, "kinematics")
                elif key["Theme"] == "Механика":
                    return self._generate_test(key, "mechanics")
                elif key["Theme"] == "Баллистика":
                    return self._generate_test(key, "ballistics")

        return "Тип работы не поддерживается", ""

    def _generate_test(self, key, test_type):
        que_text_result = ""
        ans_text_result = ""
        n = int(key["N"])

        # Распределение вопросов: 30% теории, 20% тестов, 50% задач
        num_questions = max(1, round(0.3 * n))
        num_tests = max(1, round(0.2 * n))
        num_problems = max(1, n - num_questions - num_tests)

        generator = TaskGenerator()

        # Теоретические вопросы
        for i in range(num_questions):
            if test_type == "kinematics":
                question = generator.questions_for_kr_kinematics()
            elif test_type == "mechanics":
                question = generator.questions_for_kr_mechanics()
            elif test_type == "ballistics":
                question = generator.questions_for_kr_ballistics()
            que_text_result += f'{i+1}) {question}\n\n'

        # Тестовые вопросы
        for i in range(num_tests):
            if test_type == "kinematics":
                test = generator.tests_for_kr_kinematics()
            elif test_type == "mechanics":
                test = generator.tests_for_kr_mechanics()
            elif test_type == "ballistics":
                test = generator.tests_for_kr_ballistics()
            que_text_result += f'{num_questions + i+1}) {test}\n\n'

        # Практические задачи
        for i in range(num_problems):
            if test_type == "kinematics":
                task = generator.phis_kr_kinematics()
            elif test_type == "mechanics":
                task = generator.phis_kr_mechanics()
            elif test_type == "ballistics":
                task = generator.phis_kr_ballistics()

            que_text_result += f'{num_questions + num_tests + i+1}) {task[0]}\n\n'
            ans_text_result += f'{num_questions + num_tests + i+1}) Ответ: {task[1][0]} {task[2][0]}\n'

        return que_text_result, ans_text_result


def GetTaskText(key):
    creator = Creator()
    result = creator.function_creator(key)
    return f"{result[0]}\n\nОтветы:\n{result[1]}"
