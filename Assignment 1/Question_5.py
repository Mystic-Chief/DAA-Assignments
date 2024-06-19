""" 
5. Write a program to check if an input number is prime or not
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(13)) 
print(is_prime(6))  
