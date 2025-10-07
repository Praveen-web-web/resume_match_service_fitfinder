import React, { useState } from "react";
import api from "../services/api";

export default function JobMatchScoring() {
  const [jobId, setJobId] = useState("");
  const [scores, setScores] = useState([]);
  const [message, setMessage] = useState("");

  const runScoring = async () => {
    if (!jobId) return setMessage("Please enter a job ID.");
    setMessage("Scoring candidates...");
    try {
      const response = await api.post(`/matches/score/${jobId}`);
      setScores(response.data);
      setMessage("Scoring complete.");
    } catch (error) {
      setScores([]);
      setMessage(
        "Error scoring candidates: " +
          (error.response?.data?.detail || error.message)
      );
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">Run Candidate Matching</h2>
      <div className="mb-4">
        <input
          type="number"
          placeholder="Enter Job ID"
          className="border px-3 py-2 rounded mr-2"
          value={jobId}
          onChange={(e) => setJobId(e.target.value)}
        />
        <button
          onClick={runScoring}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Score Candidates
        </button>
      </div>
      {message && <div className="mb-4 text-indigo-700">{message}</div>}
      {scores.length > 0 && (
        <div className="mt-4">
          <h3 className="font-semibold mb-2">Score Results:</h3>
          <ul>
            {scores.map((s) => (
              <li key={s.candidate_id}>
                {s.candidate?.name || s.candidate_id}: {s.score} (
                {s.is_shortlisted ? "Shortlisted" : "Not shortlisted"})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
