import { api } from "../api/client";
import { authHeaders } from "../auth";

export async function getQCErrors() {
  return api("/qc/errors", { headers: authHeaders() });
}
