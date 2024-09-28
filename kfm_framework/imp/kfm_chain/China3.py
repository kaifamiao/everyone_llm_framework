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
class Chain3(KfmChain):

    def __init__(self):
        kfm_logger.debug("Chain3 is initialization")
        ppppp("Chain3 is initialization")
    def execute(self, input: Dict) -> str:
        print("==================== Chain3 execute Start ==================")
        print(type(input))
        print(f"input.get('model'){type(input.get('model'))}")
        print(input.get('kfm_embedding'))
        print(input.get('template'))
        print(input.get('vector'))
        print("==================== Chain3 execute Ebd ==================")

        kkm = input.get('model')


        chat = ChatChain3(input.get("input"),"", kkm, input.get('session_id'))
        # for chunk in chat.response_stream():
        #     print(chunk.content, end='', flush=True)

        return chat.response_str()



from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_session_history(session_id):
    db_path = "sqlite:///"+get_project_root() +"/chain_memory_data/chain3_memory.db"
    kfm_logger.debug(f"get_session_history db_path : {db_path}")
    return SQLChatMessageHistory(session_id, connection=db_path)
class ChatChain3:

    def __init__(self, input: str, prompt: str, llm="", session_id="abc"):
        self.response2 = None
        self.response1 = None
        self.config = None
        self.prompt=prompt
        if len(prompt) <2:
            self.prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a helpful assistant. Answer all questions to the best of your ability.",
                    ),
                    MessagesPlaceholder(variable_name="messages"),
                ]
            )
        print("use self.prompt")
        print(self.prompt)
        self.chain = self.prompt | llm
        self.with_message_history = RunnableWithMessageHistory(llm, get_session_history)
        self.session_id=session_id
        self.input=input

    def response_stream(self):
        self.config = {"configurable": {"session_id": self.session_id}}
        self.response1 = self.with_message_history.stream(
            [HumanMessage(content=self.input)],
            config=self.config,
        )
        return self.response1
    def response_str(self):
        self.config = {"configurable": {"session_id": self.session_id}}
        self.response2 = self.with_message_history.invoke(
            [HumanMessage(content=self.input)],
            config=self.config,
        )
        return self.response2

if __name__ == '__main__':
    chat=ChatChain3("","",kfm_llm,"linrui_abc4")
    # chat.response_stream()
    for chunk in chat.response_stream():
        print(chunk.content, end='', flush=True)
