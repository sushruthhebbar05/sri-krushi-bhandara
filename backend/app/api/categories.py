"""Categories API endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/")
async def list_categories(db: Session = Depends(get_db)):
    """List all product categories"""
    categories = db.query(Category).filter(Category.is_active == True).order_by(Category.order).all()
    return {"items": categories, "total": len(categories)}


@router.get("/{slug}")
async def get_category(
    slug: str,
    db: Session = Depends(get_db),
):
    """Get category by slug"""
    category = db.query(Category).filter(Category.slug == slug).first()
    if not category:
        return {"error": "Category not found"}
    return category
