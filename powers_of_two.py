"""
Complete the function that takes a non-negative integer n as input,
and returns a list of all the powers of 2 with the exponent ranging
from 0 to n ( inclusive ).
"""


def powers_of_two(number: int) -> list:
    result = [1]
    for i in range(1,number+1):
            digit = 2**i
            result.append(digit)
    return result

"""
Optimal solution

def powers_of_two(number: int) -> list:
    return [2**x for x in range(n+1)]
"""