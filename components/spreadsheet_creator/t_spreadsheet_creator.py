
import os
import json
import pytest
from typing import List, Dict, Union
from pydantic import BaseModel
from core.abstract_component import AbstractComponent

from your_component_directory import SpreadsheetCreator, SpreadsheetCreatorInputDict, SpreadsheetCreatorOutputDict

# Define test cases
test_cases = [
    (
        SpreadsheetCreatorInputDict(
            product_data=[
                {
                    "url": "https://example.com/product1",
                    "reviews": ["Review 1", "Review 2"],
                },
                {
                    "url": "https://example.com/product2",
                    "reviews": ["Review 3", "Review 4"],
                },
            ]
        ),
        SpreadsheetCreatorOutputDict(
            spreadsheet_url="https://docs.google.com/spreadsheets/d/test_spreadsheet_id"
        ),
    ),
    (
        SpreadsheetCreatorInputDict(
            product_data=[
                {
                    "url": "https://example.com/product3",
                    "reviews": ["Review 5", "Review 6"],
                }
            ]
        ),
        SpreadsheetCreatorOutputDict(
            spreadsheet_url="https://docs.google.com/spreadsheets/d/test_spreadsheet_id"
        ),
    ),
]

@pytest.mark.parametrize("input_data,expected_output", test_cases)
def test_spreadsheet_creator(input_data: SpreadsheetCreatorInputDict, expected_output: SpreadsheetCreatorOutputDict, mocker):
    # Mock the Google credentials, Google Sheets API call and URL generation
    mocker.patch.dict(os.environ, {"GOOGLE_CREDENTIALS_JSON": json.dumps({})})
    mocker.patch("your_component_directory.service_account.Credentials.from_service_account_info")
    mocker.patch("your_component_directory.pygsheets.authorize")
    mocker.patch("your_component_directory.gc.open_by_url")

    spreadsheet_mock = mocker.MagicMock()
    spreadsheet_mock.spreadsheetId = "test_spreadsheet_id"
    spreadsheet_mock.set_dataframe.return_value = None
    mocker.patch("your_component_directory.gc.open_by_url").return_value = spreadsheet_mock
    
    spreadsheet_creator = SpreadsheetCreator()
    output = spreadsheet_creator.transform(input_data)
    assert output == expected_output
