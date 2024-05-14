import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Create a cursor object
cursor = mydb.cursor()

# Create a new database
cursor.execute("CREATE DATABASE mydatabase")

cursor.execute("USE mydatabase")

# Connect to the newly created database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# Create a cursor for the new database
cursor = mydb.cursor()

# Create a table
cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Insert data into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('John', 'Highway 21'),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345')
]
cursor.executemany(sql, val)

# Commit changes
mydb.commit()

# Print the number of records inserted
print(cursor.rowcount, "records inserted.")

# Close the cursor and database connection
cursor.close()
mydb.close()
