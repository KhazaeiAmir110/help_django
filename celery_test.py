from celery import Celery

app = Celery('first', broker='amqp://guest@localhost//')
