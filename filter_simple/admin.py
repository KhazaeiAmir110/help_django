from django.contrib import admin
from filter_simple.models import Post, PostImage, CategorySimple

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(CategorySimple)
