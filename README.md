# Conversational Knowledge Retrieval System on VA Disability Compensation

## Overview
This repository demonstrates the integration of GPT-4, the open-source model Orca Mini, various vector databases, and LangChain to develop a conversational knowledge retrieval system tailored for the VA disability compensation website. 

## Key Features and Experiments
- **Multiple Vector Databases and Retrieval Methods**: Incorporation of Elasticsearch, Chrom, FAISS, Self-querying, and ensemble methods for data retrieval.
- **Quality Assurance with NeMo Guardrail**: Implementation of NeMo Guardrail to ensure high-quality responses.
- **Comprehensive Evaluation**: A batch evaluation was conducted on a set of 10 questions, each with manually created ground truths, using the RAG framework. The evaluation metrics and their respective average scores are:
  - Answer Correctness: 82%
  - Answer Relevancy: 89%
  - Context Precision: 94%
  - Context Recall: 85%
- **Interactive Query Chatbot**: Development of a terminal-based chatbot enabling user interactions. Users can choose between the GPT-4 or the open-source Orca Mini model for responses.

## Prerequisites
- **Elasticsearch Setup**:
  To run Elasticsearch locally, execute the following Docker command:
  ```bash
  docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.http.ssl.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.9.0
  ```
  After setting up Elasticsearch, proceed to ingest data by running `Experiments/knowledge_retrieval_experiment.ipynb`.

- **Open-Source LLM**:
  For using the open-source LLM, install Ollama from [here](https://github.com/jmorganca/ollama).

## Getting Started with the Query Chatbot
1. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Chatbot**:
   ```bash
   python query_bot.py 
   ```

## Sample Outputs
- **GPT-4 with OpenAI Embedding and Elasticsearch**:
  ![Output from GPT-4, OpenAI embedding, and Elasticsearch](pics/GPT4_Example.png)

- **Orca Mini with e5 Embedding and Elasticsearch**:
  ![Output from Orca Mini, e5 embedding, and Elasticsearch](pics/Orca_Mini_Example.png)

## Future Work

The ongoing development and enhancement of the RAG system will focus on several key areas to improve performance and functionality. Our planned initiatives include:

1. **PDF Document Preprocessing**: Implementing advanced techniques for processing and extracting information from PDF documents. This will improve the system's ability to access and utilize data from a variety of sources.

2. **Optimized Chunking Strategies**: Developing and testing various chunking strategies to efficiently manage and process large datasets. This will enhance the system's capability to handle complex queries and deliver more precise results.

3. **Enhanced Vector Search Capabilities**: 
    - **Semantic Search Integration**: Leveraging advanced semantic search techniques to improve the accuracy and relevancy of search results.
    - **Proprietary LLM Utilization**: Exploring the use of proprietary Large Language Models (LLMs) to enrich the system's understanding and processing of natural language queries.

4. **Batch Experiment Framework Establishment**: Setting up a comprehensive batch experiment framework, possibly utilizing AWS Batch. This framework will enable systematic testing to identify the most effective combinations of RAG approaches and LLMs. The goal is to optimize performance through empirical evaluation and fine-tuning.

