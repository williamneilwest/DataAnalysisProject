from data_generator import generate_data_tables
from tables import customers, contracts, equipment, service_call_schedule




def print_tables():
    for customer in customers:
        print('Customers: ', customer)
    for contract in contracts:
        print('Contract: ', contract)
    for equipment_or_tool in equipment:
        print('Equipment: ', equipment_or_tool)
    for service_call in service_call_schedule:
        print('Service Call: ', service_call)


for i in range(100):
    generate_data_tables()
    i += 1

print_tables()

from database_connector import insert_data, connect_to_database, commit_and_close
import database_connector




