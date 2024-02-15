import numpy as np
import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
class Drow():
    def __init__(self,Object):
        self.object =  Object
    'Класс для отрисовки данных'
    def DrowSimplePlot(self):
        N = 100
        fig = go.Figure()
        x = np.linspace(0,2*np.pi,N)
        if self.object.ChooseFunction.value == 'Sin':
            y = np.sin(x)*float(self.object.InputA.value)
        elif self.object.ChooseFunction.value == 'Cos':
            y = np.cos(x)*float(self.object.InputA.value)
        else:
            raise ValueError('Функция не выбрана')
        fig.add_trace(go.Line(x=x,y=y))
        fig.show()