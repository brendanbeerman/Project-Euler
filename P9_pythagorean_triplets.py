# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

limit = 1000

# since a and b split the c value pretty evenly
for a in range(int(limit / 2)):
    for b in range(a + 1, int(limit / 2)):
        c = limit - (a + b)
        if a**2 + b**2 == c**2:
            print(a * b * c)
