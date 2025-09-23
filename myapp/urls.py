from django.contrib import admin
from django.urls import path
from .views import indexx,create,delete

urlpatterns = [
    path('', indexx, name='index'),
    path('create', create, name = 'create'),
    path('delete/<int:c_id>/', delete, name='delete')

]
