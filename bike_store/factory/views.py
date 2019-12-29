from django.shortcuts import render
from . import rentals_factory as rf
from . import vehicles_factory as vf
from . import customers_factory as cf
from rent.models import Rental, Vehicle, Customer


def rentals_factory(request, num):
    rf.fake_rentals(num)
    rentals_list = Rental.objects.all()
    return render(request, 'factory/rentals_factory.html', {'rentals': rentals_list})


def vehicles_factory(request, num):
    vf.fake_vehicles(num)
    vehicles_list = Vehicle.objects.all()
    return render(request, 'factory/vehicles_factory.html', {'vehicles': vehicles_list})


def customers_factory(request, num):
    cf.fake_customers(num)
    customers_list = Customer.objects.all()
    return render(request, 'factory/customers_factory.html', {'vehicles': customers_list})
