"""
یک فایل در پوشه اصلی با نام celery ایجاد میکنیم
"""
from celery import Celery

app = Celery('celery')

# میخواهیم celery تنظیمات مارا بشناسد
app.config_from_object('django.conf:settings', namespace='CELERY')

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
