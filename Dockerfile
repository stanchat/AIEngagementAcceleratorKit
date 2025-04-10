# Dockerfile for CLI or App
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install gradio langchain openai faiss-cpu PyPDF2

CMD ["python", "tools/cli_test_model.py", "--backend", "huggingface", "--prompt", "Hello AI"]
