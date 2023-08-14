from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'documentation', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['user__username', 'documentation__title']
    date_hierarchy = 'created'


admin.site.register(Reservation, ReservationAdmin)
