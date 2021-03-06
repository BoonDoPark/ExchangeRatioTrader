from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QMessageBox

from src.process_receive.process_receive import RatioReceiveProcess
from src.utils.ui_utils_table import QTableFormat, QTableWidgetUtils
from src.utils.util_date import DateUtils
from src.utils.util_path import PathUtils


class TabReceive:
    def __init__(self, window):
        self.window = window
        self.proc_receive = None
        self.refresh()
        self.init_signal()

    def init_signal(self):
        self.window.pushButton_refresh.clicked.connect(self.on_clicked_refresh)

    def refresh_table_widget(self, duration):
        print('refresh_table_widget', self.window)
        self.window.tableWidget_exchange_trader.setRowCount(0)
        key_date = DateUtils.before_duration(duration)
        exchange_ratios = self.proc_receive.ratios.get(key_date)
        form_display = QTableFormat()

        for r, exchange_ratio in enumerate(exchange_ratios):
            self.window.tableWidget_exchange_trader.insertRow(r)
            contents = (exchange_ratio.result,
                        exchange_ratio.cur_unit,
                        exchange_ratio.cur_nm,
                        exchange_ratio.ttb,
                        exchange_ratio.tts,
                        exchange_ratio.deal_bas_r,
                        exchange_ratio.bkpr,
                        exchange_ratio.yy_eeee_r,
                        exchange_ratio.ten_dd_efee_r,
                        exchange_ratio.kftc_deal_bas_r,
                        exchange_ratio.kftc_bkpr)
            form_display.append_by_row(contents)

        QTableWidgetUtils.refresh_by_items(self.window.tableWidget_exchange_trader, form_display)
        QTableWidgetUtils.resize_table_widget(self.window.tableWidget_exchange_trader)

    def refresh(self, duration=0):
        print('refresh', f'duration is {duration}')
        self.proc_receive = RatioReceiveProcess.instance()
        self.proc_receive.ratios.clear()
        self.proc_receive.run(duration)
        self.refresh_table_widget(duration)

    def on_clicked_refresh(self):
        self.spinBox_duration: QSpinBox
        duration = self.spinBox_duration.value()
        self.refresh(duration)
        msg = f'{duration}??? ?????? ????????? ??????????????????.' if duration != 0 else '????????? ????????? ??????????????????.'
        return QMessageBox.information(self, '??????', msg)