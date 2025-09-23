from django.contrib import admin
from .models import Customer,Category,Order,Product

admin.site.register([Customer,Category,Order,Product])
