from Config import Config
from EmbeddingManager import EmbeddingManager
from LanguageModel import LanguageModel
from Retriever import Retriever
from QueryManager import QueryManager
from langchain.document_loaders import PyPDFDirectoryLoader

def load_configuration():
    """
    Loads configuration settings.
    Returns: Config object with necessary settings.
    """
    config = Config()
    return config

def initialize_components(api_key):
    """
    Initializes and returns key components based on the API key.
    """
    embedding_manager = EmbeddingManager(api_key)
    embeddings = {
        'openai': embedding_manager.get_openai_embeddings(),
        'e5_large_v2': embedding_manager.get_hf_e5_large_v2_embeddings(),
    }

    language_model = LanguageModel(temperature=0, openai_api_key=api_key)
    llms = {
        'gpt-4': language_model.get_llm(),
        'orca-mini': language_model.get_orca_mini_llm()
    }

    return embeddings, llms

def get_user_model_choice():
    """
    Presents a menu to the user to choose a language model.
    Returns: A string representing the user's choice.
    """
    choices = {
        '1': 'gpt-4',
        '2': 'orca-mini'
    }
    for key, value in choices.items():
        print(f"{key}: {value}")
    choice = input("Choose a language model: ")
    return choices.get(choice, 'gpt-4')

def get_index_choice():
    """
    Presents a menu to the user to choose an index if gpt-4 is selected.
    Returns: A string representing the user's index choice.
    """
    choices = {
        '1': 'index_repo',
        '2': 'index_ui_wb',
        '3': 'index_oai'
    }
    for key, value in choices.items():
        print(f"{key}: {value}")
    choice = input("Choose an index: ")
    return choices.get(choice, 'index_repo')

def create_retriever_and_query_manager(embeddings, llms, model_choice, index_choice):
    """
    Creates and returns a retriever and query manager based on the chosen model.
    """
    if model_choice == 'gpt-4':
        index_choice = index_choice
    else:
        index_choice = 'index_e5'

    embedding = embeddings['openai'] if model_choice == 'gpt-4' else embeddings['e5_large_v2']
    llm = llms[model_choice]
    retriever = Retriever(embedding, index_choice, llm)
    selected_retriever = retriever.get_es_retriever()
    query_manager = QueryManager(llm, selected_retriever)
    return query_manager

def main():
    config = load_configuration()
    openai_api_key = config.get_openai_api_key()

    embeddings, llms = initialize_components(openai_api_key)
    model_choice = get_user_model_choice()
    index_choice = get_index_choice()
    query_manager = create_retriever_and_query_manager(embeddings, llms, model_choice, index_choice)

    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        try:
            response = query_manager.get_response(query)
            print("Response:", response)
            print("--------------------")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
