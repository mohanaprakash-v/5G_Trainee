--AND OR Operators--

select * from Customer 
where customername like 'G%' or customername like 'R%'

select * from Customer 
where country = "Spain" and customername like 'G%' or customername like 'R%'

select * from Customer
where City="Berlin" or City = "London"

--NOT Operator--

select * from Customer
where not country = "Spain"

select * from Customer
where customername not like 'A%'

--INSERT INTO--

INSERT INTO Customer
values ('Mohan', '4005', 'Chennai')

--DISTINCT--

select DISTINCT from Customer
where customerid > 40

select count(DISTINCT country) from Customer

--UPDATE--

-- SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city --

UPDATE Customer
SET customername = "Mohan" and City = "Chennai" 
where CustomerID = 1;

update Customer
set contactname = "Jaun"
where country = "Mexico"

update Customer
set City = "Oslo"

-- DELETE --

DELETE FROM Customers WHERE CustomerName='naresh';
