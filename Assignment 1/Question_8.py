""" 
8. Write a program to find the sum of digits of an input number
"""

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print(sum_of_digits(123))
