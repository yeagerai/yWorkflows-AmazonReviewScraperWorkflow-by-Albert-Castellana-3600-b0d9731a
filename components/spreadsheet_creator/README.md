markdown
# 1. Component Name

Spreadsheet Creator

# 2. Description

The Spreadsheet Creator component is designed to create a spreadsheet with product data and reviews, specifically generating an Excel file and uploading it to Google Sheets. The newly created Google Sheet is then returned as a shareable URL.

# 3. Input and Output Models

The component utilizes two custom data models defined using Pydantic:

- `SpreadsheetCreatorInputDict`: This model accepts a list of dictionaries containing `product_data`. Each dictionary in the list must contain the keys 'url' (str) and 'reviews' (List[str]).
- `SpreadsheetCreatorOutputDict`: This model contains a single key, 'spreadsheet_url', which represents the shareable URL of the resulting Google Sheet (str).

The Pydantic library takes care of validation and serialization of the input and output data models.

# 4. Parameters

The `SpreadsheetCreator` component class has no additional parameters besides the required input argument in its `transform()` method.

# 5. Transform Function

The `transform()` method of the `SpreadsheetCreator` component is implemented as follows:

1. Initialize an empty Excel spreadsheet using OpenPyXL.
2. Add a header row to the spreadsheet with columns 'Product URL' and 'Reviews'.
3. Iterate over the `product_data` input list and append rows with the product URL and corresponding reviews.
4. Save the spreadsheet locally as 'output.xlsx'.
5. Set up Google Sheets API credentials using the Google service account and Pygsheets library.
6. Upload the local spreadsheet to Google Sheets.
7. Generate a shareable URL for the newly created Google Sheet.
8. Return the spreadsheet_url wrapped in the `SpreadsheetCreatorOutputDict` data model.

# 6. External Dependencies

The component relies on the following external dependencies:

- **OpenPyXL:** For creating and manipulating Excel files.
- **Dotenv:** For loading environment variables from a .env file.
- **Pygsheets:** For interacting with the Google Sheets API.
- **Google-auth and Google-auth-oauthlib:** For Google API authentication and authorization.

# 7. API Calls

The component utilizes the Google Sheets API for uploading the local Excel spreadsheet and generating a shareable URL. The specific API call being used is the Pygsheets `open_by_url()` method, which opens a spreadsheet using its shareable URL.

# 8. Error Handling

The component doesn't include any specific error handling logic. However, any issues related to validating input data, accessing the Google Sheets API, or other runtime exceptions will be raised by their respective libraries (e.g., Pydantic, Pygsheets, etc.).

# 9. Examples

To use the `SpreadsheetCreator` component within a Yeager Workflow, follow the example below:

1. Prepare the input data in the format expected by `SpreadsheetCreatorInputDict`. For example:

   