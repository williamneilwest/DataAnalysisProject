from data_generator import generate_customer
from tables import customers


def print_customers():
    for customer in customers:
        print('Customers: ', customer)


generate_customer()
generate_customer()

print_customers()

