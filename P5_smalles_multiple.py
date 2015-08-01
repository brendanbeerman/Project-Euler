# Project Euler
# Problem 5: Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import sqrt
from math import pow
from math import ceil

def find_primes(p, n):
    check = True
    for i in range(3, n, 2):
        for j in p:
            if i % j == 0:
                check = False
                break;
        if check:
            p.append(i)
        check = True
    return p


def smallest_multiple(p, n):
    total = 1
    for x in p:
        if x > ceil(sqrt(n)) + 1:
            total = total * x
        else:
            total = total * smallest_power(x, n)
    return total


def smallest_power(y, r):
    largest = 0
    current = 0
    for i in range(2, r):
        current = pow(y, i)
        if current > r:
            if largest == 0:
                largest = y
            break
        if current >= largest and current <= r:
            largest = current
    return largest


limit = 20
primes = [2]
primes = find_primes(primes, limit)
print(primes)
print(smallest_multiple(primes, limit))

