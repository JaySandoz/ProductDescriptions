# 🛒 WooCommerce Product Description Updater

This Python script updates the descriptions of all products in your WooCommerce store with ease! 🚀 The descriptions are based on local Markdown files where the filename corresponds to the product name.

## Prerequisites

- Python 3.7 or later.
- A WooCommerce store with the WooCommerce REST API enabled.
- API credentials (consumer key and secret) for your WooCommerce store.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages: `pip install -r requirements.txt`
3. Move the descriptions.py file into the ProductDescriptions directory.

## Configuration

1. Export the required API credentials as environment variables:
    ```shell
    export CONSUMER_KEY=<your_consumer_key>
    export CONSUMER_SECRET=<your_consumer_secret>
    ```
   Replace `<your_consumer_key>` and `<your_consumer_secret>` with your actual API credentials.

2. Update the `url` variable in the Python script to point to your WooCommerce store's API endpoint.

## Usage

Prepare Markdown files for each product with the product's description. The filename should be the product name with special characters removed, spaces replaced with underscores, and the `.md` extension.

Run the script in your ProductDescriptions directory: `python3 descriptions.py`

Voilà! The script will fetch all products from your WooCommerce store and effortlessly update their descriptions based on the corresponding Markdown files. 📝✨

## Notes

- Make sure that the product names in your WooCommerce store match the Markdown file names.
- The script uses basic error handling. For a more polished and robust implementation, it's recommended to add advanced error handling, consider API rate limits, and implement necessary security measures.

Enjoy updating your product descriptions with ease and have fun shopping! 🛍️💡
