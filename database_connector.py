import mysql.connector

from tables import customers as customerslist, contracts as contractslist, equipment as equipmentlist, service_call_schedule as servicelist


def connect_to_database():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='test',
        database='tolindata'
    )
    return conn


def insert_data(cursor1, query1, values):
    # Insert data into the database
    cursor.execute(query, values)


def commit_and_close(conn1):
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


query = f"INSERT INTO customers (CustomerNumber, CustomerName, Address, City, ZIP, " \
        f"Contact, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
query2 = f"INSERT INTO contracts (ContractNumber, CustomerNumber, ContractStartDate, ContractEndDate, ContractValue, " \
         f"ContractType) VALUES (%s, %s, %s, %s, %s, %s)"
query3 = f"INSERT INTO equipment (EquipmentId, EquipmentType, ContractNumber, Manufacture, Age) " \
         f"VALUES (%s, %s, %s, %s, %s)"
query4 = f"INSERT INTO service_call_schedule (ServiceCallNumber, ServiceCallDescription, ScheduledDate, ContractNumber) " \
         f"VALUES (%s, %s, %s, %s)"

conn = connect_to_database()
cursor = conn.cursor()


for customer_entry in customerslist:
    customer_number = customer_entry.customer_number
    customer_name = customer_entry.customer_name
    address = customer_entry.address
    city = customer_entry.city
    zip_code = customer_entry.zip_code
    email = customer_entry.email
    phone_number = customer_entry.phone_number

    cursor.execute(query, (customer_number, customer_name, address, city, zip_code, email, phone_number))

for contract_entry in contractslist:
    contract_number = contract_entry.contract_number
    customer_number = contract_entry.customer_number
    start_date = contract_entry.contract_start_date
    end_date = contract_entry.contract_end_date
    contract_value = contract_entry.contract_value
    contract_type = contract_entry.contract_type

    cursor.execute(query2, (contract_number, customer_number, start_date, end_date, contract_value, contract_type))

for equipment_entry in equipmentlist:
    equipment_id = equipment_entry.equipment_id
    equipment_type = equipment_entry.equipment_type
    contract_number = equipment_entry.contract_number
    manufacture = equipment_entry.manufacture
    age = equipment_entry.age

    cursor.execute(query3, (equipment_id, equipment_type, contract_number, manufacture, age))


for service_call_entry in servicelist:
    service_call_number = service_call_entry.service_call_number
    service_call_description = service_call_entry.service_call_description
    service_call_scheduled_date = service_call_entry.scheduled_date
    contract_number = service_call_entry.contract_number

    cursor.execute(query4, (service_call_number, service_call_description, service_call_scheduled_date, contract_number))




commit_and_close(conn)
