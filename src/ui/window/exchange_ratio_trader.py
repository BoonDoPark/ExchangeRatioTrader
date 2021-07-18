"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from src.ui.dialog.dialog_receive import DialogReceive
from src.ui.dialog.dialog_trade import DialogTrade
from src.ui.dialog.dialog_visualize import DialogVisualize
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/window/window_exchange_ratio_trader.ui'))


class WindowExchangeRatioTrader(QMainWindow, FORM_CLASS):
    def __init__(self):
        print(PathUtils.ui_path('window\\window_exchange_ratio_trader.ui'))
        super().__init__()

        self.dialog_receive = None
        self.dialog_visualize = None
        self.dialog_trade = None

        self.setupUi(self)
        self.init_signal()
        self.show()

    def init_signal(self):
        self.pushButton_receive.clicked.connect(self.on_clicked_receive)
        self.pushButton_visualize.clicked.connect(self.on_clicked_visualize)
        self.pushButton_trade.clicked.connect(self.on_clicked_trade)

    def on_clicked_receive(self):
        print('on_clicked_receive')
        self.dialog_receive = DialogReceive()

    def on_clicked_visualize(self):
        print('on_clicked_visualize')
        self.dialog_visualize = DialogVisualize()

    def on_clicked_trade(self):
        print('on_clicked_trade')
        self.dialog_trade = DialogTrade()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WindowExchangeRatioTrader()
    app.exec()
