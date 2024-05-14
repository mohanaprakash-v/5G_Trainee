import mysql.connector

mydb = mysql.connector.connect(
    host = "",
    username = "root",
    password = "root"
)

print(mydb)