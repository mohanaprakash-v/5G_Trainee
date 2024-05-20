-- USING CLAUSE --
use sql_invoicing;

select 
	p.date, 
    c.name as client, 
    p.amount, 
    pm.name as pay_method
from payments as p
left join payment_methods as pm on p.payment_method = pm.payment_method_id
left join clients as c using (client_id)

-- NATURAL JOINS -- (JOINS TWO TABLE BASED ON COMMON COLOUMN)
use sql_invoicing;

select * from clients as c
natural join invoices as i

--CROSS JOINS--
use sql_store;
select * 
from customers as c
cross join products as p
order by c.customer_id

--IMPLICIT CROSS JOIN--
use sql_store;
select * 
from shippers as s, products as p
order by s.shipper_id

--------UNIONS----------
--SAME TABLE JOINING ROWS--
use sql_store;

select order_id, order_date,
 'active' as Status
 from orders as o where order_date >= '2019-01-30'
 union
 select order_id, order_date,
 'archive' as Status
 from orders as o where order_date < '2019-01-30'
 
--DIFFERENT TABLE JOINING ROWS--
use sql_store;
select 
	customer_id, 
	first_name, points,
	'Gold' as Type
from customers 
where points >= '3000'
union
select 
	customer_id, 
	first_name, points,
	'Silver' as Type
from customers 
where points >= '2000' and points < '3000'
union
select 
	customer_id, 
	first_name, points,
	'Bronze' as Type
from customers 
where points < '2000'
order by first_name

--INSERTING A SINGLE ROW IN A TABLE--
use sql_store;
insert into customers (first_name, last_name, birth_date, phone, address, city, state, points)
values ('Mohan', 'Prakash', '2002-05-20', '9789030247', 'address', 'Chennai', 'TN', '876')

--MULTIPLE ROWS--
use sql_store;
insert into customers (first_name, last_name, birth_date, phone, address, city, state, points)
values ('Mohan', 'Prakash', '2002-05-20', '9789030247', 'address', 'Chennai', 'TN', '876'),
		('Naresh', 'Kumar', '2002-05-23', '978903111', 'address', 'Madara', 'MP', '1876')
    
-- INSERTING HIERARCHICAL ROWS -- MULTIPLE TABLES
use sql_store;

insert into orders (customer_id, order_date, status)
values (1,'2019-03-20',2);

insert into order_items
values (last_insert_id(),2, 1, 4.66)

