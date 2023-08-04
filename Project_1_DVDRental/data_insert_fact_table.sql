insert into sales_table(
	date_key, customer_key,
	movie_key, store_key, sales_amount
)
select 
	to_char(payment_date :: DATE, 'yyyMMDD')::integer as date_key,
	p.customer_id as customer_key,
	i.film_id as movie_key,
	i.store_id as store_key,
	p.amount as sales_amount
from payment p
join rental as r on r.rental_id = p.rental_id
join inventory as i on i.inventory_id = r.inventory_id ;
