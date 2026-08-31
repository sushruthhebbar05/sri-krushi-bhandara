"""Application configuration"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""

    # Database
    database_url: str
    
    # JWT
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 86400  # 24 hours
    
    # Admin
    admin_email: str
    admin_password: Optional[str] = None
    
    # Llama AI
    llama_api_key: Optional[str] = None
    llama_base_url: str = "http://localhost:11434"
    llama_model: str = "llama2"
    
    # Frontend
    frontend_url: str = "http://localhost:3000"
    
    # Environment
    environment: str = "development"
    debug: bool = True
    
    # Business Info
    business_name: str = "Sri Krushi Bhandara"
    business_phone: str = "9535839987"
    business_phone_alt: str = "7483940895"
    business_email: Optional[str] = None
    business_gstin: str = "29BYRPP6958A1ZQ"
    business_address: str = "Near SBI Bank, Rajanasiriyur Road, Halebeedu - 573121"
    business_city: str = "Halebeedu"
    business_state: str = "Karnataka"
    business_country: str = "India"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
