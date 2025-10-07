export default function CandidateCard({ candidate, score, onView }) {
  return (
    <div className="bg-white p-4 rounded-md shadow-md hover:shadow-lg transition-shadow duration-300 mb-4">
      <h3 className="text-lg font-semibold">{candidate.name}</h3>
      <p className="text-gray-600">{candidate.email}</p>
      <p className="text-indigo-700 font-semibold">Score: {score.toFixed(2)}</p>
      <button
        onClick={onView}
        className="mt-2 px-3 py-1 bg-indigo-600 rounded text-white hover:bg-indigo-700"
      >
        View Details
      </button>
    </div>
  );
}
