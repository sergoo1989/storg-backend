import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function getAccountingErrors() {
  return api("/accounting/errors", { headers: authHeaders() });
}
