"""AI Chat API endpoints"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AIConversation, AIMessage
from app.services.ai.llama_service import llama_service
from app.services.ai.crop_analyzer import CropAnalyzer
from app.schemas.ai import ChatRequest, CropAnalysisRequest
import uuid
import logging
from typing import AsyncGenerator

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    """Chat with AI Crop Doctor"""
    try:
        # Get or create conversation
        if request.conversation_id:
            conversation = db.query(AIConversation).filter(
                AIConversation.session_id == request.conversation_id
            ).first()
            if not conversation:
                raise HTTPException(status_code=404, detail="Conversation not found")
        else:
            conversation = AIConversation(
                session_id=str(uuid.uuid4()),
                conversation_type="general",
            )
            db.add(conversation)
            db.commit()
            db.refresh(conversation)

        # Build context from previous messages
        previous_messages = db.query(AIMessage).filter(
            AIMessage.conversation_id == conversation.id
        ).order_by(AIMessage.created_at).limit(5).all()

        context = "\n".join(
            f"{msg.role}: {msg.content}" for msg in previous_messages
        )

        # Build prompt
        from app.services.ai.prompts import CROP_DOCTOR_SYSTEM_PROMPT, CHAT_PROMPT_TEMPLATE
        prompt = CROP_DOCTOR_SYSTEM_PROMPT + "\n\n" + CHAT_PROMPT_TEMPLATE.format(
            context=context,
            message=request.message,
        )

        # Generate response
        response = await llama_service.generate_response(
            prompt,
            temperature=0.7,
            max_tokens=500,
        )

        # Store messages
        user_msg = AIMessage(
            conversation_id=conversation.id,
            role="user",
            content=request.message,
        )
        db.add(user_msg)

        assistant_msg = AIMessage(
            conversation_id=conversation.id,
            role="assistant",
            content=response,
        )
        db.add(assistant_msg)
        db.commit()

        return {
            "conversation_id": conversation.session_id,
            "response": response,
            "sources": [],
        }
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail="AI service error")


@router.post("/crop-analysis")
async def analyze_crop(
    request: CropAnalysisRequest,
    db: Session = Depends(get_db),
):
    """Analyze crop problem with AI"""
    try:
        analysis = await CropAnalyzer.analyze_crop_problem(
            request.crop_name,
            request.symptoms,
            request.location,
        )
        return analysis
    except Exception as e:
        logger.error(f"Crop analysis error: {e}")
        raise HTTPException(status_code=500, detail="Analysis failed")


@router.get("/health")
async def ai_health():
    """Check AI service health"""
    is_healthy = await llama_service.check_health()
    return {"status": "healthy" if is_healthy else "unhealthy", "service": "llama"}
