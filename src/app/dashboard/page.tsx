import Card from "@/components/ui/Card";
import { getUsers } from "@/lib/services/userService";

export default async function DashboardPage() {
  const users = await getUsers();

  return (
    <>
      <h1 className="text-2xl font-bold mb-6">Overview</h1>

      <div className="grid grid-cols-3 gap-6">
        <Card title="Total Users" value={users.length} />
        <Card title="Total Orders" value="Coming Soon" />
        <Card title="Inventory Items" value="Coming Soon" />
      </div>
    </>
  );
}
