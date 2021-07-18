"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow

from src.process_receive.process_receive import RatioReceiveProcess
from src.utils.util_path import PathUtils

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/window/window_receive.ui'))


class WindowReceive(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.proc_receive = RatioReceiveProcess(10)
        self.proc_receive.run()

        self.refresh_table_widget()

        self.init_signal()
        self.show()

    def init_signal(self):
        pass

    def refresh_table_widget(self):
        print('refresh_table_widget')
        print(self.tableWidget_exchange_trader)
        self.tableWidget_exchange_trader: QTableWidget
        self.tableWidget_exchange_trader.setRowCount(0)

        for r, exchange_ratio in enumerate(self.proc_receive.ratios):
            self.tableWidget_exchange_trader.insertRow(r)
            contents = [exchange_ratio.result,
                        exchange_ratio.cur_unit,
                        exchange_ratio.ttb,
                        exchange_ratio.tts,
                        exchange_ratio.deal_bas_r,
                        exchange_ratio.bkpr,
                        exchange_ratio.yy_eeee_r,
                        exchange_ratio.ten_dd_efee_r,
                        exchange_ratio.kftc_deal_bas_r,
                        exchange_ratio.kftc_bkpr]
            for c, content in enumerate(contents):
                print(r, c)
                item = QTableWidgetItem(content)
                self.tableWidget_exchange_trader.setItem(r, c, item)
