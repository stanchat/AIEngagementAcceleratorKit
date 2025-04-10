# ai_model_wrapper.py

from typing import List
import openai
from transformers import pipeline

class AIModelWrapper:
    def __init__(self, backend: str, api_key: str = None):
        self.backend = backend
        if backend == 'openai':
            openai.api_key = api_key
        elif backend == 'huggingface':
            self.generator = pipeline("text-generation", model="gpt2")
        else:
            raise ValueError("Unsupported backend")

    def generate(self, prompt: str, **kwargs) -> str:
        if self.backend == 'openai':
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']
        elif self.backend == 'huggingface':
            output = self.generator(prompt, max_length=50, num_return_sequences=1)
            return output[0]['generated_text']
