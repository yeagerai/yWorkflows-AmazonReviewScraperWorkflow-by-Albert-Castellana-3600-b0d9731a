
import os
from typing import List, Dict, Union

import yaml
import openpyxl
import pygsheets
from google.oauth2 import service_account
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent

class SpreadsheetCreatorInputDict(BaseModel):
    product_data: List[Dict[str, Union[str, List[str]]]]

class SpreadsheetCreatorOutputDict(BaseModel):
    spreadsheet_url: str

class SpreadsheetCreator(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: SpreadsheetCreatorInputDict
    ) -> SpreadsheetCreatorOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Initialize an empty spreadsheet
        wb = openpyxl.Workbook()
        ws = wb.active

        # Add header row with columns 'Product URL' and 'Reviews'
        ws.append(['Product URL', 'Reviews'])

        # Iterate over the input product_data list
        for product in args.product_data:
            product_url = product['url']
            reviews = product['reviews']

            # For each dictionary, add a new row with the product URL and corresponding reviews
            ws.append([product_url, ', '.join(reviews)])

        # Save the spreadsheet locally
        wb.save('output.xlsx')

        # Set up Google Sheets API credentials
        load_dotenv()
        google_credentials_dict = json.loads(os.environ['GOOGLE_CREDENTIALS_JSON'])
        credentials = service_account.Credentials.from_service_account_info(google_credentials_dict)
        gc = pygsheets.authorize(custom_credentials=credentials)

        # Upload the spreadsheet to Google Sheets & and generate a shareable URL
        spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1LABoratory1cx00zibutpk/resourcekey')
        spreadsheet.set_dataframe(pd.read_excel('output.xlsx'), start='A1', index=False)
        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet.spreadsheetId}"

        # Return the spreadsheet_url
        return SpreadsheetCreatorOutputDict(spreadsheet_url=spreadsheet_url)


sp_app = FastAPI()


@sp_app.post("/transform/")
async def transform(
    args: SpreadsheetCreatorInputDict,
) -> SpreadsheetCreatorOutputDict:
    spreadsheet_creator = SpreadsheetCreator()
    return spreadsheet_creator.transform(args)
