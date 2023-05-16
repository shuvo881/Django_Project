from django.contrib import admin

from django.contrib import admin
from .models import Company, Employee, Device


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    list_filter = ('company',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_to', 'assigned_date', 'returned_date', 'description')
    #list_filter = ('company',)




