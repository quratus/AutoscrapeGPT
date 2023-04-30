from bs4 import BeautifulSoup
import requests
import os
import streamlit as st


def scrape_website(url, extract_paragraphs, extract_headings, extract_images):
    # Make a request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the desired data based on user preferences
    extracted_data = []
    
    if extract_paragraphs:
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            paragraph_text = paragraph.get_text()
            extracted_data.append(paragraph_text)
            # Print the paragraph in Streamlit
            st.write("Paragraph:", paragraph_text)
    
    # Example: Extract headings
    if extract_headings:
        headings = soup.find_all('h1')
        for heading in headings:
            heading_text = heading.get_text()
            extracted_data.append(heading_text)
            # Print the heading in Streamlit
            st.write("Heading:", heading_text)
    
    # Example: Extract images
    if extract_images:
        images = soup.find_all('img')
        for image in images:
            image_src = image['src']
            extracted_data.append(image_src)
            # Print the image source in Streamlit
            st.write("Image Source:", image_src)
    
    # Create the "data" folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Create or update the .txt file with the scraped data
    file_path = os.path.join('data', url.replace('/', '_') + '.txt')
    with open(file_path, 'w') as file:
        file.write('\n'.join(extracted_data))