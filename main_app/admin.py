from django.contrib import admin
from .models import Car, CarType

# Register your models here.
admin.site.register(Car) # this line will add the model to the admin panel
admin.site.register(CarType) # this line will add the model to the admin panel

