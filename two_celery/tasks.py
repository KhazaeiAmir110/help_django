from celery import shared_task
import time


@shared_task()
def plus(x, y):
    time.sleep(5)
    file = open('test.txt', 'a')
    file.write('hello word!!!!')
    file.close()
