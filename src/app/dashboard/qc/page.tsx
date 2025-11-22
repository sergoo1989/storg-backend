import { getQCErrors } from "@/lib/services/qcService";

export default async function QCPage() {
  const errors = await getQCErrors();

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Quality Control</h1>

      <div className="bg-white p-6 rounded-xl shadow">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-2">Order Ref</th>
              <th className="p-2">Error Code</th>
              <th className="p-2">Message</th>
              <th className="p-2">Severity</th>
            </tr>
          </thead>

          <tbody>
            {errors.map((e: any, i: number) => (
              <tr key={i} className="border-b">
                <td className="p-2">{e.order_reference}</td>
                <td className="p-2 font-bold">{e.error_code}</td>
                <td className="p-2">{e.error_message}</td>
                <td
                  className={`p-2 font-semibold ${
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
