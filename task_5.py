"""
Exercise 10: Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from
the first list and even numbers from the second list.
Given:                                          Expected Output:
list1 = [10, 20, 25, 30, 35]                    result list: [25, 35, 40, 60, 90]
list2 = [40, 45, 60, 75, 90]
"""


def create_new_list(list_1, list_2):
    res_list = []
    for num in list_1:
        if num % 2 != 0:
            res_list.append(num)
    for num in list_2:
        if num % 2 == 0:
            res_list.append(num)
    return res_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(create_new_list(list1, list2))

