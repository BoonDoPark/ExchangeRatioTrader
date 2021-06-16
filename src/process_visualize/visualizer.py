import matplotlib.pyplot as plt
from src.process_receive.process_receive import RatioReceiveProcess


# 그래프 이미지형태로 뽑아내는법 차트, 히스토그램
class DataVisualizer:
    def __init__(self):
        self.proc = RatioReceiveProcess()
        self.proc.run(duration=1)

    def run(self):
        ratios = self.proc.ratios
        print(ratios)

        
visualizer = DataVisualizer()
visualizer.run()
