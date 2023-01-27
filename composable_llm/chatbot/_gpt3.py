import openai


class GPT3Model:
    def __init__(self, api_key, temperature=0.9, max_tokens=150,
                 top_p=1, frequency_penalty=1,
                 presence_penalty=1):
        openai.api_key = api_key

        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def ask(self, context, question):
        # initialize the model
        response = openai.Completion.create(
            engine="text-curie-001",
            prompt=f"{context} {question}",
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        return response.choices[0].text
