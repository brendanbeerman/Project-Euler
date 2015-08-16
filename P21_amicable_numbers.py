"""
Problem 21: Amicable Numbers
s
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt

def divisor_sum(n):
    total = 1
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            total = total + i + (n / i)
    return total

def is_amicable(p, q):
    if p == divisor_sum(q):
        return True
    return False

limit = 10000
# the first set of amicable numbers are (220, 284)
first = 285
total = 504

for x in range(first, limit):
    if is_amicable(x, divisor_sum(x)) and x != divisor_sum(x):
        total = total + x

print(total)





