"use client";

import { useState } from "react";
import { calculatePrice } from "@/lib/services/pricingService";

export default function PricingPage() {
  const [data, setData] = useState({
    material_cost: 0,
    packing_cost: 0,
    operating_cost: 0,
    fulfillment_cost: 0,
    shipping_cost: 0,
    target_margin: 0.30,
  });

  const [result, setResult] = useState<any>(null);

  async function handleSubmit(e: any) {
    e.preventDefault();
    const res = await calculatePrice(data);
    setResult(res);
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Pricing Engine</h1>

      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-xl shadow w-[600px]">
        {Object.keys(data).map((key) => (
          <div className="mb-4" key={key}>
            <label className="block font-medium mb-1">{key}</label>
            <input
              type="number"
              value={data[key as keyof typeof data]}
              onChange={(e) =>
                setData({ ...data, [key]: parseFloat(e.target.value) })
              }
              className="border p-2 w-full rounded"
            />
          </div>
        ))}

        <button className="bg-primary text-white py-2 px-4 rounded">
          Calculate
        </button>
      </form>

      {result && (
        <div className="bg-white p-6 rounded-xl shadow mt-6">
          <h2 className="text-xl font-bold">Result</h2>
          <p>Total Cost: {result.total_cost}</p>
          <p>Suggested Price: {result.price}</p>
        </div>
      )}
    </div>
  );
}
