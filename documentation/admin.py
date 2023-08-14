from django.contrib import admin
from .models import Documentation


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'type', 'status')
    list_filter = ('type', 'status')
    search_fields = ('name', 'author')
    list_per_page = 20
    ordering = ('name',)
    actions = ['make_available', 'make_unavailable']

    # def make_available(self, request, queryset):
    #     rows_updated = queryset.update(status='A')
    #     self.message_user(request, f"{rows_updated} documents marked as available.")
    #
    # make_available.short_description = "Mark selected documents as available"
    #
    # def make_unavailable(self, request, queryset):
    #     rows_updated = queryset.update(status='U')
    #     self.message_user(request, f"{rows_updated} documents marked as unavailable.")
    #
    # make_unavailable.short_description = "Mark selected documents as unavailable"


admin.site.register(Documentation, DocumentationAdmin)
