"""Product schemas"""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from uuid import UUID


class ProductCreate(BaseModel):
    """Create product schema"""
    name: str
    brand: Optional[str] = None
    category_id: UUID
    product_type: Optional[str] = None
    active_ingredient: Optional[str] = None
    formulation: Optional[str] = None
    dosage: Optional[str] = None
    application_method: Optional[str] = None
    crops: Optional[List[str]] = []
    target_pest: Optional[str] = None
    target_disease: Optional[str] = None
    target_weed: Optional[str] = None
    nutrients: Optional[Dict[str, float]] = {}
    description: Optional[str] = None
    pack_sizes: Optional[List[Dict[str, Any]]] = []
    manufacturer: Optional[str] = None
    safety_warnings: Optional[str] = None
    pre_harvest_interval: Optional[str] = None
    is_featured: bool = False


class ProductUpdate(BaseModel):
    """Update product schema"""
    name: Optional[str] = None
    brand: Optional[str] = None
    category_id: Optional[UUID] = None
    is_available: Optional[bool] = None
    is_featured: Optional[bool] = None
    description: Optional[str] = None


class ProductResponse(BaseModel):
    """Product response schema"""
    id: UUID
    name: str
    brand: Optional[str]
    category_id: UUID
    product_type: Optional[str]
    description: Optional[str]
    image_url: Optional[str]
    is_available: bool
    is_featured: bool
    view_count: int

    class Config:
        from_attributes = True
