from django.contrib import admin
from filter_simple.models import Post, PostImage, CategorySimple


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'publish', 'category')
    list_filter = ("publish", "category")
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'file')


@admin.register(CategorySimple)
class PostVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
