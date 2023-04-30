import streamlit as st
from scraping_functions import scrape_website, validate_url

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
        scrape_website(url)
        st.write("Web scraping completed successfully!")
    except Exception as e:
        st.write(f"An error occurred during web scraping: {str(e)}")

# Trigger web scraping when the button is clicked
if scrape_button:
    perform_scraping(url_input, extract_paragraphs, extract_headings, extract_images)


