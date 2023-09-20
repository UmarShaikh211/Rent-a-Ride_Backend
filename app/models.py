from django.db import models

# Create your models here.
# from django.db import models
#
#
# class CarPic(models.Model):
#     Name = models.CharField(max_length=100)
#     Photos = models.ImageField(upload_to='images', default="")
#
#
# class AddCar(models.Model):
#     License = models.CharField(max_length=15)
#     CarBrand = models.CharField(max_length=20)
#     CarModel = models.CharField(max_length=50)
#     CarVariant = models.CharField(max_length=50)
#     CarCity = models.CharField(max_length=20)
#     CarYear = models.CharField(max_length=4)
#     CarFuel = models.CharField(max_length=12)
#     CarTrans = models.CharField(max_length=12)
#     CarKm = models.CharField(max_length=25)
#     CarChassisNo = models.CharField(max_length=17)
#     CarShare = models.CharField(max_length=30)
#
#
# class PopCar(models.Model):
#     Name = models.CharField(max_length=100)
#     Photo = models.ImageField(upload_to='images', default="")
#     City = models.ForeignKey(AddCar, related_name='popcar_by_city', on_delete=models.CASCADE)
#     Transmission = models.ForeignKey(AddCar, related_name='popcar_by_transmission', on_delete=models.CASCADE)
#     Price = models.IntegerField()
#     Fuel = models.ForeignKey(AddCar, related_name='popcar_by_fuel', on_delete=models.CASCADE)
#     Seat = models.CharField(max_length=20)
#
#
# class CarInfo(models.Model):
#     CYear = models.IntegerField(default=0)
#     # Image1 = models.ImageField(upload_to='images', default="")
#     Image1 = models.ForeignKey(PopCar, default="", on_delete=models.CASCADE)
#     Image2 = models.ImageField(upload_to='images', default="")
#     Image3 = models.ImageField(upload_to='images', default="")
#     Image4 = models.ImageField(upload_to='images', default="")
#     HostImage = models.ImageField(upload_to='images', default="")
#     HostName = models.CharField(max_length=100)
#     HostBio = models.CharField(max_length=300)


import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isshared = models.BooleanField(default=False)  # Add the isshared field

    def __str__(self):
        return f"{self.user.name}'s Car"


class Trip(models.Model):
    car = models.ForeignKey(Car,related_name='trip',on_delete=models.CASCADE)
    cname = models.CharField(max_length=50)
    sdate = models.CharField(max_length=50)
    edate = models.CharField(max_length=50)

    def __str__(self):
        return f"Trip with {self.cname}"


class AddCar(models.Model):
    car = models.ForeignKey(Car, related_name='added_cars', on_delete=models.CASCADE)
    License = models.CharField(max_length=15)
    CarBrand = models.CharField(max_length=20)
    CarModel = models.CharField(max_length=50)
    CarVariant = models.CharField(max_length=50)
    CarCity = models.CharField(max_length=20)
    CarYear = models.CharField(max_length=4)
    CarFuel = models.CharField(max_length=12)
    CarTrans = models.CharField(max_length=12)
    CarSeat = models.CharField(max_length=12, default="5 Seats")
    CarKm = models.CharField(max_length=25)
    CarChassisNo = models.CharField(max_length=17)


# class CarInfo(models.Model):
#     car = models.ForeignKey(Car, related_name='car_info', on_delete=models.CASCADE)
#     CYear = models.IntegerField(default=0)
#     Image1 = models.ImageField(upload_to='images', default="")
#     Image2 = models.ImageField(upload_to='images', default="")
#     Image3 = models.ImageField(upload_to='images', default="")
#     Image4 = models.ImageField(upload_to='images', default="")
#     HostImage = models.ImageField(upload_to='images', default="")
#     HostName = models.CharField(max_length=100)
#     HostBio = models.CharField(max_length=300)

class HostBio(models.Model):
    car = models.ForeignKey(Car, related_name='host_bio', on_delete=models.CASCADE)
    # Hname = models.CharField(max_length=40)
    # Hemail = models.CharField(max_length=30)
    # Hphone = models.CharField(max_length=15)
    Gphone = models.CharField(max_length=15)
    Himage = models.ImageField(upload_to='images', default="")
    Hbio = models.CharField(max_length=100)


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='car_image', on_delete=models.CASCADE)
    Image1 = models.ImageField(upload_to='images', default="")
    Image2 = models.ImageField(upload_to='images', default="")
    Image3 = models.ImageField(upload_to='images', default="")
    Image4 = models.ImageField(upload_to='images', default="")
    Image5 = models.ImageField(upload_to='images', default="")
    Image6 = models.ImageField(upload_to='images', default="")
    Image7 = models.ImageField(upload_to='images', default="")


class Notification(models.Model):
    car = models.ForeignKey(Car, related_name='host_notification', on_delete=models.CASCADE)
    N1 = models.CharField(max_length=100)
    N2 = models.CharField(max_length=100)
    N3 = models.CharField(max_length=100)
    N4 = models.CharField(max_length=100)
    N5 = models.CharField(max_length=100)


class Price(models.Model):
    car = models.ForeignKey(Car, related_name='car_price', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.car)


class Income(models.Model):
    car = models.ForeignKey(Car,related_name='income',on_delete=models.CASCADE)
    cname = models.CharField(max_length=50)
    cinc = models.CharField(max_length=50)
    sidate = models.CharField(max_length=50)
    eidate = models.CharField(max_length=50)

    def __str__(self):
        return f"Income of {self.cname}"


