#!/usr/bin/python3
"""todo list to save to postgre"""
import psycopg2


# Connect to the PostgreSQL database
conn = psycopg2.connect(database="richardchekwas", user="richardchekwas", password="1234", host="localhost", port="5432")

# Create a cursor object to execute SQL commands
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS todo (id INT PRIMARY KEY, todo_item VARCHAR(255));"""
)

cur.execute("""INSERT INTO todo (id, todo_item) VALUES (10, 'wake up'), (11, 'pray'), (12, 'bath'), (13, 'dress up'), (14, 'eat'), (15, 'goto work');""")

conn.commit()

# Execute a SQL command
cur.execute("SELECT * FROM todo")

# Fetch all result rows
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and the database connection
cur.close()
conn.close()
