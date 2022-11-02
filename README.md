# FastAPI Asynchronous Task

<img height=200 src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" align='center'>

## Celery <img height=60 src="https://docs.celeryq.dev/en/stable/_static/celery_512.png" align='center'> + <img height=20 src="https://www.rabbitmq.com/img/logo-rabbitmq.svg" align='center'> + Flower

Deploy RabbitMQ: `docker-compose up --build -d`

Run celery worker: `celery -A celery_worker.celery worker --loglevel=info`

Run app: `uvicorn main:app --reload`

Run flower: `celery -A main.celery flower --port=5555`

App Swagger UI: ` http://127.0.0.1:8000/docs`

Flower tasks: `http://127.0.0.1:5555/tasks`

RabbitMQ: `http://127.0.0.1:15672/`

Thanks by this [Guide](https://medium.com/thelorry-product-tech-data/celery-asynchronous-task-queue-with-fastapi-flower-monitoring-tool-e7135bd0479f)