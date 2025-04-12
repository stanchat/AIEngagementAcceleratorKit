## 🛠️ Using Technical Artifacts (Notebooks, MLOps, Dashboards)

This kit includes starter technical artifacts to accelerate project implementation, collaboration, and evaluation.

### 📓 Jupyter Notebooks
- Found in `/notebooks`
- Use them to:
  - Clean and transform datasets
  - Evaluate and compare baseline models
  - Track and visualize experimental results
- Customize cells to integrate your specific datasets or models

### ⚙️ MLOps Scripts & Pipelines
- Found in `/tools` or `/pipelines`
- Common use cases:
  - Automate model retraining or batch scoring
  - Trigger CI/CD workflows on code commits
  - Manage model versioning and deployment
- Examples may include bash, YAML (for GitHub Actions), and Python SDK usage

### 📊 Streamlit Dashboards
- Found in `/streamlit_apps`
- Run via:
  ```bash
  streamlit run streamlit_apps/your_dashboard.py
  ```
- Use for:
  - Reviewing stakeholder feedback
  - Monitoring live model outputs
  - Collecting user annotations or input for RLHF loops

### 🤖 CLI Utilities
- Found in `/tools` or `/cli`
- Use to test prompts or API outputs locally (e.g., OpenAI, Hugging Face)
- Make sure to set API keys as environment variables or in `.env` files

### 🧠 RAG Pipeline Scripts
- Located in `helpers/rag_model_wrapper.py`
- Integrate with documents (Notion, PDFs) and serve responses via UI or API
- Useful for internal knowledge bases, smart assistants, and search interfaces

These artifacts are meant to be forked, extended, and adapted to your environment. Follow usage notes in each file or request an implementation guide if needed.

---
