
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">FitFinder Dashboard</h1>
      <ul className="space-y-4">
        <li>
          <Link
            to="/upload"
            className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
          >
            Upload Candidate Resume
          </Link>
        </li>
        <li>
          <Link
            to="/job-create"
            className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
          >
            Create Job Posting
          </Link>
        </li>
        <li>
          <Link
            to="/ranking"
            className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
          >
            View Candidate Rankings
          </Link>
        </li>
        {/* <li>
          <Link
            to="/assessments"
            className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
          >
            Track Assessment Status
          </Link>
        </li> */}
        <li>
      <Link
    to="/match-scoring"
    className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
  >
    Run Candidate Matching
  </Link>
</li>
<li>
  <Link
    to="/notify-shortlisted"
    className="block px-6 py-4 bg-indigo-600 rounded text-white text-lg hover:bg-indigo-700"
  >
    Notify Shortlisted Candidates
  </Link>
</li>

      </ul>
    </div>
  );
}
