"""AI Conversation and Message models"""
import uuid
from sqlalchemy import Column, String, Text, DateTime, func, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class AIConversation(Base):
    """AI chat conversation session"""
    __tablename__ = "ai_conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    session_id = Column(String(255), unique=True, nullable=False)  # Session identifier
    conversation_type = Column(String(50), default="general")  # general, crop_analysis, disease_identification
    title = Column(String(255))  # Conversation title
    crop_name = Column(String(255))  # For crop-specific conversations
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<AIConversation {self.session_id}>"


class AIMessage(Base):
    """Individual message in AI conversation"""
    __tablename__ = "ai_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("ai_conversations.id"), nullable=False)
    role = Column(String(50), nullable=False)  # user or assistant
    content = Column(Text, nullable=False)
    image_url = Column(String(500))  # For uploaded images
    analysis_data = Column(Text)  # For structured analysis results
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<AIMessage {self.role}>"
