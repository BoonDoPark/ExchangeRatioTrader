from src.common.process import RatioProcess
from src.process_receive.receiver import DataReceiver


class RatioReceiveProcess(RatioProcess):
    """
    환율정보를 얻어오는 전체 프로세스
    """
    def run(self):
        receiver = DataReceiver()
        response = receiver.get(1)
        print(response)
        print(response.status_code)
        print(response.json())


proc = RatioReceiveProcess()
proc.run()
