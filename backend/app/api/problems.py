"""Crop problems API endpoints"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import CropProblem

router = APIRouter(prefix="/problems", tags=["problems"])


@router.get("/")
async def list_problems(
    db: Session = Depends(get_db),
    problem_type: str = Query(None),
    crop_slug: str = Query(None),
):
    """List crop problems with filters"""
    query = db.query(CropProblem)
    
    if problem_type:
        query = query.filter(CropProblem.problem_type == problem_type)
    
    problems = query.all()
    return {"items": problems, "total": len(problems)}


@router.get("/{slug}")
async def get_problem(
    slug: str,
    db: Session = Depends(get_db),
):
    """Get crop problem by slug"""
    problem = db.query(CropProblem).filter(CropProblem.slug == slug).first()
    if not problem:
        return {"error": "Problem not found"}
    return problem
