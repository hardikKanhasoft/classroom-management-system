from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register('classroomapi',views.classroomModelViewSet, basename ='classroom'),
router.register('get_all_students',views.StudentViewSet, basename="student")
router.register('get_div',views.divViewSet, basename="div")
router.register('get_all_std',views.stdViewSet, basename ='std'),
router.register('get_all_teachers',views.teacherViewSet, basename ='teacher'),
router.register("get_students_by_std", views.getStudentsByStd_is_monitor, basename='getStudentsByStd_is_monitor'),
router.register("getStudentsBydiv_is_monitor", views.getStudentsBydiv_is_monitor, basename='getStudentsBydiv_is_monitor'),
router.register("get_students_by_teacher", views.getStudentsByteacher, basename='get_students_by_teacher'),
router.register("get_students_by_division", views.getStudentsBydivision, basename='get_students_by_division'),
router.register("get_students_by_is_monitor", views.getStudentsByis_monitor, basename='get_students_by_is_monitor'),

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
