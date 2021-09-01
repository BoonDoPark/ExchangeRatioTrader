from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem

from src.common.data import ExchangeRatio
from src.utils.ui_utils_table import QTableFormat, QTableWidgetUtils
from src.utils.util_date import DateUtils
from src.utils.util_path import PathUtils

from src.process_receive.process_receive import RatioReceiveProcess
from src.process_visualize.process_visualize import RatioVisualizeProcess


class TabVisualize:
    def __init__(self, window):
        self.window = window
        self.proc_receive = RatioReceiveProcess.instance()
        self.refresh_table_widget()
        self.init_signal()

    def init_signal(self):
        self.window.tableWidget_country_list.itemClicked.connect(self.on_clicked_refresh_chart)
        self.window.spinBox_duration.valueChanged.connect(self.on_value_change_duration)

    def on_value_change_duration(self):
        self.refresh_table_widget()

    def refresh_table_widget(self):
        self.window.tableWidget_country_list.setRowCount(0)

        # duration 전의 날짜에 대한 환율 정보들을 수집
        duration = self.window.spinBox_duration.value()
        self.proc_receive.run(duration)
        key_date = DateUtils.before_duration(duration)
        exchange_ratios = self.proc_receive.ratios.get(key_date)

        form_display = QTableFormat()
        form_user = QTableFormat()

        for exchange_ratio in exchange_ratios:
            display_row = exchange_ratio.kftc_bkpr.split()
            if len(display_row) != 2:
                continue
            display_row.append(exchange_ratio.cur_unit)
            user_row = (exchange_ratio,) * len(display_row)  # * 3
            form_display.append_by_row(display_row)
            form_user.append_by_row(user_row)

        QTableWidgetUtils.refresh_by_items(self.window.tableWidget_country_list, form_display, form_user)
        QTableWidgetUtils.resize_table_widget(self.window.tableWidget_country_list)

    def on_clicked_refresh_chart(self, item: QTableWidgetItem):
        duration = self.window.spinBox_duration.value()
        key_dates = []
        selected_exchange_ratio: ExchangeRatio = self.window.item.data(Qt.UserRole)
        selected_cur_unit = selected_exchange_ratio.cur_unit

        for d in range(duration, 0, -1):
            # 0일 전부터 duration 까지의 기간중 해당 일자의 데이터가 누락되어 있는 경우 환율 데이터 수집
            key_date = DateUtils.before_duration(d)
            key_dates.append(key_date)
            if key_date in self.proc_receive.ratios:
                continue
            self.proc_receive.run(d)

        selected_cur_unit_exchange_ratios = []
        for key_date in key_dates:
            # 각각의 일자로부터 선택된 아이템의 국가 코드와 일치하는 환율 정보들만 추출
            exchange_ratios = self.proc_receive.ratios.get(key_date)
            filtered_exchange_ratios = list(filter(lambda exchange_ratio: exchange_ratio.cur_unit == selected_cur_unit, exchange_ratios))
            selected_cur_unit_exchange_ratios.extend(filtered_exchange_ratios)
            if not len(filtered_exchange_ratios):
                # 주말에 대한 예외처리
                selected_cur_unit_exchange_ratios.append(ExchangeRatio(kftc_deal_bas_r=0))

            PathUtils.create_folder('imgs')
            # https://dev-ryuon.tistory.com/4?category=908968 : kwargs 참고
            selected_kftc_deal_bas_r = [str(exchange_ratio.kftc_deal_bas_r) for exchange_ratio in
                                        selected_cur_unit_exchange_ratios]
            params = {'file_name': f'{PathUtils.img_path(selected_cur_unit)}.png', 'xs': key_dates,
                      'ys': selected_kftc_deal_bas_r, 'x_label': f'{selected_cur_unit}', 'y_label': 'WON'}
            RatioVisualizeProcess.run(**params)

            self.pixmap = QPixmap()
            self.pixmap.load(f'{PathUtils.img_path(selected_cur_unit)}.png')
            # self.pixmap.load(f'{selected_cur_unit}.png')
            self.window.label_for_pixmap.setPixmap(self.pixmap)
