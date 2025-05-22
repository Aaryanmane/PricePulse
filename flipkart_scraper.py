# flipkart_scraper.py

import requests
from bs4 import BeautifulSoup
import re

def search_flipkart(query: str):
    print(f"Searching Flipkart for: {query}")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.93 Safari/537.36"
        )
    }

    search_url = f"https://www.flipkart.com/search?q={requests.utils.quote(query)}"
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch Flipkart search page")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Try product grid price structure
    price_tag = soup.select_one("div._30jeq3._1_WHN1")
    if not price_tag:
        # Try alternate price class
        price_tag = soup.select_one("div._30jeq3")

    if price_tag:
        price_text = price_tag.get_text()
        price_cleaned = re.sub(r"[^\d.]", "", price_text)
        try:
            return float(price_cleaned)
        except:
            return None

    print("Flipkart price not found")
    return None
