from Class_Gener import *
from fpdf import FPDF


class Creator():
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

        # if key["Type"].lower() == "однотипные задания":
        if key["Subject"].lower() == "физика":
            if key["Theme"].lower() == "кинематика":
                if key["Theme_section"].lower() == "равномерное движение":
                    for i in range(int(key["N"])):
                        que_ans_text = TaskGenerator().uniform_motion()
                        ans_text_result += f'{i + 1}) Ответ: '
                        for j, answer in enumerate(que_ans_text[1]):
                            ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                        que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                        ans_text_result += '\n'
                    return que_text_result, ans_text_result
                elif key["Theme_section"].lower() == "равноускоренное движение":
                    for i in range(int(key["N"])):
                        que_ans_text = TaskGenerator().equiaxed_motion()
                        ans_text_result += f'{i + 1}) Ответ: '
                        for j, answer in enumerate(que_ans_text[1]):
                            ans_text_result += f'{answer} {que_ans_text[2][j]}; '
                        que_text_result += f'{i+1}) {que_ans_text[0]}\n\n'
                        ans_text_result += '\n'
                    return que_text_result, ans_text_result

        #         elif key["Theme"] == "баллистика":
        #             if key["Theme_section"] == "свободное падение тел":
        #                     for i in range(int(key["N"])):
        #                         que_text_result += f'{i+1}) {TaskGenerator().ballistics_motion()}\n\n'
        #                     return que_text_result
        #             elif key["Theme_section"] == "баллистическое движение":
        #                     for i in range(int(key["N"])):
        #                         que_text_result += f'{i+1}) {TaskGenerator().ballistics_corner_motion()}\n\n'
        #                     return que_text_result
        #         elif key["Theme"] == "статика":
        #             pass
        #         elif key["Theme"] == "работа и энергия":
        #             pass
        #     elif key["Subject"] == "математика":
        #         pass
        # elif key["Type"] == "контрольная работа":
        #     if key["Subject"] == "физика":
        #         if key["Theme"] == "кинематика":
        #             if key["Theme_section"] == "":
        #                 num_questions = round(0.3 * int(key["N"]))
        #                 num_tests = round(0.2 * int(key["N"]))
        #                 num_problems = int(key["N"]) - num_questions - num_tests
        #                 for i in range(num_questions):
        #                     que_text_result += f'{i+1}) {TaskGenerator().questions_for_kr_kinematics()}\n\n'
        #                 for i in range(num_tests):
        #                     que_text_result += f'{num_questions + i+1}) {TaskGenerator().tests_for_kr_kinematics()}\n\n'
        #                 for i in range(num_problems):
        #                     que_text_result += f'{num_questions + num_tests + i+1}) {TaskGenerator().phis_kr_kinematics()}\n\n'
        #                 return que_text_result
        #         elif key["Theme"] == "механика":
        #             if key["Theme_section"] == "":
        #                 for i in range(int(key["N"])):
        #                     que_text_result += f'{i+1}) {TaskGenerator().phis_kr_mechanics()}\n\n'
        #                 return que_text_result
        #         elif key["Theme"] == "баллистика":
        #             if key["Theme_section"] == "":
        #                 for i in range(int(key["N"])):
        #                     que_text_result += f'{i+1}) {TaskGenerator().phis_kr_ballistics()}\n\n'
        #                 return que_text_result