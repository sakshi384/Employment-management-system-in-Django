from django.contrib import admin
from .models import emp_details

# admin.site.register(Crud_op)
@admin.register(emp_details)
class employeeAdmin(admin.ModelAdmin):
    display_list=('id','name','email','location','technology','domain','project','blogs','score','placed')