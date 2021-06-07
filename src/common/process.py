from abc import *


class RatioProcess(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass
