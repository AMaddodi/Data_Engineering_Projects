CREATE TABLE sales_table(
	sales_key serial primary_key,
	date_key integer references date_table (date_key),
	customer_key integer references customer_table (customer_key),
	movie_key interger references movie_table (movie_key),
	store_key interger references store_table (store_key),
	sales_amount numeric
);
