# gradio_rag_app.py

import gradio as gr
from helpers.rag_model_wrapper import RAGPipeline

# Sample docs to vectorize
documents = [
    "LangChain enables easy integration of LLMs with vector stores.",
    "RAG (Retrieval-Augmented Generation) combines search and generation."
]

rag_pipeline = RAGPipeline(documents)

def answer_question(query):
    return rag_pipeline.answer_question(query)

iface = gr.Interface(fn=answer_question, inputs="text", outputs="text", title="RAG Q&A")
iface.launch()
