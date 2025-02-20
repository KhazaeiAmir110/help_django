import time

from django.http import HttpResponse


def home(request):
    time.sleep(10)
    return HttpResponse("Hello, world. You're at the polls home view.")
