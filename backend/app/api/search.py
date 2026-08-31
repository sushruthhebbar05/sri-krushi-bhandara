"""Search API endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/")
async def global_search(
    q: str = Query(...),
    language: str = Query("en"),
    db: Session = Depends(get_db),
):
    """Global search across all data"""
    results = SearchService.global_search(db, q, language)
    return results
