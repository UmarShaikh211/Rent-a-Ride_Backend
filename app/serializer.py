# from rest_framework import serializers
#
# from .models import CarPic, PopCar, CarInfo, AddCar
#
#
# class CarPicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarPic
#         fields = [
#             'Name',
#             'Photos',
#         ]
#
#
# class PopCarSerializer(serializers.ModelSerializer):
#     City = serializers.CharField(source='City.CarCity')
#     Transmission = serializers.CharField(source='Transmission.CarTrans')
#     Fuel = serializers.CharField(source='Fuel.CarFuel')
#
#     class Meta:
#         model = PopCar
#         fields = [
#             'Name',
#             'Photo',
#             'City',
#             'Transmission',
#             'Price',
#             'Fuel',
#             'Seat'
#         ]
#
#
# class CarInfoSerializer(serializers.ModelSerializer):
#     Image1 = serializers.ImageField(source='Image1.Photo')
#
#     class Meta:
#         model = CarInfo
#         fields = [
#             'CYear',
#             'Image1',
#             'Image2',
#             'Image3',
#             'Image4',
#             'HostImage',
#             'HostName',
#             'HostBio'
#         ]
#
#
# class AddCarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AddCar
#         fields = [
#             'License',
#             'CarBrand',
#             'CarModel',
#             'CarVariant',
#             'CarCity',
#             'CarYear',
#             'CarFuel',
#             'CarTrans',
#             'CarKm',
#             'CarChassisNo',
#             'CarShare'
#         ]


# serializers.py
from rest_framework import serializers
from .models import User, Car, AddCar, HostBio, CarImage, Notification, Trip, Price, Income, CarDate, BrandLogo, \
    Homeslider, Review, Rating, Bank, Location
from rest_framework import generics


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AddCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCar
        fields = '__all__'


class HostBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostBio
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


# class CarSerializer(serializers.ModelSerializer):
#     added_cars = AddCarSerializer(many=True, read_only=True)
#     host_bio = HostBioSerializer(many=True, read_only=True)
#     car_image = CarImageSerializer(many=True, read_only=True)
#     host_notification = NotificationSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Car
#         #fields = ['carid', 'isshared', 'added_cars', 'host_bio', 'car_image', 'host_notification']
#         fields = '__all__'

# serializers.py
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    added_cars = AddCarSerializer(many=True, read_only=True)  # Serialize the related AddCar data
    car_image = CarImageSerializer(many=True, read_only=True)  # Serialize the related AddCar data
    host_bio = HostBioSerializer(many=True, read_only=True)  # Serialize the related AddCar data
    car_price = PriceSerializer(many=True, read_only=True)  # Serialize the related AddCar data
    car_location = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'  # Include all fields, including 'isshared'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class CarDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDate
        fields = '__all__'


class BrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandLogo
        fields = '__all__'


class HomesliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeslider
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
