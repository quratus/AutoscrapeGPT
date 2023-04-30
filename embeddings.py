
import langchain.llms
 # Let's import OpenAI library. 
from langchain.llms import OpenAI
 # To access the OpenAI environment, you can import it using your unique API key provided by OpenAI.
import os
os.environ["OPENAI_API_KEY"] = "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"

 #  Let's import CharacterTextSplitter and break down our documents into small chunks. 
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from scraping_functions import scrape_website

text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
docs = []
metadatas = []
for i, d in enumerate(extracted_data):
     splits = text_splitter.split_text(d)
     docs.extend(splits)
     metadatas.extend([{"source":"https://python.langchain.com/en/latest/index.html"} ])
embeddings = OpenAIEmbeddings()

search_index = FAISS.from_texts(docs, embeddings)

from langchain.chains.qa_with_sources import load_qa_with_sources_chain
chain = load_qa_with_sources_chain(OpenAI(temperature=0))

def print_answer(question):
     print(
         chain(
             {
                 "input_documents": search_index.similarity_search(question, k=4),
                 "question": question,
             },
             return_only_outputs=True,
         )["output_text"]
     )
print_answer("what is langchain framework?")