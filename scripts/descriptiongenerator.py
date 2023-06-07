import os
import requests
import json
import re
import openai

# Set your WooCommerce REST API URL and authentication info
url = 'https://wellnesssupply.co/wp-json/wc/v3/products'
auth = ('ck_', 'cs_')

# Set the pagination parameters
page = 1
per_page = 100

# Set your OpenAI API key
openai.api_key = 'sk_'

# Create the 'products' and 'output' directories if they don't exist
products_dir = os.path.abspath('products')
response_dir = os.path.abspath('response')
if not os.path.exists(products_dir):
    os.makedirs(products_dir)
if not os.path.exists(response_dir):
    os.makedirs(response_dir)

print("Initialized directories.")

# Send GET requests to the WooCommerce API with pagination
while True:
    # Add pagination parameters to the URL
    params = {
        'page': page,
        'per_page': per_page
    }

    # Send a GET request to the WooCommerce API
    response = requests.get(url, auth=auth, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        products = json.loads(response.text)

        # Check if there are any products in the response
        if len(products) == 0:
            print("No more products received. Exiting...")
            break  # Exit the loop if there are no more products

        # Loop through each product
        for product in products:
            # Get product details
            product_name = product['name']
            brand_name = product['brands'][0]['name'] if product['brands'] else 'N/A'  # Extract brand name
            category_name = product['categories'][0]['name'] 
            attributes = ', '.join([attr['name'] for attr in product['attributes']]) if product['attributes'] else 'N/A'
            tags = ', '.join([tag['name'] for tag in product['tags']]) if product['tags'] else 'N/A'

            # Strip special characters from the file name
            file_name = re.sub(r'[^\w\s-]', '', product_name)

            # Remove '&' and replace 'amp' with 'and' in the file name
            file_name = file_name.replace('&', '').replace('amp', 'and')

            # Create product description using HTML format
            product_desc = f'''
            You are an experienced SEO marketing specialist specializing in promoting CBD or THC products. Your role involves closely collaborating with CBD brands to help them navigate the ever-changing digital landscape and optimize their online visibility. 
            Leveraging your expertise, you excel at website optimization, creating engaging content, and implementing effective SEO strategies tailored specifically for CBD products. You stay up-to-date with industry regulations and trends, providing valuable insights, marketing advice, and optimization techniques to help CBD businesses thrive in the competitive online market.
            Write a compelling product description for the following CBD or THC product. Be descriptive, use vivid details, and effectively market the product to potential customers.

            Here are some product details:

            Product Name: {product_name}
            Brand: {brand_name}
            Attributes: {attributes}
            Tags: {tags}
            Product type - {category_name}

                        Use the following template: 

           #{product_name}
             Two paragraphs briefly hyping the product up and building excitment

           ##Description
                - Three paragraphs providing a comprehensive overview of the product
                
           ##Ingredients
                - Discuss the product's high-quality ingredients, cannabinoids, dosage, etc.
                
           ##How to Use
                - Two paragraphs explaining the proper usage and application of the product
                
           ##Lab Results, Certifications, and Quality Assurance
                - Highlight the product's quality, certifications, and any relevant quality assurance measures, along with a link to the lab results
                
           ##Benefits
                - Emphasize the unique benefits of the product to captivate potential customers
                
           ##Safety Information
           	- discuss general saftey information of the product
           	
           ##Customer Testimonials
                - Generate authentic-sounding testimonials using unique names
                
           ##Frequently Asked Questions
                - Provide answers to at least eight common questions related to the product

            ##Educational Resources
            - Provide informative resources about CBD or THC, depending on the product and their benefits
            - Include links to articles, blog posts, or videos that educate customers about CBD or THC depending on the product, its uses, and how it can improve their well-being

            Please respond with your revised product description, using Markdown format.

            '''

            # Write product description to a text file
            try:
                with open(os.path.join(products_dir, f'{file_name}.txt'), 'w') as f:
                    f.write(product_desc)
                print(f"Saved product description to '{file_name}.txt'.")
            except Exception as e:
                print(f"Error occurred while writing file '{file_name}.txt': {e}")
                continue

            # Read the file content
            with open(os.path.join(products_dir, f'{file_name}.txt'), 'r') as f:
                file_content = f.read()

            # Send the file content as a prompt to OpenAI API with streaming
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=file_content,
                temperature=0.5,
                max_tokens=3000,
                stream=True
            )

            # Store the generated response as a string
            response_text = ''
            for chunk in response:
                response_text += chunk['choices'][0]['text']

            # Adjust the indentation of the generated description
            response_text = response_text.strip()  # Remove leading and trailing whitespace
            response_text = re.sub(r'\n\s+', '\n', response_text)  # Remove extra indentation

            # Save the generated description to the response folder with the product name as the file name
            try:
                with open(os.path.join(response_dir, f'{file_name}.md'), 'w') as f:
                    f.write(response_text)
                print(f"Saved response to '{file_name}.md'.")
            except Exception as e:
                print(f"Error occurred while writing file '{file_name}.md': {e}")
                continue

        # Increment the page number for the next request
        page += 1
    else:
        print(f"Request failed with status code {response.status_code}")
        break
