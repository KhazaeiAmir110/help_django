from celery import shared_task


@shared_task
def my_task_2():
    file = open('test.txt', 'a')
    file.write('hello word!!!!')
    file.close()
