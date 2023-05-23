'''
Write a program to calculate factorial using iterative method
The factorial numbers are a sequence of integers that are the products of all positive integers less than or equal
to a given integer n. The factorial of n is denoted by n!, and is defined as:
n! = n * (n-1) * (n-2) * ... * 2 * 1
'''

def get_factorial(num):

    fact = 1
    while num > 1:
        fact *= num
        num = num-1

    return fact

num = int(input("Enter a number:"))
fact = get_factorial(num)
print(fact)