from .tasks import plus
from django.http import HttpResponse


def alaki(request):
    for i in range(100):
        plus.delay(1398, 1)
    return HttpResponse('OK')
