# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
COPY streamlit_apps ./streamlit_apps
COPY .env.example .env

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run app
CMD ["streamlit", "run", "streamlit_apps/agentic_pdf_chroma_app.py"]
