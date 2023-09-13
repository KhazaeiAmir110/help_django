from django.contrib import admin
from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'published'
    )
    list_filter = ('published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ['title']}
    ordering = ['published']


admin.site.register(Category, CategoryAdmin)
