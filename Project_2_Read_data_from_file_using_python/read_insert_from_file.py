import psycopg2
import pandas as pd

def create_database():
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=root")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create database 
    #cur.execute("DROP DATABASE accounts")
    cur.execute("CREATE DATABASE accounts")
    
    #close the connection
    conn.close()
    
    # connect to the database which we create
    conn = psycopg2.connect("host=localhost dbname=accounts user=postgres password=root")
    cur = conn.cursor()
    
    return conn, cur

def create_table(conn, cur, queries):
    for query in queries:
        cur.execute(query)
        conn.commit()
    
def insert_data(conn, cur, data, insert_query):
    for i, row in data.iterrows():
        cur.execute(insert_query, list(row))
    conn.commit()


# create database
conn, cur = create_database()

# create table
accounts_table = ("""CREATE TABLE IF NOT EXISTS accountscountry(
Country VARCHAR PRIMARY KEY,
Rank INT ,
CCA3 VARCHAR,
Capital VARCHAR,
Continent VARCHAR,
Population INT,
World_Population_Percentage FLOAT);
""")

create_table(conn, cur, accounts_table)

# Insert data to table

# read CSV file
file_data = pd.read_csv(r"C:\Users\Archana\Documents\DataAnalysis\python\world_population.csv")
file_data = file_data[['Country', 'Rank', 'CCA3', 'Capital', 'Continent', '2022 Population', 'World Population Percentage']]

accounts_data_query = ("""INSERT INTO accountscountry(
Country,
Rank,
CCA3,
Capital,
Continent,
Population,
World_Population_Percentage)
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

insert_data(conn, cur, file_data, accounts_data_query)
