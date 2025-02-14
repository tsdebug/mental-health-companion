import React, { useState } from "react";

const Mood = () => {
  const [mood, setMood] = useState("");

  const handleMoodSubmit = (e) => {
    e.preventDefault();
    console.log("Mood recorded:", mood);
    // Save mood data
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-96">
        <h2 className="text-2xl font-semibold text-center mb-4">How are you feeling today?</h2>
        <form onSubmit={handleMoodSubmit}>
          <select
            className="w-full p-2 border rounded mb-4"
            value={mood}
            onChange={(e) => setMood(e.target.value)}
          >
            <option value="">Select your mood</option>
            <option value="Happy">Happy 😊</option>
            <option value="Sad">Sad 😔</option>
            <option value="Anxious">Anxious 😟</option>
            <option value="Excited">Excited 🤩</option>
          </select>
          <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded">
            Save Mood
          </button>
        </form>
      </div>
    </div>
  );
};

export default Mood;