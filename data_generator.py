import pyodbc
from faker import Faker
import random
import datetime

fake = Faker()


# Function to generate a random date between two given dates
def random_date(start_date, end_date):
    return fake.date_between_dates(date_start=start_date, date_end=end_date)


# Function to generate random contract value
def random_contract_value():
    return random.randint(1000, 100000)


# Function to generate random equipment age
def random_equipment_age():
    return random.randint(1, 10)


# Generate entries for the Customers table
customers_data = []
for _ in range(1000):
    customer = {
        'CustomerName': fake.company(),
        'Address': fake.address(),
        'City': fake.city(),
        'ZIP': fake.zipcode(),
        'Contact': fake.email(),
        'PhoneNumber': fake.phone_number(),
    }
    customers_data.append(customer)

# Generate entries for the Contracts table
contracts_data = []
for _ in range(1000):
    contract = {
        'CustomerNumber': random.randint(1, 1000),  # Randomly assigned customer number
        'ContractStartDate': random_date(datetime.date(2010, 1, 1), datetime.date(2022, 12, 31)),
        'ContractEndDate': random_date(datetime.date(2023, 1, 1), datetime.date(2026, 12, 31)),
        'ContractValue': random_contract_value(),
        'ContractType': fake.random_element(elements=('Active', 'Expired', 'Terminated')),
    }
    contracts_data.append(contract)

# Generate entries for the Equipment table
equipment_data = []
for i in range(1000):
    equipment = {
        'EquipmentType': fake.random_element(elements=('Condenser', 'Motor', 'Fan', 'Compressor')),
        'ContractNumber': random.randint(1, 1000),  # Randomly assigned contract number
        'Manufacture': fake.random_element(elements=('Goodman', 'Whirlpool', 'GE')),
        'Age': random_equipment_age(),
    }
    equipment_data.append(equipment)

# Generate entries for the CallSchedule table
call_schedule_data = []
for i in range(1000):
    call_schedule = {
        'ServiceCallDescription': fake.sentence(),
        'ScheduledDate': random_date(datetime.date(2023, 1, 1), datetime.date(2030, 12, 31)),
        'ContractNumber': random.randint(1, 1000),  # Randomly assigned contract number
    }
    call_schedule_data.append(call_schedule)

# Set up the connection to the SQL Server database
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=WNW\MSSQLSERVER01;DATABASE=TolinData' \
                    ';Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Generate entries for the Customers table
for customer in customers_data:
    sql = "INSERT INTO Customers (CustomerName, Address, City, ZIP, Contact, PhoneNumber) VALUES (?, " \
          "?, ?, ?, ?, ?)"
    cursor.execute(sql, (
        customer['CustomerName'], customer['Address'], customer['City'], customer['ZIP'],
        customer['Contact'], customer['PhoneNumber']))
connection.commit()

# Generate entries for the Contracts table
for contract in contracts_data:
    sql = "INSERT INTO Contracts (CustomerNumber, ContractEndDate, ContractValue, ContractType) " \
          "VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (
        contract['CustomerNumber'], contract['ContractStartDate'],
        contract['ContractEndDate'],
        contract['ContractValue'], contract['ContractType']))
connection.commit()

# Generate entries for the Equipment table
for equipment in equipment_data:
    sql = "INSERT INTO Equipment (EquipmentType, Manufacture, Age) VALUES (?, ?, ?)"
    cursor.execute(sql, (
        equipment['EquipmentType'], equipment['ContractNumber'], equipment['Manufacture'],
        equipment['Age']))
connection.commit()

# Generate entries for the CallSchedule table
for call_schedule in call_schedule_data:
    sql = "INSERT INTO CallSchedule (ServiceCallDescription, ScheduledDate, ContractNumber) VALUES " \
          "(?, ?, ?)"
    cursor.execute(sql, (
        call_schedule['ServiceCallDescription'], call_schedule['ScheduledDate'],
        call_schedule['ContractNumber']))
connection.commit()

# Close the connection to the database
connection.close()
