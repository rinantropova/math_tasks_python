"""
Exercise 13: Print multiplication table from 1 to 10
"""

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        num = i * j
        row.append(str(num))
    print(' '.join(row))