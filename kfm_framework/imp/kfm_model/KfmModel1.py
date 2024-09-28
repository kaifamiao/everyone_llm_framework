# 接口实现
from kfm_framework.public import *
from kfm_framework.interface.kfm_model.KfmModel import KfmModel
from kfm_core.kfm_chatllama.KfmChatLlama import kfm_llm
from kfm_core.kfm_log.log_config import setup_logger
kfm_logger = setup_logger(__name__)

class KfmModel1(KfmModel):
    def __init__(self, params: Dict[str, Any]):
        self.params = params
        ppppp("KfmModel1  init llm  qwen2.5:latest")
        kfm_logger.info(f"KfmModel1 init params : {self.params}")

    def process(self, input: str) -> object:
        return kfm_llm
        # return f"Processed by KfmModel1 A: {input}"
