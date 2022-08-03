from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
# from django.conf.urls import url


router=DefaultRouter()
router.register('classroomapi',views.classroomModelViewSet, basename ='classroom'),
router.register('get_all_students',views.StudentViewSet, basename="student")
router.register('get_div',views.divViewSet, basename="div")
router.register('get_all_std',views.stdViewSet, basename ='std'),
router.register('get_all_teachers',views.teacherViewSet, basename ='teacher'),
router.register("get_students_by_std", views.getStudentsByStd_is_monitor, basename='getStudentsByStd_is_monitor'),
router.register("getStudentsBydiv_is_monitor", views.getStudentsBydiv_is_monitor, basename='getStudentsBydiv_is_monitor'),
router.register("get_students_by_division", views.getStudentsBydivision, basename='get_students_by_division'),
router.register("get_students_by_is_monitor", views.getStudentsByis_monitor, basename='get_students_by_is_monitor'),
router.register("get_div_by_teacher", views.getdivByteacher, basename='get_div_by_teacher'),
# router.register("get_div_student_by_teacher_id", views.getdivStudentByteacher_id, basename='get_div_student_by_teacher_id'),
router.register("get_div_by_teacher_name_is_monitor", views.getStudentsByTeacher_is_monitor
, basename='get_div_by_teacher_name_is_monitor'),



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_teacher1/',views.getTeacher1.as_view(), name ='classroom'),
    path('get_teacher/',views.getTeacher.as_view(), name ='classroom'),
    path('register/',views.Register.as_view(), name ='register'),
    path('set_pass/',views.SetPass.as_view(), name ='setpassword'),
    path('set_password/',views.SetPassword.as_view(), name ='setpass'),
]
