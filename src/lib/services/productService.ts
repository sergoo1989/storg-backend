import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function getProducts() {
  return api("/products", { headers: authHeaders() });
}

export async function createProduct(data: any) {
  return api("/products", {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });
}
