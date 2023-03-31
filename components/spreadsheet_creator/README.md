
# SpreadsheetCreator

This component takes in a list of dictionaries containing product URLs and reviews from the ReviewExtractor component and creates a spreadsheet with the link and reviews for each product. The URL of the generated spreadsheet is returned as output.

## Initial generation prompt
description: This component will take in the list of dictionaries containing the product
  URLs and reviews from the ReviewExtractor component, and create a spreadsheet with
  the link and reviews for each product. It will return the URL of the generated spreadsheet.
inputs_from_nodes:
- ReviewExtractor
name: SpreadsheetCreator


## Transformer breakdown
- Initialize an empty spreadsheet
- Add header row with columns 'Product URL' and 'Reviews'
- Iterate over the input product_data list
- For each dictionary, add a new row with the product URL and corresponding reviews
- Save the spreadsheet and generate a shareable URL
- Return the spreadsheet_url

## Parameters
[]

        