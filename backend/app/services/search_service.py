"""Search service for crops, nutrients, problems"""
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import Crop, CropProblem, Nutrient, Product
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class SearchService:
    """Search across agricultural data"""

    @staticmethod
    def search_crops(db: Session, query: str, language: str = "en") -> List[Crop]:
        """Search crops"""
        name_field = Crop.name_en if language == "en" else Crop.name_kn
        return db.query(Crop).filter(
            or_(
                name_field.ilike(f"%{query}%"),
                Crop.description.ilike(f"%{query}%"),
            )
        ).limit(20).all()

    @staticmethod
    def search_problems(db: Session, query: str, language: str = "en") -> List[CropProblem]:
        """Search crop problems"""
        name_field = CropProblem.name_en if language == "en" else CropProblem.name_kn
        return db.query(CropProblem).filter(
            or_(
                name_field.ilike(f"%{query}%"),
                CropProblem.symptoms.ilike(f"%{query}%"),
            )
        ).limit(20).all()

    @staticmethod
    def search_nutrients(db: Session, query: str, language: str = "en") -> List[Nutrient]:
        """Search nutrients"""
        name_field = Nutrient.name_en if language == "en" else Nutrient.name_kn
        return db.query(Nutrient).filter(
            or_(
                name_field.ilike(f"%{query}%"),
                Nutrient.symbol.ilike(f"%{query}%"),
                Nutrient.description.ilike(f"%{query}%"),
            )
        ).limit(20).all()

    @staticmethod
    def global_search(db: Session, query: str, language: str = "en") -> Dict[str, List[Any]]:
        """Search across all data types"""
        return {
            "crops": SearchService.search_crops(db, query, language),
            "problems": SearchService.search_problems(db, query, language),
            "nutrients": SearchService.search_nutrients(db, query, language),
            "products": db.query(Product).filter(
                or_(
                    Product.name.ilike(f"%{query}%"),
                    Product.brand.ilike(f"%{query}%"),
                )
            ).limit(20).all(),
        }
