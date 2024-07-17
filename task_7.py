"""
Exercise 12: Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:
For example, suppose the taxable income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
"""

tax_income = int(input('Enter your taxable income: '))
# first = 10_000
# second = 10_000
# remaining = tax_income - first - second
#
# if remaining > 0:
#     tax = first * 0 + second * 0.1 + remaining * 0.2
#
# print(int(tax))
if tax_income <= 10000:
    tax = 0
elif tax_income <= 20000:
    x = tax_income - 10000
    tax = x * 10 / 100
else:
    tax = 0
    tax = 10000 * 10 / 100
    tax += (tax_income - 20000) * 20 / 100
print(int(tax))