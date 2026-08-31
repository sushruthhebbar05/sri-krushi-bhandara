"""AI schemas"""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from uuid import UUID


class CropAnalysisRequest(BaseModel):
    """Crop analysis request"""
    crop_name: str
    image_url: Optional[str] = None
    symptoms: Optional[str] = None
    location: Optional[str] = None


class CropAnalysisResponse(BaseModel):
    """Crop analysis response"""
    crop: str
    observations: List[str]
    possible_issues: List[Dict[str, Any]]
    confidence: str  # low, moderate, high
    recommended_checks: List[str]
    general_next_steps: List[str]
    safety_note: str


class ChatMessage(BaseModel):
    """Chat message"""
    role: str  # user or assistant
    content: str


class ChatRequest(BaseModel):
    """Chat request"""
    message: str
    conversation_id: Optional[str] = None
    crop_context: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response"""
    conversation_id: str
    response: str
    sources: Optional[List[str]] = None
