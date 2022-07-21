from django.contrib import admin
from .models import Std, Teacher, classroom, division

# Register your models here.
admin.register(classroom,Std,Teacher, division)(admin.ModelAdmin)