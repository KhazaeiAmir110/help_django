from django.contrib import admin
from .models import Company, Category, WorkDate, WorkTime


@admin.register(Company)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkDate)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkTime)
class ReservationAdmin(admin.ModelAdmin):
    pass
