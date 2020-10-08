from django.contrib import admin
from .models import OrderModel, OrderOption

# Register your models here.
admin.site.register(OrderModel)
admin.site.register(OrderOption)