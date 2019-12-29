from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rental-home'),
    path('rentals/', views.rentals, name='rentals'),
    path('rental/<int:id>', views.myrental, name='myrental'),
    # path('rental/add', views.add_rental, name='addrental'),
    path('rental/add/<int:customer>', views.add_rental, name='addrental'),
    path('rental/return/<int:id>', views.return_vehicle, name='returnvehicle'),

    path('customers/', views.customers, name='customers'),
    path('customers/filtered', views.customers_search, name='customerssearch'),
    path('customer/<int:id>', views.mycustomer, name='mycustomer'),
    path('customer/add', views.addcustomer, name='addcustomer'),

    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicle/<int:id>', views.myvehicle, name='myvehicle'),
    path('vehicle/add', views.addvehicle, name='addvehicle'),
]
