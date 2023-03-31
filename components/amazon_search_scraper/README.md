
# AmazonSearchScraper

This component will take the input product name and use web scraping techniques (e.g., BeautifulSoup for HTML parsing) to search Amazon for the top 50 related products. It will return a list of product URLs.

## Initial generation prompt
description: This component will take the input product name and use web scraping
  techniques (e.g., BeautifulSoup for HTML parsing) to search Amazon for the top 50
  related products. It will return a list of product URLs.
inputs_from_nodes:
- InputProduct
name: AmazonSearchScraper


## Transformer breakdown
- Get the input product_name
- Use web scraping technique (e.g., BeautifulSoup) to search Amazon for the input product_name
- Extract the product URLs from the search results
- Return the top 50 product URLs (or less, depending on the results_limit parameter)

## Parameters
[{'default_value': 50, 'description': 'The maximum number of product URLs to return.', 'name': 'results_limit', 'type': 'int'}]

        