import logging
import time

from help_django.celery import app

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.task
def task_hellow():
    logging.info("Start Process")
    time.sleep(5)
    logging.info("End Process")
