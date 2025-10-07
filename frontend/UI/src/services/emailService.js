import api from "./api";

/**
 * Send notification emails to shortlisted candidates for a specific job.
 * @param {number} jobId - The job ID for which to send notifications.
 * @returns {Promise} - Axios response promise.
 */

export const sendShortlistNotifications = async (jobId) => {
  const response = await api.post(`/notifications/notify_shortlisted/${jobId}`);
  return response.data;
};



