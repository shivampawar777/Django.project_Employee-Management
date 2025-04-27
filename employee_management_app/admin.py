from django.contrib import admin
from .models import Empdata


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_id', 'name','working', 'jdate', 'ldate', 'dept', 'user']
    list_filter=['working', 'dept', 'user']

admin.site.register(Empdata,EmployeeModelAdmin)

