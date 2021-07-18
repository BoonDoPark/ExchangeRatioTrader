"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/dialog/dialog_visualize.ui'))


class DialogVisualize(QDialog, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_signal()
        self.show()

    def init_signal(self):
        pass
