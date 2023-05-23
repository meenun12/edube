'''
Python program to calculate LCM of given two numbers.
This text refers to a Python program that calculates the least common multiple (LCM) of two given numbers.
The LCM is the smallest positive integer that is divisible by both of the input numbers without leaving a remainder
The program takes two input numbers from the user and calculates their LCM using a formula based on their greatest
common divisor (GCD). The GCD is the largest positive integer that divides both of the input numbers without leaving a remainder.
To calculate the LCM of two numbers a and b, you can use the formula:
'''

import math

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = print(math.gcd(num1, num2))
print(gcd)

# calculate the LCM using the formula
lcm = (num1 * num2) // math.gcd(num1, num2)

# output the result
print("The LCM of", num1, "and", num2, "is", lcm)

