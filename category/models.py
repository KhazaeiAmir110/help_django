from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['published']

    def __str__(self):
        return self.title
