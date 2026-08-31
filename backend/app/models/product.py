"""Product model"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, ForeignKey, Float, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    """Agricultural product"""
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    sku = Column(String(100), unique=True)
    brand = Column(String(255))
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)
    
    # Product type details
    product_type = Column(String(100))  # fertilizer, herbicide, fungicide, insecticide, etc.
    active_ingredient = Column(Text)  # For pesticides: active ingredient
    formulation = Column(String(100))  # Granule, Liquid, Powder, WP, EC, etc.
    
    # Application details
    dosage = Column(Text)  # Recommended dosage
    application_method = Column(Text)  # Spray, Drench, Foliar, etc.
    crops = Column(JSONB, default=[])  # List of crop slugs this product is for
    
    # Target details
    target_pest = Column(Text)  # For insecticides
    target_disease = Column(Text)  # For fungicides
    target_weed = Column(Text)  # For herbicides
    
    # Nutrient composition (for fertilizers)
    nutrients = Column(JSONB, default={})  # {"N": 20, "P": 20, "K": 20}
    
    # Product information
    description = Column(Text)
    pack_sizes = Column(JSONB, default=[])  # [{"size": "1 kg", "price": 500}]
    image_url = Column(String(500))
    manufacturer = Column(String(255))
    
    # Status
    is_available = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)
    view_count = Column(Integer, default=0)
    
    # Safety & Compliance
    safety_warnings = Column(Text)
    pre_harvest_interval = Column(String(100))  # For pesticides
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Product {self.name}>"


class ProductCrop(Base):
    """Many-to-many relationship between products and crops"""
    __tablename__ = "product_crops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    crop_id = Column(UUID(as_uuid=True), ForeignKey("crops.id"), nullable=False)
    recommended = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())


class ProductNutrient(Base):
    """Many-to-many relationship between products and nutrients"""
    __tablename__ = "product_nutrients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    nutrient_id = Column(UUID(as_uuid=True), ForeignKey("nutrients.id"), nullable=False)
    percentage = Column(Float)  # % content
    created_at = Column(DateTime, server_default=func.now())
