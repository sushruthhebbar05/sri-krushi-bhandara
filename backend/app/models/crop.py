"""Crop and crop problem models"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Crop(Base):
    """Agricultural crop"""
    __tablename__ = "crops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String(255), unique=True, nullable=False)
    name_kn = Column(String(255))  # Kannada name
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    image_url = Column(String(500))
    growth_period = Column(String(100))  # e.g., "120-150 days"
    season = Column(String(100))  # e.g., "Kharif, Rabi"
    region = Column(String(255))  # e.g., "Karnataka, Tamil Nadu"
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Crop {self.name_en}>"


class CropProblem(Base):
    """Crop problems/diseases/pests/deficiencies"""
    __tablename__ = "crop_problems"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String(255), nullable=False)
    name_kn = Column(String(255))  # Kannada name
    slug = Column(String(255), unique=True, nullable=False)
    problem_type = Column(String(50), nullable=False)  # disease, pest, deficiency, weed
    crop_id = Column(UUID(as_uuid=True), ForeignKey("crops.id"))
    symptoms = Column(Text)
    causes = Column(Text)
    management = Column(Text)
    image_url = Column(String(500))
    severity = Column(String(50))  # mild, moderate, severe
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<CropProblem {self.name_en}>"
