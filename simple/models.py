from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    short_description = models.TextField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    title = models.CharField(max_length=50)
    alt = models.CharField(max_length=256)
    file = models.ImageField()
    post = models.ForeignKey('Post', on_delete=models.PROTECT, related_name='image')

    def __str__(self):
        return self.title


class PostVideo(models.Model):
    title = models.CharField(max_length=50)
    alt = models.CharField(max_length=256)
    file = models.FileField()
    post = models.ForeignKey('Post', on_delete=models.PROTECT, related_name='video')

    def __str__(self):
        return self.title
