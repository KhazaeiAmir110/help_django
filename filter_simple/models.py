from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    publish = models.BooleanField(default=False)
    category = models.ForeignKey('CategorySimple', on_delete=models.PROTECT,
                                 related_name='post_category')

    def __str__(self):
        return self.title


class PostImage(models.Model):
    title = models.CharField(max_length=50)
    file = models.ImageField()
    post = models.ForeignKey('Post', on_delete=models.PROTECT, related_name='image')

    def __str__(self):
        return self.title


class CategorySimple(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str_(self):
        return self.title
