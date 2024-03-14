from django.contrib import admin
from .models import StudentModel, Teachers, Group



# Register your models here.

admin.site.register(StudentModel,list_display = ['name','coins'])
admin.site.register(Teachers,list_display=['name','directory','phone'])
admin.site.register(Group)
