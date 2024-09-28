from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="qwen2.5:latest")
for chunk in llm.stream("给我一首杜甫的诗"):
    print(chunk.content, end='', flush=True)