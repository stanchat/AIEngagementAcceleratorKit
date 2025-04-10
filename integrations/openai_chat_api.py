# OpenAI API Integration Example
import openai
import os

# Set your API key securely (e.g., via environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Send a prompt to OpenAI GPT-4 model
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the concept of Retrieval-Augmented Generation (RAG)."}
    ]
)

print("OpenAI Response:", response['choices'][0]['message']['content'])
