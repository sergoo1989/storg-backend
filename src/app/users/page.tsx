import { fetchUsers } from "@/lib/services/userService";

export default async function UsersPage() {
  const users = await fetchUsers();

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Users</h1>

      <div className="bg-white p-4 rounded-lg shadow">
        <pre>{JSON.stringify(users, null, 2)}</pre>
      </div>
    </div>
  );
}
