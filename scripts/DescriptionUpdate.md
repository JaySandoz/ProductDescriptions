# 😃 Documentation for WooCommerce Product Updater Script 🚀

## ⚠️ Alert!

Please note, the script uses basic error handling. For a more polished and robust implementation, it's recommended to add advanced error handling, consider API rate limits, and implement necessary security measures. Also, make sure to remove the developer section of the Md file before running the script.

## 🎯 Introduction

Hear Ye! Hear Ye! This is a fun-loving Python script 🐍 that takes those boring markdown files (yawn...), spins them into pretty HTML (ooo... shiny!), and then updates product descriptions on a WooCommerce store via the WooCommerce API (whoosh!).

## 🔨 Prerequisites

Here's what you need to be one of the cool kids:

- Python 3.6 or higher (it's 2023, c'mon!)
- Python `requests` library (because, how else are we going to request things?)
- Python `decouple` library (not for couple's therapy)
- Python `bs4` (BeautifulSoup4) library (makes your HTML pretty like soup… wait, what?)
- Python `markdown` library (because we love markdown, remember?)

Here's how to get them:

    pip install requests python-decouple beautifulsoup4 markdown

## 📚 File Names and Product Names

In this script, each product should have a corresponding Markdown file. The product name is used to determine the file name of the corresponding Markdown file. 

All non-alphanumeric characters, except for hyphens and spaces, are removed from the product name to form the file name. Furthermore, ampersands (&) are specially handled to be removed entirely, while the string "amp" is replaced with "and". 

This file name conversion allows for a simple and consistent mapping from product names to file names. Note that the file names are case sensitive.

For example, a product named "M&Ms: Candy - Pack of 50" will correspond to a markdown file named "MMs Candy - Pack of 50.md".

## 🚦 Usage

1. The script wants your WooCommerce API credentials (`CONSUMER_KEY` and `CONSUMER_SECRET`). Don't worry, it won't post them on Facebook. We will set them via the terminal:

```bash
    export CONSUMER_KEY=your_consumer_key
    export CONSUMER_SECRET=your_consumer_secret
    ```

2. Run the script in your ProductDescriptions directory:

    python3 descriptions.py

Voilà! The script will fetch all products from your WooCommerce store and effortlessly update their descriptions based on the corresponding Markdown files. 📝✨

## 📌 Notes

- Make sure that the product names in your WooCommerce store match the Markdown file names.
- The script uses basic error handling. For a more polished and robust implementation, it's recommended to add advanced error handling, consider API rate limits, and implement necessary security measures.

## 🧩 Script Details

Here's what goes on under the hood (shh, it's secret!)

### `md_to_html(filename: str) -> Optional[str]`

This clever little function reads a Markdown file and turns it into HTML. It's kind of like magic, but with more BeautifulSoup.

### `update_product_description(product_id: int, description: str) -> None`

This one is a smooth talker. It sweet-talks the WooCommerce API to update your product description.

### `get_all_products(page: int = 1, per_page: int = 100)`

A dedicated fetcher of products, this function won't rest until it's got them all!

### `process_all_products() -> None`

The chief in command, calling the shots. It oversees the whole operation from turning Markdown into HTML to updating the product descriptions.

## 👬 Contributing

Feel free to fork this project, make changes in your own fork, and then issue Pull Requests back for review. We appreciate any contributions, whether they're feature requests, improvements, or bug fixes.

## 📃 License

This script is distributed under the MIT License. 

## 👏 Acknowledgments

Thanks to WooCommerce for providing a simple and powerful API.

## ⚠️ Disclaimer

This script is provided as-is, and may be freely modified or adapted to fit specific needs. It comes without any warranty, express or implied.
