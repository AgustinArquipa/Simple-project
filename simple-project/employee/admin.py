from django.contrib import admin
from .models import Employee
from lockers.admin import LockerInline

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [LockerInline]

admin.site.register(Employee, EmployeeAdmin)