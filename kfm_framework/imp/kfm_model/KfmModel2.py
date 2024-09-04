# 接口实现
from kfm_framework.public import *


from kfm_framework.interface.kfm_model.KfmModel import KfmModel

class KfmModel2(KfmModel):
    def __init__(self, params: Dict[str, Any]):
        self.params = params
        print(f"KfmModel2 B init params : {self.params}")

    def process(self, input: str) -> str:
        return f"Processed by KfmModel2 B: {input}"