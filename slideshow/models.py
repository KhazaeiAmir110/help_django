from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(default=False)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title


class Slideshow(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-post__publish']

    def __str__(self):
        return self.post.title
