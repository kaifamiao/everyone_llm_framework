from typing import Dict

from langchain_community.chat_models import ChatOllama

from kfm_core.kfm_utils.utils import ppppp
from kfm_framework.interface.kfm_chain.KfmChain import KfmChain

from kfm_core.kfm_log.log_config import setup_logger

kfm_logger = setup_logger(__name__)
class Chain1(KfmChain):
    def __init__(self):
        kfm_logger.debug("Chain1 is initialization")
        ppppp("Chain1 is initialization")

    def execute(self, input: Dict) -> str:
        print("==================== Chain1 execute Start ==================")
        print(type(input))
        print(f"input.get('model'){type(input.get('model'))}")
        print(input.get('kfm_embedding'))
        print(input.get('template'))
        print(input.get('vector'))
        print("==================== Chain1 execute Ebd ==================")

        kkm = input.get('model')
        res = kkm.invoke(input.get("input")).content
        return res