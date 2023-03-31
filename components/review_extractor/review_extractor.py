
import os
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from core.abstract_component import AbstractComponent

# Additional imports for web scraping functionality
import requests
from bs4 import BeautifulSoup

class ReviewExtractorInputDict(BaseModel):
    product_urls: List[str]

class ReviewExtractorOutputDict(BaseModel):
    product_reviews: List[Dict[str, List[str]]]

class ReviewExtractor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: ReviewExtractorInputDict
    ) -> ReviewExtractorOutputDict:
        product_reviews = []

        for url in args.product_urls:
            reviews = self.scrape_reviews(url)
            product_reviews.append({"url": url, "reviews": reviews})

        return ReviewExtractorOutputDict(product_reviews=product_reviews)

    def scrape_reviews(self, url: str) -> List[str]:
        # Modify this function to implement the web scraping logic to get the reviews from each URL
        extracted_reviews = []
        
        # Example:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, "html.parser")
        # reviews = soup.select("div.review-text")
        # for review in reviews:
        #     extracted_reviews.append(review.text.strip())

        return extracted_reviews

load_dotenv()
review_extractor_app = FastAPI()

@review_extractor_app.post("/transform/")
async def transform(
    args: ReviewExtractorInputDict,
) -> ReviewExtractorOutputDict:
    review_extractor = ReviewExtractor()
    return review_extractor.transform(args)
