import streamlit as st
from scraping_functions import scrape_website
import re
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from embedding import search_index

# URL input
url_input = st.text_input("Enter the URL of the website to scrape:")

# Data extraction preferences
extract_paragraphs = st.checkbox("Extract paragraphs")
extract_headings = st.checkbox("Extract headings")
extract_images = st.checkbox("Extract images")

# Button to trigger scraping
scrape_button = st.button("Scrape")

# Function to handle web scraping
def perform_scraping(url, extract_paragraphs, extract_headings, extract_images):
    # Validate the URL
    if not validate_url(url):
        st.write("Invalid URL. Please enter a valid URL.")
        return
    
    try:
        # Perform web scraping
        scrape_website(url, extract_paragraphs, extract_headings, extract_images)
        st.write("Web scraping completed successfully!")
    except Exception as e:
        st.write(f"An error occurred during web scraping: {str(e)}")

# URL validation function
def validate_url(url):
    # Regular expression pattern for URL validation
    url_pattern = r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$'
    
    if re.match(url_pattern, url):
        return True
    else:
        return False

# Trigger web scraping when the button is clicked
if scrape_button:
    perform_scraping(url_input, extract_paragraphs, extract_headings, extract_images)
