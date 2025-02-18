from django.http import HttpResponse

from settings.base import check_rabbitmq_connection


def test_rabbitmq_connection(request):
    check_rabbitmq_connection()
    return HttpResponse("RabbitMQ Connection Checked")
