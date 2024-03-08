#!/usr/bin/python3
""" Extract first middle and other names from file fullname"""

import os

# Read the file
file_path = "fullname"
with open(file_path, 'r') as fe:
    name = fe.read()

# Split the full name into first, middle, and last name
names = name.split()
first_name = names[0]
last_name = names[-1]

# Check if there's a middle name
if len(names) > 2:
        middle_name = names[1]
else:
        middle_name = None

# Print the extracted names
print("First Name:", first_name)
print("Middle Name:", middle_name)
print("Last Name:", last_name)

# Print the file path
print("File Path:", os.path.abspath(file_path))
