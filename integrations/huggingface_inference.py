# Hugging Face Transformers Integration Example
from transformers import pipeline

# Load a text generation model (e.g., GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Generate text from a prompt
prompt = "In the future, AI will"
output = generator(prompt, max_length=50, num_return_sequences=1)

print("Generated Text:", output[0]['generated_text'])
