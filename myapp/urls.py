from django.contrib import admin
from django.urls import path
from .views import index_html,create_html,detail_html,delete_html

urlpatterns = [
    path('', index_html ),
    path('create/', create_html),
    path('detail/<int:pro_id>', detail_html),
    path('delete/<int:pro_id>', delete_html)
]
