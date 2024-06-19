""" 
12. Write a program to find the least common multiple (LCM) of two input numbers
"""

def lcm(a, b):
    multiple = max(a, b)

    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1

print(lcm(12, 18)) 

