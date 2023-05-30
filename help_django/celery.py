"""
یک فایل در پوشه اصلی با نام celery ایجاد میکنیم
"""
from celery import Celery

app = Celery('celery')

# میخواهیم celery تنظیمات مارا بشناسد
app.config_from_object('django.conf:settings', namespace='CELERY')
