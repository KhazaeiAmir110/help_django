from django.db import models
from category.models import Category
from users.models import User
from django.urls import reverse


# Create your models here.
class Demand(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشرشده'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT,
                                 related_name='category')
    description = models.TextField()
    short_description = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    image = models.ForeignKey('Image', on_delete=models.PROTECT, related_name='image')
    video = models.ForeignKey('Video', on_delete=models.PROTECT, related_name='video')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')

    def get_absolute_url(self):
        return reverse('users:home-profile')


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    alt = models.CharField(max_length=256)
    published = models.BooleanField(default=False)
    file = models.ImageField()


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    alt = models.CharField(max_length=256)
    published = models.BooleanField(default=False)
    file = models.FileField()
