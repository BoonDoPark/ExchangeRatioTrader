"""
/***************************************************************************
        begin                : 2021-06-18
        email                : hsung951027@gmail.com
 ***************************************************************************/
"""
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QTableWidget

from src.utils.ui_utils_table import QTableFormat, QTableWidgetUtils
from src.utils.util_date import DateUtils
from src.utils.util_path import PathUtils

from src.process_receive.process_receive import RatioReceiveProcess
from src.process_visualize.process_visualize import RatioVisualizeProcess

FORM_CLASS, _ = uic.loadUiType(PathUtils.ui_path('../../../ui/window/window_visualize.ui'))


class WindowVisualize(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.proc_receive = RatioReceiveProcess.instance()

        self.refresh_table_widget()
        self.refesh_chart(duration=0)

        self.init_signal()
        self.show()

    def init_signal(self):
        self.spinBox_duration.valueChanged.connect(self.on_value_change_duration)

    def on_value_change_duration(self):
        self.refresh_table_widget()

    def refresh_table_widget(self):
        self.tableWidget_country_list: QTableWidget
        self.tableWidget_country_list.setRowCount(0)

        # duration 전의 날짜에 대한 환율 정보들을 수집
        duration = self.spinBox_duration.value()
        self.proc_receive.run(duration)
        key_date = DateUtils.before_duration(duration)
        exchange_ratios = self.proc_receive.ratios.get(key_date)

        form_display = QTableFormat()
        form_user = QTableFormat()

        for exchange_ratio in exchange_ratios:
            row = exchange_ratio.kftc_bkpr.split()
            if len(row) == 2:
                row.append(exchange_ratio.cur_unit)
                user_row = (row[2], row[2], row[2])
                form_display.append_by_row(row)
                form_user.append_by_row(user_row)

        QTableWidgetUtils.refresh_by_items(self.tableWidget_country_list, form_display, form_user)
        QTableWidgetUtils.resize_table_widget(self.tableWidget_country_list)

    def refesh_chart(self, duration):
        key_date = DateUtils.before_duration(duration)
        exchange_ratios = self.proc_receive.ratios.get(key_date)

        names = []
        for exchange_ratio in exchange_ratios:
            names.append((exchange_ratio.cur_unit, exchange_ratio.kftc_deal_bas_r))

            self.save_file = RatioVisualizeProcess(f'{names[0][0]}.png', key_date, names[0][1])
            self.save_file.run()
            self.save_file._visualizer.export_to_img()

        self.load_file = QPixmap()
        self.load_file.load(f'{names[0][0]}.png')
        self.label_for_pixmap.setPixmap(self.load_file)

