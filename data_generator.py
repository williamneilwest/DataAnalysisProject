from faker import Faker
import random
from tables import Customer, Equipment, ServiceCallSchedule, Contract, customers, contracts
from datetime import datetime

# Create Faker instance
fake = Faker()
contract_type_options = ['Active', 'Expired', 'Terminated', 'Pending']
equipment_type_options = ['Machine', 'Mechanical', 'Electrical', 'Truck', 'Forklift']
service_call_description_options = ['Repair', 'Installation', 'Consultation', 'Replacement', 'Cleaning']
manufacture_types = ['Tolin', 'General Electric', 'Whirlpool', 'Godrej']


def generate_customer():
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


def generate_contract():
    # Generate Faker data
    starting_date = datetime(2000, 1, 1).date()
    ending_date = datetime(2040, 1, 1).date()
    contract_start_date = fake.date_between(start_date=starting_date, end_date=ending_date)
    contract_end_date = fake.date_between(start_date=contract_start_date, end_date=ending_date)
    contract_value = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    contract_type = fake.random_element(contract_type_options)
    fake_contract = Contract(random.choice(customers).customer_number, contract_start_date, contract_end_date,
                             contract_value,
                             contract_type)
    if fake_contract.contract_end_date < datetime.today().date():
        fake_contract.contract_type = 'Expired'
    if fake_contract.contract_end_date > datetime.today().date() and not fake_contract.contract_type == 'Pending':
        fake_contract.contract_type = 'Active'
    if fake_contract.contract_start_date > datetime.today().date():
        fake_contract.contract_type = 'Pending'
    Contract.add_data(fake_contract)


def generate_equipment():
    # Generate Faker data
    equipment_type = fake.random_element(equipment_type_options)
    manufacture = fake.random_element(manufacture_types)
    age = random.randint(1, 16)
    fake_equipment = Equipment(equipment_type, random.choice(contracts).contract_number, manufacture, age)
    Equipment.add_data(fake_equipment)


def generate_sales_call():
    # Generate Faker data
    starting_date = datetime.today().date()
    ending_date = datetime(2024, 5, 26).date()
    service_call_date = fake.date_between(start_date=starting_date, end_date=ending_date)
    service_call_description = fake.random_element(service_call_description_options)
    service_call_contract_number = random.choice(contracts).contract_number
    fake_service_call = ServiceCallSchedule(service_call_description, service_call_date, service_call_contract_number)
    ServiceCallSchedule.add_data(fake_service_call)


def generate_data_tables():
    generate_customer()
    generate_contract()
    generate_equipment()
    generate_sales_call()
