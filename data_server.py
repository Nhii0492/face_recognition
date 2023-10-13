import pypyodbc as odbc

def retrieve_students():
    server = 'localhost.database.windows.net'
    database = 'DATAFACE'
    username = 'sa'  # Replace with your actual username
    password = 'Password.1'  # Replace with your actual password
    driver = '{ODBC Driver 17 for SQL Server}'

    # Establish a connection
    conn = odbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')

    sql = 'SELECT ID, Name FROM STUDENTS'

    cursor = conn.cursor()
    cursor.execute(sql)

    dataset = cursor.fetchall()

    # Print the retrieved data
    for row in dataset:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Call the function to retrieve students' data
retrieve_students()
