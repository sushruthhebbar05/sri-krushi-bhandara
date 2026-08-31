"""Product category model"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Category(Base):
    """Product category"""
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String(255), nullable=False)
    name_kn = Column(String(255), nullable=False)  # Kannada name
    slug = Column(String(255), unique=True, nullable=False)
    description_en = Column(Text)
    description_kn = Column(Text)
    image_url = Column(String(500))
    order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Category {self.name_en}>"
