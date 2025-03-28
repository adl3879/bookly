from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(le=5)
    review_text: str
    user_id: uuid.UUID | None
    book_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime


class ReviewCreateModel(ReviewModel):
    rating: int = Field(le=5)
    review_text: str
