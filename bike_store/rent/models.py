from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class VehicleType(models.Model):

    VEHICLE_TYPES = (('b', 'Bike'),
                     ('eb', 'Electric bike'),
                     ('s', 'Scooter'),
                     ('es', 'Electric scooter'))

    name = models.CharField(max_length=2, choices=VEHICLE_TYPES, unique=True)

    def __str__(self):
        if self.name == 'b':
            return('Bike')
        elif self.name == 'eb':
            return('Electric bike')
        elif self.name == 's':
            return('Scooter')
        elif self.name == 'es':
            return('Electric scooter')


class VehicleSize(models.Model):

    VEHICLE_SIZES = (('s', 'Small'),
                     ('m', 'Medium'),
                     ('l', 'Large'))
    size = models.CharField(max_length=1, choices=VEHICLE_SIZES, unique=True)

    def __str__(self):
        return f"{self.size.capitalize()}"


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField()
    real_cost = models.DecimalField(max_digits=6, decimal_places=2)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type}, {self.vehicle_size}"


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return(f"{self.customer} | {self.vehicle} | {self.rental_date} | {self.return_date}")


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=4, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.daily_rate}"
