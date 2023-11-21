from langchain.chains import ConversationalRetrievalChain

class QueryManager:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever

    def get_response(self,query):
        qa = ConversationalRetrievalChain.from_llm(
            self.llm,
            self.retriever,
            return_source_documents=True
        )
        result = qa({"question": query, "chat_history":[]})
        return result['answer'], result['source_documents']