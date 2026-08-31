"""Products API endpoints"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product, Category
from app.services.product_service import ProductService
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from typing import List, Optional
from uuid import UUID

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=dict)
async def list_products(
    db: Session = Depends(get_db),
    category_id: Optional[str] = Query(None),
    crop: Optional[str] = Query(None),
    featured: Optional[bool] = Query(None),
    skip: int = Query(0),
    limit: int = Query(20),
):
    """List all products with filters"""
    try:
        category_uuid = UUID(category_id) if category_id else None
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid category_id")
    
    products, total = ProductService.get_products(
        db,
        category_id=category_uuid,
        crop=crop,
        is_featured=featured,
        skip=skip,
        limit=limit,
    )
    
    return {
        "total": total,
        "page": skip // limit + 1,
        "per_page": limit,
        "items": products,
    }


@router.get("/{product_id}")
async def get_product(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    """Get product by ID"""
    product = ProductService.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=dict)
async def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    """Create new product (admin only)"""
    # TODO: Add admin authentication check
    product = ProductService.create_product(db, product_data)
    return {"success": True, "product_id": str(product.id)}


@router.put("/{product_id}")
async def update_product(
    product_id: UUID,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
):
    """Update product (admin only)"""
    # TODO: Add admin authentication check
    product = ProductService.update_product(db, product_id, product_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"success": True, "product_id": str(product.id)}


@router.delete("/{product_id}")
async def delete_product(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    """Delete product (admin only)"""
    # TODO: Add admin authentication check
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"success": True}


@router.get("/search/{query}")
async def search_products(
    query: str,
    db: Session = Depends(get_db),
):
    """Search products"""
    products = ProductService.search_products(db, query)
    return {"items": products, "total": len(products)}
