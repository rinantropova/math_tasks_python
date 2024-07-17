"""
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
"""


def name_count(string, a_word):
    str_list = string.split(" ")
    count = 0
    for word in str_list:
        if word == a_word:
            count += 1
    return count


str_x = 'Emma is good developer. Emma is a writer'
word_to_count = 'Emma'
print(name_count(str_x, word_to_count))
