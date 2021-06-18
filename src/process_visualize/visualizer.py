import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure


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
        figure: Figure = plt.figure()
        ax = figure.add_subplot(1, 1, 1, xlabel=self._x_label, ylabel=self._y_label)
        # ax.set_xlabel(self._x_label)
        # ax.set_ylabel(self._y_label)
        x = np.array(xs)
        y = np.array(ys)
        ax.plot(x, y)
        plt.show()
        return figure

    def export_to_img(self, figure):
        """
        차트를 이미지로 내보내는 메소드
        :return:
        """
        figure.savefig(self._file_name)

    # def subplot_exam(self):
    #     """
    #     subplot 연습용 메소드
    #     :return:
    #     """
    #     figure: Figure = plt.figure()
    #     axes1, axes2 = figure.subplots(2, 2)
    #     print(axes1); print(axes2)
    #     ax1, ax2 = axes1; ax3, ax4 = axes2
    #     ax1.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
    #     ax2.hist(np.random.randn(30))
    #     plt.show()
