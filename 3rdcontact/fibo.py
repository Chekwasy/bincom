#!/usr/bin/python3
"""function for fibo series"""


def fibogen(n):
    """generate fibo series base on given n"""
    fib_seq = [0, 1]
    if n <= 0:
        return [0]
    if n == 1:
        return fib_seq

    while len(fib_seq) < n:
        nex = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(nex)
    return fib_seq


if __name__ == "__main__":
    print(fibogen(100))
