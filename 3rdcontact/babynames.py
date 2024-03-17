#!/usr/bin/python3
""" Extract first middle and other names from file fullname"""
import re
import os


def babynames():
    # Read the file
    file_path = "baby2008.html"
    with open(file_path, 'r') as fe:
        babynames = fe.read()

    # Split the full name into first, middle, and last name
    names = babynames.split("\n")

    count = 47
    pattern = r'\b[A-Z]\w+\b'
    string_lst = []

    # Append the extracted names
    for a in range(len(names) - count - 16):
        matches = re.findall(pattern, names[a + count])
        if matches:
            string_lst.append(matches)

    return string_lst
