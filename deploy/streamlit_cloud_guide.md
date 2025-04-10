# Deploying to Streamlit Cloud

## 1. Setup
- Create a new repo with your Streamlit or Gradio app

## 2. Add required files
- Add `gradio_rag_multisource_app.py` to root
- Create `requirements.txt`:
```
gradio
openai
langchain
faiss-cpu
PyPDF2
notion-client
```

## 3. Connect to Streamlit Cloud
- Visit https://streamlit.io/cloud
- Click **New app**
- Select your repo and file to run (`gradio_rag_multisource_app.py`)
- Click **Deploy**

Done! Your app will launch publicly with automatic redeploys.
