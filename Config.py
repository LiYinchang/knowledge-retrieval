class Config:
    def __init__(self):
        # OpenAI API Key
        self.OPENAI_API_KEY = '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'

    def get_openai_api_key(self):
        return self.OPENAI_API_KEY

# Instance of the Config class
config = Config()
