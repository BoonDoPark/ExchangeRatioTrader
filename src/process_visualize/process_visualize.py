from src.common.process import RatioProcess
from src.process_visualize.visualizer import DataVisualizer


class RatioVisualizeProcess:
    @staticmethod
    def run(xs: list, ys: list, x_label: str = 'x', y_label: str = 'y', file_name: str = ''):
        figure = DataVisualizer.visualize(xs, ys, x_label, y_label)
        DataVisualizer.export_to_img(file_name, figure)
