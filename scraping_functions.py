from bs4 import BeautifulSoup

def scrape_website(url):
    # Make a request to the URL and retrieve the HTML content
    # You can use libraries like requests to handle the HTTP request
    # response = requests.get(url)
    # html_content = response.text
    
    # For demonstration purposes, we'll use a sample HTML content
    html_content = '''
    <html>
    <body>
        <h1>Hello, World!</h1>
        <p>This is an example paragraph.</p>
    </body>
    </html>
    '''
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the desired data based on user preferences
    extracted_data = []
    
    # Example: Extract paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        extracted_data.append(paragraph.get_text())
    
    # Example: Extract headings
    headings = soup.find_all('h1')
    for heading in headings:
        extracted_data.append(heading.get_text())
    
    # Example: Extract images
    images = soup.find_all('img')
    for image in images:
        extracted_data.append(image['src'])
    
    # Store the extracted data in a .txt file
    with open('scraped_data.txt', 'w') as file:
        file.write('\n'.join(extracted_data))
