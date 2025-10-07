from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, repository
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return repository.create_job(db, job)

@router.get("/", response_model=List[schemas.Job])
def list_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return repository.get_jobs(db, skip, limit)

@router.get("/{job_id}", response_model=schemas.Job)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = repository.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
