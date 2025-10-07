
---

```markdown
# 🧠 Resume Match Service – FitFinder

A modular, production-grade microservice for parsing resumes and matching them to job descriptions using configurable NLP pipelines. Built for seamless integration into FitFinder’s recruitment platform.

---

## 🚀 Features

- 🔍 **Resume Parsing**: Extracts structured data (name, email, location, summary, skills, certifications) using heading-based segmentation and regex/NLP.
- 🧠 **Match Scoring**: Computes semantic and keyword-based match scores against TRF schema or job descriptions.
- ⚙️ **Config-Driven Architecture**: Easily extendable via YAML/JSON configs for parsing rules, scoring weights, and schema mappings.
- 📤 **Triggerable Workflows**: Supports auto-notification, assessment triggers, and candidate shortlisting.
- 🧱 **Microservice Ready**: Designed for containerization, horizontal scaling, and plug-and-play integration.

---

## 🛠️ Tech Stack

| Layer         | Technology                     |
|---------------|--------------------------------|
| Database      | MySQL                          |
| NLP Layer     | FastAPI (Python) via REST      |
| Frontend      | React , tailwindcss            |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/Praveen-web-web/resume_match_service_fitfinder.git
cd resume_match_service_fitfinder

# Backend setup
.create an virtual environment run : python -m venv resume_env
.activate the virtual environment  run : resume_env/Scripts/activate (you will see in the green(colour) resume_env on the starting of the directory path in the terminal (if activated))
.pip install -r requirements.txt (make sure requirements.txt exist with required(libraries)) in the root directory
.uvicorn main:app --reload (make sure the uvicorn is in requirements.txt and main.py should be in root directory) 


# Frontend Setup
.run : npm create vite@latest (and choose the project directory name , react , Javascript)
.cd project directory name
.run : npm install (if node modules not present)
.run : npm install -D tailwindcss postcss autoprefixer
.run : npx tailwindcss init -p
.run : npm run dev
```

---

## 📄 API Overview

### `POST /parse-resume`
Parses uploaded resume and returns structured JSON.

```json
{
  "name": "John Doe",
  "location": "Delhi, India",
  "skills": ["Java", "Spring Boot", "MySQL"],
  "certifications": ["AWS Certified Developer"]
}
```

### `POST /match`
Accepts parsed resume + job description or TRF schema, returns match score and rationale.

---

## 🧪 Testing

```bash
# Run unit tests
./gradlew test

# Run integration tests
./gradlew integrationTest
```

---

## 📁 Project Structure

```
resume_match_service_fitfinder/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── candidates.py
│   │   │   │   ├── jobs.py
│   │   │   │   ├── matches.py
│   │   │   │   ├── notifications.py
│   │   │   │   └── assessments.py
│   │   │   └── _init_.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── email_service.py
│   │   │   ├── parsing.py        # resume parsing core logic
│   │   │   ├── scoring.py        # matching and scoring engine
│   │   │   └── _init_.py
│   │   ├── db/
│   │   │   ├── models.py
│   │   │   ├── repository.py
│   │   │   ├── schemas.py         # Pydantic schemas for validation
│   │   │   └── session.py         # DB session and connection
│   │   ├── main.py                # FastAPI app entrypoint
│   │   └── _init_.py
│   ├── Dockerfile               # containerize backend
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/               # images, icons etc.
│   │   ├── components/
│   │   │   ├── CandidateCard.jsx
│   │   │   ├── JobCard.jsx
│   │   │   ├── NotificationToast.jsx
│   │   │   └── AssessmentModal.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── CandidateUpload.jsx
│   │   │   ├── JobCreation.jsx
│   │   │   ├── CandidateRanking.jsx
│   │   │   └── AssessmentStatus.jsx
│   │   ├── services/
│   │   │   ├── api.js          # axios instance for API calls
│   │   │   └── emailService.js
│   │   ├── styles/
│   │   │   └── tailwind.css
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── tailwind.config.js
│   ├── package.json
│   ├── postcss.config.js
│   └── README.md
│
├── docker-compose.yml          # orchestration of backend + frontend + DB
└── README.md
```

---

## 🔐 Security & Legal

- All endpoints protected via JWT. (not implemented as of now)
- Resume data processed in-memory; no persistent storage unless explicitly configured.
- Licensed under MIT. Attribution required for derivative works.

---

## 📈 Roadmap

- [x] Heading-based segmentation
- [x] Regex + NLP hybrid parser
- [x] TRF schema alignment
- [ ] PDF/DOCX ingestion
- [ ] Multilingual resume support
- [ ] Admin dashboard for parser tuning

---

## 🤝 Contributing

Pull requests welcome. Please ensure:
- Code is modular and test-covered
- Configs are documented
- No unused variables or incomplete modules(except the candidate ranking logic)

---

## 👨‍💻 Author

**Praveen Baghel**  
Final-year CSE | Backend & ML Systems Architect  
📍 T.Y.C, Agra-282006, India  
📫 [LinkedIn](https://www.linkedin.com/in/praveenbaghel5573) | [GitHub](https://github.com/Praveen-web-web)

---

```

---


