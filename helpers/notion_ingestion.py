# notion_ingestion.py

import os
from notion_client import Client
from langchain.document_loaders import NotionDBLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = Client(auth=NOTION_API_KEY)

# Load documents from Notion DB
loader = NotionDBLoader(
    integration_token=NOTION_API_KEY,
    database_id=DATABASE_ID
)

docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Save results for use in vector DB
for i, chunk in enumerate(chunks[:5]):
    print(f"[{i+1}] {chunk.page_content[:200]}...")
