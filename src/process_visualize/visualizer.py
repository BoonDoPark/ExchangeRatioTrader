import matplotlib.pyplot as plt


# 그래프 이미지형태로 뽑아내는법 차트, 히스토그램
class DataVisualizer:
    def __init__(self, x_label: str = 'x', y_label: str = 'y'):
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
        # xs, ys, self._x_label, self._y_label 를 활용하여 차트를 그려볼것
        pass

    def export_to_img(self):
        """
        차트를 이미지로 내보내는 메소드
        :return:
        """
        pass

        
visualizer = DataVisualizer()
visualizer.visualize([1, 2, 3, 4], [2, 4, 6, 8])
