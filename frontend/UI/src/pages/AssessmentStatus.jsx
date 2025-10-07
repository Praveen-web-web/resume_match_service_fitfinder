import React, { useState } from "react";

export default function AssessmentStatus() {
  const [candidateId, setCandidateId] = useState("");
  const [jobId, setJobId] = useState("");
  const [statusMessage, setStatusMessage] = useState("");

  const checkStatus = async () => {
    // Placeholder for calling assessment status API
    setStatusMessage(`Checking assessment status for Candidate ${candidateId} on Job ${jobId}...`);

    // Implement actual API call here later
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Assessment Status</h2>
      <input
        type="number"
        placeholder="Candidate ID"
        value={candidateId}
        onChange={(e) => setCandidateId(e.target.value)}
        className="border rounded p-2 mb-4 w-full"
      />
      <input
        type="number"
        placeholder="Job ID"
        value={jobId}
        onChange={(e) => setJobId(e.target.value)}
        className="border rounded p-2 mb-4 w-full"
      />
      <button
        onClick={checkStatus}
        className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 w-full"
      >
        Check Status
      </button>
      {statusMessage && (
        <div className="mt-4 p-3 bg-blue-100 text-blue-700 rounded">{statusMessage}</div>
      )}
    </div>
  );
}
