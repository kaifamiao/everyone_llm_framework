from kfm_config import get_project_root
from kfm_framework.Kfm_Chatbot import Kfm_Chatbot

# 使用示例
kfm_config = {
    "kfm_model": "kfm_model1",
    "kfm_template": "kfm_template2",
    "kfm_vector": "vector2",
    "kfm_embedding": "embedding2",
    "kfm_chain": "chain3",
    "kfm_knowledge_lib_param": [{"k": 1, "chunk": 200, "overlap": 50}],
    "kfm_model_param": [{"p1": 0, "p2": 0, "p3": 0}, {"top": 1, "max_token": 9000}]
}

kfm = Kfm_Chatbot(kfm_config)
response = kfm.response("我叫什么名字", user_id="linrui", session_id="123")
print("response")
print(type(response))
print(response)
# for chunk in response:
#     print(chunk.content, end='', flush=True)

