import React from "react";

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-gray-800">Your Dashboard</h1>
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="p-6 bg-white rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">Mood Tracker</h2>
          <p className="text-gray-600">Your recent mood entries and trends.</p>
        </div>
        <div className="p-6 bg-white rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">Recommendations</h2>
          <p className="text-gray-600">Personalized mental health tips for you.</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;