from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esalary','emobile']
admin.site.register(Employee,EmployeeAdmin)
