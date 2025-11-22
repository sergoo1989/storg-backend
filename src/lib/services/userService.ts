import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function fetchUsers() {
  return api("/users", { headers: authHeaders() });
}
