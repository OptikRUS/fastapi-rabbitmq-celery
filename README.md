# FastAPI Asynchronous Task
<p align="center">
    <img height=100 src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"/>
</p>

## Celery <img height=30 src="https://camo.githubusercontent.com/d2728a5a2bfb9d718cb15762d2e9514a5782a46b33d0b240ebe1c1a4f825cb7c/68747470733a2f2f646f63732e63656c65727970726f6a6563742e6f72672f656e2f737461626c652f5f7374617469632f63656c6572795f3531322e706e67"/> + RabbitMQ <img height=30 src="https://camo.githubusercontent.com/e004fa3316e855d2f4fa6c7077333d12b3783c54dedf9c8628207fe025d134bc/68747470733a2f2f6173736574732e7a61626269782e636f6d2f696d672f6272616e64732f7261626269746d712e737667"/> + Flower <img height=30 src=""/>

Deploy RabbitMQ: `docker-compose up --build -d`

Run celery worker: `celery -A celery_worker.celery worker --loglevel=info`

Run app: `uvicorn main:app --reload`

Run flower: `celery -A main.celery flower --port=5555`

App Swagger UI: ` http://127.0.0.1:8000/docs`

Flower tasks: `http://127.0.0.1:5555/tasks`

RabbitMQ: `http://127.0.0.1:15672/`

Thanks by this [Guide](https://medium.com/thelorry-product-tech-data/celery-asynchronous-task-queue-with-fastapi-flower-monitoring-tool-e7135bd0479f)