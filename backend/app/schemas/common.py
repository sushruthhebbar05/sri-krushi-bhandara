"""Common schemas"""
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class TimestampMixin(BaseModel):
    """Mixin for timestamp fields"""
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ResponseBase(BaseModel):
    """Base response schema"""
    success: bool
    message: str


class PaginatedResponse(BaseModel):
    """Paginated response schema"""
    total: int
    page: int
    per_page: int
    items: list
