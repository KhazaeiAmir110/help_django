from django.contrib import admin
from .models import Post, PostImage, PostVideo


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created', 'short_description', 'author')
    list_filter = ("status", "author")
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'file')


@admin.register(PostVideo)
class PostVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'file')
