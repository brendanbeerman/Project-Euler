# Project Euler
# Problem 3: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def find_primes(p, n):
        counter = 5
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

def find_largest(p, n):
        p.reverse()
        for x in p:
                if n % x == 0:
                        return x
        return 0

primes = [3]
number = 600851475143

primes = find_primes(primes, sqrt(number) + 1)
print(find_largest(primes, number))
