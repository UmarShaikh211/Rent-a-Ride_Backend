# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views
# from .views import add_cars
#
# router = DefaultRouter()
# router.register(r'photodetails', views.CarPhotoViewSet.as_view({'get': 'list'}), basename='photo')
# router.register(r'popcaretails', views.PopCarViewSet.as_view({'get': 'list'}), basename='popCar')
# router.register(r'infopage', views.CarInfoViewSet.as_view({'get': 'list'}), basename='info')
# router.register(r'addcar', views.AddCarViewSet.as_view({'get': 'list'}), basename='addcar')
#
# urlpatterns = [
#
#     path("Pic/", views.CarPhotoViewSet.as_view({'get': 'list'})),  # Include DRF router URLs
#     path("PopCarDetails"
#          "/", views.PopCarViewSet.as_view({'get': 'list'})),  # Include DRF router URLs
#     path("InfoPage"
#          "/", views.CarInfoViewSet.as_view({'get': 'list'})),  # Include DRF router URLs
#
#     path("AddCar"
#          "/", add_cars, name="Cars"),  # Include DRF router URLs
#
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from .views import UserViewSet, CarViewSet, AddCarViewSet, HostBioViewSet, CarImageViewSet, NotificationViewSet, \
    SharedCarViewSet, TripViewSet, PriceViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet)
router.register(r'addcars', AddCarViewSet)
router.register(r'hostbios', HostBioViewSet)
router.register(r'carimages', CarImageViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'price', PriceViewSet)
router.register(r'sharecar', views.SharedCarViewSet)
router.register(r'trips', TripViewSet)
router.register(r'income', IncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
