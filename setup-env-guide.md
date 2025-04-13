# 🔐 Environment Setup Guide (.env Configuration)

This guide explains how to securely set up your environment variables for working with APIs like OpenAI, Hugging Face, and LangChain. These credentials are required to run the notebooks, Streamlit dashboards, and Gradio apps in this project.

---

## 📁 Step 1: Create a `.env` File
Create a new file in the root of the project directory named `.env`.

### Example `.env` File:
```env
# OpenAI API
OPENAI_API_KEY=sk-xxxxx

# Hugging Face API
HF_TOKEN=hf_xxxxx

# LangChain or other LLM provider
LANGCHAIN_API_KEY=your-langchain-api-key

# Optional for Pinecone, Weaviate, etc.
VECTOR_DB_API_KEY=your-db-key
VECTOR_DB_INDEX=my-genai-index
```

---

## 🚫 Important Security Notice
- **Do NOT commit** this `.env` file to GitHub or version control.
- Always include `.env` in your `.gitignore` file:

```bash
# .gitignore
.env
```

- If you are collaborating, share keys securely using a vault or password manager.

---

## 🧠 How the Project Uses These Variables

| Variable             | Used In                               | Description                            |
|----------------------|----------------------------------------|----------------------------------------|
| `OPENAI_API_KEY`     | Notebooks, Gradio, Streamlit           | Access OpenAI's GPT models             |
| `HF_TOKEN`           | Helpers, Notebooks                     | Auth for Hugging Face Transformers     |
| `LANGCHAIN_API_KEY`  | RAG pipeline and vector integrations   | Power LangChain-powered workflows      |
| `VECTOR_DB_API_KEY`  | RAG helpers and vector store access    | Secures connection to vector databases |

In code:
```python
import os
openai_key = os.getenv("OPENAI_API_KEY")
```

---

## ✅ Quick Test
To confirm your `.env` is configured:
```bash
# Activate virtual environment
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dotenv if not present
pip install python-dotenv

# Run a quick test
python helpers/test_env.py
```

Create `helpers/test_env.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))
```

---

Having your API keys centralized and managed through a `.env` file allows for safe, portable collaboration across teams and environments.

> Keep it secure. Keep it clean. Automate when needed.
