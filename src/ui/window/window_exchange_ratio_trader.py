"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSpinBox

from src.ui.window.window_receive import WindowReceive
from src.ui.window.window_trade import WindowTrade
from src.ui.window.window_visualize import WindowVisualize
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/window/window_exchange_ratio_trader.ui'))


class WindowExchangeRatioTrader(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()

        self.window_receive = None
        self.window_visualize = None
        self.window_trade = None

        self.setupUi(self)
        self.init_signal()
        self.show()

    def init_signal(self):
        self.pushButton_receive.clicked.connect(self.on_clicked_receive)
        self.pushButton_visualize.clicked.connect(self.on_clicked_visualize)
        self.pushButton_trade.clicked.connect(self.on_clicked_trade)

    def on_clicked_receive(self):
        print('on_clicked_receive')
        self.window_receive = WindowReceive()

    def on_clicked_visualize(self):
        print('on_clicked_visualize')
        self.window_visualize = WindowVisualize()

    def on_clicked_trade(self):
        print('on_clicked_trade')
        self.window_trade = WindowTrade()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WindowExchangeRatioTrader()
    app.exec()
