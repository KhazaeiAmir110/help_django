import time

from django.http import HttpResponse

from help_django.celery import app


@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def firstCelery(request):
    print(my_task)
    my_task.delay()
    return HttpResponse('hello')
