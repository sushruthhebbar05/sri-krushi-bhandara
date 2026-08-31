"""Product service"""
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from app.models import Product, Category, Crop
from app.schemas.product import ProductCreate, ProductUpdate
from typing import List, Optional
from uuid import UUID
import logging

logger = logging.getLogger(__name__)


class ProductService:
    """Product business logic"""

    @staticmethod
    def get_product(db: Session, product_id: UUID) -> Optional[Product]:
        """Get product by ID"""
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            product.view_count += 1
            db.commit()
        return product

    @staticmethod
    def get_products(
        db: Session,
        category_id: Optional[UUID] = None,
        crop: Optional[str] = None,
        is_featured: Optional[bool] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> tuple[List[Product], int]:
        """Get products with filters"""
        query = db.query(Product)

        if category_id:
            query = query.filter(Product.category_id == category_id)

        if crop:
            query = query.filter(Product.crops.contains([crop]))

        if is_featured is not None:
            query = query.filter(Product.is_featured == is_featured)

        total = query.count()
        products = query.offset(skip).limit(limit).all()
        return products, total

    @staticmethod
    def create_product(db: Session, product_data: ProductCreate) -> Product:
        """Create new product"""
        product = Product(**product_data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        logger.info(f"Product created: {product.id}")
        return product

    @staticmethod
    def update_product(
        db: Session,
        product_id: UUID,
        product_data: ProductUpdate,
    ) -> Optional[Product]:
        """Update product"""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None

        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)
        logger.info(f"Product updated: {product_id}")
        return product

    @staticmethod
    def delete_product(db: Session, product_id: UUID) -> bool:
        """Delete product"""
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return False

        db.delete(product)
        db.commit()
        logger.info(f"Product deleted: {product_id}")
        return True

    @staticmethod
    def search_products(db: Session, query: str, limit: int = 20) -> List[Product]:
        """Search products"""
        search_filter = or_(
            Product.name.ilike(f"%{query}%"),
            Product.description.ilike(f"%{query}%"),
            Product.brand.ilike(f"%{query}%"),
        )
        return db.query(Product).filter(search_filter).limit(limit).all()
