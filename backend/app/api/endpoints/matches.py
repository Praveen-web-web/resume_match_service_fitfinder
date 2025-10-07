from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, repository
from app.db.session import get_db
from app.core.scoring import score_candidate_resume
from typing import List

router = APIRouter()

@router.post("/score/{job_id}", response_model=List[schemas.CandidateScore])
def score_candidates_for_job(job_id: int, db: Session = Depends(get_db)):
    job = repository.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    parsed_candidates = repository.get_all_parsed_resumes(db)
    results = []

    for parsed_resume in parsed_candidates:
        score_val = score_candidate_resume(parsed_resume.json_data, job.required_skills)
        is_shortlisted = score_val >= 60  # example threshold 60%
        score_record = repository.create_candidate_score(
            db,
            parsed_resume.candidate_id,
            job_id,
            score_val,
            is_shortlisted,
            details=f"Matched against skills: {job.required_skills}"
        )
        results.append(score_record)

    return results

@router.get("/shortlisted/{job_id}", response_model=List[schemas.CandidateScore])
def get_shortlisted_candidates(job_id: int, db: Session = Depends(get_db)):
    return repository.get_shortlisted_candidates(db, job_id)
