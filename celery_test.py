from celery import Celery
import time

app = Celery('first', broker='amqp://guest@localhost//')


@app.task(name='celery_test.adding')
def add(a, b):
    time.sleep(10)
    return a + b
