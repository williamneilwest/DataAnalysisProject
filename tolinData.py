import pyodbc
from faker import Faker
import random
import datetime

fake = Faker()


# Function to generate a random date between two given dates
def random_date(start_date, end_date):
    return fake.date_between_dates(date_start=start_date, date_end=end_date)


def set_type(start_date, end_date):
    today = '2023-06-07'
    if start_date.strftime("%Y-%m-%d") > today:
        return 'Pending'
    if end_date.strftime("%Y-%m-%d") < today:
        return 'Expired'
    else:
        return 'Active'


# Generate data structures for sample data
customersData = []
contractsData = []
equipmentData = []
callsData = []
cities = [
    'Denver',
    'Los Angeles',
    'Kansas City',
    'Dallas',
    'Miami',
    'Boston',
    'Chicago',
    'New York']
zipCodes = [
    '80202',
    '90001',
    '64101',
    '75201',
    '33101',
    '02101',
    '60601',
    '10001'
]

equipmentManufacturers = ['GE', 'Whirlpool', 'Hampton', 'Friedrich']
contractTypes = ['Expired', 'Active', 'Pending', 'Terminated']

for _ in range(200):
    randCityZip = random.randint(0, 7)
    customer = {
        'CustomerName': fake.company(),
        'Address': fake.address().split("\n")[0],
        'City': cities[randCityZip],
        'ZipCode': zipCodes[randCityZip],
        'Contact': fake.email(),
        'PhoneNumber': fake.phone_number()
    }
    customersData.append(customer)


for _ in range(350):
    randCustomer = random.randint(1, 200)
    startDate = random_date(datetime.date(2015, 1, 1), datetime.date(2023, 12, 31))
    endDate = random_date(startDate, datetime.date(2023, 12, 31))
    contract = {
        'CustomerNumber': randCustomer,
        'ContractStartDate': startDate.strftime("%Y-%m-%d"),
        'ContractEndDate': endDate.strftime("%Y-%m-%d"),
        'ContractValue': random.randint(1000, 600000),
        'ContractType': set_type(startDate, endDate)
    }
    contractsData.append(contract)


for _ in range(100):
    equipment = {
        'EquipmentType': '',
        'ContractNumber': random.randint(1, 350),
        'Manufacture': fake.random_element(elements=('Goodman', 'Whirlpool', 'GE')),
        'Age': random.randint(1, 15)
    }
    equipmentData.append(equipment)

for _ in range(40):
    call = {
        'ServiceCallDescription': fake.random_element(elements=('Repair', 'Installment', 'Removal', 'Upgrade')),
        'ScheduledDate': random_date(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)).strftime("%Y-%m-%d"),
        'ContractNumber': random.randint(1,350)
    }
    callsData.append(call)


# Set up the connection to the SQL Server database
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=WNW\MSSQLSERVER01;DATABASE=TolinDatabase' \
                    ';Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

if connection:
    print("Connection Successful")
else:
    print("Connection refused!")

# Generate entries for the Customers table
for customer in customersData:
    sql = "INSERT INTO Customers (CustomerName, Address, City, ZIP, Contact, PhoneNumber) VALUES (?, " \
          "?, ?, ?, ?, ?)"
    cursor.execute(sql, (
        customer['CustomerName'], customer['Address'], customer['City'], customer['ZipCode'],
        customer['Contact'], customer['PhoneNumber']))
connection.commit()

# Generate entries for the Contracts table
for contract in contractsData:
    sql = "INSERT INTO Contracts (CustomerNumber,ContractStartDate, ContractEndDate, ContractValue, ContractType) " \
          "VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (
        contract['CustomerNumber'], contract['ContractStartDate'],
        contract['ContractEndDate'],
        contract['ContractValue'], contract['ContractType']))
connection.commit()

# Generate entries for the Equipment table
for equipment in equipmentData:
    sql = "INSERT INTO Equipment (EquipmentType,ContractNumber, Manufacture, Age) VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (
        equipment['EquipmentType'], equipment['ContractNumber'], equipment['Manufacture'],
        equipment['Age']))
connection.commit()

# Generate entries for the CallSchedule table
for call_schedule in callsData:
    sql = "INSERT INTO CallSchedule (ServiceCallDescription, ScheduledDate, ContractNumber) VALUES " \
          "(?, ?, ?)"
    cursor.execute(sql, (
        call_schedule['ServiceCallDescription'], call_schedule['ScheduledDate'],
        call_schedule['ContractNumber']))
connection.commit()

# Close the connection to the database
connection.close()





