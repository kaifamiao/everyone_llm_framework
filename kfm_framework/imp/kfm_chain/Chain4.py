from typing import Dict

from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

from kfm_config import get_project_root
from kfm_core.kfm_chatllama.KfmChatLlama import kfm_llm
from kfm_framework.public import *
from kfm_framework.interface.kfm_chain.KfmChain import KfmChain

from kfm_core.kfm_log.log_config import setup_logger
# from kfm_core.kfm_chatllama.KfmChatLlama import kfm_llm
kfm_logger = setup_logger(__name__)
class Chain4(KfmChain):
    def __init__(self):
        kfm_logger.debug("Chain3 is initialization")
        ppppp("Chain4 is initialization")
        print("==================== Chain3 execute Start ==================")
        self.template=None
        self.kfm_embedding=None
        self.vector=None
        self.kfm_llm=None
        print("==================== Chain3 execute Ebd ==================")



    def execute(self, input: Dict) -> str:
        self.template = input.get('template')
        self.kfm_embedding = input.get('kfm_embedding')
        self.vector = input.get('vector')
        self.kfm_llm = input.get('model')
        return self.kfm_llm.stream(input.get("input"))


