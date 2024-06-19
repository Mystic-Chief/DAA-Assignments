""" 
9. Write a program to check if an input number is an Armstrong number
"""

def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    return num == sum(int(digit) ** num_len for digit in num_str)

print(is_armstrong(153)) 
print(is_armstrong(123))  
