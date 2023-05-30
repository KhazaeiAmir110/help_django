from django.shortcuts import render
from django.http import HttpResponse
import time


# Create your views here.
def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def home(request):
    my_task()
    return HttpResponse('hello')
