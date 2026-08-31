"""Nutrients API endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Nutrient

router = APIRouter(prefix="/nutrients", tags=["nutrients"])


@router.get("/")
async def list_nutrients(db: Session = Depends(get_db)):
    """List all nutrients"""
    nutrients = db.query(Nutrient).all()
    return {"items": nutrients, "total": len(nutrients)}


@router.get("/{symbol}")
async def get_nutrient(
    symbol: str,
    db: Session = Depends(get_db),
):
    """Get nutrient by symbol"""
    nutrient = db.query(Nutrient).filter(Nutrient.symbol == symbol.upper()).first()
    if not nutrient:
        return {"error": "Nutrient not found"}
    return nutrient
