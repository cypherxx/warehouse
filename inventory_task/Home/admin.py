from .models import Location, Product, Product_movement
from django.contrib import admin


# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Product_movement)
