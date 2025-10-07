import React, { useState } from "react";
import api from "../services/api";

export default function JobCreation() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [requiredSkills, setRequiredSkills] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const skillsList = requiredSkills.split(",").map((s) => s.trim());
      await api.post("/jobs/", {
        title,
        description,
        required_skills: skillsList,
      });
      setMessage("Job created successfully!");
      setTitle("");
      setDescription("");
      setRequiredSkills("");
    } catch (error) {
      setMessage("Error creating job: " + (error.response?.data?.detail || error.message));
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Create Job Posting</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          placeholder="Job Title"
          className="w-full border rounded px-3 py-2"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea
          placeholder="Job Description"
          rows={4}
          className="w-full border rounded px-3 py-2"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Required Skills (comma separated)"
          className="w-full border rounded px-3 py-2"
          value={requiredSkills}
          onChange={(e) => setRequiredSkills(e.target.value)}
          required
        />
        <button
          type="submit"
          className="w-full bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
        >
          Create Job
        </button>
      </form>
      {message && (
        <div className="mt-4 p-3 bg-green-100 text-green-700 rounded">{message}</div>
      )}
    </div>
  );
}
