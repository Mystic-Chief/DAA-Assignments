""" 
4. Write a program to find factors of a given number
"""

def finding_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

print(finding_factors(12))
