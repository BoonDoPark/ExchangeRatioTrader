import datetime
from typing import List, Dict

from src.common.data import ExchangeRatio
from src.common.process import RatioProcess
from src.patterns.pattern_singletone import SingletonInstance
from src.process_receive.receiver import DataReceiver
from src.utils.util_date import DateUtils


class RatioReceiveProcess(RatioProcess, SingletonInstance):
    """
    환율정보를 얻어오는 전체 프로세스
    """
    def __init__(self):
        self._receiver = DataReceiver()
        self._ratios: Dict[str, List[ExchangeRatio]] = dict()

    @property
    def ratios(self) -> Dict[str, List[ExchangeRatio]]:
        return self._ratios

    def run(self, duration: int = 0):
        key_date = DateUtils.before_duration(duration)
        self.ratios.setdefault(key_date, list()).clear()
        response = self._receiver.get(duration)
        responses = response.json()
        # 응답 객체 생성 후 리스트에 보관
        for res in responses:
            # https://dev-ryuon.tistory.com/4?category=908968 참고
            v = list(res.values())
            self.ratios.setdefault(key_date, list()).append(ExchangeRatio(*v))
