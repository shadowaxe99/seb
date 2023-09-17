import openai

class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze_text(self, text):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()