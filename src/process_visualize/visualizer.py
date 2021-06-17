import numpy as np
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, file_name: str, x_label: str = 'x', y_label: str = 'y'):
        # 이미지 파일명
        self._file_name = file_name
        # x, y 축 라벨
        self._x_label = x_label
        self._y_label = y_label

    def visualize(self, xs: list, ys: list):
        """
        차트로 시각화
        :param xs: x 축 데이터
        :param ys: Y 축 데이터
        :return:
        """
        figure = plt.figure()
        ax = figure.add_subplot(1, 1, 1)
        x = np.array(xs)
        y = np.array(ys)
        ax.plot(x, y)
        ax.set_xlabel(self._x_label)
        ax.set_ylabel(self._y_label)
        plt.show()
        return figure

    def export_to_img(self, figure):
        """
        차트를 이미지로 내보내는 메소드
        :return:
        """
        figure.savefig(self._file_name)

        
visualizer = DataVisualizer('plot.png')
figure = visualizer.visualize([1, 2, 3, 4], [4, 6, 8, 2])
visualizer.export_to_img(figure)
