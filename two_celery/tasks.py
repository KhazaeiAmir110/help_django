from celery import shared_task
import time
from django.http import HttpResponse


@shared_task()
def plus(x, y):
    time.sleep(5)
    file = open('test.txt', 'a')
    file.write('hello word!!!!')
    file.close()


"""
برای شروع باید beat and worker را ران کنیم 
"""

# celery -A help_django beat
# redis-server
