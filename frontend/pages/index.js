import React from "react";

const Index = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-400 to-purple-500 text-white">
      <div className="text-center">
        <h1 className="text-4xl font-bold">Welcome to MindMate</h1>
        <p className="mt-4 text-lg">
          Your AI-powered mental health companion. Track your mood, get insights, and improve your well-being.
        </p>
        <div className="mt-6">
          <a href="/login" className="px-6 py-3 bg-white text-blue-600 font-semibold rounded-lg shadow-md">
            Get Started
          </a>
        </div>
      </div>
    </div>
  );
};

export default Index;