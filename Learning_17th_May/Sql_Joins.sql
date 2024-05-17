-- SQL JOINS --

--JOIN OR INNER JOIN--
select order_id, p.product_id, quantity, oi.unit_price
	from order_items as oi
	join products as p on p.product_id = oi.product_id

--JOINING ACROSS DATABASES--
use sql_store; --SELECTED DB--
select * from order_items as oi 
join sql_inventory.products as p on oi.product_id = p.product_id

--SELF JOIN-- (Getting the informations of the employees and their id also whom they want to report)
use sql_hr;
select m.first_name as manager,
    e.first_name as employees, e.employee_id
	from employees as e
	join employees as m on m.employee_id = e.reports_to

--JOINING MULTIPLE TABLES USING JOIN--
use sql_store;
select o.order_id, o.order_date, c.first_name, os.name as status
	from orders as o
	join customers as c on c.customer_id = o.customer_id
	join order_statuses as os on o.status = os.order_status_id

use sql_invoicing;
                           
select c.client_id, p.invoice_id, date, amount, pm.name, c.name
	from payments as p 
	join payment_methods as pm on p.payment_method = pm.payment_method_id
	join clients as c on c.client_id = p.client_id

--COMPOUND JOIN CONDITIONS--
--WHEN WE HAVE A COMPOSITE PRIMARY KEY WE NEED TO ACCESS BOTH WITH THE JOINING TABLE-- (ORDER_ID & PRODUCT_ID)
USE sql_store;
select * 
	from order_items as oi
	join order_item_notes as oin 
	on oi.order_id = oin.order_id
	and oin.product_id = oi.product_id

--IMPLICIT JOIN SYNTAX--(NOT RECOMMENDED BECOZ IF WE MISS WHERE CLAUSE IT WILL MAKE CROSS JOINS)
USE sql_store;
select * 
	from order_items as oi, orders as o
    where oi.order_id = o.order_id

--LEFT JOIN AND RIGHT JOIN (OUTER JOIN)--
--------LIKE INNER - OUTER IS ALSO A OPTIONAL WHEN USING JOIN
USE sql_store;
select * 
	from customers as c
--------LEFT JOIN (RETRIVES ALL VALUES FROM ORDERS TABLE NEGLECTING THE CONDITIONS)
    left join orders as o on o.customer_id = c.customer_id
--------RIGHT JOIN (RETRIVES ALL VALUES FROM ORDERS TABLE NEGLECTING THE CONDITIONS)
    right join orders as o on o.customer_id = c.customer_id

USE sql_store;
select p.product_id, p.name, oi.quantity
	from products as p 
	left join order_items as oi on p.product_id = oi.product_id

--MULTIPLE TABLES JOINING USING OUTER JOINS--   
USE sql_store;
select c.customer_id, c.first_name, o.order_id, sh.name as shipper
	from customers as c
    left join orders as o on o.customer_id = c.customer_id
    left join shippers as sh on sh.shipper_id = o.shipper_id

select o.order_date, o.order_id, c.first_name as customer, sh.name as shipper, os.name as status
	from orders as o
	join order_statuses as os on o.status = os.order_status_id
    left join shippers as sh on sh.shipper_id = o.shipper_id
    join customers as c on c.customer_id = o.customer_id

--SELF OUTER JOIN--
use sql_hr;
select m.first_name as manager,
    e.first_name as employees, e.employee_id
	from employees as e
	left join employees as m on m.employee_id = e.reports_to

--USING CLAUSE--
use sql_store;
select * 
	from order_items as oi 
    join order_item_notes as oin
	using (product_id, order_id) 