from django.contrib import admin
from django.urls import path,include
from .views import store_page,task_list

urlpatterns = [
    path('',task_list,name="task_list"),
    path('store/',store_page,name="store_page"),
]
