from sqlalchemy.orm import Session
from app.db import models, schemas
from typing import List

def get_candidate_by_email(db: Session, email: str):
    return db.query(models.Candidate).filter(models.Candidate.email == email).first()

def get_candidate(db: Session, candidate_id: int):
    return db.query(models.Candidate).filter(models.Candidate.candidate_id == candidate_id).first()

def create_candidate(db: Session, candidate: schemas.CandidateCreate):
    db_candidate = models.Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        resume_path=candidate.resume_path
    )
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def update_candidate_resume_path(db: Session, candidate_id: int, resume_path: str):
    candidate = get_candidate(db, candidate_id)
    if candidate:
        candidate.resume_path = resume_path
        db.commit()
        db.refresh(candidate)
    return candidate

def create_parsed_resume(db: Session, candidate_id: int, parsed_data: dict):
    db_parsed = models.ParsedResumeData(
        candidate_id=candidate_id,
        json_data=parsed_data,
        status="success"
    )
    db.add(db_parsed)
    db.commit()
    db.refresh(db_parsed)
    return db_parsed

def get_candidates(db: Session, skip: int = 0, limit: int = 10) -> List[models.Candidate]:
    return db.query(models.Candidate).offset(skip).limit(limit).all()

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        title=job.title,
        description=job.description,
        required_skills=job.required_skills
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db: Session, skip: int = 0, limit: int = 10) -> List[models.Job]:
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.job_id == job_id).first()

def create_candidate_score(db: Session, candidate_id: int, job_id: int, score: float, is_shortlisted: bool, details: str):
    db_score = models.CandidateScore(
        candidate_id=candidate_id,
        job_id=job_id,
        score=score,
        is_shortlisted=is_shortlisted,
        details=details
    )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def get_all_parsed_resumes(db: Session):
    return db.query(models.ParsedResumeData).all()

def get_shortlisted_candidates(db: Session, job_id: int):
    return db.query(models.CandidateScore).filter(
        models.CandidateScore.job_id == job_id,
        models.CandidateScore.is_shortlisted == True
    ).all()

def create_notification(db: Session, candidate_id: int, job_id: int, email_status: str):
    notification = models.Notification(
        candidate_id=candidate_id,
        job_id=job_id,
        email_status=email_status
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification
