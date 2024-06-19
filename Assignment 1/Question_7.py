""" 
7. Write a program to check if an input string is a palindrome
"""

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("baab")) 
print(is_palindrome("hello"))  