from bs4 import BeautifulSoup
import requests
import os

def scrape_website(url, extract_paragraphs, extract_headings, extract_images):
    # Make a request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the desired data based on user preferences
    extracted_data = []
    
    # Example: Extract paragraphs
    if extract_paragraphs:
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            extracted_data.append(paragraph.get_text())
    
    # Example: Extract headings
    if extract_headings:
        headings = soup.find_all('h1')
        for heading in headings:
            extracted_data.append(heading.get_text())
    
    # Example: Extract images
    if extract_images:
        images = soup.find_all('img')
        for image in images:
            extracted_data.append(image['src'])
    
    # Create the "data" folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Create or update the .txt file with the scraped data
    file_path = os.path.join('data', url.replace('/', '_') + '.txt')
    with open(file_path, 'w') as file:
        file.write('\n'.join(extracted_data))
