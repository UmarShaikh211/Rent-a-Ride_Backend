from datetime import datetime

from django.db.models import Avg
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
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ViewSet

from .models import User, Car, AddCar, HostBio, CarImage, Notification, Trip, Price, Income, CarDate, BrandLogo, \
    Homeslider, Review, Rating, Bank
from .serializer import UserSerializer, CarSerializer, AddCarSerializer, HostBioSerializer, CarImageSerializer, \
    NotificationSerializer, TripSerializer, PriceSerializer, IncomeSerializer, CarDateSerializer, BrandLogoSerializer, \
    HomesliderSerializer, ReviewSerializer, RatingSerializer, BankSerializer
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


def check_add_car_filled(request, car_id):
    try:
        add_car = AddCar.objects.get(car_id=car_id)
        is_filled = add_car.isFilled
        return JsonResponse({'isFilled': is_filled})
    except AddCar.DoesNotExist:
        return JsonResponse({'isFilled': False})


class HostBioViewSet(viewsets.ModelViewSet):
    queryset = HostBio.objects.all()
    serializer_class = HostBioSerializer


def check_host_bio_filled(request, car_id):
    try:
        h_bio = HostBio.objects.get(car_id=car_id)
        is_filled = h_bio.isFilled
        return JsonResponse({'isFilled': is_filled})
    except HostBio.DoesNotExist:
        return JsonResponse({'isFilled': False})


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


def check_car_img_filled(request, car_id):
    try:
        c_img = CarImage.objects.get(car_id=car_id)
        is_filled = c_img.isFilled
        return JsonResponse({'isFilled': is_filled})
    except CarImage.DoesNotExist:
        return JsonResponse({'isFilled': False})


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


def check_price_filled(request, car_id):
    try:
        c_price = Price.objects.get(car_id=car_id)
        is_filled = c_price.isFilled
        return JsonResponse({'isFilled': is_filled})
    except Price.DoesNotExist:
        return JsonResponse({'isFilled': False})


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

class CarDateViewSet(viewsets.ModelViewSet):
    queryset = CarDate.objects.all()
    serializer_class = CarDateSerializer


@api_view(['POST'])
def create_car_date(request):
    try:
        # Deserialize data using the serializer
        serializer = CarDateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'CarDate created successfully'}, status=201)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['PUT'])
def update_car_isshared(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def filter_cars_with_date(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            start_date_str = data.get('start_date')
            end_date_str = data.get('end_date')

            # Parse start and end dates to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            # Query cars that match the date range and isshared=True
            filtered_car_dates = CarDate.objects.filter(
                sharesdate__lte=end_date,
                shareedate__gte=start_date,
                car__isshared=True
            ).select_related('car')  # Use select_related to fetch related car data efficiently

            # Extract the car objects from the filtered car dates
            cars = [car_date.car for car_date in filtered_car_dates]

            # Serialize the filtered cars using CarSerializer
            car_serializer = CarSerializer(cars, many=True)

            return JsonResponse({'cars': car_serializer.data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def filter_cars_by_brand(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_brands = data.get('selected_brands', [])

            # Query cars that have CarBrand in the selected_brands list
            filtered_cars = Car.objects.filter(added_cars__CarBrand__in=selected_brands)

            # Serialize the filtered cars using CarSerializer
            car_serializer = CarSerializer(filtered_cars, many=True)

            return JsonResponse({'cars': car_serializer.data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class BrandLogoViewSet(viewsets.ModelViewSet):
    queryset = BrandLogo.objects.all()
    serializer_class = BrandLogoSerializer


class HomesliderViewSet(viewsets.ModelViewSet):
    queryset = Homeslider.objects.all()
    serializer_class = HomesliderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        car_id = self.request.query_params.get('carId')
        if car_id:
            return Review.objects.filter(car_id=car_id)
        else:
            return Review.objects.all()


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


@api_view(['GET'])
def get_total_rating_for_car(request, car_id):
    try:
        ratings = Rating.objects.filter(car_id=car_id)
        total_rating = ratings.aggregate(Avg('rating'))['rating__avg']

        return Response({'total_rating': total_rating})
    except Rating.DoesNotExist:
        return Response({'error': 'Ratings not found for this car'}, status=404)


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


def get_bank_details(request, user_id):
    print(f"Received user_id: {user_id}")

    bank_details = get_object_or_404(Bank, user__id=user_id)

    print(f"Bank details: {bank_details}")

    bank_data = {
        'acc_no': bank_details.acc_no,
        'ifsc': bank_details.ifsc,
        'pan': bank_details.pan,
        # Add other fields as needed
    }

    return JsonResponse(bank_data)

