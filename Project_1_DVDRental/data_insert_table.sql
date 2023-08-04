
INSERT INTO date_table(
	date_key,
	date,
	year,
	quarter,
	month,
	week,
	day,
	is_weekend
)
SELECT 
	DISTINCT(TO_CHAR(payment_date :: DATE, 'yyyMMDD')::integer) AS date_key,
	date(payment_date) AS date,
	EXTRACT(year FROM payment_date) AS year,
	EXTRACT(quarter FROM payment_date) AS quarter,
	EXTRACT(month FROM payment_date) AS month,
	EXTRACT(week FROM payment_date) AS week,
	EXTRACT(day FROM payment_date) AS day,
	CASE 
		WHEN EXTRACT(ISODOW FROM payment_date) in (6,7) THEN true ELSE false
		END AS is_weekend
FROM payment;

INSERT INTO customer_table(
	customer_key, customer_id, first_name, last_name, email, 
	address, address2, district, city, country, postal_code,
	phone, active, create_date, start_date, end_date)
select 
	customer_id as customer_key,
	customer_id ,
	first_name ,
	last_name ,
	email ,
	a.address ,
	a.address2 ,
	a.district ,
	ci.city ,
	co.country ,
	a.postal_code ,
	a.phone ,
	c.active ,
	c.create_date ,
	now() as start_date,
	now() as end_date
from customer as c 
join address as a on a.address_id = c.address_id
join city as ci on ci.city_id = a.city_id
join country as co on co.country_id = ci.country_id
;


insert into movie_table(
	movie_key, film_id, title, description, release_year,
	language, original_language, rental_duration, length,
	rating, special_features
)
select 
	film_id as movie_key,
	film_id,
	title,
	description,
	release_year,
	l.name as language,
	l.name as original_language,
	rental_duration,
	length,
	rating,
	special_features
from film as f
join language as l on f.language_id = l.language_id
;

insert into store_table(
	store_key, store_id, address, address2,
	district, city, country, postal_code,
	manager_first_name, manager_last_name, start_date, end_date
)
select 
	s,store_id as store_key,
	s.store_id,
	a.address,
	a.address2,
	a.district,
	city,
	country,
	postal_code,
	first_name as manager_first_name,
	last_name as manager_last_name,
	now() as start_date,
	now() as end_date
from store as s
join address as a on a.address_id = s.address_id
join city as c on c.city_id =  a.city_id
join country as co on co.country_id = c.country_id
join staff as st on s.manager_staff_id = st.staff_id
;


SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'movie_table'



