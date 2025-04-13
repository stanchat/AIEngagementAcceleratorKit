# 🧪 Notebook Structure and Pruning Guide

To ensure clarity, alignment, and value for GenAI-focused teams, the notebook directory has been reviewed and updated to reflect a more targeted and helpful structure.

---

## ✅ New Notebook Structure

| Notebook Name                     | Purpose                                                                 |
|----------------------------------|-------------------------------------------------------------------------|
| `00_index.ipynb`                 | Overview of all notebooks and how they relate                          |
| `01_prompt_basics.ipynb`         | Interactive guide to prompt design and chaining                        |
| `02_langchain_quickstart.ipynb`  | Demonstration of LangChain pipelines and chaining logic                |
| `03_rag_intro.ipynb`             | Building a RAG flow from scratch using vector store + retriever        |
| `04_eval_outputs.ipynb`          | Methods for evaluating LLM output quality (BLEU, ROUGE, toxicity)      |
| `99_sandbox.ipynb`               | Scratchpad for experimentation                                         |

---

## ❌ Removed / Deprecated Notebooks
- `linear_regression_intro.ipynb` — Moved to `/archive/`
- `basic_eda.ipynb` — Not aligned with GenAI theme
- `scikit_tuning_exercise.ipynb` — Better suited for a classic ML workflow repo

---

## 📂 Folder Suggestions

```
/notebooks
  ├── 00_index.ipynb
  ├── 01_prompt_basics.ipynb
  ├── 02_langchain_quickstart.ipynb
  ├── 03_rag_intro.ipynb
  ├── 04_eval_outputs.ipynb
  └── 99_sandbox.ipynb
/archive
  ├── linear_regression_intro.ipynb
  └── scikit_tuning_exercise.ipynb
```

---

## 📘 Tips
- Link to these notebooks in your README and use cases
- Consider turning `00_index.ipynb` into a JupyterBook or Voila dashboard for team walkthroughs
- Keep notebooks focused and single-purpose — each should teach or deliver one core capability

Let notebooks serve as **launchpads** for collaboration, not clutter.
