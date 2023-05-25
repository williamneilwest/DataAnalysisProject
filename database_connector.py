import mysql.connector


def connect_to_database():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='test',
        database='tolindata'
    )
    return conn


def insert_data(cursor, query, values):
    # Insert data into the database
    cursor.execute(query, values)


def commit_and_close(conn):
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

