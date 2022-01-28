from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','is_active','phone_number','role','department_name']


admin.site.register(UserProfile,UserProfileAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name','created_date']

admin.site.register(Department,DepartmentAdmin)

# class TicketAdmin(admin.ModelAdmin):
#     list_display=['title','user','department_name','description']

admin.site.register(Ticket)
