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
    SharedCarViewSet, TripViewSet, PriceViewSet, IncomeViewSet, CarDateViewSet, filter_cars_by_brand, BrandLogoViewSet, \
    HomesliderViewSet, ReviewViewSet, RatingViewSet, BankViewSet, LocationViewSet

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
router.register(r'cardate', CarDateViewSet)
router.register(r'brandlogo', BrandLogoViewSet)
router.register(r'homeslider', HomesliderViewSet)
router.register(r'review', ReviewViewSet,basename='review')
router.register(r'rating', RatingViewSet)
router.register(r'bank', BankViewSet)
router.register(r'location', LocationViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('addcars/<int:car_id>/', views.check_add_car_filled),
    path('hostbios/<int:car_id>/', views.check_host_bio_filled),
    path('carimages/<int:car_id>/', views.check_car_img_filled),
    path('price/<int:car_id>/', views.check_price_filled),
    path('price/<int:car_id>/', views.check_location_filled),
    path('create_car_date/', views.create_car_date, name='create_car_date'),
    path('car/<int:car_id>/', views.update_car_isshared),
    path('filter_cars_with_date/', views.filter_cars_with_date, name='filter_cars_with_date'),
    path('filter_cars_by_brand/', views.filter_cars_by_brand, name='filter_cars_by_brand'),
    path('cars/<int:car_id>/total_rating/', views.get_total_rating_for_car, name='get-total-rating'),
    path('bank/<uuid:user_id>/', views.get_bank_details, name="get-bank"),
    path('users/<uuid:user_id>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('users/<str:user_name>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-login'),
    path('get_reviews_by_car_id/<int:car_id>/', views.get_reviews_by_car_id, name='get_reviews_by_car_id'),
    path('statistics/', views.statistics, name='statistics'),
    path('get_locations/<int:car_id>/', views.get_locations_by_car, name='get_locations_by_car'),

]
