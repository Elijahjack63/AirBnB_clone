#!/usr/bin/python3

"""This is a python code that passes the pycodestyle checks"""
def sum_multiples(num1, num2, limit):
    """Return the sum of all multiples num1, num2 and up to a limit"""
    return sum(i for i in range(limit) if i % num1 == 0 or i % num2 == 0)

print(sum_multiples(3, 5, 1000))

