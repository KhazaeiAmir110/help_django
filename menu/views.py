from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render

from menu.models import Desk, Category, Requests


def menu(request):
    code = request.GET.get('desk', None)
    if code is None:
        raise Http404

    desk_item = get_object_or_404(Desk, code=code)
    categories = Category.objects.all()

    return render(request, 'menu.html', {'desk': desk_item, 'categories': categories})


def request_water(request):
    code = request.GET.get('desk', None)
    if code is None:
        raise Http404

    desk_item = get_object_or_404(Desk, code=code)

    request = Requests(desk=desk_item)
    request.save()

    return JsonResponse({'Successes': True})


def water(request):
    return render(request, 'water.html')
