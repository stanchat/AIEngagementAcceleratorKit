# rag_model_wrapper.py

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

class RAGPipeline:
    def __init__(self, documents: list[str]):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = FAISS.from_texts(documents, self.embeddings)
        self.retriever = self.vectorstore.as_retriever()
        self.llm = OpenAI(temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.retriever)

    def answer_question(self, query: str) -> str:
        result = self.qa_chain.run(query)
        return result
