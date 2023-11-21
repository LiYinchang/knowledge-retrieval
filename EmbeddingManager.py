class EmbeddingManager:
    def __init__(self, openai_api_key):
        from langchain.embeddings import OpenAIEmbeddings, HuggingFaceBgeEmbeddings

        # OpenAI Embeddings
        self.openai_embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

        # HuggingFace Embeddings
        self.hf_embeddings_miniLM = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        self.hf_embeddings_e5_large_v2 = HuggingFaceBgeEmbeddings(model_name='intfloat/e5-large-v2')

    def get_openai_embeddings(self):
        return self.openai_embeddings

    def get_hf_miniLM_embeddings(self):
        return self.hf_embeddings_miniLM

    def get_hf_e5_large_v2_embeddings(self):
        return self.hf_embeddings_e5_large_v2


