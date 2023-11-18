from django.urls import path
from .views import *
from student.views import delete_std
from student.views import update_std
from student.views import do_update_std

urlpatterns = [
    path("home/",home),
    path("add-std/",std_Add),
    path("delete-std/<int:roll>",delete_std),
    path("update-std/<int:roll>",update_std),
    path("do-update-std/<int:roll>",do_update_std),
]