from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
#
# from .models import CarPic, PopCar, CarInfo, AddCar
# from .serializer import CarPicSerializer, PopCarSerializer, CarInfoSerializer, AddCarSerializer
#
#
# # Create your views here.
# class CarPhotoViewSet(viewsets.ModelViewSet):
#     queryset = CarPic.objects.all()
#     serializer_class = CarPicSerializer
#
#
# class PopCarViewSet(viewsets.ModelViewSet):
#     queryset = PopCar.objects.all()
#     serializer_class = PopCarSerializer
#
#
# class CarInfoViewSet(viewsets.ModelViewSet):
#     queryset = CarInfo.objects.all()
#     serializer_class = CarInfoSerializer
#
#
# @csrf_exempt
# def add_cars(request):
#     if request.method == 'POST':
#         licenses = request.POST.get('License')
#         carbrand = request.POST.get('CarBrand')
#         carmodel = request.POST.get('CarModel')
#         carvariant = request.POST.get('CarVariant')
#         carcity = request.POST.get('CarCity')
#         caryear = request.POST.get('CarYear')
#         carfuel = request.POST.get('CarFuel')
#         cartrans = request.POST.get('CarTrans')
#         carkm = request.POST.get('CarKm')
#         carchassisno = request.POST.get('CarChassisNo')
#         carshare = request.POST.get('CarShare')
#
#         add_cars = AddCar.objects.create(License=licenses, CarBrand=carbrand, CarModel=carmodel,CarVariant=carvariant,
#                                          CarCity=carcity,
#                                          CarYear=caryear, CarFuel=carfuel, CarTrans=cartrans, CarKm=carkm,
#                                          CarChassisNo=carchassisno, CarShare=carshare)
#         add_cars.save()
#         return JsonResponse({'message': 'Data saved successfully'})
#     else:
#         return JsonResponse({'error': 'Invalid requestmethod'})
#
#
# class AddCarViewSet(viewsets.ModelViewSet):
#     queryset = AddCar.objects.all()
#     serializer_class = AddCarSerializer

# views.py

# views.py

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Car, AddCar,HostBio,CarImage,Notification
# from .serializer import CarSerializer
# from django.http import Http404
#
# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
# class CreateCarWithRelatedData(APIView):
#     def post(self, request, format=None):
#         # Creating a new car instance with a generated UUID
#         new_car = Car.objects.create()
#
#         # Creating related data entries
#         add_car = AddCar.objects.create(car=new_car, License='ABC123', CarBrand='Toyota')
#
#
#         return Response({"message": "New car and related data entries created."})
#

from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ViewSet

from .models import User, Car, AddCar, HostBio, CarImage, Notification, Trip, Price, Income
from .serializer import UserSerializer, CarSerializer, AddCarSerializer, HostBioSerializer, CarImageSerializer, \
    NotificationSerializer, TripSerializer, PriceSerializer, IncomeSerializer
from rest_framework import status
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class AddCarViewSet(viewsets.ModelViewSet):
    queryset = AddCar.objects.all()
    serializer_class = AddCarSerializer


class HostBioViewSet(viewsets.ModelViewSet):
    queryset = HostBio.objects.all()
    serializer_class = HostBioSerializer


# class CarImageViewSet(viewsets.ModelViewSet):
#     queryset = CarImage.objects.all()
#     serializer_class = CarImageSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


# @api_view(['POST'])
# def create_car_images(request):
#     # Deserialize the request data
#     serializer = CarImageSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
class CarImageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CarImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


# def share_car(request):
#     if request.method == 'POST':
#         car_id = request.POST.get('car_id')
#         try:
#             car = Car.objects.get(id=car_id)
#             car.isshared = True
#             car.save()
#             return JsonResponse({'message': 'Car shared successfully'})
#         except Car.DoesNotExist:
#             return JsonResponse({'message': 'Car not found'}, status=404)
#     return JsonResponse({'message': 'Invalid request method'}, status=400)
#
#
# def shared_cars_data(request):
#     shared_cars = Car.objects.filter(isshared=True)
#     car_data = []
#
#     for car in shared_cars:
#         add_car = AddCar.objects.get(car=car)
#         host_bio = HostBio.objects.get(car=car)
#         car_images = CarImage.objects.filter(car=car)
#         notifications = Notification.objects.filter(car=car)
#
#         # Create a dictionary with the data you want to send to Flutter
#         car_data.append({
#             'car_id': car.id,
#             'car_brand': add_car.CarBrand,
#             # Add more fields from different models here
#         })
#
#     return JsonResponse(car_data, safe=False)


class SharedCarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(isshared=True).prefetch_related('added_cars', 'car_image',
                                                                  'host_bio',
                                                                  'car_price')  # Retrieve cars with isshared=True
    serializer_class = CarSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


# class TripCreateView(viewsets.ViewSet):
#     def post(self, request, *args, **kwargs):
#         serializer = TripSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
