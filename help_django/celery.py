import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'help_django.settings')

app = Celery('celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_task_in_every_2_sec': {
        'task': 'home.tasks.my_task_2',
        'schedule': 2,
        'options': {
            'expires': 10
        }
    }
}
