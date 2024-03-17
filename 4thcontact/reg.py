#!/usr/bin/python3
"""read from csv and perform regression analysis"""
import csv

rows = []
with open("freq.csv") as fe:
    csvreader = csv.reader(fe)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(header)
print(rows)
