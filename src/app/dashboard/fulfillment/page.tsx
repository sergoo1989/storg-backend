import { getOrders, getDuplicates, getKPI } from "@/lib/services/fulfillmentService";

export default async function FulfillmentPage() {
  const [orders, duplicates, kpi] = await Promise.all([
    getOrders(),
    getDuplicates(),
    getKPI(),
  ]);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Fulfillment Dashboard</h1>

      <div className="grid grid-cols-3 gap-6 mb-6">
        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="font-bold text-lg mb-2">Total Orders</h2>
          {kpi.total_orders}
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="font-bold text-lg mb-2">Avg Processing Hours</h2>
          {kpi.avg_processing_hours}
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="font-bold text-lg mb-2">Avg Delivery Hours</h2>
          {kpi.avg_delivery_hours}
        </div>
      </div>

      <div className="bg-white p-6 rounded-xl shadow mb-8">
        <h2 className="font-bold text-lg mb-4">Duplicates</h2>
        <pre>{JSON.stringify(duplicates, null, 2)}</pre>
      </div>

      <div className="bg-white p-6 rounded-xl shadow">
        <h2 className="font-bold text-lg mb-4">All Orders</h2>
        <pre>{JSON.stringify(orders, null, 2)}</pre>
      </div>
    </div>
  );
}
