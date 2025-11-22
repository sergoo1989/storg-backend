"use client";

import { useEffect, useState } from "react";

export default function Header() {
  const [user, setUser] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      const payload = JSON.parse(atob(token.split(".")[1]));
      setUser(payload.sub);
    }
  }, []);

  return (
    <header className="w-full bg-white shadow-sm px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold text-primary">STORG Dashboard</h1>

      <div className="flex items-center gap-4">
        <span className="font-medium">{user}</span>
        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/login";
          }}
          className="bg-danger text-white px-4 py-2 rounded-md"
        >
          Logout
        </button>
      </div>
    </header>
  );
}
