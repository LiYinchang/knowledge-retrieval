# Import necessary libraries
import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.vectorstores import Chroma, ElasticsearchStore
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.embeddings import OpenAIEmbeddings
import os

os.environ["OPENAI_API_KEY"] = ''
# Initialize the Chat model
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Function to ingest data and create Elasticsearch index
def ingest_and_index(repo_path, index_name):
    # Load documents from the file system
    loader = GenericLoader.from_filesystem(
        repo_path,
        glob="**/*",
        suffixes=[".py",".js",".csv",".txt"],
        parser=LanguageParser(),
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # Split the documents
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    texts = python_splitter.split_documents(documents)
    print(f"Split into {len(texts)} text chunks.")

    # Embeddings and Elasticsearch setup
    embedding = OpenAIEmbeddings()
    es_db = ElasticsearchStore.from_documents(
        texts,
        embedding,
        es_url="http://localhost:9200",
        index_name=index_name,
        distance_strategy="COSINE",
    )
    print(f"Elasticsearch index '{index_name}' created.")

# Main function
if __name__ == "__main__":
    repo_path = input("Enter the directory path to ingest data from: ")
    index_name = input("Enter the Elasticsearch index name (optional, press Enter to use default): ")
    ingest_and_index(repo_path, index_name)
