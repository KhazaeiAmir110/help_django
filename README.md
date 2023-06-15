# help_django
For help with django and drf code as well as their related libraries
##To help with libraries in Django

###Celery
```bash
1. pipenv install celery
2. cd name_file
3. pip list
4. celery  -A celery_test worker -l info
```

برای اینکه کاربر در صفحه مورد نظر خیلی معطل نشود از broker ها استفاده میکنیم که یک صفی درست میکند و
کار ها را ردیف میکند.
ولی از آنجایی که کارکردن با آنها سخت است روی آن celery را نصب میکنیم.
که خود broker را celery مدیریت میکند.

###flower

```bash
1. pipenv install flower
2. celery --broker=amqp://guest@localhost// flower
```

###clery_beat
اگر بخواهیم یک تسک هر چند وقت یکبار برای ما اجرا شود باید غیر از یک broker یک beat نیز بالا بیاوریم.

```bash
1. celery  -A celery_test worker -l info
2. celery -A celery_test beat
```