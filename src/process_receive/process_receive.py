from typing import List

from src.common.data import ExchangeRatio
from src.common.process import RatioProcess
from src.process_receive.receiver import DataReceiver


class RatioReceiveProcess(RatioProcess):
    """
    환율정보를 얻어오는 전체 프로세스
    """
    def __init__(self, duration: int = 0):
        self._duration = duration
        self._receiver = DataReceiver()
        self._ratios: List[ExchangeRatio] = list()

    @property
    def ratios(self) -> List[ExchangeRatio]:
        return self._ratios

    def run(self):
        response = self._receiver.get(self._duration)
        responses = response.json()
        # 응답 객체 생성 후 리스트에 보관
        for res in responses:
            # https://dev-ryuon.tistory.com/4?category=908968 참고
            v = list(res.values())
            self.ratios.append(ExchangeRatio(*v))
