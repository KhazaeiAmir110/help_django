from django.contrib import admin
from .models import Category, Desk, Item, Requests

admin.site.register(Category)
admin.site.register(Desk)
admin.site.register(Item)
admin.site.register(Requests)
