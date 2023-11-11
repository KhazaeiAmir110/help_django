from django.contrib import admin
from .models import Post, Category, File


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'picture'
    )
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    ordering = ['created']

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])


class FiledAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
        'post'
    )
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published'
    )
    list_filter = ('published',)
    search_fields = ('title',)
    ordering = ['published']


admin.site.register(Post, PostAdmin)
admin.site.register(File, FiledAdmin)
admin.site.register(Category, CategoryAdmin)
