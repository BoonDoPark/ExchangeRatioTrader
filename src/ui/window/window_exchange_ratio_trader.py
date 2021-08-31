"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSpinBox

from src.ui.tab.tab_receive import TabReceive
from src.ui.tab.tab_visualize import TabVisualize
from src.ui.window.window_receive import WindowReceive
from src.ui.window.window_trade import WindowTrade
from src.ui.window.window_visualize import WindowVisualize
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('/window/window_exchange_ratio_trader.ui'))


class WindowExchangeRatioTrader(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tab_receive = TabReceive(self)
        self.tab_visualize = TabVisualize(self)

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WindowExchangeRatioTrader()
    app.exec()
