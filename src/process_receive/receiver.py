import requests

from datetime import date, timedelta
from collections import OrderedDict


class Key:
    """
    환율정보를 얻어오는 API 요청 파라미터 인스턴스
    """
    def __init__(self, duration: int):
        self._auth_key = 'AJzeBrLvsmODLLS0JpVe9e0aFaKiTEt4'
        self._search_date = date.today() - timedelta(duration)
        self._data = 'AP01'

    @property
    def auth_key(self) -> str:
        return self._auth_key

    @property
    def search_date(self) -> str:
        return str(self._search_date)

    @property
    def data(self) -> str:
        return self._data


class DataReceiver:
    """
    환율정보를 얻어오는 클래스
    """
    def __init__(self):
        self.host = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        self.key = OrderedDict()

    def get(self, duration: int):
        # Key 객체 생성
        _key = Key(duration)
        # Key 객체의 프로퍼티로 요청 파라미터 생성
        self.key['authkey'] = _key.auth_key
        self.key['searchdate'] = _key.search_date
        self.key['data'] = _key.data
        # GET 요청 (response 를 얻어옴)
        res = requests.get(self.host, self.key)
        return res
