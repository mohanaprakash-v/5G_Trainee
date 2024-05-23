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

# sql = "insert into customers (name, address, phone) values (%s, %s, %s)"
# val = [('mohan', 'chennai', '123'),
#        ('naresh', 'madurai', '456'),
#        ('vijay', 'kolathur', '123'), 
#        ('sree', 'chennai', '123')] 


#need to use executemany while working with tuples
# mycursor.executemany(sql,val) 


# mycursor.execute("select * from customers where phone = 456")
# mycursor.fetchall()


# if we want to fetch only one row
# result = mycursor.fetchone()


# my_db.commit()
# print(mycursor.rowcount, "records inserted")
