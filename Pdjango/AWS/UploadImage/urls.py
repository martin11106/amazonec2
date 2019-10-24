from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from UploadImage import views

urlpatterns = [

    re_path(r'/alumno_list/$', views.AlumnoList.as_view()),#/alumno+ aqui agrego hacia donde quiero
]
