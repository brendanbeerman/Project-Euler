# Project Euler
# Problem 7: 10001st Prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

number = 10001 
current = 3
primes = [2]
state = False

while len(primes) < number:
    for p in primes:
        if current % p == 0:
            state = False
            break
        state = True
    if state:
        primes.append(current)
    state = False
    current = current + 1
            
primes.reverse()
result = primes.pop(0)
print(result)
