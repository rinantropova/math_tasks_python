"""
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
"""


def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


number = input('Input number: ')
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")




