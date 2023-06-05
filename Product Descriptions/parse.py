import os

# Define the SEO tables to be appended
seo_tables = """
# 🛠️ For Developer Use Only 🔐

Below are the tables for storing SEO-related information of WooCommerce products. 👇

## 🏷️ Basic Information 

| 🏷️ Product Name | 📝 Meta Description | 🕸️ Slug | 🏷️ SEO-friendly Title |
| -------------- | ------------------ | ------ | ---------------------- |
|                |                    |        |                        |
|                |                    |        |                        |

## 📸 Media Information

| 🖼️ Alt Tags for Images | 📊 Schema Markup |
| --------------------- | --------------- |
|                       |                 |
|                       |                 |

## 🔎 SEO Optimization

| 🎯 Keyword Targeting | 🏷️ SEO Tags |
| ------------------- | ---------- |
|                     |            |
|                     |            |

## 🔗 Linking Strategy 

| 🔗 Internal Links | 🔗 External Links |
| ---------------- | ---------------- |
|                  |                  |
|                  |                  |

## 🏷️ Product Classification 

| 📂 Product Categories | 🏷️ Product Tags | 🕸️ Canonical URL |
| ------------------ | ------------ | ------------- |
|                    |              |               |
|                    |              |               |
"""

# Use the current working directory
directory = os.getcwd()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # If file is a Markdown file
    if filename.endswith('.md'):
        with open(os.path.join(directory, filename), 'a') as f:
            # Append the SEO tables to the file
            f.write(seo_tables)

print("Done appending SEO tables to all Markdown files.")

