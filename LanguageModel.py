class LanguageModel:
    def __init__(self, temperature=0, openai_api_key=None):
        from langchain.chat_models import ChatOpenAI
        from langchain.callbacks.manager import CallbackManager
        from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
        from langchain.llms import Ollama

        # Initialize the standard language model with the provided API key
        self.llm = ChatOpenAI(model_name='gpt-4', temperature=temperature, openai_api_key=openai_api_key)

        # Initialize the orca-mini model using Ollama
        self.llm_orca_mini = Ollama(
            model='orca-mini', 
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )

    def get_llm(self):
        return self.llm

    def get_orca_mini_llm(self):
        return self.llm_orca_mini
