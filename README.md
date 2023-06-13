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