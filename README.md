# Noon.com Scrapers

## Description

This repository contains Python-based scrapers for Noon.com search results and product pages. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.
➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-noon-data/) to learn more.

## Scrapers Overview

### Noon.com Search Results Scraper

The Noon.com Search Results Scraper (noon_serp_scraper.py) extracts:

1. **Product Title**
2. **Price & Currency**
3. **Ratings**
4. **Product Page URL**

It also automatically handles pagination, ensuring comprehensive data extraction. It saves the extracted data in a CSV file.

### Noon.com Product Page Scraper

The Noon.com Product Page Scraper (noon_product_page_scraper.py) extracts detailed product information, including:

1. **Product Name**
2. **Price**
3. **Product Highlights**
4. **Specifications**

It saves the extracted data in a CSV file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux with Python 3 installed
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4 pandas
```

**Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
**BeautifulSoup** – Parses and extracts structured data from HTML.
**Pandas** – Formats and stores extracted data, enabling CSV exports.

## Running the Scrapers

1. **Get Your Crawlbase Access Token**

   - Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
   - Use the JS token for Noon.com scraping, as the site uses JavaScript-rendered content.

2. **Update the Scraper with Your Token**

   - Replace `"YOUR_CRAWLBASE_TOKEN"` in the script with your Crawlbase JS Token.

3. **Run the Scraper**

```bash
# Use python3 if required (for Linux/macOS)
python SCRAPER_FILE_NAME.py
```

Replace `"SCRAPER_FILE_NAME.py"` with the actual script name (`noon_serp_scraper.py` or `noon_product_page_scraper.py`).

## To-Do List

- Expand scrapers to extract additional product details.
- Optimize data storage and export formats (e.g., JSON, database integration).
- Enhance scraper efficiency and speed.

## Why Use This Scraper?

- **Bypasses anti-bot protections** with Crawlbase.
- **Handles JavaScript-rendered content** seamlessly.
- **Extracts accurate and structured product data** efficiently.
