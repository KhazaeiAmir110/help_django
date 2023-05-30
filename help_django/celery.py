"""
یک فایل در پوشه اصلی با نام celery ایجاد میکنیم
"""
from celery import Celery
from first_celery.tasks import *
import os

# اگر اینکار را نکنیم ما باید هردفعه export کنیم
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'help_django.settings')

app = Celery('celery')

# میخواهیم celery تنظیمات مارا بشناسد
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_task_in_every_2_sec': {
        # Address task
        'task': 'home.tasks.my_task_2',
        # Time
        'schedule': 2,
        # اگر پس از ۱۰ ثانیه نتوانستی انجامش بدهی بیخیالش شو
        'options': {
            'expires': 10
        }
    }
}
