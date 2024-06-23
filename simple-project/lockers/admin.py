from django.contrib import admin

# Register your models here.
from .models import Locker

class LockerInline(admin.TabularInline):
    model = Locker
    extra = 1

admin.site.register(Locker)