from src.common.process import RatioProcess
from src.process_receive.receiver import DataReceiver


class RatioReceiveProcess(RatioProcess):
    """
    환율정보를 얻어오는 전체 프로세스
    """
    def run(self):
        receiver = DataReceiver()
        response = receiver.get(10)
        print(response.status_code)
        print(response.json())
        print(response.text)


proc = RatioReceiveProcess()
proc.run()
