'''
Python Program to calculate the power without using POW function.(using for loop).
'''

base = int(input("Enter a base :"))
exponent = int(input("Enter a exponent :"))

result = 1
for i in range(exponent):
    result *= base

print(result)

