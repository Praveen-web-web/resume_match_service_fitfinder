

export default function JobCard({ job, onView }) {
  return (
    <div className="bg-white p-4 rounded-md shadow-md hover:shadow-lg transition-shadow duration-300 mb-4 cursor-pointer" onClick={onView}>
      <h3 className="text-lg font-semibold text-indigo-700">{job.title}</h3>
      <p className="text-gray-700 mb-2">{job.description}</p>
      <div className="text-sm text-gray-500">
        <strong>Required Skills: </strong>
        {job.required_skills.join(", ")}
      </div>
    </div>
  );
}
