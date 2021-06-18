from src.common.process import RatioProcess
from src.process_visualize.visualizer import DataVisualizer


class RatioVisualizeProcess(RatioProcess):
    def __init__(self, file_name: str, xs: list, ys: list, x_label: str = 'x', y_label: str = 'x'):
        self._xs = xs
        self._ys = ys
        self._visualizer = DataVisualizer(file_name=file_name,
                                          x_label=x_label,
                                          y_label=y_label)

    def run(self):
        self._visualizer.visualize(xs=self._xs, ys=self._ys)
