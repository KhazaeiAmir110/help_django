from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"
        ordering = ['name']
        constraints = []


class WorkDate(models.Model):
    date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class WorkTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    work_date = models.ForeignKey(WorkDate, on_delete=models.CASCADE)
