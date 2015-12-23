"""
Problem 35: Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

def find_primes(n):
    add = True
    p = [2]

    for i in range(3, n, 2):
        for j in p:
            if i % j == 0:
                add = False
                break
        if add:
            p.append(i)
        add = True

    return p

def is_circular(n, p):
    if len(str(n)) == 1:
        return True

    word = str(n)
    for i in range(0, len(word)):
        word = word[1:] + word[0]
        if not int(word) in p:
            return False

    return True

limit = 1000000
count = 0

primes = find_primes(limit)
circular_primes = []

for p in primes:
    if is_circular(p, primes):
        circular_primes.append(p)

print(len(circular_primes))


