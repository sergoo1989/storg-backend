export default function Card({ title, value }: { title: string; value: any }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-sm">
      <h2 className="text-sm text-gray-500">{title}</h2>
      <p className="text-2xl font-bold mt-2">{value}</p>
    </div>
  );
}
