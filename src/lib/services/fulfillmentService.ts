import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function getOrders() {
  return api("/fulfillment/orders", { headers: authHeaders() });
}

export async function getDuplicates() {
  return api("/fulfillment/duplicates", { headers: authHeaders() });
}

export async function getKPI() {
  return api("/fulfillment/kpi", { headers: authHeaders() });
}
