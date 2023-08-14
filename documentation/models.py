from django.db import models
from django.utils.translation import gettext_lazy as _


class Documentation(models.Model):
    TYPE_CHOICES = (
        ('B', _('Book')),
        ('A', _('Article')),
    )
    STATUS_CHOICES = (
        ('A', _('Available')),
        ('U', _('Unavailable')),
    )

    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='B')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return str(self.name)
