from faker import Faker
from tables import Customer


def generate_customer():
    # Create Faker instance
    fake = Faker()

    # Generate Faker data
    customer_name = fake.name()
    customer_address = fake.street_address()
    city_name = fake.city()
    zip_code = fake.zipcode()
    contact = fake.email()
    phone_number = fake.phone_number()
    fake_customer = Customer(customer_name, customer_address, city_name, zip_code, contact,
                             phone_number)

    Customer.add_data(fake_customer)

