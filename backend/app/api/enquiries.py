"""Enquiries API endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Enquiry
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

router = APIRouter(prefix="/enquiries", tags=["enquiries"])


class EnquiryCreate(BaseModel):
    """Create enquiry"""
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = None
    product_id: Optional[UUID] = None
    product_name: Optional[str] = None
    message: Optional[str] = None


@router.post("/")
async def create_enquiry(
    enquiry: EnquiryCreate,
    db: Session = Depends(get_db),
):
    """Create new enquiry"""
    new_enquiry = Enquiry(**enquiry.dict())
    db.add(new_enquiry)
    db.commit()
    db.refresh(new_enquiry)
    return {"success": True, "enquiry_id": str(new_enquiry.id)}


@router.get("/")
async def list_enquiries(db: Session = Depends(get_db)):
    """List enquiries (admin only)"""
    # TODO: Add admin authentication
    enquiries = db.query(Enquiry).order_by(Enquiry.created_at.desc()).all()
    return {"items": enquiries, "total": len(enquiries)}
