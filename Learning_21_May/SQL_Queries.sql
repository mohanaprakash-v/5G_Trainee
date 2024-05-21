---CREATING A COPY OF TABLE---

--CREATING A COPY--
use sql_store;
create table order_archive as 
select * from orders
--CREATING A COPY WITH CONDITION--
insert into order_archive 
select * from orders
where order_date < '2019-01-30'

--EXERCISE--
-----JOIN CLIENTS AND INVOICES
-----NEW TABLE NAME INVOICES_ARCHIVE
-----INSTEAD OF CLIENT ID - NEED CLIENT NAME COLUMN
-----NEED TO COPY INVOICES THAT HAVE A PAYMENT

use sql_invoicing;

create table invoice_archive as
select iv.invoice_id, iv.payment_total, c.name as clients, iv.payment_date
 from invoices as iv
join clients as c using (client_id) 

where iv.payment_date is not null
order by invoice_id

--UPDATE A SINGLE ROW--
use sql_invoicing;
update invoices
set payment_total = 10, payment_date = '2019-05-20'
where invoice_id = '1'

--UPDATE MULTIPLE ROWS--
use sql_store;

update customers
set points = points+50
where birth_date < '1990-01-01' 
-------
update invoices
set payment_total = invoice_total * 0.5, payment_date = due_date
where client_id = 3

--EXERCISE IF CLIENT ID IS NOT KNOWN ONLY NAME IS KNOWN
--USING SUB QUERY WITH UPDATE--
update invoices
set payment_total = invoice_total * 0.5, payment_date = due_date
where client_id = (select client_id from clients where name = 'Topiclounge')

--EXERCISE CUSTOMERS WHO HAVE MORE THAN 3000 POINTS UPDATE COMMENTS FOR THEM--
use sql_store;
update orders set comments = 'Gold'
where customer_id in
(select customer_id from customers 
where points > 3000)

