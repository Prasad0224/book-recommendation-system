from pydantic import BaseModel, Field
from typing import Annotated


class PopularBooks(BaseModel):
    top_n: Annotated[int, Field(..., gt=0, lt=51, description="Number of books")]


class SimilarBooks(BaseModel):
    book_name: Annotated[str, Field(..., description="Book name")]
    top_n: Annotated[int, Field(5, gt=0, lt=21)]
