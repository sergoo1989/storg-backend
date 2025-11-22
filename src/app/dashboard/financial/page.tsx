import { getAccountingErrors } from "@/lib/services/accountingService";

export default async function FinancialPage() {
  const errors = await getAccountingErrors();

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Financial Error Detection</h1>

      <div className="bg-white p-6 rounded-xl shadow">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-2">Reference</th>
              <th className="p-2">Error Code</th>
              <th className="p-2">Description</th>
              <th className="p-2">Severity</th>
            </tr>
          </thead>

          <tbody>
            {errors.map((e: any, i: number) => (
              <tr key={i} className="border-b">
                <td className="p-2">{e.reference}</td>
                <td className="p-2 font-bold">{e.error_code}</td>
                <td className="p-2">{e.message}</td>
                <td
                  className={`p-2 ${
                    e.severity === "critical"
                      ? "text-red-600"
                      : e.severity === "high"
                      ? "text-orange-500"
                      : e.severity === "medium"
                      ? "text-yellow-600"
                      : "text-green-600"
                  }`}
                >
                  {e.severity}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
