import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

orders = [
    {"orderId": 123, "price": 200.10, "orderDate": "2025-01-01"},
    {"orderId": 456, "price": 50.30, "orderDate": "2024-12-01"}
]


@app.route(route="orders", methods=[func.HttpMethod.GET])
def get_orders(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(json.dumps(orders))


@app.route(route="orders/{orderId:int?}", auth_level=func.AuthLevel.ANONYMOUS)
def get_order_by_id(req: func.HttpRequest) -> func.HttpResponse:
    order = [orderr for orderr in orders if orderr["orderId"]
             == int(req.route_params.get("orderId"))]

    logging.info(f"orderFound: {order}")

    if len(order) > 0:
        return func.HttpResponse(json.dumps(order[0]))
    else:
        return func.HttpResponse(
            json.dumps({"status": "order_not_found"}),
            status_code=404
        )


@app.route(route="orders", auth_level=func.AuthLevel.ANONYMOUS, methods=[func.HttpMethod.POST])
def create_order(req: func.HttpRequest) -> func.HttpResponse:
    new_order = req.get_json()

    orders.append({
        "orderId": int(new_order.get('orderId')),
        "price": float(new_order.get('price')),
        "orderDate": new_order.get('orderDate'),
    })

    return func.HttpResponse(json.dumps({"status": "order_created"}))
