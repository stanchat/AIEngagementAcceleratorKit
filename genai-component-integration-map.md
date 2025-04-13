# 🔗 GenAI Component Integration Map

This visual and conceptual overview explains how the major technical components of the AI Engagement Accelerator Kit connect to form a **cohesive experience** for developers, architects, and engagement teams.

---

## 🧭 Flow of Usage

```
[ Data Ingestion + Indexing (PDFs, Notion) ]
            │
            ▼
     [ Vector Store Setup ] ←───────┐
            │                      │
            ▼                      │
  [ RAG Pipeline & LangChain Wrapper ]
            │
            ▼
  [ Streamlit Dashboard + Gradio UI ] ←─ Prompt Playground, RAG QA Chat, QA Feedback
            │
            ▼
      [ Logs + Output Evaluation ]  ─→ Evaluation Notebooks, CI Scripts
```

---

## 🔧 Component Roles

| Component                 | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `notion_ingestion.py`    | Grabs content from Notion and formats for embedding                         |
| `index_pdfs.py`          | Converts PDFs to chunks and indexes in FAISS or Pinecone                    |
| `rag_model_wrapper.py`   | LangChain-based retrieval-augmented generation pipeline                     |
| `streamlit_rag_app.py`   | Business-friendly UI for testing RAG search and responses                   |
| `gradio_rag_app.py`      | Dev-facing, component-level interface to test prompts and embeddings        |
| `validate_model_response.py` | Performs semantic similarity, hallucination checks, and scoring             |
| `notebooks/04_eval_outputs.ipynb` | Deep-dive notebook for RAG evaluation pipelines and scoring            |

---

## 🧠 Suggested Workflow for Teams

1. Ingest content → `PDF` / `Notion`
2. Index using vector store of choice (local or cloud)
3. Plug into `rag_model_wrapper.py` for LangChain-style orchestration
4. Expose prototype via `streamlit_rag_app.py` or `gradio_rag_app.py`
5. Evaluate output with `validate_model_response.py` or notebook
6. Collaborate across PM/QA/UX teams using Streamlit feedback hooks

---

> By connecting ingestion, retrieval, interaction, and evaluation, this kit becomes a modular yet **end-to-end GenAI reference architecture** for internal use or prototyping.
