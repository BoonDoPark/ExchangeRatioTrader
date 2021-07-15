"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('..\\..\\..\\ui\\window\\ExchangeRatioTrader.ui'))


class WindowExchangeRatioTrader(QMainWindow, FORM_CLASS):
    def __init__(self):
        print(PathUtils.ui_path('window\\ExchangeRatioTrader.ui'))
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WindowExchangeRatioTrader()
    app.exec()
