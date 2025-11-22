import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function calculatePrice(data: any) {
  return api("/pricing/calculate", {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });
}
