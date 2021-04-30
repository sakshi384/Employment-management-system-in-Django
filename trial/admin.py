from django.contrib import admin
from .models import trial_details
# Register your models here.
@admin.register(trial_details)
class Admindetails(admin.ModelAdmin):
    display_list=['id','name','email','location','technology','domain','project','blogs']
    # display_list = ['id','name','email']