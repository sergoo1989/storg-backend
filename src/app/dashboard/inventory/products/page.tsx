import { getProducts } from "@/lib/services/productService";

export default async function ProductsPage() {
  const products = await getProducts();

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Products</h1>

      <div className="bg-white p-6 rounded-xl shadow">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-2 text-left">SKU</th>
              <th className="p-2 text-left">Name</th>
              <th className="p-2 text-left">Category</th>
            </tr>
          </thead>

          <tbody>
            {products.map((p: any) => (
              <tr key={p.id} className="border-b">
                <td className="p-2">{p.sku}</td>
                <td className="p-2">{p.name}</td>
                <td className="p-2">{p.category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
