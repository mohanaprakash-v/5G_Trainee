import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")

# Switch to the new database
cursor.execute("USE test_db")

# Create a new table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Insert data into the table
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
val = ("John Doe", 30)
cursor.execute(sql, val)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully!")