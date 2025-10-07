import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import CandidateUpload from "./pages/CandidateUpload.jsx";
import JobCreation from "./pages/JobCreation.jsx";
import CandidateRanking from "./pages/CandidateRanking.jsx";
import JobMatchScoring from "./pages/JobMatchScoring.jsx";
import NotifyShortlisted from "./pages/NotifyShortlisted.jsx";
// import AssessmentStatus from "./pages/AssessmentStatus.jsx";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/upload" element={<CandidateUpload />} />
        <Route path="/job-create" element={<JobCreation />} />
        <Route path="/ranking" element={<CandidateRanking />} />
        <Route path="/match-scoring" element={<JobMatchScoring />} />
        <Route path="/notify-shortlisted" element={<NotifyShortlisted />} />
        {/* <Route path="/assessments" element={<AssessmentStatus />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
