from fastapi import FastAPI
from app.core.db import init_db
from app.routers import users, auth, products, warehouses, inventory, movements, pricing, fulfillment, qc, accounting

app = FastAPI(title="STORG Backend API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(warehouses.router)
app.include_router(inventory.router)
app.include_router(movements.router)
app.include_router(pricing.router)
app.include_router(fulfillment.router)
app.include_router(qc.router)
app.include_router(accounting.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}
