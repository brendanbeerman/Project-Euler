# Project Euler
# Problem 10: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def find_primes(p, n):
        counter = 3
        while counter < n:
                check = 1
                for x in p:
                        if counter % x == 0:
                                check = 0
                                break
                if check == 1:
                        p.append(counter)
                counter = counter + 2
        return p

def add_items(lst):
    total = 0
    for i in lst:
        total = total + i
    return total + 2

primes = [3]
number = 2000000

primes = find_primes(primes, number)
print(add_items(primes))