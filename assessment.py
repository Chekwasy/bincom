#!/usr/bin/python3
""" Assessment test """
from collections import Counter
"""import psycopg2"""
import random

MONDAY = {'GREEN': 1, 'YELLOW': 2, 'GREEN': 1, 'BROWN': 3,
          'BLUE': 4, 'PINK': 5, 'BLUE': 4, 'YELLOW': 2,
          'ORANGE': 6, 'CREAM': 7, 'ORANGE': 6, 'RED': 8,
          'WHITE': 9, 'BLUE': 4, 'WHITE': 9, 'BLUE': 4,
          'BLUE': 4, 'BLUE': 4, 'GREEN': 1}

TUESDAY = {'ARSH': 1, 'BROWN': 2, 'GREEN': 3, 'BROWN': 2,
           'BLUE': 4, 'BLUE': 4, 'BLEW': 5, 'PINK': 6,
           'PINK': 6, 'ORANGE': 7, 'ORANGE': 7, 'RED': 8,
           'WHITE': 9, 'BLUE': 4, 'WHITE': 9, 'WHITE': 9,
           'BLUE': 4, 'BLUE': 4, 'BLUE': 4}

WEDNESDAY = {'GREEN': 1, 'YELLOW': 2, 'GREEN': 1, 'BROWN': 3,
             'BLUE': 4, 'PINK': 5, 'RED': 6, 'YELLOW': 2,
             'ORANGE': 7, 'RED': 6, 'ORANGE': 7, 'RED': 6,
             'BLUE': 4, 'BLUE': 4, 'WHITE': 8, 'BLUE': 4,
             'BLUE': 4, 'WHITE': 8, 'WHITE': 8}

THURSDAY = {'BLUE': 1, 'BLUE': 1, 'GREEN': 2, 'WHITE': 3,
            'BLUE': 1, 'BROWN': 4, 'PINK': 5, 'YELLOW': 6,
            'ORANGE': 7, 'CREAM': 8, 'ORANGE': 7, 'RED': 9,
            'WHITE': 3, 'BLUE': 1, 'WHITE': 3, 'BLUE': 1,
            'BLUE': 1, 'BLUE': 1, 'GREEN': 2}

FRIDAY = {'GREEN': 1, 'WHITE': 2, 'GREEN': 1, 'BROWN': 3,
          'BLUE': 4, 'BLUE': 4, 'BLACK': 5, 'WHITE': 2,
          'ORANGE': 6, 'RED': 7, 'RED': 7, 'RED': 7,
          'WHITE': 2, 'BLUE': 4, 'WHITE': 2, 'BLUE': 4,
          'BLUE': 4, 'BLUE': 4, 'WHITE': 2}

MON = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED','WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
TUE = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
WED = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
THU = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
FRI = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

WEEK1 = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]
WEEK2 = [MON, TUE, WED, THU, FRI]
"""KEY FEATURES"""


def meanColour(week: list) -> list:
    """function to get mean coulour for each week and arrange
    in a list returned
    """
    output_idx = []
    for a in week:
        fx = len(a)
        efx = 0
        for b in a.values():
            efx = efx + b
        meann = efx / fx
        output_idx.append(round(meann))

    mean_color = []
    count = 0
    for c in output_idx:
        for e, f in week[count].items():
            if f == c:
                mean_color.append(e)
                break
        count = count + 1

    return mean_color


def mostColour(week: list) -> list:
    """function to get most occured colour for each week and arrange
    in a list returned
    """
    most_occ = []
    for a in week:
        count_color = Counter(a)
        most_occ.append(count_color.most_common(1)[0][0])
        del count_color

    return most_occ


def medianColour(week: list) -> list:
    """function to get median colour for each week and arrange
    in a list returned
    """
    med_col = []
    for a in week:
        count = len(a)
        cnt = round(count/2)
        med_col.append(a[cnt])

    return med_col

def varColour(week: list) -> list:
    """function to get var for each week and arrange
    in a list returned
    """
    output_idx = []
    for a in week:
        fx = len(a)
        efx = 0
        for b in a.values():
            efx = efx + b
        meann = efx / fx
        output_idx.append(meann)

    sqrss = []
    allsq = 0
    varr = []
    count = 0
    for c in output_idx:
        for e, f in week[count].items():
            sqrss.append(((f - c) * (f - c)))
        for h in sqrss:
            allsq = allsq + h
        varr.append(allsq / fx)
        sqrss = []
        allsq = 0
        count = count + 1

    return varr

def redProb(week: list) -> list:
    """function to get red colour at random for each week and arrange
    in a list returned
    """
    prob = []
    val = 0
    for a in week:
        val = Counter(a)['RED']
        prob.append(val / len(a))
        val = 0

    return prob

def savePostgre(week: list) -> list:
    """function to save colours and frequencies to postgre
    """
    """sql
    CREATE TABLE color_frequency_per_day (
    day_of_week VARCHAR(20),
    color_name VARCHAR(50),
    frequency INT
    );"""

    """dayinwk = ['mon', 'tue', 'wed', 'thu', 'fri']
    color_freq = {}
    cnt = 0
    for a in dayinwk:
        color_freq[a] = week[cnt]
        cnt = cnt + 1

    conn = psycopg2.connect(
        dbname="dbname",
        user="username",
        password="password",
        host="host"
    )

    cursor = conn.cursor()

    for day, colors in color_freq.items():
        color_counter = Counter(colors)
        for color, frequency in color_counter.items():
            cursor.execute("INSERT INTO color_frequency_per_day (day_of_week, color_name, frequency) VALUES (%s, %s, %s);", (day, color, frequency))

    conn.commit()

    cursor.close()
    conn.close()
"""

def recur_srch(arr, target, index=0):
    if index >= len(arr):
        return False
    if arr[index] == target:
        return True
    return recursive_search(arr, target, index + 1)

def generateRan():
    """generate random 1s and 0s and convert to base 10"""
    binary_num = ""
    for a in range(4):
        binary_num += str(random.randint(0, 1))
    return int(binary_num, 2)

def fibo(n):
    """return fibonacci of n given"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_fib)
        total = 0
        for a in fib_sequence:
            total = total + a
        return total


if __name__ == '__main__':
    mean = meanColour(WEEK1)
    print(mean)
    most = mostColour(WEEK2)
    print(most)
    med = medianColour(WEEK2)
    print(med)
    var = varColour(WEEK1)
    print(var)
    prob = redProb(WEEK2)
    print(prob)
    print(generateRan())
    print(fibo(50))
