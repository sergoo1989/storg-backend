"use client";
import { useState, useEffect } from "react";

export function Toast({ message }: { message: string }) {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const timeout = setTimeout(() => setVisible(false), 2500);
    return () => clearTimeout(timeout);
  }, []);

  if (!visible) return null;

  return (
    <div className="fixed bottom-6 right-6 bg-primary text-white px-6 py-3 rounded-lg shadow-lg">
      {message}
    </div>
  );
}
