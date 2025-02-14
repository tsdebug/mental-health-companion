import React from "react";

const Recommendations = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-gray-800">Your Wellness Tips</h1>
      <div className="mt-6 space-y-4">
        <div className="p-4 bg-white rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">Take a deep breath</h2>
          <p className="text-gray-600">Practice deep breathing exercises to reduce stress.</p>
        </div>
        <div className="p-4 bg-white rounded-lg shadow-md">
          <h2 className="text-xl font-semibold">Stay Active</h2>
          <p className="text-gray-600">A short walk or some light exercise can boost your mood.</p>
        </div>
      </div>
    </div>
  );
};

export default Recommendations;