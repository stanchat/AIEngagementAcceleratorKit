# index_pdfs.py

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdfs(folder_path):
    all_docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            pages = loader.load()
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            docs = splitter.split_documents(pages)
            all_docs.extend([doc.page_content for doc in docs])
    return all_docs

# Example usage
if __name__ == "__main__":
    folder = "sample_pdfs"
    documents = load_and_split_pdfs(folder)
    print(f"Indexed {len(documents)} chunks from PDF files.")
