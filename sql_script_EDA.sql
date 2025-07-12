select * from walmart;

---- to check data type of column
select pg_typeof() from walmart;


select 
	payment_method,
	count(*)
from walmart
group by payment_method;
-- There is 4256 invoices that paid by Credit Card, 3881 invoices paid with Ewallet and 1832 with Cash.

select count(distinct branch) from walmart; --  there are 100 branches.


--- EDA, explore business problems and potential insights
-- Assumption
-- 1. Which are the top 5 branches contributing to the most total revenue ?
select 
	sum(total) total_revenue, 
	branch, 
	city 
from 
	walmart
group by 
	branch,
	city
order by 
	total_revenue desc
limit 5;
-- 2. What are the busiest hours of the day, so we can schedule staff more effectively?
select 
	extract (hour from time::time) hour_of_day,
	count(invoice_id) transaction_count
from
	walmart
group by
	hour_of_day
order by transaction_count desc;
/* we can see that the range of hour from 15pm to 20pm has the most invoiced in a day, 
so we should arrange more staff in this hours*/

-- 3. Which product categories are most popular (by quantity sold) versus most profitable (by average profit margin)?
select
	category,
	sum(quantity) total_quan_sold,
	avg(profit_margin) avr_pm
from walmart
group by category
order by total_quan_sold desc;
/*  The purpose is to identify hidden opportunities and risks, by compare these two, we can categorize our product:
- For those which high popularity, low profitability: bring customers but dont make much money on their own.
We could bundle these with a high-profit item or increase the price slightly.
- For those which low popularity, high profitability: very valuable but may not be getting enough attention.
We could increase their visibility with better placement or marketing to sell more.
- For those high in both popularity and profitability, ensure it's always in stock and well-marketed.
we could get rid the low in both to save the resource for this one. */

-- 4. Do some branches have significantly lower average customer ratings than others, indicating potential issues with service or quality?
select 
	branch,
	avg(rating) average_rating,
	count(rating)
from walmart
group by branch
order by average_rating desc;
/* The purpose is to 
- Identify any branch with low rating so that we can investigate that branch more closely on the reason,
staffing levels, management effectiveness, cleanliness, or product availability, etc.
- make sure the quality of all the branch are consistent, customers should have a similar, positive experience regardless which branch they
visit.
- Can compare and learn from the top.
*/

-- 5. What is the distribution of payment methods, and does the average transaction value differ between them?
select 
	payment_method,
	count(payment_method) number_of_uses,
	avg(unit_price * quantity) avg_transaction_value
from walmart
group by payment_method
order by number_of_uses desc;

/* we can see that people pay with cash is the lowest but once they buy a lots. */

-- 6. Which days of the week generate the most transactions?(0: sunday, 1: monday and so on)
select 
	extract (DOW from to_date(date, 'DD/MM/YY')) day_of_week,
	count(*) transaction_count
from walmart
group by day_of_week
order by transaction_count;
/* same with identify which hours has the most transaction, this one is for which day, so 
we can arrange more staff on busy day and less staff on less busy day. 
we can also do some more promotions and marketing for less busy day to get more customers.
moreover, we can do restocking on less busy day for preparing for busy day. */

/* 7.What product categories are most frequently purchased together in the same transaction, 
which could suggest a product bundling or cross-selling opportunity? */
select
	a.category as categoryA,
	b.category as categoryB,
	count(*) as frequency
from walmart a
join walmart b on a.invoice_id = b.invoice_id and a.category < b.category
group by categoryA, categoryB
order by frequency desc
limit 10;
/* There is no output, which we can conclude that customers already have thing to buy in mind when they visit the store. 
They buy items from a single product category and leave without makking purchases from other categories in the same transaction.
Therefore, we can do some marketing campain to change that, more opportunities */

/* 8.Segment Customers into Tier  base on their total spending */
with customer_spending as (
	select
		invoice_id,
		sum(total) total_spent
	from walmart
	group by invoice_id
)
select
	invoice_id,
	total_spent,
	ntile(3) over (order by total_spent desc) customter_tier
from customer_spending
order by total_spent desc;

/* 9.What was the month-over-month (MoM) percentage growth or decline in revenue for the entire business? */
with monthly_revenue as ( /* to create a temp table */ 
	select 
		date_trunc('month', to_date(date, 'DD/MM/YY')) sales_month,/* to cut a date down to the beginning fo its month, this is how to group
		all sales that happened inthe same month together */ 
		sum(total) total_revenue
	from walmart
	group by sales_month
)
select 
	sales_month,
	total_revenue,
	lag(total_revenue, 1) over (order by sales_month) previous_month_revenue,
	(total_revenue - lag(total_revenue,1) over (order by sales_month))
	/ lag(total_revenue, 1) over (order by sales_month) * 100 mom_growth_pct
	/* lag() */
from monthly_revenue
order by sales_month;
/* The purpose is to check if the business is growing consistently, to identify a seasonal patterns, or checking if the business is
declining or has hit a sharp drop. 
*/

