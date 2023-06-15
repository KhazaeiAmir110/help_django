task_default_queue = 'mongard'

task_routes = {
    'celery_test.add': {'queue': 'first'},
    'celery_test.sub': {'queue': 'second'},
}

# celery  -A celery_test worker -l info -Q first,second
