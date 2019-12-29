from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Rental, RentalRate, Customer, Vehicle
from .forms import AddRentalForm, AddCustomerForm, AddVehicleForm
from django.db.models import F
from datetime import date
from crispy_forms.utils import render_crispy_form


def home(request):
    return redirect('rentals')


def rentals(request):
    all_rentals = Rental.objects.all().order_by(F('return_date').desc(nulls_first=True), '-rental_date')

    return render(request, 'rent/rentals.html', {'all_rentals': all_rentals})


def myrental(request, id):
    rental = Rental.objects.get(id=id)
    customer = rental.customer
    vehicle = rental.vehicle
    daily_rate = RentalRate.objects.get(vehicle_type=vehicle.vehicle_type, vehicle_size=vehicle.vehicle_size).daily_rate
    total_days = 0

    if rental.return_date is None:
        total_days = (date.today() - rental.rental_date).days + 1
    else:
        total_days = (rental.return_date - rental.rental_date).days + 1

    total_rate = total_days * daily_rate

    return render(request, 'rent/myrental.html', {'rental': rental, 'customer': customer, 'vehicle': vehicle, 'daily_rate': daily_rate, 'total_days': total_days, 'total_rate': total_rate})


def add_rental(request, customer):
    if request.method == 'POST':
        form = AddRentalForm(request.POST, my_customer=customer)
        passed_from_views = {'form': form,
                             'customer': customer}

        if form.is_valid():
            rental_date = form.cleaned_data['rental_date']
            return_date = form.cleaned_data['return_date']
            customer = form.cleaned_data['customer']
            vehicle = form.cleaned_data['vehicle']
            new_rental = Rental(rental_date=rental_date, return_date=return_date, customer=customer, vehicle=vehicle)

            new_rental.save()
            return HttpResponseRedirect(reverse('rentals'))

    else:
        form = AddRentalForm(my_customer=customer)
        # my_id_int = 0
        # if type(my_id) is int:
        #     my_id_int = my_id
        passed_from_views = {'form': form,
                             'customer': customer}

    return render(request, 'rent/addrental.html', passed_from_views)


def return_vehicle(request, id):
    rental = Rental.objects.get(id=id)
    rental.return_date = date.today()
    rental.save()

    return HttpResponseRedirect(reverse('rentals'))


def customers(request):
    customers = Customer.objects.order_by('last_name', 'first_name')
    return render(request, 'rent/customers.html', {'customers': customers})


def customers_search(request):
    if request.method == 'GET':
            search = request.GET
            print(search)
    customers = Customer.objects.order_by('last_name', 'first_name')
    return render(request, 'rent/customers.html', {'customers': customers})


def mycustomer(request, id):
    customer = Customer.objects.get(id=id)

    return render(request, 'rent/mycustomer.html', {'customer': customer})


def addcustomer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']

            new_customer = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, address=address, city=city, country=country)

            new_customer.save()
            return HttpResponseRedirect(reverse('addrental'))
    else:
        form = AddCustomerForm()

    return render(request, 'rent/addcustomer.html', {'form': form})


def vehicles(request):
    rented_vehicles = Rental.objects.filter(return_date__isnull=True)
    rented_vehicles_ids = [rental.vehicle_id for rental in rented_vehicles]
    available_vehicles = Vehicle.objects.exclude(id__in=rented_vehicles_ids).order_by('vehicle_type', 'vehicle_size')

    b = available_vehicles.filter(vehicle_type=1).order_by('vehicle_size', 'real_cost')
    eb = available_vehicles.filter(vehicle_type=2).order_by('vehicle_size', 'real_cost')
    s = available_vehicles.filter(vehicle_type=3).order_by('vehicle_size', 'real_cost')
    es = available_vehicles.filter(vehicle_type=4).order_by('vehicle_size', 'real_cost')

    return render(request, 'rent/vehicles.html', {'vt': [b, eb, s, es]})


def myvehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'rent/myvehicle.html', {'vehicle': vehicle})


def addvehicle(request):
    if request.method == 'POST':
        print(request.POST)
        form = AddVehicleForm(request.POST)

        if form.is_valid():
            vehicle_type = form.cleaned_data['vehicle_type']
            vehicle_size = form.cleaned_data['vehicle_size']
            real_cost = form.cleaned_data['real_cost']
            date_created = form.cleaned_data['date_created']

            new_vehicle = Vehicle(vehicle_type=vehicle_type, vehicle_size=vehicle_size, real_cost=real_cost, date_created=date_created)

            new_vehicle.save()
            new_vehicle_id = new_vehicle.id
            print(new_vehicle_id)
            return HttpResponseRedirect(reverse('myvehicle', kwargs={'id': new_vehicle_id}))
    else:
        form = AddVehicleForm()

    return render(request, 'rent/addvehicle.html', {'form': form})
