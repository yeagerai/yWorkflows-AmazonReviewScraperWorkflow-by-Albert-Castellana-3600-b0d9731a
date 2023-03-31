
# AmazonReviewScraperWorkflow

This workflow consists of the following components:
1. Receive the product_name as input in the InputProduct data model.
2. Scrape the Amazon product reviews for the given product_name.
3. Create a spreadsheet containing the scraped reviews.
4. Return the spreadsheet_url as output in the OutputProductReviews data model.


## Initial generation prompt
description: "IOs - - InputProduct:\n    classname: InputProduct\n    fields:\n  \
  \  - product_name: str\n- OutputProductReviews:\n    classname: OutputProductReviews\n\
  \    fields:\n    - spreadsheet_url: str\n"
name: AmazonReviewScraperWorkflow


## Transformer breakdown
- Receive product_name as InputProduct
- Scrape Amazon product reviews for the given product_name
- Create a spreadsheet containing the scraped reviews
- Return spreadsheet_url as OutputProductReviews

## Parameters
[]

        