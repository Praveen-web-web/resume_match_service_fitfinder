import React, { useState } from "react";
import api from "../services/api";

export default function CandidateUpload() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [resumeFile, setResumeFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setResumeFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Step 1: create candidate (without resume)
      const resCandidate = await api.post("/candidates/", {
        name,
        email,
        phone,
        resume_path: "", // placeholder
      });

      // Step 2: upload resume file for created candidate
      const candidateId = resCandidate.data.candidate_id;
      const formData = new FormData();
      formData.append("file", resumeFile);

      await api.post(`/candidates/upload_resume/${candidateId}`, formData, {
        // headers: {
        //   "Content-Type": "multipart/form-data",
        // },
      });

      setMessage("Candidate and resume uploaded successfully!");
      setName("");
      setEmail("");
      setPhone("");
      setResumeFile(null);
    } catch (error) {
      setMessage("Error uploading candidate: " + (error.response?.data?.detail || error.message));
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Upload Candidate Resume</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          placeholder="Full Name"
          className="w-full border rounded px-3 py-2"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          className="w-full border rounded px-3 py-2"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="tel"
          placeholder="Phone"
          className="w-full border rounded px-3 py-2"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
        <input type="file" onChange={handleFileChange} required accept=".pdf,.docx,.txt" />
        <button
          type="submit"
          className="w-full bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
        >
          Upload
        </button>
      </form>
      {message && (
        <div className="mt-4 p-3 bg-green-100 text-green-700 rounded">{message}</div>
      )}
    </div>
  );
}
