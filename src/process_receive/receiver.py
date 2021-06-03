import requests
from datetime import date, timedelta


class DataReceiver:
    def __init__(self):
        self.yesterday = date.today() - timedelta(1)
        self.host = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        self.key = {'authkey': 'AJzeBrLvsmODLLS0JpVe9e0aFaKiTEt4',
                    'searchdate': str(self.yesterday),
                    'data': 'AP01'}

    def api_process(self):
        api = requests.get(self.host, self.key)
        return api


receiver = DataReceiver()
response = receiver.api_process()
print(response.status_code)
print(response.json())
print(response.text)
