import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Fallback strategy
if OPENAI_API_KEY:
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
else:
    embeddings = HuggingFaceInferenceAPIEmbeddings(api_key=HF_API_TOKEN)

st.set_page_config(page_title="🤖 Agentic Workflow: PDF Knowledge Assistant")
st.header("🤖 Agentic Workflow: PDF Knowledge Assistant")
st.markdown("Upload a PDF")

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    file_path = os.path.join("temp", pdf.name)
    with open(file_path, "wb") as f:
        f.write(pdf.read())

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    db = Chroma.from_documents(texts, embeddings)
    st.success("Vector store created from PDF.")
