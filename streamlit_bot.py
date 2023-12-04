import streamlit as st
from query_bot import *  # Replace with your actual script import

# Load configuration at startup
config = load_configuration()
openai_api_key = config.get_openai_api_key()

# UI for API Key (you can make this hidden or pre-loaded)
api_key = st.text_input("Enter API Key", openai_api_key)

embeddings, llms = initialize_components(api_key)

# UI for model choice
model_choice = st.selectbox("Choose a language model", ['gpt-4', 'orca-mini'])

# Conditional UI for index choice if gpt-4 is selected
if model_choice == 'gpt-4':
    index_choice = st.selectbox("Choose an index", ['index_repo', 'index_ui_wb', 'index_oai'])
else:
    index_choice = 'index_e5'  # Default or alternative for other models

# UI for Query
user_query = st.text_input("Enter your query")

# When the user submits a query
# if st.button('Submit'):
#     try:
#         query_manager = create_retriever_and_query_manager(embeddings, llms, model_choice, index_choice)  # Pass the index choice here
#         response, source_documents = query_manager.get_response(user_query)
#         st.write("Response:", response)
#     except Exception as e:
#         st.error(f"An error occurred: {e}")

# ... previous code ...

# When the user submits a query
if st.button('Submit'):
    try:
        query_manager = create_retriever_and_query_manager(embeddings, llms, model_choice, index_choice)
        response, source_documents = query_manager.get_response(user_query)
        
        # Displaying the response
        if response:
            st.subheader("Response:")
            st.write(response)
            # st.subheader("Source Documents:")
            # for doc in source_documents:
            #     st.write(doc)  # Adjust this based on how you want to display source documents

    except Exception as e:
        st.error(f"An error occurred: {e}")
