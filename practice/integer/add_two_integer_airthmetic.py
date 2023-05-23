'''
Write a program in Python to add two integer without using arithmetic operator?
'''

def add_without_arithmetic_operator(a, b):
    """
    Function to add two integers a and b without using any arithmetic operator.
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a


num1 = int(input("Enter first number: "))  # take input from user
num2 = int(input("Enter second number: "))

# add the numbers without using arithmetic operator
result = add_without_arithmetic_operator(num1, num2)

# print the result
print("The sum of", num1, "and", num2, "is", result)