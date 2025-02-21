import json

from django.core.cache import cache
from django.http import HttpResponse


def view_one(request):
    # data = {"key": "value"}
    # cache.set("my_custom_data", data, timeout=60 * 60)

    data = cache.get("my_custom_data")
    return HttpResponse(data)


def set_session(request):
    request.session['user_data'] = {'name': 'Alice', 'role': 'admin'}
    return HttpResponse("Set user")


def get_session(request):
    user_data = request.session.get('user_data')
    return HttpResponse(json.dumps(user_data))
