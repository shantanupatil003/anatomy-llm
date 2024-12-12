import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import openai
import os
import time
import sys

class Query():

    CHROMA_PATH = "chroma"

    PROMPT_TEMPLATE = """
        Answer the question based only on the following context:

        {context}

        ---

        Answer the question based on the above context: {question}
    """
    def __init__(self):
        """QueryData INIT"""
        

    def runMain(self,query_text):
        # Command line parser
        # parser = argparse.ArgumentParser()
        # parser.add_argument("query_text", type=str, help="The query text.")
        # args = parser.parse_args()
        # query_text = args.query_text

        # get text from api
        # query_text = 'where is the right ventricle?'

        # Preparing the Chroma database
        embedding_function = OpenAIEmbeddings()
        db = Chroma(persist_directory=self.CHROMA_PATH, embedding_function=embedding_function)

        #Searching the database
        try:
            results = db.similarity_search_with_relevance_scores(query_text, k=3)
            if len(results) == 0 or results[0][1] < 0.7:
                print(f"Unable to find matching results.")
                return
            
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
            prompt_template = ChatPromptTemplate.from_template(self.PROMPT_TEMPLATE)
            prompt = prompt_template.format(context=context_text, question=query_text)
            # print(prompt)

            model = ChatOpenAI()
            response_text = model.invoke(prompt).content

            sources = [doc.metadata.get("source", None) for doc, _source in results]
            formatted_text = f"Response: {response_text}\nSources: {sources}"
            return response_text
        except openai.RateLimitError:
            print("rate limit exceeded, waiting for 5 seconds")
            time.sleep(5)
