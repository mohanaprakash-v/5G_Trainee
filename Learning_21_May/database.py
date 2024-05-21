import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "mydatabase"
)

mycursor = my_db.cursor()

# mycursor.execute("create database mydatabase")
# mycursor.execute("create table customers(name varchar(200), address varchar(200), phone varchar(200))")
# mycursor.execute("alter table customers add column customer_id int auto_increment primary key")

sql = "insert into customers (name, address, phone) values (%s, %s)"




