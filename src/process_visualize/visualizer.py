import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure


class DataVisualizer:
    @staticmethod
    def visualize(xs: list, ys: list, x_label: str = 'x', y_label: str = 'y'):
        """
        차트로 시각화
        :param y_label:
        :param x_label:
        :param xs: x 축 데이터
        :param ys: Y 축 데이터
        :return:
        """
        figure: Figure = plt.figure()
        ax = figure.add_subplot(1, 1, 1, xlabel=x_label, ylabel=y_label)
        x = np.array(xs)
        y = np.array(ys)
        ax.plot(x, y)
        # plt.show()
        return figure

    @staticmethod
    def export_to_img(file_name, figure):
        """
        차트를 이미지로 내보내는 메소드
        :return:
        """
        figure.savefig(file_name)

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
