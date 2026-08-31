"""FastAPI main application"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.utils.logger import logger

# Import API routers
from app.api import products, categories, crops, problems, nutrients, enquiries, search
from app.api.ai import router as ai_router

# Create FastAPI app
app = FastAPI(
    title="Sri Krushi Bhandara API",
    description="AI-powered agricultural platform for farmers in Halebeedu, Karnataka",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        settings.frontend_url,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    try:
        init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Sri Krushi Bhandara API",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "environment": settings.environment,
        "business": settings.business_name,
    }


@app.get("/info")
async def business_info():
    """Business information endpoint"""
    return {
        "name": settings.business_name,
        "phone": settings.business_phone,
        "phone_alt": settings.business_phone_alt,
        "address": settings.business_address,
        "city": settings.business_city,
        "state": settings.business_state,
        "country": settings.business_country,
        "gstin": settings.business_gstin,
    }


# Include API routers
app.include_router(products.router, prefix="/api")
app.include_router(categories.router, prefix="/api")
app.include_router(crops.router, prefix="/api")
app.include_router(problems.router, prefix="/api")
app.include_router(nutrients.router, prefix="/api")
app.include_router(enquiries.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(ai_router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
