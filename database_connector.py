import mysql.connector
from tables import customers as customerslist


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


query = f"INSERT INTO customers (customerNumber, CustomerName, Address, City, ZIP, " \
        f"Contact, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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

commit_and_close(conn)
