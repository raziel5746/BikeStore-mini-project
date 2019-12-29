from faker import Faker
from django.db.models import Max
from random import randint
from datetime import date, timedelta
from rent.models import Rental, Customer, Vehicle

fake = Faker()


def get_random(Model):

    max_id = Model.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = randint(1, max_id)
        record = Model.objects.filter(pk=pk).first()
        if record:
            return record


def fake_rentals(num):

    for i in range(num):
        fake_rental_date = fake.date_between(start_date="-89d", end_date="today")
        print("FAKE RENTAL DATE CREATED AAAAAAAAAAAAAAAAAAAAAAAA")
        fake_return_date = fake_rental_date + timedelta(days=randint(1, 15))
        print("FAKE RETURN DATE CREATED BBBBBBBBBBBBBBBBBBBBBBBB")
        random_customer_id = get_random(Customer).id
        random_vehicle_id = get_random(Vehicle).id
        print("RANDOM V_ID: ", random_vehicle_id)

        available_rentals = []

        if Rental.objects.filter(vehicle_id=random_vehicle_id):
            print("RENTAL RECORDS EXIST WITH THIS V-ID")
            for rental in Rental.objects.filter(vehicle_id=random_vehicle_id):
                print("RENTALLLLLLLLLLLLLLL: ", rental)
                if (rental.return_date is not None and (fake_rental_date >= rental.return_date or fake_return_date <= rental.rental_date)):
                    available_rentals.append(True)
                    print("AAAAAAAAAAAAAAAAAAAAAA", available_rentals)
                else:
                    available_rentals.append(False)
                    print("AAAAAAAAAAAAAAAAAAAAAA", available_rentals)
                    # break
        else:
            print("NO RENTAL RECORDS WITH THIS V-ID")

        if all(available_rentals) or available_rentals == []:
            print("STARTING RECORD CREATION")
            new_rental = Rental(rental_date=fake_rental_date,
                                # return_date=None,
                                customer_id=random_customer_id,
                                vehicle_id=random_vehicle_id)

            print("RECORD CREATED BUT NOT YET SAVED")

            if fake_return_date <= date.today():
                new_rental.return_date = fake_return_date

            else:
                print("RETURN DATE NULLLLLLLLLLLL")
            new_rental.save()
            print("RENTAL CREATED SUCCESSFULLY")

        else:
            print("RENTAL NNNNOOOOTTTT CREATED")
