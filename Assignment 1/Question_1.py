"""
1. Write a program to check is a given number is
- even or odd
- positive, negative or zero
"""
def check_number(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

check_number(9)
check_number(-22)
check_number(0)