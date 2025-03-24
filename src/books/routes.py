from fastapi import APIRouter, status, Depends
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession


book_router = APIRouter()

@book_router.get("/")
async def get_all_books():
    pass


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book():
    pass