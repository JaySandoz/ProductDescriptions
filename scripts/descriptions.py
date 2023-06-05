import os
import re
import markdown
from bs4 import BeautifulSoup
import requests
from typing import Optional
from decouple import config
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Your WooCommerce API credentials from environment variables
consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
url = 'https://wellnesssupply.co/wp-json/wc/v3/'


def md_to_html(filename: str) -> Optional[str]:
    """Read Markdown file and return HTML content."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        logging.error(f"File does not exist: {filename}")
        return None
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        return None

    html = markdown.markdown(text)
    
    # Use BeautifulSoup to prettify the HTML
    soup = BeautifulSoup(html, 'html.parser')
    pretty_html = soup.prettify()

    return pretty_html


def update_product_description(product_id: int, description: str) -> None:
    """Update product description via WooCommerce API."""
    product_data = {
        'description': description
    }

    try:
        response = requests.put(
            f"{url}products/{product_id}",
            params={'consumer_key': consumer_key, 'consumer_secret': consumer_secret},
            json=product_data
        )
    except requests.exceptions.RequestException as e:
        logging.error(f"Error updating product {product_id}: {e}")
        return

    if response.status_code == 200:
        logging.info(f"Product {product_id} updated successfully.")
    else:
        logging.error(f"Failed to update product {product_id}. Status code: {response.status_code}")


def get_all_products(page: int = 1, per_page: int = 100):
    """Fetch products with pagination."""
    while True:
        try:
            response = requests.get(
                f"{url}products",
                params={
                    'consumer_key': consumer_key,
                    'consumer_secret': consumer_secret,
                    'page': page,
                    'per_page': per_page
                }
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching products: {e}")
            break

        if response.status_code != 200:
            logging.error(f"Failed to fetch products. Status code: {response.status_code}")
            break

        products = response.json()
        if not products:
            break

        yield from products

        page += 1


def process_all_products() -> None:
    """Process all products."""
    script_directory = os.path.dirname(os.path.realpath(__file__))

    for product in get_all_products():
        product_name = product['name']
        # Convert product name to file name
        file_name = re.sub(r'[^\w\s-]', '', product_name)
        file_name = file_name.replace('&', '').replace('amp', 'and')
        file_name = os.path.join(script_directory, f"{file_name}.md")

        logging.debug(f"Looking for file: {file_name}")

        # Convert Markdown to HTML and update product description
        html = md_to_html(file_name)
        if html:
            update_product_description(product['id'], html)


if __name__ == "__main__":
    process_all_products()
