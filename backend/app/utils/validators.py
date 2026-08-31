"""Input validators"""
from typing import List
import os


ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB


def validate_image_file(filename: str, file_size: int) -> tuple[bool, str]:
    """Validate image file"""
    if file_size > MAX_IMAGE_SIZE:
        return False, "Image size exceeds 10MB limit"
    
    _, ext = os.path.splitext(filename.lower())
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        return False, f"Image format not allowed. Use: {', '.join(ALLOWED_IMAGE_EXTENSIONS)}"
    
    return True, ""


def validate_crop_name(crop_name: str) -> tuple[bool, str]:
    """Validate crop name"""
    if not crop_name or len(crop_name) < 2:
        return False, "Crop name must be at least 2 characters"
    
    if len(crop_name) > 255:
        return False, "Crop name exceeds maximum length"
    
    return True, ""


def validate_phone(phone: str) -> tuple[bool, str]:
    """Validate phone number"""
    # Remove common separators
    cleaned = ''.join(c for c in phone if c.isdigit())
    
    if len(cleaned) < 10:
        return False, "Phone number must be at least 10 digits"
    
    if len(cleaned) > 20:
        return False, "Phone number exceeds maximum length"
    
    return True, ""
