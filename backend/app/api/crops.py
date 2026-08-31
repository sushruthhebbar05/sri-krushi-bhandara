"""Crops API endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Crop

router = APIRouter(prefix="/crops", tags=["crops"])


@router.get("/")
async def list_crops(db: Session = Depends(get_db)):
    """List all crops"""
    crops = db.query(Crop).all()
    return {"items": crops, "total": len(crops)}


@router.get("/{slug}")
async def get_crop(
    slug: str,
    db: Session = Depends(get_db),
):
    """Get crop by slug"""
    crop = db.query(Crop).filter(Crop.slug == slug).first()
    if not crop:
        return {"error": "Crop not found"}
    return crop
