# gradio_rag_multisource_app.py

import gradio as gr
from helpers.rag_model_wrapper import RAGPipeline
from helpers.index_pdfs import load_and_split_pdfs
from helpers.notion_ingestion import load_notion_docs

# Initialize empty doc list
documents = []

def load_docs(source_type):
    global documents
    if source_type == "PDF":
        documents = load_and_split_pdfs("sample_pdfs")
    elif source_type == "Notion":
        documents = load_notion_docs()
    return f"Loaded {len(documents)} documents from {source_type}"

def answer_question(query):
    if not documents:
        return "⚠️ No documents loaded. Please select a source first."
    rag = RAGPipeline(documents)
    return rag.answer_question(query)

with gr.Blocks() as app:
    source_type = gr.Radio(choices=["PDF", "Notion"], label="Select Document Source")
    load_btn = gr.Button("Load Documents")
    doc_status = gr.Textbox(label="Document Load Status")
    question = gr.Textbox(label="Enter your question")
    response = gr.Textbox(label="Answer")

    load_btn.click(fn=load_docs, inputs=source_type, outputs=doc_status)
    question.submit(fn=answer_question, inputs=question, outputs=response)

app.launch()
