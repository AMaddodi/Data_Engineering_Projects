CREATE TABLE date_table(
	date_key INT NOT NULL PRIMARY KEY,
	date date NOT NULL,
	year smallint NOT NULL,
	quarter smallint NOT NULL,
	month smallint NOT NULL,
	week smallint NOT NULL,
	day smallint NOT NULL,
	is_weekend boolean
);

CREATE TABLE customer_table(
	customer_key SERIAL PRIMARY KEY,
	customer_id  INT NOT NULL,
	first_name   VARCHAR(50) NOT NULL,
	last_name    VARCHAR(50) NOT NULL,
	email        VARCHAR(50),
	address      VARCHAR(50) NOT NULL,
	address2     VARCHAR(50),
	district     VARCHAR(20) NOT NULL,
	city         VARCHAR(50) NOT NULL,
	country      VARCHAR(50) NOT NULL,
	postal_code  VARCHAR(10) NOT NULL,
	phone        VARCHAR(20) NOT NULL,
	active       SMALLINT NOT NULL,
	create_date  TIMESTAMP NOT NULL,
	start_date   DATE NOT NULL,
	end_date     DATE NOT NULL
);

CREATE TABLE movie_table(
	movie_key 	       SERIAL PRIMARY KEY,
	film_id            SMALLINT NOT NULL,
	title              VARCHAR(255) NOT NULL,
	description        TEXT,
	release_year       YEAR,
	language           VARCHAR(50) NOT NULL,
	original_language  VARCHAR(50),
	rental_duration    SMALLINT NOT NULL,
	length             INT NOT NULL,
	rating             VARCHAR(5) NOT NULL,
	special_features   VARCHAR(50) NOT NULL
);

CREATE TABLE store_table(
	store_key           SERIAL PRIMARY KEY,
	store_id            INT NOT NULL,
	address             VARCHAR(50) NOT NULL,
	address2            VARCHAR(50),
	district            VARCHAR(50) NOT NULL,
	city                VARCHAR(50) NOT NULL,
	country             VARCHAR(50) NOT NULL,
	postal_code         VARCHAR(50) NOT NULL,
	manager_first_name  VARCHAR(50) NOT NULL,
	manager_last_name   VARCHAR(50) NOT NULL,
	start_date          DATE NOT NULL,
	end_date            DATE NOT NULL
);


