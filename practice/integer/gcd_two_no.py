'''
Python Program to find GCD or HCF of two numbers.
'''

# define a function to calculate the GCD using Euclid's algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calculate the GCD using the gcd() function
result = gcd(num1, num2)

# output the result
print("The GCD of", num1, "and", num2, "is", result)
