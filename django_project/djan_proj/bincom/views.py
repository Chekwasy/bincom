from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from .models import Name


""" Connect to the PostgreSQL database"""
conn = psycopg2.connect(database="richardchekwas", user="richardchekwas", password="1234", host="localhost", port="5432")


"""Create a cursor object to execute SQL commands"""
cur = conn.cursor()

"""Execute a SQL command"""
cur.execute("SELECT * FROM babynames")

"""Fetch all result rows"""
names = []
rows = cur.fetchall()
for row in rows:
    names.append(row)

cur.close()
conn.close()

# Create your views here.
def home(request):
    baby_names = {
        'names': names
        }
    return render(request, 'bincom_temp/home.html', baby_names)


def about(request):
    baby_names = {
        'names': names
        }
    return render(request, 'bincom_temp/about.html', baby_names)
