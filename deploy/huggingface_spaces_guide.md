# Deploying to Hugging Face Spaces

## Prerequisites
- Hugging Face account
- Git and Python installed locally

## Steps

1. **Create a new Space**
   - Go to https://huggingface.co/spaces
   - Click on “Create new Space”
   - Choose `Gradio` SDK

2. **Clone the Space Repo**
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
```

3. **Add Files**
   - Copy your `gradio_rag_app.py` into the root of the repo
   - Add a `requirements.txt`:
```
gradio
openai
langchain
faiss-cpu
```

4. **Push to Hugging Face**
```bash
git add .
git commit -m "initial commit"
git push
```

Done! Your app will build and deploy automatically.
