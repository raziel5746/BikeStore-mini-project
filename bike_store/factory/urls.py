from django.urls import path
from . import views

urlpatterns = [
    path('rentals_factory/<int:num>', views.rentals_factory, name='rentals_factory'),

    path('vehicles_factory/<int:num>', views.vehicles_factory, name='vehicles_factory'),

    path('customers_factory/<int:num>', views.customers_factory, name='customers_factory'),
]
