import Sidebar from "@/components/layout/Sidebar";
import { ReactNode } from "react";
import { redirect } from "next/navigation";
import { getRole } from "@/lib/auth";

export default function DashboardLayout({ children }: { children: ReactNode }) {
  // Server side protection
  if (typeof window !== "undefined") {
    const role = getRole();
    if (role !== "admin") redirect("/login");
  }

  return (
    <div className="flex min-h-screen bg-gray-100">
      <Sidebar />

      <main className="flex-1 p-6">
        {children}
      </main>
    </div>
  );
}
