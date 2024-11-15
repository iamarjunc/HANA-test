from hdbcli import dbapi

# Set up the connection details
host = "qs-saphana.legvi.org"
port = 30015  # Default port for HANA
user = "B1ADMIN"
password = "HopBwENw4CbUPZkXe!!!"
database = "BILLTRACKING"  # Specify your database name here

# Establish the connection
connection = dbapi.connect(
    address=host,
    port=port,
    user=user,
    password=password,
    database=database  # Add the database parameter
)

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
connection.close()
