"""Enquiry model for customer inquiries"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Enquiry(Base):
    """Customer product enquiry"""
    __tablename__ = "enquiries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = Column(String(255), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    customer_email = Column(String(255))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    product_name = Column(String(255))  # In case product is deleted
    message = Column(Text)
    status = Column(String(50), default="new")  # new, contacted, resolved
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Enquiry {self.customer_phone}>"
