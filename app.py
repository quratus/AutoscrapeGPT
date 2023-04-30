import streamlit as st
import re

# URL input
url_input = st.text_input("Enter the URL of the website to scrape:")

# Data extraction preferences
extract_paragraphs = st.checkbox("Extract paragraphs")
extract_headings = st.checkbox("Extract headings")
extract_images = st.checkbox("Extract images")

# Button to trigger scraping
scrape_button = st.button("Scrape")


# URL validation function
def validate_url(url):
    # Regular expression pattern for URL validation
    url_pattern = r'^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*/?$'
    
    return bool(re.match(url_pattern, url))


# Usage example
if validate_url(url_input):
    st.write("URL is valid")
else:
    st.write("Invalid URL")


