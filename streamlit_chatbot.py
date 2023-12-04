import streamlit as st
from query_bot import * 
from ingest_data_es import *
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
# Retrieve all indices as a string
indices_string = es.cat.indices()

# Splitting the string by line breaks to get each index information
indices_info = indices_string.strip().split('\n')

# Extracting index names and storing them in a list
index_names = [index.split()[2] for index in indices_info]

# Load configuration and initialize components
config = load_configuration()
openai_api_key = config.get_openai_api_key()
embeddings, llms = initialize_components(openai_api_key)

# Initialize conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Chat interface
st.title("Knowledge-Retrieval Chatbot")
st.sidebar.write("This Chatbot will help you retrieve information based on selected Index")

index_options = index_names

# Display the selectbox in the sidebar
selected_index = st.sidebar.selectbox("Choose an index", index_options, key="index_choice")

# Function to handle sending of the query
def handle_send():
    user_query = st.session_state.query  # Get the current query
    if user_query:
        # Update conversation with user query
        st.session_state.conversation.insert(0, f"**You**: {user_query}")
        # Process query and get response
        model_choice = 'gpt-4'  # or any default/selected model
        query_manager = create_retriever_and_query_manager(embeddings, llms, model_choice, selected_index)
        try:
            response = query_manager.get_response(user_query)
            # Update conversation with response
            st.session_state.conversation.insert(0, f"**Bot**: {response}")
        except Exception as e:
            st.session_state.conversation.insert(0, f"**Bot**: An error occurred - {e}")

    # Reset the query input
    st.session_state.query = ""

# Text input for user query
st.text_input("Your Message", key="query", on_change=handle_send)

# Display conversation history
st.write("Conversation:")
for chat in st.session_state.conversation:
    st.markdown(chat)
