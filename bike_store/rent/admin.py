from django.contrib import admin
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate


admin.site.register(Customer)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Vehicle)
admin.site.register(Rental)
admin.site.register(RentalRate)
