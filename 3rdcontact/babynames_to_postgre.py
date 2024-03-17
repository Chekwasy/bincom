#!/usr/bin/python3
"""todo list to save to postgre"""
import psycopg2
from babynames import babynames


""" Connect to the PostgreSQL database"""
conn = psycopg2.connect(database="richardchekwas", user="richardchekwas", password="1234", host="localhost", port="5432")

"""Create a cursor object to execute SQL commands"""
cur = conn.cursor()

"""create table with its rows and columns"""
cur.execute("""CREATE TABLE IF NOT EXISTS babynames (id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255));"""
)


baby_names = babynames()

for a in baby_names:
    cur.execute("INSERT INTO babynames (first_name, last_name) VALUES (%s, %s);", (a[0], a[1],))

conn.commit()

"""Execute a SQL command"""
cur.execute("SELECT * FROM babynames")

"""Fetch all result rows"""
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cur.close()
conn.close()
