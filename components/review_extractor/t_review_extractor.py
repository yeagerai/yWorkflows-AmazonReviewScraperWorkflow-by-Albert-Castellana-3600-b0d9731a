
import pytest
from pydantic import ValidationError
from typing import List, Dict
from fastapi.testclient import TestClient
from your_component_path import (
    ReviewExtractor, 
    ReviewExtractorInputDict, 
    ReviewExtractorOutputDict,
    review_extractor_app
)

client = TestClient(review_extractor_app)

# Define the mocked input and expected output data.
mocked_input_data = [
    {"product_urls": ["https://example.com/product1", "https://example.com/product2"]},
    {"product_urls": []},
    {"product_urls": ["https://example.com/product1"]}
]

mocked_expected_output_data = [
    {
        "product_reviews": [
            {"url": "https://example.com/product1", "reviews": ["Review 1", "Review 2"]},
            {"url": "https://example.com/product2", "reviews": ["Review 3", "Review 4"]}
        ]
    },
    {"product_reviews": []},
    {
        "product_reviews": [
            {"url": "https://example.com/product1", "reviews": ["Review 1", "Review 2"]}
        ]
    }
]

# Define the test cases.
test_cases = [
    (mocked_input_data[0], mocked_expected_output_data[0]),
    (mocked_input_data[1], mocked_expected_output_data[1]),
    (mocked_input_data[2], mocked_expected_output_data[2])
]

# Use @pytest.mark.parametrize to create multiple test scenarios.
@pytest.mark.parametrize("input_data,expected_output", test_cases)
def test_review_extractor(input_data: Dict, expected_output: Dict):
    try:
        input_args = ReviewExtractorInputDict(**input_data)
    except ValidationError as err:
        pytest.fail(f"Validation Error: {err}")

    # Call the component's transform() method.
    review_extractor = ReviewExtractor()
    output = review_extractor.transform(input_args)

    # Assert the output matches the expected output.
    assert output == expected_output

# Test the FastAPI endpoint.
@pytest.mark.parametrize("input_data,expected_output", test_cases)
def test_review_extractor_endpoint(input_data: Dict, expected_output: Dict):
    response = client.post("/transform/", json=input_data)

    assert response.status_code == 200
    assert response.json() == expected_output
