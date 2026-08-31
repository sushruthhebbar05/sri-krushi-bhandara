"""Crop analyzer for AI-assisted crop diagnosis"""
import json
import logging
from app.services.ai.llama_service import llama_service
from app.services.ai.prompts import CROP_ANALYSIS_PROMPT
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class CropAnalyzer:
    """AI-powered crop problem analyzer"""

    @staticmethod
    async def analyze_crop_problem(
        crop_name: str,
        symptoms: str,
        location: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Analyze crop problem using Llama"""
        try:
            # Build prompt
            location_info = f"Location: {location}" if location else ""
            prompt = CROP_ANALYSIS_PROMPT.format(
                crop=crop_name,
                symptoms=symptoms,
                location_info=location_info,
            )

            # Get response from Llama
            response = await llama_service.generate_response(
                prompt,
                temperature=0.3,  # More deterministic for medical-like tasks
                max_tokens=1000,
            )

            # Parse JSON response
            try:
                analysis = json.loads(response)
            except json.JSONDecodeError:
                logger.warning(f"Could not parse Llama response as JSON: {response}")
                analysis = {
                    "observations": [symptoms],
                    "possible_issues": [],
                    "recommended_checks": [
                        "Inspect leaves and stems closely",
                        "Check soil moisture",
                        "Look for pest presence",
                    ],
                    "general_next_steps": [
                        "Consult with local agricultural expert",
                        "Visit Sri Krushi Bhandara for personalized advice",
                    ],
                    "safety_note": "Always verify field diagnosis before applying any treatment.",
                }

            return {
                "crop": crop_name,
                "observations": analysis.get("observations", []),
                "possible_issues": analysis.get("possible_issues", []),
                "confidence": "moderate",
                "recommended_checks": analysis.get("recommended_checks", []),
                "general_next_steps": analysis.get("general_next_steps", []),
                "safety_note": analysis.get(
                    "safety_note",
                    "Always verify field diagnosis before applying any treatment.",
                ),
            }
        except Exception as e:
            logger.error(f"Crop analysis error: {e}")
            return {
                "crop": crop_name,
                "observations": [symptoms],
                "possible_issues": [],
                "confidence": "low",
                "recommended_checks": [
                    "Please consult with Sri Krushi Bhandara agricultural advisor",
                ],
                "general_next_steps": [
                    "Visit our store or call 9535839987 for personalized guidance",
                ],
                "safety_note": "AI analysis is preliminary. Always consult with experts before taking action.",
            }
