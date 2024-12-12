from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import openai
import os
import shutil
import nltk



class DataStoreInit():
    
    CHROMA_PATH = "chroma"
    DATA_PATH = "data/"
    def __init__(self):    
        nltk.download('punkt')
        nltk.download('punkt_tab')
        nltk.download('averaged_perceptron_tagger_eng')

    def generate_data_store(self):
        documents = self.load_documents()
        chunks = self.split_text(documents)
        self.save_to_chroma(chunks)

    def load_documents(self):
        loader = DirectoryLoader(self.DATA_PATH, glob = "*.pdf")
        #loader = DirectoryLoader(DATA_PATH, glob="Hacking Exposed Wireless_ Wireless Security Secrets & Solutions.pdf.pdf")
        documents = loader.load()
        return documents

    def split_text(self,documents: list[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 5000,
            chunk_overlap = 100,
            length_function = len,
            add_start_index = True
        )
        chunks = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

        # Printing a random chunk
        """
        document = chunks[10]
        print(document.page_content)
        print(document.metadata)

        """
        return chunks
    
    def save_to_chroma(self,chunks: list[Document]):
        # Clear out database first
        if os.path.exists(self.CHROMA_PATH):
            shutil.rmtree(self.CHROMA_PATH)

        # Create a new DB from the documents
        db = Chroma.from_documents(
            chunks, OpenAIEmbeddings(), persist_directory=self.CHROMA_PATH
        )
        #db.persist()
        print(f"Saved {len(chunks)} chunks to {self.CHROMA_PATH}.")

