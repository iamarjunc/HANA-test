from hdbcli import dbapi

# Set up the connection details
host = "qs-saphana.legvi.org"
port = 30015  # Default port for HANA
user = "B1ADMIN"
password = "HopBwENw4CbUPZkXe!!!"
database = "BILLTRACKING"  # Specify your database name here

# Try to establish the connection
try:
    # Establish the connection
    connection = dbapi.connect(
        address=host,
        port=port,
        user=user,
        password=password,
        database=database  # Add the database parameter
    )
    
    # If connection is successful
    print("Connection successful!")

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Prepare and execute the stored procedure using the CALL statement
    procedure = "CALL QSYS_BTS_SponList(30711, 'S')"
    cursor.execute(procedure)

    # Fetch the results, if any
    result = cursor.fetchall()

    # Print the results
    print(result)

    # Close the cursor and connection
    cursor.close()

except dbapi.Error as e:
    # If there is an error with the connection
    print(f"Connection failed: {e}")
finally:
    # Ensure the connection is closed if it was successful
    if 'connection' in locals():
        connection.close()
