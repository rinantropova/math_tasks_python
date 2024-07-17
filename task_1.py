"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

numbers = input('Add list of numbers: ')
list_of_nums = list(map(int, numbers.split(" ")))

for num in list_of_nums:
    if num % 5 == 0:
        print(num, end=" ")
