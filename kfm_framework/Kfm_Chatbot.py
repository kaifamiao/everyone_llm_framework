from kfm_framework.KfmComponentFactory import KfmComponentFactory
from kfm_framework.public import *


# 主类
class Kfm_Chatbot:
    def __init__(self, config: Dict[str, Any]):
        self.model = KfmComponentFactory.create_model(config['kfm_model'], config['kfm_model_param'])
        self.template = KfmComponentFactory.create_template(config['kfm_template'])
        self.vector = KfmComponentFactory.create_vector(config['kfm_vector'], config['kfm_knowledge_lib_param'])
        self.embedding = KfmComponentFactory.create_embedding(config['kfm_embedding'])
        self.chain = KfmComponentFactory.create_chain(config['kfm_chain'])

    def response(self, input: str, user_id: str, session_id: str) -> str:
        vectorized = self.vector.vectorize(input)
        embedded = self.embedding.embed(vectorized)
        processed = self.model.process(embedded)
        templated = self.template.apply(processed)
        return self.chain.execute(templated)

