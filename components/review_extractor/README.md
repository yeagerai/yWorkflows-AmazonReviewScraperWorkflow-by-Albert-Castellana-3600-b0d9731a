
# ReviewExtractor

This component will take in the list of product URLs from the AmazonSearchScraper component and use web scraping techniques to extract the reviews for each product. It will return a list of dictionaries containing the product URL and associated reviews.

## Initial generation prompt
description: This component will take in the list of product URLs from the AmazonSearchScraper
  component and use web scraping techniques to extract the reviews for each product.
  It will return a list of dictionaries containing the product URL and associated
  reviews.
inputs_from_nodes:
- AmazonSearchScraper
name: ReviewExtractor


## Transformer breakdown
- Loop through the product_urls
- For each URL, scrape its respective reviews
- Append the URL and the extracted reviews into a dictionary
- Add the dictionary to the product_reviews list

## Parameters
[]

        