import React, { useEffect } from "react";

export default function NotificationToast({ message, type = "info", onClose }) {
  useEffect(() => {
    if (!message) return;
    const timer = setTimeout(() => {
      onClose();
    }, 4000); // auto close after 4 seconds
    return () => clearTimeout(timer);
  }, [message, onClose]);

  if (!message) return null;

  const bgColors = {
    info: "bg-blue-500",
    success: "bg-green-500",
    warning: "bg-yellow-500",
    error: "bg-red-500",
  };

  return (
    <div
      className={`fixed top-5 right-5 z-50 px-4 py-2 rounded shadow-lg text-white ${bgColors[type]}`}
      role="alert"
    >
      <div className="flex items-center">
        <span className="mr-2 font-semibold">
          {type.charAt(0).toUpperCase() + type.slice(1)}
        </span>
        <span>{message}</span>
        <button
          onClick={onClose}
          className="ml-4 text-white opacity-75 hover:opacity-100"
          aria-label="Close notification"
        >
          &#10005;
        </button>
      </div>
    </div>
  );
}
