'''
Python Program to calculate the power without using POW function.(using while loop).
'''

base = int(input("Enter a base :"))
exponent = int(input("Enter a exponent :"))

i = 0
result = 1
while i < exponent:
    result *= base
    i += 1

print(result)

