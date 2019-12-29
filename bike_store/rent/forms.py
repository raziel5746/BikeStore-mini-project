from django import forms
from .models import Rental, Vehicle, Customer
from datetime import date


class AddRentalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = ('rental_date', 'return_date', 'customer', 'vehicle')
        labels = {
            'vehicle': "Available vehicles",
        }

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('my_customer')
        super(AddRentalForm, self).__init__(*args, **kwargs)
        rented_vehicles = Rental.objects.filter(return_date__isnull=True)
        rented_vehicles_ids = [rental.vehicle_id for rental in rented_vehicles]

        self.fields['rental_date'].initial = date.today()

        self.fields['vehicle'].queryset = Vehicle.objects.exclude(id__in=rented_vehicles_ids).order_by('vehicle_type', 'vehicle_size')

        if type(customer) is int:
            if customer == 0:
                self.fields['customer'].queryset = Customer.objects.order_by('last_name', 'first_name')
            if customer > 0 :
                my_customer = Customer.objects.get(id=customer)
                self.fields['customer'].initial = customer


class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'country')


class AddVehicleForm(forms.ModelForm):

    date_created = forms.DateField(initial=date.today())

    class Meta:
        model = Vehicle
        fields = ('vehicle_type', 'vehicle_size', 'real_cost', 'date_created')