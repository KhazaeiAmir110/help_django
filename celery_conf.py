from celery.schedules import crontab

beat_schedule = {
    'call_show_every_one_minute': {
        'task': 'celery_test.show',
        'schedule': crontab(minute='*/1'),
        'args': ('amir',),
    }
}
