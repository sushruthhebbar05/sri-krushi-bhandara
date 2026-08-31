"""Llama AI integration service"""
import httpx
import json
import logging
from app.config import settings
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class LlamaService:
    """Llama AI service for crop analysis and chat"""

    def __init__(self):
        self.base_url = settings.llama_base_url
        self.model = settings.llama_model
        self.timeout = 120

    async def generate_response(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 500,
    ) -> str:
        """Generate response from Llama model"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "temperature": temperature,
                        "top_k": 40,
                        "top_p": 0.9,
                        "stream": False,
                    },
                )
                response.raise_for_status()
                data = response.json()
                return data.get("response", "")
        except Exception as e:
            logger.error(f"Llama API error: {e}")
            raise

    async def stream_response(
        self,
        prompt: str,
        temperature: float = 0.7,
    ):
        """Stream response from Llama model"""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                async with client.stream(
                    "POST",
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "temperature": temperature,
                        "stream": True,
                    },
                ) as response:
                    async for line in response.aiter_lines():
                        if line:
                            data = json.loads(line)
                            yield data.get("response", "")
        except Exception as e:
            logger.error(f"Llama streaming error: {e}")
            raise

    async def check_health(self) -> bool:
        """Check if Llama service is available"""
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                return response.status_code == 200
        except Exception as e:
            logger.error(f"Llama health check failed: {e}")
            return False


llama_service = LlamaService()
