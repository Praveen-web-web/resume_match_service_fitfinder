from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models, schemas, repository
from app.db.session import get_db
from app.core.parsing import parse_resume
from typing import List
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploaded_resumes"

@router.post("/", response_model=schemas.Candidate)
def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = repository.get_candidate_by_email(db, candidate.email)
    if db_candidate:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repository.create_candidate(db, candidate)

@router.post("/upload_resume/{candidate_id}", status_code=201)
def upload_resume(candidate_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_location = os.path.join(UPLOAD_DIR, f"{candidate_id}_{file.filename}")
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed_data = parse_resume(file_location)
    if not parsed_data:
        raise HTTPException(status_code=400, detail="Failed to parse resume")

    # Update candidate resume_path and add parsed data
    candidate = repository.get_candidate(db, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    repository.update_candidate_resume_path(db, candidate_id, file_location)
    repository.create_parsed_resume(db, candidate_id, parsed_data)
    return {"filename": file.filename, "parsed": True}



#extra
@router.get("/", response_model=List[schemas.Candidate])
def list_candidates(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return repository.get_candidates(db, skip, limit)

@router.get("/{candidate_id}", response_model=schemas.Candidate)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    db_candidate = repository.get_candidate(db, candidate_id)
    if not db_candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return db_candidate