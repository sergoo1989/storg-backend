"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Sidebar() {
  const pathname = usePathname();

  const menu = [
    { name: "Overview", path: "/dashboard" },
    { name: "Users", path: "/dashboard/users" },
    { name: "Inventory", path: "/dashboard/inventory" },
    { name: "Pricing Engine", path: "/dashboard/pricing" },
    { name: "Fulfillment", path: "/dashboard/fulfillment" },
    { name: "Quality Control", path: "/dashboard/qc" },
  ];

  return (
    <aside className="w-64 bg-white shadow-lg p-4">
      <h1 className="text-xl font-bold text-primary mb-6">STORG Admin</h1>

      {menu.map((item) => (
        <Link
          key={item.path}
          href={item.path}
          className={`block p-3 rounded-lg mb-2 ${
            pathname === item.path
              ? "bg-primary text-white shadow"
              : "hover:bg-gray-200"
          }`}
        >
          {item.name}
        </Link>
      ))}

      <button
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/login";
        }}
        className="mt-10 w-full p-3 text-left bg-red-500 text-white rounded-lg hover:bg-red-600"
      >
        Logout
      </button>
    </aside>
  );
}
