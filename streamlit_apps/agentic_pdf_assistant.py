import streamlit as st
import os
from dotenv import load_dotenv
# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Load API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Agentic PDF Assistant", layout="wide")
st.title("🤖 Agentic Workflow: PDF Knowledge Assistant")

# File uploader
pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file is not None:
    with st.spinner("Processing PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.read())

        # Step 1: Load and split
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load_and_split()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(pages)

        # Step 2: Vector store
        embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
        db = FAISS.from_documents(docs, embeddings)

        # Step 3: Setup LLM + QA Chain
        llm = OpenAI(openai_api_key=openai_key, temperature=0)
        qa_chain = load_qa_chain(llm, chain_type="stuff")

        def search_and_summarize(query):
            matches = db.similarity_search(query)
            return qa_chain.run(input_documents=matches, question=query)

        # Step 4: Agent
        tools = [Tool(name="PDFSearch", func=search_and_summarize, description="Answers questions about the uploaded PDF.")]
        agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

        query = st.text_input("Ask a question about your PDF:", placeholder="e.g., What are the main challenges discussed?")

        if query:
            with st.spinner("Agent reasoning..."):
                result = agent.run(query)
                st.success("Answer:")
                st.write(result)

