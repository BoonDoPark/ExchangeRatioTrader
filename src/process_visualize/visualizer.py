import matplotlib.pyplot as plt
from src.process_receive.process_receive import proc

# 그래프 이미지형태로 뽑아내는법 차트, 히스토그램
class DataVisualizer:
    def __init__(self):
        self.day = proc.run()
        self.exchange = proc.ratios()

    def func_x(self):
        pass

    def func_y(self):
        pass

    def run(self):
        # func_x값에 임시로 숫자를 넣어줌
        self.mat = plt.plot([self.func_x], [self.func_y])
        # return self.mat.show()
        pass


d = DataVisualizer
print(d)