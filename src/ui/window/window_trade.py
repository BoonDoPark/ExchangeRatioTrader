"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/window/window_trade.ui'))


class WindowTrade(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_signal()
        self.show()

    def init_signal(self):
        pass
