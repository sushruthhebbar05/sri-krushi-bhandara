"""Nutrient model"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, Float
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Nutrient(Base):
    """Plant nutrient"""
    __tablename__ = "nutrients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol = Column(String(10), unique=True, nullable=False)  # N, P, K, Zn, etc.
    name_en = Column(String(255), nullable=False)
    name_kn = Column(String(255))  # Kannada name
    category = Column(String(50), nullable=False)  # macro, secondary, micro
    description = Column(Text)
    deficiency_symptoms = Column(Text)
    plant_role = Column(Text)
    sources = Column(Text)  # Organic and inorganic sources
    image_url = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Nutrient {self.symbol}>"
