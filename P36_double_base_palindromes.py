"""
Problem 36: Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def is_palindrome(n):
    word = str(n)
    return word == word[::-1]

def convert_and_check(n):
    binary_n = bin(n)[2:]
    return is_palindrome(binary_n)

sum = 0
limit = 1000000

for p in range(1, limit):
    if is_palindrome(p) and convert_and_check(p):
        sum = sum + p

print(sum)
