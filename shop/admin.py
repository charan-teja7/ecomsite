from django.contrib import admin
from .models import product
from .models import Order
admin.site.register(product)
admin.site.register(Order)