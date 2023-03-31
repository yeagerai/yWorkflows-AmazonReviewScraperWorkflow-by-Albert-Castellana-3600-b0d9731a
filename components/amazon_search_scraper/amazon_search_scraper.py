
import os
from typing import List

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests

from core.abstract_component import AbstractComponent


class AmazonSearchScraperInput(BaseModel):
    product_name: str


class AmazonSearchScraperOutput(BaseModel):
    product_urls: List[str]


class AmazonSearchScraper(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.results_limit: int = yaml_data["parameters"]["results_limit"]

    def transform(
        self, args: AmazonSearchScraperInput
    ) -> AmazonSearchScraperOutput:
        product_name = args.product_name
        amazon_url = f"https://www.amazon.com/s?field-keywords={product_name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
        }
        response = requests.get(amazon_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        product_urls = []
        for tag in soup.find_all("a", class_="a-link-normal s-no-outline", limit=self.results_limit):
            product_urls.append("https://www.amazon.com" + tag.get("href"))

        return AmazonSearchScraperOutput(product_urls=product_urls)


load_dotenv()
amazon_search_scraper_app = FastAPI()


@amazon_search_scraper_app.post("/transform/")
async def transform(
    args: AmazonSearchScraperInput,
) -> AmazonSearchScraperOutput:
    amazon_search_scraper = AmazonSearchScraper()
    return amazon_search_scraper.transform(args)
