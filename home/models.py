from django.db import models

from core.structs import EnumMember, EnumBase
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=256)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    class StatusEnum(EnumBase):
        SENT = EnumMember(0, 'Sent')
        APPROVED = EnumMember(1, 'Approved')
        PUBLISHED = EnumMember(2, 'Published')

    title = models.CharField(max_length=100)
    category = models.ManyToManyField(to='Category', related_name='category')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(
        default=StatusEnum.SENT,
        choices=StatusEnum.to_tuple())
    picture = models.ImageField(upload_to='picture')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, upload_to='file')
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='images')

    def __str__(self):
        return self.title
