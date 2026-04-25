import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_product(url: str):
    print(f"Scraping URL: {url}")
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.93 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        raise Exception("Failed to fetch product page.")

    soup = BeautifulSoup(response.content, "html.parser")

    # Title
    title = soup.find("span", {"id": "productTitle"})
    if not title:
        raise Exception("Could not extract product title.")
    product_name = title.get_text(strip=True)

    # Price
    price = soup.find("span", {"class": "a-price-whole"})
    if not price:
        # Try alternate price selector
        price = soup.select_one("span.a-offscreen")

    if not price:
        raise Exception("Could not extract product price.")
    price_text = price.get_text(strip=True)
    price_clean = re.sub(r"[^\d.]", "", price_text)

    # Image
    image_tag = soup.find("img", {"id": "landingImage"})
    if image_tag and image_tag.has_attr("src"):
        image_url = image_tag["src"]
    else:
        image_url = None  # fallback if needed

    print(f"Product Name: {product_name}")
    print(f"Product Price: {price_clean}")
    print(f"Product Image URL: {image_url}")

    return {
        "name": product_name,
        "price": price_clean,
        "image_url": image_url
    }
import requests
from bs4 import BeautifulSoup
import re

def search_flipkart(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.find("div", {"class": "_30jeq3 _1_WHN1"})  # Product price
    if price_tag:
        return re.sub(r"[^\d]", "", price_tag.text)
    return None
