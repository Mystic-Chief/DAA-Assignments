""" 
11. Write a program to find the greatest common divisor (GCD) of two input numbers
"""

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(gcd(48, 18))
