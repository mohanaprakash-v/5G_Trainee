select 
	name, unit_price, unit_price * 1.1 as "new price"
    from products

select * from orders
where order_date >= '2019-01-01'

--AND
select order_id, unit_price from order_items
where order_id = 6 and unit_price * quantity > 30

--IN
select * from products
where quantity_in_stock in (49, 38, 72) --IN operator
select * from products
where quantity_in_stock = 49 or quantity_in_stock = 38 or quantity_in_stock = 72

--BETWEEN
select * from customers
where birth_date between '1990-01-01' and '2000-01-01'

--LIKE
select * from customers
where address like '%Trail%' or address like '%Avenue%' 
	and phone like '%9'

--REGEXP
select * from customers
where first_name regexp '[a-z]s'

--IS NULL
select * from orders
where shipped_date is null

--ORDER BY
select product_id, order_id, quantity * unit_price as 'total_price' from order_items
where order_id = 2 
order by total_price desc

--LIMIT
select * from customers
order by points desc
limit 3

--JOINS
select distinct orders.customer_id, first_name, last_name from customers
join orders on customers.customer_id = orders.customer_id

select quantity, order_id, order_items.product_id, order_items.unit_price from order_items
join products on order_items.product_id = products.product_id

--JOINING ACROSS DATABASES
select * from order_items as oi
join sql_inventory.products as p
on oi.product_id = p.product_id

--SELF JOINS
select e.employee_id, e.first_name, m.first_name as manager
from employees e
join employees m on e.reports_to = m.employee_id