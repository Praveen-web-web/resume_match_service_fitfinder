from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, JSON, Text, ForeignKey
from sqlalchemy.orm import relationship
from .session import Base
import datetime

class Candidate(Base):
    __tablename__ = "candidates"
    candidate_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(320), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    resume_path = Column(String(512), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    parsed_resume = relationship("ParsedResumeData", back_populates="candidate", uselist=False)
    scores = relationship("CandidateScore", back_populates="candidate")
    notifications = relationship("Notification", back_populates="candidate")

class ParsedResumeData(Base):
    __tablename__ = "parsed_resume_data"
    parsed_resume_id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.candidate_id"), nullable=False)
    json_data = Column(JSON, nullable=False)
    status = Column(String(50), default="success")
    parsed_on = Column(DateTime, default=datetime.datetime.utcnow)

    candidate = relationship("Candidate", back_populates="parsed_resume")

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    required_skills = Column(JSON, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(50), default="active")

    scores = relationship("CandidateScore", back_populates="job")
    notifications = relationship("Notification", back_populates="job")

class CandidateScore(Base):
    __tablename__ = "candidate_scores"
    score_id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.candidate_id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.job_id"), nullable=False)
    score = Column(Float, nullable=False)
    is_shortlisted = Column(Boolean, default=False)
    details = Column(Text, nullable=True)
    scored_on = Column(DateTime, default=datetime.datetime.utcnow)

    candidate = relationship("Candidate", back_populates="scores")
    job = relationship("Job", back_populates="scores")

class Notification(Base):
    __tablename__ = "notifications"
    notification_id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.candidate_id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.job_id"), nullable=False)
    email_status = Column(String(50), default="pending")
    sent_on = Column(DateTime, nullable=True)

    candidate = relationship("Candidate", back_populates="notifications")
    job = relationship("Job", back_populates="notifications")
