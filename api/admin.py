from django.contrib import admin
from .models import  Std, Teacher, classroom, division,CustomUser
# Register your models here.
from .models import Agenda

# @admin.register(classroom,Std,Teacher, division)
@admin.register(classroom)
class classroomAdmin(admin.ModelAdmin):
    pass

@admin.register(Std)
class StdAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(division)
class divisionAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','type']     

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id','start_time','end_time','agenda']