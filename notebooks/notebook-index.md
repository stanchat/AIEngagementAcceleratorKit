# 📓 Notebook Index for GenAI Engagement Kit

This page provides an overview of the core notebooks included in the project. These interactive Jupyter notebooks walk through prompt engineering, LangChain pipelines, Retrieval-Augmented Generation (RAG), evaluation metrics, and sandboxing ideas. All notebooks support both **OpenAI** and **Hugging Face** integrations.

---

## 🧭 Navigation Table

| Notebook File | Description | Key Features |
|---------------|-------------|---------------|
| `00_index.ipynb` | Overview hub for linking into all other notebooks. | Navigation, annotations |
| `01_prompt_basics.ipynb` | Explore prompt crafting with both OpenAI and Hugging Face models. | Prompt design, chaining, LLM APIs |
| `02_langchain_quickstart.ipynb` | Simple LangChain flows using PromptTemplate + LLMs. | Prompt chaining, LangChain basics |
| `03_rag_intro.ipynb` | Full RAG pipeline setup using FAISS, Chroma, and Pinecone. | Embeddings, retrievers, LangChain RAG |
| `04_eval_outputs.ipynb` | Score LLM-generated output with BLEU, ROUGE, and semantic similarity. | Output evaluation, NLTK, ROUGE metrics |
| `99_sandbox.ipynb` | Freeform notebook for prototyping new workflows. | Experimental workspace |

---

## ✅ Getting Started

Make sure your `.env` file is set up with the following:

```bash
OPENAI_API_KEY=your-key
HF_TOKEN=your-huggingface-token
VECTOR_DB_API_KEY=your-pinecone-api-key
VECTOR_DB_INDEX=your-index-name
```

Run this in terminal:
```bash
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

> _These notebooks are modular. Use them independently or in sequence, depending on your use case._

---

Happy experimenting! 🚀
