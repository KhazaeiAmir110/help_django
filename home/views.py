
from django.http import HttpResponse

from home.tasks import task_hellow


def home(request):
    task_hellow.apply_async()
    return HttpResponse("Hello, world. You're at the polls home view.")
