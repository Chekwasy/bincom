#!/usr/bin/python3
""" Extract first middle and other names from file fullname"""
import re
import os

# Read the file
file_path = "baby2008.html"
with open(file_path, 'r') as fe:
    babynames = fe.read()

# Split the full name into first, middle, and last name
names = babynames.split("\n")

count = 47
pattern = r'\b[A-Z]\w+\b'
string_lst = []

# Print the extracted names
for a in range(len(names) - count - 16):
    matches = re.findall(pattern, names[a + count])
    if matches:
        string_lst.append(matches)


print(string_lst)



"""
# Search for the pattern in the HTML content
match = pattern2.search(names[49])

# Check if the pattern is found
if match:
        print("Pattern found:", match.group())
else:
        print("Pattern not found")
"""
