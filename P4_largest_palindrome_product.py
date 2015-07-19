# Project Euler
# Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(word):
        for i, char in enumerate(word):
                if char != word[-i - 1]:
                        return False
        return True            

def largest_palindrome(n):
        first = n
        second = n
        largest = 0
        current = 0

        while first > 99:
                while second > 99:
                        current = first * second
                        if is_palindrome(str(current)) and current > largest:
                                largest = current
                        second = second - 1
                first = first - 1
                second = n
        return largest


number = 999               
print(largest_palindrome(number))
