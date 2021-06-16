import matplotlib.pyplot as plt
from src.process_receive.process_receive import proc
from src.process_receive.receiver import DataReceiver
# 그래프 이미지형태로 뽑아내는법 차트, 히스토그램
class DataVisualizer:
    def __init__(self):
        data = DataReceiver()
        self.day = data
        self.day = data.get(0)
        self.exchange = proc._ratios()

    def func_x(self):
        pass

    def func_y(self):
        pass

    def run(self):
        # func_x값에 임시로 숫자를 넣어줌
        self.mat = plt.plot([self.day], self.exchange)
        # return self.mat.show()
        return self.mat


d = DataVisualizer()
d.run()
