from faker import Faker
from rent.models import Customer

fake = Faker()


def fake_customers(num):

    for i in range(num):
        customer = Customer(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            email=fake.email(),
                            phone_number=fake.phone_number(),
                            address=fake.address(),
                            city=fake.city(),
                            country=fake.country())

        customer.save()
