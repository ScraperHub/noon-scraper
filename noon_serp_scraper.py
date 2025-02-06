from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import csv

# Initialize Crawlbase API
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def scrape_noon_search(query, page):
    """Scrape product listings from Noon search results."""
    url = f"https://www.noon.com/uae-en/search/?q={query}&page={page}"
    options = {'ajax_wait': 'true', 'page_wait': '5000'}
    
    response = crawling_api.get(url, options)
    
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch page {page}.")
        return None

def extract_product_data(html):
    """Extract product details from Noon search results."""
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.select('div.grid > span.productContainer'):
        title = item.select_one('div[data-qa="product-name"]').text.strip() if item.select_one('div[data-qa="product-name"]') else ''
        price = item.select_one('strong.amount').text.strip() if item.select_one('strong.amount') else ''
        currency = item.select_one('span.currency').text.strip() if item.select_one('span.currency') else ''
        rating = item.select_one('div.dGLdNc').text.strip() if item.select_one('div.dGLdNc') else ''
        link = f"https://www.noon.com{item.select_one('a')['href']}" if item.select_one('a') else ''

        if title and price:
            products.append({
                'Title': title,
                'Price': price,
                'Currency': currency,
                'Rating': rating,
                'URL': link
            })

    return products

def scrape_all_pages(query, max_pages):
    """Scrape multiple pages of search results."""
    all_products = []
    
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        html = scrape_noon_search(query, page)
        
        if html:
            products = extract_product_data(html)
            if not products:
                print("No more results found. Stopping.")
                break
            all_products.extend(products)
        else:
            break
    
    return all_products

def save_to_csv(data, filename):
    """Save scraped data to a CSV file."""
    keys = data[0].keys() if data else ['Title', 'Price', 'Rating', 'URL']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {filename}")

def main():
    """Main function to run the scraper."""
    query = "smartphones"  # Change the search term as needed
    max_pages = 5  # Set the number of pages to scrape
    all_products = scrape_all_pages(query, max_pages)
    save_to_csv(all_products, 'noon_smartphones.csv')

if __name__ == "__main__":
    main()