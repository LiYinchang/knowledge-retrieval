class Retriever:
    def __init__(self, embedding, index_name, llm):
        from langchain.vectorstores import Chroma, ElasticsearchStore
        from langchain.retrievers import SelfQueryRetriever, EnsembleRetriever, BM25Retriever
        from langchain.chains.query_constructor.base import AttributeInfo
        from langchain.document_loaders import PyPDFDirectoryLoader 

        # Elasticsearch retriever
        self.vectorstore = ElasticsearchStore(
            index_name = index_name, 
            es_url='http://localhost:9200', 
            embedding = embedding,
            # es_user=es_user, 
            # es_password=es_password
        )
        self.es_retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        
        # Self-querying retriever
        self.self_query_retriever = None

        # Metadata field information
        self.metadata_field_info = [
            AttributeInfo(
                name="disability_type",
                description="The type of disability being referenced. Examples include 'PTSD', 'hearing loss', 'musculoskeletal', 'mental health', etc.",
                type="string",
            ),
            AttributeInfo(
                name="compensation_criteria",
                description="Key criteria or conditions for compensation eligibility related to the disability",
                type="string",
            ),
            AttributeInfo(
                name="benefit_rate",
                description="The rate or range of VA disability compensation for the specific disability, often dependent on severity and other factors",
                type="string",
            ),
            AttributeInfo(
                name="documentation_required",
                description="Description of the documentation required for the compensation claim, such as medical records, service records, etc.",
                type="string",
            ),
        ]

        # Document content description
        self.document_content_description = "Answers to common questions or explanations related to VA disability compensation"

    def get_es_retriever(self):
        return self.es_retriever

    def setup_self_query_retriever(self, llm):
        from langchain.retrievers.self_query.base import SelfQueryRetriever
        self.self_query_retriever = SelfQueryRetriever.from_llm(
            llm,
            self.vectorstore,
            self.document_content_description,
            self.metadata_field_info,
        )

    def get_self_query_retriever(self):
        return self.self_query_retriever

    def get_ensemble_retriever(self):
        return self.ensemble_retriever
