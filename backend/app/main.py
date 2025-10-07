from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.endpoints import candidates, jobs, matches, notifications, assessments
from app.db.session import engine, Base


app = FastAPI(title="FitFinder Resume Matching Microservice")  # Define once

# CORS setup

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB setup
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(matches.router, prefix="/matches", tags=["Matches"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
# app.include_router(assessments.router, prefix="/assessments", tags=["Assessments"])
