from fastapi import APIRouter, Depends
from src.db.models import User
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import ReviewCreateModel 
from src.auth.dependencies import AccessTokenBearer
from .service import ReviewService


review_router = APIRouter()
review_service = ReviewService()
access_token_bearer = AccessTokenBearer()


@review_router.post("/books/{book_uid}")
async def add_review_to_book(
    book_uid: str,
    review_data: ReviewCreateModel,
    current_user: User = Depends(access_token_bearer),
    session: AsyncSession = Depends(get_session),
):
    new_review = await review_service.add_review_to_book(
        user_email=current_user.email,
        book_uid=book_uid,
        review_data=review_data,
        session=session,
    )

    return new_review
