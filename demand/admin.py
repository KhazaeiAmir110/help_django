from django.contrib import admin
from .models import Demand, Image, Video


class DemandAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'status'
    )
    list_filter = ('status',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ['title']}
    ordering = ['status']


class ImagedAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'alt',
        'published'
    )
    list_filter = ('published',)
    search_fields = ('title', 'description')
    ordering = ['published']


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'alt',
        'published'
    )
    list_filter = ('published',)
    search_fields = ('title', 'description')
    ordering = ['published']


admin.site.register(Demand, DemandAdmin)
admin.site.register(Image, ImagedAdmin)
admin.site.register(Video, VideoAdmin)
