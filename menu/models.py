from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Desk(models.Model):
    code = models.CharField(max_length=16, null=False, blank=False)
    title = models.CharField(max_length=64, null=False, blank=False)
    waiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)


class Requests(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)


channel = get_channel_layer()


@receiver(post_save, sender=Requests)
def send_notif(sender, instance, **kwargs):
    async_to_sync(channel.group_send)(instance.desk.code, {'type': 'request_water', 'code': instance.desk.code})
