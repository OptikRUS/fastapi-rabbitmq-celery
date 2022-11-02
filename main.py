from fastapi import FastAPI
from celery_worker import create_order
from schemas import Order

app = FastAPI()


@app.post('/order')
async def add_order(order: Order):
    # use delay() method to call the celery task
    create_order.delay(order.customer_name, order.order_quantity)
    return {"message": "Order Received! Thank you for your patience."}


# celery -A celery_worker.celery worker --loglevel=info
# celery -A main.celery flower --port=5555
