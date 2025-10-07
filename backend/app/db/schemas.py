from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class CandidateBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]

class CandidateCreate(CandidateBase):
    resume_path: str

class Candidate(CandidateBase):
    candidate_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ParsedResumeDataBase(BaseModel):
    candidate_id: int
    json_data: dict
    status: Optional[str] = "success"

class ParsedResumeDataCreate(ParsedResumeDataBase):
    pass

class ParsedResumeData(ParsedResumeDataBase):
    parsed_resume_id: int
    parsed_on: datetime

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    title: str
    description: str
    required_skills: List[str]

class JobCreate(JobBase):
    pass

class Job(JobBase):
    job_id: int
    created_on: datetime
    status: Optional[str] = "active"

    class Config:
        orm_mode = True

class CandidateScoreBase(BaseModel):
    candidate_id: int
    job_id: int
    score: float
    is_shortlisted: Optional[bool] = False
    details: Optional[str]

class CandidateScoreCreate(CandidateScoreBase):
    pass

class CandidateScore(CandidateScoreBase):
    score_id: int
    scored_on: datetime

    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    candidate_id: int
    job_id: int
    email_status: Optional[str] = "pending"
    sent_on: Optional[datetime]

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    notification_id: int

    class Config:
        orm_mode = True
