from django.db import models
from user.models import User
from documentation.models import Documentation


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
