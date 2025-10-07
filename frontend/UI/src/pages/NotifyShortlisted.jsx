import React, { useState } from "react";
import api from "../services/api";

export default function NotifyShortlisted() {
  const [jobId, setJobId] = useState("");
  const [notifications, setNotifications] = useState([]);
  const [message, setMessage] = useState("");

  const handleNotify = async () => {
    if (!jobId) return setMessage("Please enter a job ID.");
    setMessage("Sending notifications...");
    try {
      const response = await api.post(
        `/notifications/notify_shortlisted/${jobId}`
      );
      setNotifications(response.data);
      setMessage("Notifications sent.");
    } catch (error) {
      setNotifications([]);
      setMessage(
        "Error sending notifications: " +
          (error.response?.data?.detail || error.message)
      );
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">Notify Shortlisted Candidates</h2>
      <div className="mb-4">
        <input
          type="number"
          placeholder="Enter Job ID"
          className="border px-3 py-2 rounded mr-2"
          value={jobId}
          onChange={(e) => setJobId(e.target.value)}
        />
        <button
          onClick={handleNotify}
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Notify
        </button>
      </div>
      {message && <div className="mb-4 text-indigo-700">{message}</div>}
      {notifications.length > 0 && (
        <div className="mt-4">
          <h3 className="font-semibold mb-2">Notification Status:</h3>
          <ul>
            {notifications.map((n) => (
              <li key={n.notification_id}>
                Candidate {n.candidate_id} for Job {n.job_id} - Status: {n.status}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
