from kfm_framework.public import *

class KfmChain(ABC):
    @abstractmethod
    def execute(self, input: str) -> str:
        pass
