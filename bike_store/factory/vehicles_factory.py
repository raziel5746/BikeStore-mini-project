from faker import Faker
from django.db.models import Max
from random import randint
from rent.models import Vehicle, VehicleSize, VehicleType, RentalRate

fake = Faker()


def get_random(Model):

    max_id = Model.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        record = Model.objects.filter(pk=pk).first()
        if record:
            return record


def fake_vehicles(num):

    for i in range(num):
        fake_date_created = fake.date_between(
            start_date="-1y", end_date="-90d")
        fake_vehicle_type = get_random(VehicleType)
        fake_vehicle_size = get_random(VehicleSize)
        fake_real_cost = RentalRate.objects.filter(vehicle_type=fake_vehicle_type, vehicle_size=fake_vehicle_size).first()

        vehicle = Vehicle(vehicle_type=fake_vehicle_type,
                          date_created=fake_date_created,
                          real_cost=fake_real_cost.daily_rate * randint(20, 24),
                          vehicle_size=fake_vehicle_size)

        vehicle.save()
