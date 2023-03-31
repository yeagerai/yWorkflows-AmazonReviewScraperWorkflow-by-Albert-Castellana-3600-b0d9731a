
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class InputProduct(BaseModel):
    product_name: str

class OutputProductReviews(BaseModel):
    spreadsheet_url: str

class AmazonReviewScraperWorkflow(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: InputProduct, callbacks: typing.Any
    ) -> OutputProductReviews:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        spreadsheet_url = results_dict['spreadsheet_created'].spreadsheet_url
        out = OutputProductReviews(spreadsheet_url=spreadsheet_url)
        return out

load_dotenv()
amazon_review_scraper_app = FastAPI()

@amazon_review_scraper_app.post("/transform/")
async def transform(
    args: InputProduct,
) -> OutputProductReviews:
    amazon_review_scraper = AmazonReviewScraperWorkflow()
    return await amazon_review_scraper.transform(args, callbacks=None)

