"""
Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def generate_primes(n):
    sieve = [True] * int((n/2))
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int(((n - i*i - 1)/(2*i) + 1))
    return [2] + [2*i + 1 for i in range(1, int(n/2)) if sieve[i]]

def is_pandigital(n):
    word = str(n)

    keys = list(range(1, len(word) +1))
    values = [0]*len(word)
    hash_table = dict(zip(keys, values))

    for w in word:
        if not int(w) in hash_table:
            return False
        if hash_table[int(w)] == 1:
            return False
        hash_table[int(w)] = 1

    return True

limit = 10000000
primes = generate_primes(limit)

max = 0

for p in primes:
    if p < 21:
        continue
    if is_pandigital(p):
        max = p

print(max)