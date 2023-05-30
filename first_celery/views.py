import celery
from django.shortcuts import render
from django.http import HttpResponse
import time
from help_django.celery import app


# Create your views here.
@app.task
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def home(request):
    print(my_task)
    # در واقع وقتی از delay استفاده میکنیم دیگر منتظر اون تابع نیستیم
    my_task.delay()
    return HttpResponse('hello')
