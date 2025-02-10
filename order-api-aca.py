from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Order model


class Order(BaseModel):
    orderId: int
    price: float
    orderDate: str


# In-memory data storage
orders = [
    Order(orderId=123, price=200.10, orderDate="2025-01-01"),
    Order(orderId=456, price=50.30, orderDate="2024-12-01")
]


@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders


@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in orders:
        if order.orderId == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.post("/orders", response_model=Order)
def create_order(order: Order):
    orders.append(order)
    return order
