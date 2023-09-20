# from django.contrib import admin
#
# from .models import CarInfo, AddCar
#
# # Register your models here.
#
#
# admin.site.register(CarPic)
# admin.site.register(PopCar)
# admin.site.register(CarInfo)
# admin.site.register(AddCar)

# admin.py

from django.contrib import admin
from .models import User, Car, AddCar, HostBio, CarImage, Notification, Trip, Price, Income

admin.site.register(User)
admin.site.register(Car)
admin.site.register(AddCar)
admin.site.register(HostBio)
admin.site.register(CarImage)
admin.site.register(Notification)
admin.site.register(Price)
admin.site.register(Trip)
admin.site.register(Income)


