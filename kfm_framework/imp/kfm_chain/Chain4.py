from typing import Dict

from langchain_community.chat_models import ChatOllama

from kfm_framework.interface.kfm_chain.KfmChain import KfmChain

from kfm_framework.interface.kfm_chain.KfmChain import KfmChain
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory



class Chain8(KfmChain):

    def execute(self, input: Dict) -> object:
        self.llm = input.get('model')
        self.llm = input.get('kfm_embedding')
        self.llm = input.get('template')
        self.llm = input.get('vector')

        haohao_llm= ChatOllama(models="llama3.1")

        return haohao_llm.stream(input.get("input"))


