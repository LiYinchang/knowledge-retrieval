from Config import Config
from EmbeddingManager import EmbeddingManager
from LanguageModel import LanguageModel
from Retriever import Retriever
from QueryManager import QueryManager
from langchain.document_loaders import PyPDFDirectoryLoader

def main():
    # Load configuration
    config = Config()
    openai_api_key = config.get_openai_api_key()

    # Initialize Embedding Manager with the API key
    embedding_manager = EmbeddingManager(openai_api_key)
    embedding = embedding_manager.get_openai_embeddings()  
    e5_embedding = embedding_manager.get_hf_e5_large_v2_embeddings()
    hf_embedding = embedding_manager.get_hf_miniLM_embeddings()

    index_oai = 'index_oai'
    index_e5 = 'index_e5'
    
    # Initialize Language Model with the API key
    language_model = LanguageModel(temperature=0, openai_api_key=openai_api_key)
    llm = language_model.get_llm()
    llm_orca_mini = language_model.get_orca_mini_llm()

    # Allow user to choose the language model
    model_choice = input("Choose a language model (1 for gpt-4, 2 for orca-mini): ")
    if model_choice == "1":
        retriever = Retriever(embedding, index_oai, llm)
        selected_retriever = retriever.get_es_retriever()
        query_manager = QueryManager(llm, selected_retriever)
    elif model_choice == "2":
        retriever = Retriever(e5_embedding, index_e5, llm_orca_mini)
        selected_retriever = retriever.get_es_retriever()
        query_manager = QueryManager(llm, selected_retriever)
    else:
        retriever = Retriever(embedding, index_oai, llm)
        selected_retriever = retriever.get_es_retriever()
        query_manager = QueryManager(llm, selected_retriever)

    while True:
        # Allow user to input a query
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        response, source_documents = query_manager.get_response(query)
        print("Response:", response)
        print("--------------------")

if __name__ == "__main__":
    main()
