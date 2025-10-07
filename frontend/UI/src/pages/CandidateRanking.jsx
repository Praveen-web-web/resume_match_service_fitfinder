import React, { useState,} from "react";
import api from "../services/api";
// import CandidateCard from "../components/CandidateCard.jsx";

export default function CandidateRanking() {
  const [jobId, setJobId] = useState("");
  const [candidateScores, setCandidateScores] = useState([]);
  const [message, setMessage] = useState("");

  const fetchShortlisted = async () => {
    if (!jobId) return setMessage("Please enter a job ID.");
    try {
      const response = await api.get(`/matches/shortlisted/${jobId}`);
      setCandidateScores(response.data);
      setMessage("");
    }catch (error) {
      setMessage("Error fetching shortlisted candidates: " + (error.response?.data?.detail || error.message));
      setCandidateScores([]);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">Candidate Ranking</h2>
      <div className="mb-4">
        <input
          type="number"
          placeholder="Enter Job ID"
          className="border px-3 py-2 rounded mr-2"
          value={jobId}
          onChange={(e) => setJobId(e.target.value)}
        />
        <button
          onClick={fetchShortlisted}
          className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
        >
          Fetch Shortlisted
        </button>
      </div>
      {message && <div className="text-red-600 mb-4">{message}</div>}
      {candidateScores.map(({ candidate_id, score, candidate }) => (
        <CandidateCard
          key={candidate_id}
          candidate={candidate}
          score={score}
          onView={() => alert(`Viewing candidate ${candidate.name}`)}
        />
      ))}
      {candidateScores.length === 0 && !message && <p>No shortlisted candidates found.</p>}
    </div>
  );
}
