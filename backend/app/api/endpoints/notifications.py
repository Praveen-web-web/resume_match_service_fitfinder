from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db import repository, schemas
from app.db.session import get_db
from app.core.email_service import send_email
from typing import List

router = APIRouter()

@router.post("/notify_shortlisted/{job_id}", response_model=List[schemas.Notification])
def notify_shortlisted(job_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    shortlisted = repository.get_shortlisted_candidates(db, job_id)
    if not shortlisted:
        raise HTTPException(status_code=404, detail="No shortlisted candidates found")

    notifications = []
    for candidate_score in shortlisted:
        candidate = repository.get_candidate(db, candidate_score.candidate_id)
        job = repository.get_job(db, job_id)
        subject = f"Assessment Invitation for {job.title}"
        body = f"""
        Dear {candidate.name},<br><br>
        Congratulations! You have been shortlisted for the position <strong>{job.title}</strong>.<br>
        Please <a href='https://assessment.example.com/assessment/{candidate.candidate_id}/{job.job_id}'>click here</a> to take your assessment.<br><br>
        Best regards,<br>FitFinder Team
        """
        background_tasks.add_task(send_email, candidate.email, subject, body)

        notification = repository.create_notification(
            db, candidate.candidate_id, job_id, "sent"
        )
        notifications.append(notification)
    return notifications




#extra
@router.get("/notifications/{candidate_id}", response_model=List[schemas.Notification])
def get_notifications(candidate_id: int, db: Session = Depends(get_db)):
    candidate = repository.get_candidate(db, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return repository.get_notifications_for_candidate(db, candidate_id)