import pandas as pd
pd.options.mode.chained_assignment = None

from Class_Creator_for_App import *


def GetTaskText(key):
    print_text_result = Creator().function_creator(key)
    tasks = print_text_result[0]
    answers = print_text_result[1]
    text = tasks + '\n' + answers
    return text
