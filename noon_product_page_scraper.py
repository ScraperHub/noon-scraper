from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import csv
import re

# Initialize Crawlbase API
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def scrape_product_page(product_url):
    """Scrape product details from a Noon product page."""
    options = {'ajax_wait': 'true', 'page_wait': '3000'}
    
    response = crawling_api.get(product_url, options)
    
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch product page: {product_url}.")
        return None

def extract_product_details(html):
    """Extract details like name, price, description, and reviews."""
    soup = BeautifulSoup(html, 'html.parser')
    
    product = {}
    product['Name'] = soup.select_one('h1[data-qa^="pdp-name-"]').text.strip() if soup.select_one('h1[data-qa^="pdp-name-"]') else ''
    product['Price'] = soup.select_one('div[data-qa="div-price-now"]').text.strip() if soup.select_one('div[data-qa="div-price-now"]') else ''
    product['highlights'] = soup.select_one('div.oPZpQ ul').text.strip() if soup.select_one('div.oPZpQ ul') else ''
    product['specifications'] = {re.sub(r'\s+', ' ', row.find_all('td')[0].text.strip()): re.sub(r'\s+', ' ',row.find_all('td')[1].text.strip()) for row in soup.select('div.dROUvm table tr') if len(row.find_all('td')) == 2}

    return product

def save_product_data_to_csv(products, filename):
    """Save product details to a CSV file."""
    keys = products[0].keys() if products else ['Name', 'Price', 'Description', 'Reviews']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)
    
    print(f"Data saved to {filename}")

def main():
    """Main function to scrape product pages."""
    product_urls = [
        'https://www.noon.com/uae-en/galaxy-s25-ai-dual-sim-silver-shadow-12gb-ram-256gb-5g-middle-east-version/N70140511V/p/?o=e12201b055fa94ee',
        'https://www.noon.com/uae-en/a78-5g-dual-sim-glowing-black-8gb-ram-256gb/N70115717V/p/?o=c99e13ae460efc6b'
    ]  # List of product URLs to scrape
    
    product_data = []
    
    for url in product_urls:
        print(f"Scraping {url}...")
        html = scrape_product_page(url)
        if html:
            product = extract_product_details(html)
            product_data.append(product)
    
    save_product_data_to_csv(product_data, 'noon_product_details.csv')

if __name__ == "__main__":
    main()