# Project Euler
# Problem 20: Factorial Digit Sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial(n):
    factorial_helper(1, n)

def factorial_helper(total, n):
    if n != 1:
        factorial_helper(total * n, n - 1)
    else:
        digit_sum(total)

def digit_sum(n):
    total = 0
    x = str(n)

    for i in x:
        total = total + int(i)
    print(total)

number = 100
factorial(number)